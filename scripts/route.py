"""
Full-game purchase routes: items bought early and sold later, ability points,
all the way to the final build.

The per-stage solver answers "what is the best build at 20k?". A player needs
a ROUTE: what to buy, upgrade and sell, in order, from 0 souls to the final
build. Selling refunds 50% of what the item cost (deadlock.wiki/Shop; the
full refund inside the shop is ignored); upgrading from a component credits
the component in full.

For every hero and objective:

  1. Beam search over checkpoints (6k / 12k / 20k / 32k / 50k). Each route
     keeps what it owns and the souls it has lost selling; the next
     checkpoint's build is re-solved from several seeds (keep everything,
     stage-optimal, other objective, final build) under the exact rule
     cost of items held + souls lost selling <= net worth.
  2. Routes are ranked by the sum of stage-weighted log scores, so +20%
     power early counts as much as +20% late: early items that get sold
     later are used exactly when they pay for their sell loss. A never-sell
     beam is solved too, for comparison.
  3. After 50k the route continues to the END state, the optimal full build,
     completed at 50k plus whatever was lost selling -- and every route must
     be able to finish it by 56k (END_NET_WORTH), which caps sell losses.
  4. Ability points: a DP over tier allocations that only go up between
     checkpoints and end with every ability at tier 3 (32 points).
  5. The winning path becomes a timeline of buy / upgrade / sell / ability
     steps. Items are bought as souls arrive (pacing, then best value per
     soul); an old item is sold only when its slot or its refund is needed.

    python scripts/route.py   -> data/routes.json
"""

import concurrent.futures
import itertools
import json
import math
import os
import random
import sys
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import (ABILITY_TIER_COST, HEROES, ITEMS, OBJECTIVES, WALKER_NET_WORTH,  # noqa: E402
                   Loadout, ability_points_for_networth, slots_at, valid_build)
from optimize import STAGES, STAGE_WEIGHT, Search, ref_at, search_pool  # noqa: E402
from order_all import components_of  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

SELL_REFUND = 0.5
# Every route must still be able to finish the final build by this net worth:
# selling early items is fine, wasting a quarter of a full build is not.
END_NET_WORTH = 56000
TABLE = {"allround": lambda O: O["stages"], "teamfight": lambda O: O["teamfight"]["stages"]}


def cost(items):
    return sum(ITEMS[n]["cost"] for n in items)


def transition(prev, nxt):
    """(sold items, {new item: component it is upgraded from})."""
    prev_only = set(prev) - set(nxt)
    consumed, used = {}, set()
    for new in sorted(set(nxt) - set(prev), key=lambda n: (-ITEMS[n]["cost"], n)):
        for c in components_of(new):
            if c in prev_only and c not in used:
                consumed[new] = c
                used.add(c)
                break
    return sorted(prev_only - used), consumed


def sell_loss(sold):
    return (1 - SELL_REFUND) * cost(sold)


def with_components(items):
    out, frontier = set(items), list(items)
    while frontier:
        for c in components_of(frontier.pop()):
            if c not in out:
                out.add(c)
                frontier.append(c)
    return out


def score_at(hero, items, nw, ref, objective, levels=None):
    lo = Loadout(hero, list(items), net_worth=nw)
    if levels is not None:
        lo.ability_level_options = (tuple(levels),)
    return lo.evaluate(ref, objective)


def table_row(O, objective, stage, hero):
    return next(r for r in TABLE[objective](O)[stage] if r["hero"] == hero)


# ------------------------------------------------------------ beam search
class RouteSearch(Search):
    """Build search that knows what you own and what you have already lost.

    A build is affordable only if its cost plus the souls lost selling so far
    plus the loss from selling what it drops fits inside the checkpoint's net
    worth. With ``allow_sell=False`` a build must keep every owned item
    (components may still be upgraded).
    """

    def __init__(self, hero, nw, ref, objective, pool, rng, prev, loss, allow_sell=True, final=None):
        super().__init__(hero, nw - loss, ref, objective, pool, rng, net_worth=nw)
        self.prev, self.loss, self.cap, self.allow_sell = list(prev), loss, nw, allow_sell
        self.final = list(final or [])
        self.end_budget = END_NET_WORTH - cost(self.final) if final else None

    def score(self, items):
        key = frozenset(items)
        value = self.memo.get(key)
        if value is None:
            sold = transition(self.prev, items)[0]
            loss = self.loss + sell_loss(sold)
            if (sold and not self.allow_sell) or cost(items) + loss > self.cap:
                value = -1.0
            elif (self.end_budget is not None
                  and loss + sell_loss(transition(items, self.final)[0]) > self.end_budget):
                value = -1.0      # could no longer finish the final build by END_NET_WORTH
            else:
                self.evals += 1
                value = Loadout(self.hero, list(items), net_worth=self.net_worth).evaluate(
                    self.ref, self.objective)[0]
            self.memo[key] = value
        return value


