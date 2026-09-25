"""
Derive a BUILDABLE purchase order for every hero's solved build.

optimize.py produces an unordered item SET. Turning that into something you can
actually follow in a match needs two things the set does not carry:

  1. Affordability pacing. Souls accumulate over a match, so you cannot open
     with a 6,400 tier-4. Each pick is restricted to items costing at most
     twice the cheapest still-unbought item.

  2. COMPONENT ROUTING. Most tier-3/4 items build out of a cheap component:
     Leech <- Bullet Lifesteal (1,600), Crippling Headshot <- Weakening
     Headshot, Titanic Magazine <- Extended Magazine. In a real game you buy
     the component early for the lane, then pay only the DIFFERENCE to upgrade.
     Buying the tier-4 outright at minute 25 leaves you with nothing at minute
     5, so an order without component steps is not a build you can follow.
     Total souls are identical either way -- component + difference = full
     price -- but the curve is completely different.

  3. SLOTS. You start with 9 slots and unlock one more per enemy Walker, so
     the route never holds more items than the slots open at that point.

If the final set contains BOTH a component and its parent (the optimiser is
allowed to hold both, they stack), the component is bought once and kept; the
parent is then bought outright rather than consuming it.
"""

import concurrent.futures
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import BASE_SLOTS, ITEMS, OBJECTIVES, WALKER_NET_WORTH, Loadout, slots_at

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

_BY_CLASS = {i["class_name"]: n for n, i in ITEMS.items()}


def components_of(name):
    return [_BY_CLASS.get(c) for c in ITEMS[name]["components"] if _BY_CLASS.get(c)]


def plan_steps(final_items):
    """Expand a final item set into buy / upgrade steps.

    Returns a list of dicts describing what is purchasable, which the ordering
    loop then sequences.
    """
    kept = set(final_items)
    steps = []
    # A component can only be owned ONCE, so it can only feed ONE upgrade.
    # Three of Drifter's items (Fury Trance, Vampiric Burst, Leech) all build
    # from Bullet Lifesteal; routing each of them through it bought the same
    # 1,600 item three times. Each component is therefore claimed by a single
    # parent -- the one with the largest discount, since that is where routing
    # through the component saves the most -- and the rest are bought outright.
    claimed = {}
    for name in final_items:
        for c in components_of(name):
            if c in kept:
                continue          # the build deliberately holds both; don't consume it
            gain = ITEMS[c]["cost"]          # souls deferred by buying the component first
            if c not in claimed or gain > claimed[c][1]:
                claimed[c] = (name, gain)
    routed = {parent: c for c, (parent, _) in claimed.items()}

    for name in final_items:
        c = routed.get(name)
        if c:
            steps.append({"kind": "buy", "item": c, "cost": ITEMS[c]["cost"],
                          "for": name})
            steps.append({"kind": "upgrade", "item": name, "from": c,
                          "cost": ITEMS[name]["cost"] - ITEMS[c]["cost"],
                          "for": name})
        else:
            steps.append({"kind": "buy", "item": name, "cost": ITEMS[name]["cost"],
                          "for": name})
    return steps


def score_state(hero, items, net_worth, ref, objective="allround"):
    loadout = Loadout(hero, items, net_worth=net_worth)
    score, _, results = loadout.evaluate(ref, objective)
    weights = OBJECTIVES[objective]
    total = sum(weights.values())
    gun = sum(w * results[name]["gun_dps"] for name, w in weights.items()) / total
    heal = sum(w * results[name]["heal_ps"] for name, w in weights.items()) / total
    return score, loadout, gun, heal


def _net_worth_after(spent, cap):
    """Net worth when `spent` souls are in items (~8% of souls sit unspent)."""
    return min(max(int(spent / 0.92), 1000), cap)


def _walker_net_worth(slots_needed):
    """Lowest net worth at which `slots_needed` slots are unlocked."""
    extra = slots_needed - BASE_SLOTS
    return WALKER_NET_WORTH[extra - 1] if 0 < extra <= len(WALKER_NET_WORTH) else 0


