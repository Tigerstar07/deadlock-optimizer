"""
Deeper niches: counter builds, signature items, and the model vs real players.

  1. Counter / archetype builds (late 32k and full 50k) for every hero:
       vs gun-heavy team   -- the bullet-heavy teamfight scenario only
       vs spirit-heavy team -- the spirit-heavy teamfight scenario only
       pick / assassin      -- the isolated 1v1 pick scenario only
     each solved from the teamfight build with iterated local search.
  2. Signature items: how much each item is worth to a hero's late teamfight
     build (its best single swap in, or what the build loses without it),
     relative to what the same item is worth to the median hero. The top
     ratios are the hero's unusual synergies.
  3. The model vs Ascendant 1+ players (data/item_meta_source.json):
       hidden gems -- the model values them, under 10% of players buy them
       traps       -- 25%+ of players buy them, the model would swap them out
     plus per hero-item pick rate, smoothed win rate and average buy minute
     (shown next to every step of the purchase routes).

Item win rates are descriptive: items bought late appear mostly in long,
already-won games, so gems and traps are ranked by the model's value and
the win rate is shown only as context.

    python scripts/niches.py   -> data/niches.json
"""

import concurrent.futures
import json
import os
import random
import statistics
import sys
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import HEROES, ITEMS, Loadout, valid_build  # noqa: E402
from optimize import Search, search_pool, legal_items  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

ARCHETYPES = {
    "vs_gun": ("vs gun-heavy team", {"bullet_team": 1.0}),
    "vs_spirit": ("vs spirit-heavy team", {"spirit_team": 1.0}),
    "pick": ("pick / assassin", {"pick": 1.0}),
}
ARCH_STAGES = (("late", 32000), ("full", 50000))
PRIOR = 150        # empirical-Bayes prior matches for item win rates
GEM_MAX_PICK = 0.10
TRAP_MIN_PICK = 0.25


def teamfight_row(O, stage, hero):
    return next(r for r in O["teamfight"]["stages"][stage] if r["hero"] == hero)


def solve_archetypes(task):
    hero, O = task
    rng = random.Random(zlib.crc32(f"niche|{hero}".encode("utf-8")))
    pool = search_pool(hero)
    out = {}
    for stage, nw in ARCH_STAGES:
        ref = O["refs"][stage]
        base = teamfight_row(O, stage, hero)["items"]
        out[stage] = {}
        for key, (label, weights) in ARCHETYPES.items():
            s = Search(hero, nw, ref, weights, pool, rng)
            items, sc = s.solve([base], iterations=6)
            base_sc = Loadout(hero, base, net_worth=nw).evaluate(ref, weights)[0]
            tf_sc = Loadout(hero, items, net_worth=nw).evaluate(ref, "teamfight")[0]
            out[stage][key] = {
                "label": label, "items": sorted(items), "score": sc,
                "teamfight_build_score": base_sc,
                "gain_vs_teamfight_build": sc / base_sc - 1 if base_sc > 0 else 0.0,
                "teamfight_score": tf_sc,
                "added": sorted(set(items) - set(base)),
                "removed": sorted(set(base) - set(items)),
            }
    return hero, out


def item_values(task):
    """Value of every item to one hero's late teamfight build."""
    hero, O = task
    ref, nw = O["refs"]["late"], 32000
    base = teamfight_row(O, "late", hero)["items"]

    def sc(items):
        return Loadout(hero, list(items), net_worth=nw).evaluate(ref, "teamfight")[0]

    base_sc = sc(base)
    values = {}
    for item in legal_items(hero):
        if item in base:
            rest = [x for x in base if x != item]
            values[item] = base_sc / max(sc(rest), 1e-9)
            continue
        best = None
        for trial in [base + [item]] + [[x for x in base if x != out] + [item] for out in base]:
            if valid_build(trial, nw):
                v = sc(trial) / base_sc
                best = v if best is None else max(best, v)
        if best is not None:
            values[item] = best
    return hero, values