def beam_route(hero, objective, O, rng, width=3, allow_sell=True):
    """Best checkpoint builds given everything bought and sold before.

    Each beam state is (value, builds so far, scores, sell loss so far). Every
    state is extended by re-solving the next checkpoint from several seeds --
    keep what you have, the stage-optimal build, the other objective's build,
    the final build -- under the exact affordability rule above.
    """
    other = "allround" if objective == "teamfight" else "teamfight"
    final = table_row(O, objective, "full", hero)["items"]
    pool = search_pool(hero)
    beams = [(0.0, [], [], 0.0)]
    for k, (stage, nw) in enumerate(STAGES):
        ref = O["refs"][stage]
        w = STAGE_WEIGHT[stage]
        seeds = [table_row(O, objective, stage, hero)["items"],
                 table_row(O, other, stage, hero)["items"], final]
        nxt = {}
        for value, builds, scores, loss in beams:
            prev = builds[-1] if builds else []
            s = RouteSearch(hero, nw, ref, objective, pool, rng, prev, loss, allow_sell, final)
            for seed in [prev] + seeds:
                start = sorted(set(prev) | set(seed), key=lambda n: (-ITEMS[n]["cost"], n))
                items, sc = s.climb(s.greedy(start)[0])
                if sc <= 0:
                    continue
                new_loss = loss + sell_loss(transition(prev, items)[0])
                state = (value + w * math.log(sc), builds + [sorted(items)], scores + [sc], new_loss)
                key = (frozenset(items), round(new_loss))
                if key not in nxt or state[0] > nxt[key][0]:
                    nxt[key] = state
        beams = sorted(nxt.values(), key=lambda b: (-b[0], b[3]))[:width]
    return beams[0]


# --------------------------------------------------------------- abilities
def full_tiers(hero):
    return tuple([3] * len(HEROES[hero]["abilities"]))


def allocation_path(hero, builds, objective, O):
    """Monotone ability tiers across checkpoints, all maxed at 32 points."""
    n = len(HEROES[hero]["abilities"])
    weights = [STAGE_WEIGHT[s] for s, _ in STAGES]
    max_cost = n * ABILITY_TIER_COST[3]
    layers = []
    for (stage, nw), items in zip(STAGES, builds):
        pts = ability_points_for_networth(HEROES[hero], nw)
        if pts >= max_cost:
            opts = [full_tiers(hero)]
        else:
            opts = [lv for lv in itertools.product(range(4), repeat=n)
                    if pts - 5 <= sum(ABILITY_TIER_COST[t] for t in lv) <= pts]
        layers.append([(lv, score_at(hero, items, nw, O["refs"][stage], objective, lv)[0])
                       for lv in opts])
    best = [{lv: (weights[0] * math.log(max(sc, 1e-9)), None, sc) for lv, sc in layers[0]}]
    for k in range(1, len(layers)):
        cur = {}
        for lv, sc in layers[k]:
            prev = [(val, p) for p, (val, _, _) in best[-1].items()
                    if all(a >= b for a, b in zip(lv, p))]
            if prev:
                val, p = max(prev)
                cur[lv] = (val + weights[k] * math.log(max(sc, 1e-9)), p, sc)
        best.append(cur)
    lv = max(best[-1], key=lambda x: best[-1][x][0])
    path = [lv]
    for k in range(len(best) - 1, 0, -1):
        lv = best[k][lv][1]
        path.append(lv)
    path.reverse()
    return path, [best[k][path[k]][2] for k in range(len(path))]


def point_unlocks(hero):
    return sorted(info["required_gold"] for info in HEROES[hero]["level_info"].values()
                  if info.get("required_gold") is not None
                  and "EAbilityPoints" in (info.get("bonus") or []))


def ability_steps(hero, allocs, builds, objective, O):
    """Spend each point as it unlocks, best score gain per point first."""
    names = [a["name"] for a in HEROES[hero]["abilities"]]
    unlocks = point_unlocks(hero)
    queue, cur = [], tuple([0] * len(names))
    for (stage, nw), target, items in zip(STAGES, allocs, builds):
        ref = O["refs"][stage]
        while cur != tuple(target):
            base = score_at(hero, items, nw, ref, objective, cur)[0]
            best = None
            for i, (c, t) in enumerate(zip(cur, target)):
                if c < t:
                    trial = list(cur)
                    trial[i] += 1
                    pts = ABILITY_TIER_COST[trial[i]] - ABILITY_TIER_COST[c]
                    val = (score_at(hero, items, nw, ref, objective, trial)[0] - base) / pts
                    if best is None or val > best[0]:
                        best = (val, i, pts)
            _, i, pts = best
            nxt = list(cur)
            nxt[i] += 1
            queue.append((i, nxt[i], pts))
            cur = tuple(nxt)
    steps, banked, used, at = [], 0, 0, 0
    for i, tier, pts in queue:
        while banked < pts:
            at = unlocks[used]
            used += 1
            banked += 1
        banked -= pts
        steps.append({"kind": "ability", "ability": names[i], "index": i, "tier": tier,
                      "points": pts, "at_net_worth": at})
    return steps


