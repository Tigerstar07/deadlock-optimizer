"""
Benchmark real-match builds against the solver.

Each case is a build someone actually played. It is scored at its own net
worth, then the solver searches for the best build for the same hero at
  (a) the same net worth (every soul spent on items), and
  (b) the same item spend (what the player actually had in their slots),
so "the model's build is better" is never just "the model had more souls".

    python scripts/benchmarks.py      -> data/benchmarks.json
"""

import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import ITEMS, Loadout, valid_build  # noqa: E402
from optimize import STAGES, Search, ref_at, search_pool  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

CASES = [
    {
        "id": "match_drifter_57k",
        "label": "Enemy Drifter from your match — 21 / 2 / 17, 93k player damage, 36k healing",
        "note": ("Scoreboard at 57k net worth. The 11 item icons were matched against the official "
                 "shop art (correlation 0.70–0.95 each). It spends only 33.6k of 57k on items. "
                 "It is a pick / stealth tempo build (Veil Walker invisibility, Stalker reveal, "
                 "Kinetic Dash, Trophy Collector snowball): it wins by choosing fights, which this "
                 "sustained-combat model does not price. In a drawn-out teamfight the model rates it "
                 "far below a lifesteal + shred build."),
        "hero": "Drifter",
        "net_worth": 57000,
        "items": ["Stalker", "Trophy Collector", "Kinetic Dash", "Fortitude", "Veil Walker",
                  "Point Blank", "Weighted Shots", "Hollow Point", "Hunter's Aura",
                  "Burst Fire", "Vampiric Burst"],
    },
]


def summarize(hero, items, net_worth, ref):
    lo = Loadout(hero, items, net_worth=net_worth)
    tf, levels, res = lo.evaluate(ref, "teamfight")
    ar = Loadout(hero, items, net_worth=net_worth).evaluate(ref, "allround")[0]
    t = res["teamfight"]
    return {
        "items": sorted(items), "spend": lo.spend, "teamfight": tf, "allround": ar,
        "tf_dps": t["total_dps"], "tf_splash": t["cleave_dps"], "tf_heal": t["heal_ps"],
        "tf_ttk": t["ttk"], "tf_ttd": t["ttd"], "ehp": lo.ehp(0.55, levels),
        "ability_levels": list(levels),
        "scenarios": {k: v["score"] for k, v in res.items()},
    }


def solve(hero, budget, net_worth, ref, seeds, iterations=16):
    search = Search(hero, budget, ref, "teamfight", search_pool(hero),
                    random.Random(11), net_worth=net_worth)
    starts = [search.greedy()[0]]
    for seed in seeds:
        trimmed = sorted((s for s in seed if s in ITEMS), key=lambda n: -ITEMS[n]["cost"])
        while trimmed and not valid_build(trimmed, budget, net_worth):
            trimmed.pop()
        starts.append(search.greedy(trimmed)[0])
    best = max((search.climb(s) for s in starts), key=lambda p: p[1])[0]
    best, _ = search.ils(best, iterations)
    return best


def main():
    with open(os.path.join(DATA, "optimization.json"), encoding="utf-8") as f:
        O = json.load(f)
    out = {"cases": []}
    for case in CASES:
        hero, nw = case["hero"], case["net_worth"]
        ref = ref_at(O["refs"], nw)
        given = summarize(hero, case["items"], nw, ref)
        solved_rows = [r for st, _ in STAGES for r in O["teamfight"]["stages"][st] if r["hero"] == hero]
        seeds = [case["items"]] + [r["items"] for r in solved_rows[-2:]]
        best_nw = solve(hero, nw, nw, ref, seeds)
        best_spend = solve(hero, given["spend"], nw, ref, seeds)
        solved = summarize(hero, best_nw, nw, ref)
        same = summarize(hero, best_spend, nw, ref)
        entry = dict(case, given=given, solved=solved, solved_same_spend=same)
        entry["same_budget"] = (
            f"Held to the same {given['spend']:,} souls of items the player had, the best "
            f"teamfight build scores {same['teamfight']:.3f} ({same['teamfight'] / given['teamfight']:.2f}× theirs): "
            + ", ".join(same["items"]) + ".")
        out["cases"].append(entry)
        print(f"{case['id']}: given {given['teamfight']:.3f} | same spend {same['teamfight']:.3f} "
              f"| full {nw:,} {solved['teamfight']:.3f}")
        print("  same-spend build:", same["items"])
        print("  full build:     ", solved["items"])
    with open(os.path.join(DATA, "benchmarks.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("wrote data/benchmarks.json")


if __name__ == "__main__":
    main()