def main():
    with open(os.path.join(DATA, "optimization.json"), encoding="utf-8") as f:
        O = json.load(f)
    heroes = sorted(HEROES)
    workers = max(1, (os.cpu_count() or 2) - 2)
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as ex:
        archetypes = dict(ex.map(solve_archetypes, [(h, O) for h in heroes]))
        values = dict(ex.map(item_values, [(h, O) for h in heroes]))
    print(f"solved {sum(len(s) for a in archetypes.values() for s in a.values())} counter builds")

    # ---- signature items: value on this hero / value on the median hero
    medians = {}
    for item in {i for v in values.values() for i in v}:
        vs = [v[item] for v in values.values() if item in v]
        medians[item] = statistics.median(vs)
    signature = {}
    for hero, v in values.items():
        rows = [{"item": i, "value": val, "median": medians[i], "synergy": val / medians[i]}
                for i, val in v.items() if val >= 1.02]
        rows.sort(key=lambda r: -r["synergy"])
        signature[hero] = rows[:4]

    # ---- the model vs Ascendant+ players
    meta_src = json.load(open(os.path.join(DATA, "item_meta_source.json"), encoding="utf-8"))
    item_by_id = {it["id"]: n for n, it in ITEMS.items()}
    hero_by_id = {h["id"]: n for n, h in HEROES.items()}
    hero_stats = {hero_by_id[r["hero_id"]]: r for r in meta_src["hero_stats"] if r["hero_id"] in hero_by_id}
    meta, gems, traps = {}, {}, {}
    for r in meta_src["by_hero"]:
        hero, item = hero_by_id.get(r["bucket"]), item_by_id.get(r["item_id"])
        if not hero or not item or hero not in hero_stats:
            continue
        hs = hero_stats[hero]
        base_wr = hs["wins"] / max(hs["matches"], 1)
        pick = r["matches"] / max(hs["matches"], 1)
        wr = (r["wins"] + PRIOR * base_wr) / (r["matches"] + PRIOR)
        meta.setdefault(hero, {})[item] = [round(pick, 4), round(wr, 4),
                                           round(r["avg_buy_time_s"] / 60, 1), r["matches"]]
    # Everything the model ever buys for a hero: the full-game route includes
    # early items that are sold later, which is what player purchase counts
    # include too. Falls back to the late + full builds without routes.
    routes_path = os.path.join(DATA, "routes.json")
    routes = json.load(open(routes_path, encoding="utf-8")) if os.path.exists(routes_path) else {}

    def model_items(hero):
        r = (routes.get(hero) or {}).get("teamfight")
        if r:
            return {s["item"] for s in r["steps"] if s["kind"] in ("buy", "upgrade")}
        return set(teamfight_row(O, "late", hero)["items"]) | set(teamfight_row(O, "full", hero)["items"])

    bought = {h: model_items(h) for h in heroes}
    for hero in heroes:
        m, v = meta.get(hero, {}), values[hero]
        hs = hero_stats.get(hero, {"wins": 0, "matches": 1})
        base_wr = hs["wins"] / max(hs["matches"], 1)
        in_build = bought[hero]
        g, t = [], []
        for item, val in v.items():
            pick = m.get(item, [0, base_wr, None, 0])
            if val >= 1.03 and pick[0] <= GEM_MAX_PICK and ITEMS[item]["tier"] >= 2:
                g.append({"item": item, "value": val, "pick_rate": pick[0], "win_rate": pick[1],
                          "buy_min": pick[2], "matches": pick[3], "in_build": item in in_build})
            if pick[0] >= TRAP_MIN_PICK and val < 0.99 and item not in in_build:
                t.append({"item": item, "value": val, "pick_rate": pick[0], "win_rate": pick[1],
                          "buy_min": pick[2], "matches": pick[3]})
        gems[hero] = sorted(g, key=lambda r: -r["value"])[:5]
        traps[hero] = sorted(t, key=lambda r: -r["pick_rate"])[:4]

    # ---- whole-roster view per item
    total_matches = sum(r["matches"] for r in hero_stats.values()) / 12 or 1
    overall = {item_by_id[r["item_id"]]: r for r in meta_src["overall"] if r["item_id"] in item_by_id}
    roster = []
    for item in sorted({i for v in values.values() for i in v}):
        share = sum(1 for h in heroes if item in bought[h]) / len(heroes)
        o = overall.get(item)
        players = (o["matches"] / (total_matches * 12)) if o else 0.0
        roster.append({"item": item, "model_share": share, "player_share": players,
                       "median_value": medians[item],
                       "win_rate": (o["wins"] / o["matches"]) if o and o["matches"] else None,
                       "buy_min": round(o["avg_buy_time_s"] / 60, 1) if o else None})
    roster.sort(key=lambda r: -(r["model_share"] - r["player_share"]))

    out = {
        "meta_info": {"fetched_at": meta_src["fetched_at"], "rank_filter": meta_src["rank_filter"],
                      "patch": meta_src["patch"], "matches": round(total_matches),
                      "prior_matches": PRIOR, "gem_max_pick": GEM_MAX_PICK,
                      "trap_min_pick": TRAP_MIN_PICK},
        "archetypes": archetypes, "signature": signature,
        "gems": gems, "traps": traps, "meta": meta, "roster": roster,
    }
    with open(os.path.join(DATA, "niches.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"))
    top_gap = roster[:5]
    print("model likes more than players:", [(r["item"], round(r["model_share"], 2), round(r["player_share"], 2)) for r in top_gap])
    print("players like more than model:", [(r["item"], round(r["model_share"], 2), round(r["player_share"], 2)) for r in roster[-5:]])
    print("wrote data/niches.json")


if __name__ == "__main__":
    main()