# ----------------------------------------------------------------- timeline
def _stats(hero, owned, nw, objective, O, level):
    ref = ref_at(O["refs"], nw)
    lo = Loadout(hero, list(owned), net_worth=nw)
    lo.ability_level_options = (tuple(level),)
    sc, _, res = lo.evaluate(ref, objective)
    w = OBJECTIVES[objective]
    tot = sum(w.values())
    return sc, {
        "invest": [round(lo.inv_weapon), round(lo.inv_vit), round(lo.inv_spirit)],
        "gun": round(sum(w[n] * res[n]["gun_dps"] for n in w) / tot),
        "heal": round(sum(w[n] * res[n]["heal_ps"] for n in w) / tot),
        "score": round(sc, 3),
    }


def item_steps(hero, targets, objective, O):
    """targets: [(label, checkpoint net worth or None, build, ability tiers)]."""
    owned, cash, earned, loss = [], 0.0, 0.0, 0.0
    steps, checkpoints = [], []
    for label, nw, target, level in targets:
        level = tuple(level)
        sold, consumed = transition(owned, target)
        pending = list(sold)
        todo, claimed, kept = [], set(), set(target)
        for new in sorted(set(target) - set(owned)):
            if new in consumed:
                todo.append({"kind": "upgrade", "item": new, "from": consumed[new],
                             "cost": ITEMS[new]["cost"] - ITEMS[consumed[new]]["cost"]})
                continue
            comp = next((c for c in components_of(new)
                         if c not in kept and c not in owned and c not in claimed), None)
            if comp:
                claimed.add(comp)
                todo.append({"kind": "buy", "item": comp, "cost": ITEMS[comp]["cost"], "for": new})
                todo.append({"kind": "upgrade", "item": new, "from": comp,
                             "cost": ITEMS[new]["cost"] - ITEMS[comp]["cost"]})
            else:
                todo.append({"kind": "buy", "item": new, "cost": ITEMS[new]["cost"]})

        def pick_sale():
            now = max(earned, 1000)
            ref = ref_at(O["refs"], now)
            return max(pending, key=lambda n: score_at(
                hero, [x for x in owned if x != n], now, ref, objective, level)[0])

        def sell_one(reason, choice=None):
            nonlocal cash, loss
            choice = choice or pick_sale()
            pending.remove(choice)
            owned.remove(choice)
            refund = SELL_REFUND * ITEMS[choice]["cost"]
            cash += refund
            loss += ITEMS[choice]["cost"] - refund
            steps.append({"kind": "sell", "item": choice, "refund": round(refund), "stage": label,
                          "at_net_worth": round(earned), "reason": reason,
                          "slots": len(owned), "slots_open": slots_at(earned),
                          "tier": ITEMS[choice]["tier"], "slot": ITEMS[choice]["slot"]})

        while todo:
            avail = [s for s in todo if not (s["kind"] == "upgrade" and s["from"] not in owned)]
            cheapest = min(s["cost"] for s in avail)
            pool = [s for s in avail if s["cost"] <= max(2 * cheapest, 800)]
            now = max(earned, 1000)
            ref = ref_at(O["refs"], now)
            base = score_at(hero, owned, now, ref, objective, level)[0] if owned else 0.0
            best = None
            for s in pool:
                trial = [x for x in owned if x != s.get("from")] + [s["item"]]
                val = (score_at(hero, trial, now, ref, objective, level)[0] - base) / max(s["cost"], 1)
                if best is None or val > best[0]:
                    best = (val, s)
            s = best[1]
            needs_slot = s["kind"] == "buy"
            while True:
                short = s["cost"] - cash
                # would a slot be open by the time you can pay for this?
                slot_ok = not needs_slot or len(owned) + 1 <= slots_at(earned + max(0.0, short))
                if slot_ok and short <= 0:
                    break
                if pending:
                    # an item this route drops anyway: keep it until its
                    # refund plus your souls cover the purchase, then swap
                    choice = pick_sale()
                    refund = SELL_REFUND * ITEMS[choice]["cost"]
                    if cash + refund < s["cost"]:
                        earned += s["cost"] - cash - refund
                        cash = s["cost"] - refund
                    sell_one("needs the slot" if not slot_ok else "needs the souls", choice)
                    continue
                if short > 0:
                    earned += short
                    cash = s["cost"]
                if needs_slot and len(owned) + 1 > slots_at(earned):
                    need = min(w for w in WALKER_NET_WORTH if slots_at(w) > len(owned))
                    cash += need - earned
                    earned = need
            cash -= s["cost"]
            if s["kind"] == "upgrade":
                owned.remove(s["from"])
            owned.append(s["item"])
            todo.remove(s)
            _, stats = _stats(hero, owned, max(earned, 1000), objective, O, level)
            steps.append(dict({
                "kind": s["kind"], "item": s["item"], "from": s.get("from"), "cost": s["cost"],
                "stage": label, "at_net_worth": round(earned), "slots": len(owned), "slots_open": slots_at(earned),
                "tier": ITEMS[s["item"]]["tier"], "slot": ITEMS[s["item"]]["slot"],
            }, **stats))
        while pending:
            sell_one("replaced")
        if nw is not None and earned < nw:
            cash += nw - earned
            earned = nw
        assert sorted(owned) == sorted(target), (hero, label, owned, target)
        checkpoints.append({"stage": label, "net_worth": nw if nw is not None else round(earned),
                            "complete_at": round(earned), "items": sorted(owned),
                            "sell_loss": round(loss)})
    return steps, checkpoints, loss


