"""
How much does the teamfight ranking depend on the model's judgment calls?

Re-scores every hero's solved teamfight builds (all five stages, fixed items)
under alternative values of the three assumptions that are not read from the
game files, and reports each hero's stage-weighted rank per variant:

  FIGHT_WINDOW        engagement length (s)            15 / 20 / 30
  NET_INCOMING_FLOOR  share of damage healing can't stop 0.15 / 0.25 / 0.40
  CLEAVE_VALUE        value of splash vs focused damage  0.25 / 0.50 / 0.75

Builds are not re-solved per variant, so a hero's score under a variant is a
lower bound; the question is only whether the top of the table is stable.

    python scripts/sensitivity.py   -> data/sensitivity.json
"""

import concurrent.futures
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model  # noqa: E402
from optimize import STAGE_WEIGHT, STAGES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

VARIANTS = [("baseline", {})]
for key, values in (("FIGHT_WINDOW", (15.0, 30.0)),
                    ("NET_INCOMING_FLOOR", (0.15, 0.40)),
                    ("CLEAVE_VALUE", (0.25, 0.75))):
    for v in values:
        VARIANTS.append((f"{key}={v:g}", {key: v}))


def score_variant(task):
    name, overrides, rows, refs = task
    for k, v in overrides.items():
        setattr(model, k, v)
    overall = {}
    for (hero, stage, budget, items) in rows:
        lo = model.Loadout(hero, items, net_worth=budget)
        overall[hero] = overall.get(hero, 0.0) + STAGE_WEIGHT[stage] * lo.evaluate(refs[stage], "teamfight")[0]
    return name, overall


def main():
    with open(os.path.join(DATA, "optimization.json"), encoding="utf-8") as f:
        O = json.load(f)
    tf = O["teamfight"]["stages"]
    rows = [(r["hero"], st, r["budget"], r["items"]) for st, _ in STAGES for r in tf[st]]
    tasks = [(name, ov, rows, O["refs"]) for name, ov in VARIANTS]
    with concurrent.futures.ProcessPoolExecutor(max_workers=min(len(tasks), os.cpu_count() or 2)) as ex:
        results = dict(ex.map(score_variant, tasks))
    ranks = {}
    for name, overall in results.items():
        order = sorted(overall, key=lambda h: -overall[h])
        ranks[name] = {h: i + 1 for i, h in enumerate(order)}
    base = results["baseline"]
    top = sorted(base, key=lambda h: -base[h])[:10]
    summary = {h: {"baseline_rank": ranks["baseline"][h],
                   "best_rank": min(r[h] for r in ranks.values()),
                   "worst_rank": max(r[h] for r in ranks.values())} for h in top}
    out = {"variants": [n for n, _ in VARIANTS], "ranks": ranks,
           "top10": summary, "winners": {n: min(r, key=r.get) for n, r in ranks.items()}}
    with open(os.path.join(DATA, "sensitivity.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("winner per variant:")
    for n, h in out["winners"].items():
        print(f"  {n:24s} {h}")
    print("top-10 rank ranges:")
    for h, s in summary.items():
        print(f"  {h:12s} #{s['baseline_rank']}  (range #{s['best_rank']}-#{s['worst_rank']})")
    print("wrote data/sensitivity.json")


if __name__ == "__main__":
    main()