def purchase_order(hero, items, ref, net_worth, objective="allround"):
    """Order the solved item set into steps you can follow in a match.

    Rules, in priority order:
      * an upgrade only after its component is owned;
      * never hold more items than the slots unlocked at that point
        (9, then one more per enemy Walker, see model.slots_at). Upgrades
        replace their component, so they never need a free slot;
      * affordability pacing: only items up to 2x the cheapest remaining step;
      * among those, the best marginal score per soul.
    If every remaining step needs a slot that is not unlocked yet, the
    cheapest is bought once the next Walker falls, and the step records that
    net worth (``after_walker``).
    """
    steps = plan_steps(items)
    done, owned, spent, out = set(), [], 0, []
    floor_nw = 0      # net worth already committed by a Walker-gated step

    while len(done) < len(steps):
        avail = [(i, s) for i, s in enumerate(steps)
                 if i not in done and not (s["kind"] == "upgrade" and s["from"] not in owned)]
        if not avail:
            break

        def fits(s):
            if s["kind"] == "upgrade":
                return True
            nw = max(_net_worth_after(spent + s["cost"], net_worth), floor_nw)
            return len(owned) + 1 <= slots_at(nw)

        fitting = [(i, s) for i, s in avail if fits(s)]
        after_walker = False
        if not fitting:
            # every remaining step is a new item and the slots are full:
            # buy the cheapest one when the next Walker unlocks a slot
            i, s = min(avail, key=lambda p: p[1]["cost"])
            fitting = [(i, s)]
            after_walker = True
            floor_nw = max(floor_nw, _walker_net_worth(len(owned) + 1))
        cheapest = min(s["cost"] for _, s in fitting)
        pool = [(i, s) for i, s in fitting if s["cost"] <= max(cheapest * 2, 800)]

        # Rank by score gained PER SOUL: souls arrive over time, so an 800
        # item starts paying long before a 1,600 one is affordable at all.
        base_nw = max(_net_worth_after(spent, net_worth), floor_nw)
        base_sc = score_state(hero, owned, base_nw, ref, objective)[0] if owned else 0.0
        best, best_val = None, None
        for i, s in pool:
            trial = [x for x in owned if x != s.get("from")] + [s["item"]]
            nw = max(_net_worth_after(spent + s["cost"], net_worth), floor_nw)
            sc = score_state(hero, trial, nw, ref, objective)[0]
            val = (sc - base_sc) / max(s["cost"], 1)
            if best is None or val > best_val:
                best, best_val = (i, s), val

        i, s = best
        done.add(i)
        if s["kind"] == "upgrade":
            owned = [x for x in owned if x != s["from"]]
        owned = owned + [s["item"]]
        spent += s["cost"]

        nw = max(_net_worth_after(spent, net_worth), floor_nw)
        score, lo, gun, heal = score_state(hero, owned, nw, ref, objective)
        out.append({
            "kind": s["kind"],
            "item": s["item"],
            "from": s.get("from"),
            "cost": s["cost"],
            "running": spent,
            "net_worth": nw,
            "slot": ITEMS[s["item"]]["slot"],
            "tier": ITEMS[s["item"]]["tier"],
            "slots": len(owned),
            "slots_open": slots_at(nw),
            "after_walker": after_walker,
            "invest": [round(lo.inv_weapon), round(lo.inv_vit), round(lo.inv_spirit)],
            "gun": round(gun),
            "heal": round(heal),
            "score": round(score, 2),
        })
    return out


def _order_task(task):
    key, hero, items, ref, budget, objective = task
    return key, purchase_order(hero, items, ref, budget, objective)


def main():
    with open(os.path.join(DATA, "optimization.json"), encoding="utf-8") as f:
        O = json.load(f)

    tasks = []
    tables = [("allround", O["stages"]), ("teamfight", (O.get("teamfight") or {}).get("stages") or {})]
    for objective, stages in tables:
        suffix = "" if objective == "allround" else "|teamfight"
        for stage, rows in stages.items():
            for row in rows:
                tasks.append((f"{row['hero']}|{stage}{suffix}", row["hero"], row["items"],
                              O["refs"][stage], row["budget"], objective))

    out = {}
    workers = max(1, (os.cpu_count() or 2) - 2)
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as ex:
        for key, steps in ex.map(_order_task, tasks, chunksize=4):
            out[key] = steps

    with open(os.path.join(DATA, "orders.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"))
    print(f"wrote orders.json ({len(out)} builds)")


if __name__ == "__main__":
    main()