def solve_route(task):
    hero, objective = task
    with open(os.path.join(DATA, "optimization.json"), encoding="utf-8") as f:
        O = json.load(f)
    rng = random.Random(zlib.crc32(f"route|{hero}|{objective}".encode("utf-8")))
    final = table_row(O, objective, "full", hero)["items"]
    value, builds, _, _ = beam_route(hero, objective, O, rng)
    never_sell = beam_route(hero, objective, O, rng, allow_sell=False)[0]
    allocs, scores = allocation_path(hero, builds, objective, O)
    targets = [(stage, nw, b, lv) for (stage, nw), b, lv in zip(STAGES, builds, allocs)]
    end_needed = sorted(final) != sorted(builds[-1])
    if end_needed:
        targets.append(("end", None, final, allocs[-1]))
    item_tl, checkpoints, loss = item_steps(hero, targets, objective, O)
    abil_tl = ability_steps(hero, allocs, builds, objective, O)
    # item steps are already chronological; slot ability points in between
    timeline, a = [], 0
    for step in item_tl:
        while a < len(abil_tl) and abil_tl[a]["at_net_worth"] < step["at_net_worth"]:
            timeline.append(abil_tl[a])
            a += 1
        timeline.append(step)
    timeline += abil_tl[a:]
    for cp, lv, sc in zip(checkpoints, allocs, scores):
        cp.update(score=sc, ability_levels=list(lv))
    if end_needed:
        end_nw = checkpoints[-1]["complete_at"]
        sc = score_at(hero, final, end_nw, ref_at(O["refs"], end_nw), objective, allocs[-1])[0]
        checkpoints[-1].update(score=sc, ability_levels=list(allocs[-1]))
    weights = [STAGE_WEIGHT[s] for s, _ in STAGES]
    independent = [table_row(O, objective, s, hero)["score"] for s, _ in STAGES]
    return hero, objective, {
        "checkpoints": checkpoints,
        "steps": timeline,
        "final_items": sorted(final),
        "final_complete_at": checkpoints[-1]["complete_at"],
        "sell_loss": round(loss),
        "sells": sum(1 for s in timeline if s["kind"] == "sell"),
        # stage-weighted log score of the route vs the best never-sell route
        # (same search, same free ability choice) and vs the per-stage optima
        "route_value": value,
        "no_sell_value": never_sell,
        "gain_vs_never_sell": math.exp(value - never_sell) - 1,
        "upper_bound_value": sum(w * math.log(max(s, 1e-9)) for w, s in zip(weights, independent)),
        "final_abilities": list(allocs[-1]),
    }


def main():
    tasks = [(h, obj) for h in sorted(HEROES) for obj in ("teamfight", "allround")]
    out = {}
    workers = max(1, (os.cpu_count() or 2) - 2)
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as ex:
        for i, (hero, obj, route) in enumerate(ex.map(solve_route, tasks), 1):
            out.setdefault(hero, {})[obj] = route
            if obj == "teamfight":
                gain = route["gain_vs_never_sell"] * 100
                print(f"[{i:2d}/{len(tasks)}] {hero:12s} sells {route['sells']}  loss {route['sell_loss']:5d}  "
                      f"final done at {route['final_complete_at']:,}  vs never-sell {gain:+5.1f}%  "
                      f"tiers {route['final_abilities']}", flush=True)
    with open(os.path.join(DATA, "routes.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"))
    print("wrote data/routes.json")


if __name__ == "__main__":
    main()
