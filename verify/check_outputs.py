"""Audit every generated build and purchase order against the live model.

Recomputes every published row (both objectives) from scratch, re-checks shop
legality, replays every purchase order, and with --deep re-runs the exhaustive
add/drop/swap climb to prove each build is a one-exchange local optimum.
Any hand-edited or stale number fails loudly.
"""

import argparse
import concurrent.futures
import json
import math
import os
import random
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from model import (ABILITY_TIER_COST, HEROES, ITEMS, MAX_ACTIVES,  # noqa: E402
                   ability_points_for_networth, slots_at)
from optimize import STAGES, STAGE_WEIGHT, Search, make_row, search_pool  # noqa: E402

CHECKED_FIELDS = ("score", "spend", "gun_dps", "ability_dps", "total_dps",
                  "heal_ps", "ehp", "bullet_resist", "tech_resist")


def close(actual, expected, label, rel=1e-8, abs_=1e-7):
    if not math.isclose(float(actual), float(expected), rel_tol=rel, abs_tol=abs_):
        raise AssertionError(f"{label}: stored {actual!r}, recomputed {expected!r}")


def check_table(stages, overall, refs, objective):
    rows_by_key = {}
    heroes = set(HEROES)
    if set(stages) != {s for s, _ in STAGES}:
        raise AssertionError(f"{objective}: stage mismatch {sorted(stages)}")
    for stage, budget in STAGES:
        rows = stages[stage]
        if {r["hero"] for r in rows} != heroes or len(rows) != len(heroes):
            raise AssertionError(f"{objective}/{stage}: hero set mismatch")
        if rows != sorted(rows, key=lambda r: -r["score"]):
            raise AssertionError(f"{objective}/{stage}: rows are not score-sorted")
        for row in rows:
            label = f"{objective}:{row['hero']}|{stage}"
            items = row["items"]
            if row["budget"] != budget or row["stage"] != stage:
                raise AssertionError(f"{label}: wrong budget/stage")
            if len(items) != len(set(items)):
                raise AssertionError(f"{label}: duplicate item")
            if set(items) - set(ITEMS):
                raise AssertionError(f"{label}: unknown items")
            if len(items) > slots_at(budget):
                raise AssertionError(f"{label}: {len(items)} items > {slots_at(budget)} slots at {budget}")
            if sum(bool(ITEMS[i]["is_active"]) for i in items) > MAX_ACTIVES:
                raise AssertionError(f"{label}: too many actives")
            if sum(ITEMS[i]["cost"] for i in items) > budget:
                raise AssertionError(f"{label}: over budget")
            if any(ITEMS[i]["tier"] == 5 or ITEMS[i]["heroes_restricted"] for i in items):
                raise AssertionError(f"{label}: excluded item")
            fresh = make_row(row["hero"], stage, budget, refs[stage], items, objective)
            for field in CHECKED_FIELDS:
                close(row[field], fresh[field], f"{label} {field}")
            if row["ability_levels"] != fresh["ability_levels"]:
                raise AssertionError(f"{label}: ability-level mismatch")
            rows_by_key[(row["hero"], stage)] = row
    for hero in heroes:
        expected = sum(STAGE_WEIGHT[s] * rows_by_key[(hero, s)]["score"] for s, _ in STAGES)
        close(overall[hero], expected, f"{objective}:{hero} overall")
    return rows_by_key


def check_orders(orders, rows_by_key, suffix):
    for (hero, stage), row in rows_by_key.items():
        key = f"{hero}|{stage}{suffix}"
        steps = orders.get(key)
        if steps is None:
            raise AssertionError(f"missing purchase order {key}")
        owned, running = [], 0
        for step in steps:
            if step["kind"] == "upgrade":
                if step["from"] not in owned:
                    raise AssertionError(f"{key}: upgrades missing component {step['from']}")
                owned.remove(step["from"])
            elif step["kind"] != "buy":
                raise AssertionError(f"{key}: unknown step kind {step['kind']!r}")
            if step["item"] in owned:
                raise AssertionError(f"{key}: buys duplicate {step['item']}")
            owned.append(step["item"])
            running += step["cost"]
            if step["running"] != running or step["slots"] != len(owned):
                raise AssertionError(f"{key}: invalid running total or slot count")
            if len(owned) > slots_at(step["net_worth"]):
                raise AssertionError(f"{key}: holds {len(owned)} items at {step['net_worth']} net worth "
                                     f"({slots_at(step['net_worth'])} slots)")
        if set(owned) != set(row["items"]) or running != row["spend"]:
            raise AssertionError(f"{key}: order does not end in the solved build")


def check_routes(routes, tables):
    """Replay every full-game route: souls, slots, sells, components, abilities."""
    for hero, by_obj in routes.items():
        for objective, route in by_obj.items():
            key = f"route {objective}:{hero}"
            owned, spent, refunds, last_nw = [], 0.0, 0.0, 0
            tiers = [0] * len(HEROES[hero]["abilities"])
            stage_owned = {}
            for step in route["steps"]:
                nw = step["at_net_worth"]
                if nw < last_nw:
                    raise AssertionError(f"{key}: timeline goes back in time at {step}")
                last_nw = nw
                kind = step["kind"]
                if kind == "ability":
                    i, t = step["index"], step["tier"]
                    if t != tiers[i] + 1:
                        raise AssertionError(f"{key}: ability tier jump {step}")
                    tiers[i] = t
                    used = sum(ABILITY_TIER_COST[x] for x in tiers)
                    if used > ability_points_for_networth(HEROES[hero], nw):
                        raise AssertionError(f"{key}: spends {used} points at {nw}")
                    continue
                item = step["item"]
                if kind == "sell":
                    if item not in owned:
                        raise AssertionError(f"{key}: sells unowned {item}")
                    if not math.isclose(step["refund"], round(0.5 * ITEMS[item]["cost"])):
                        raise AssertionError(f"{key}: wrong refund for {item}")
                    owned.remove(item)
                    refunds += step["refund"]
                else:
                    if kind == "upgrade":
                        if step["from"] not in owned:
                            raise AssertionError(f"{key}: upgrades missing component {step['from']}")
                        if step["cost"] != ITEMS[item]["cost"] - ITEMS[step["from"]]["cost"]:
                            raise AssertionError(f"{key}: wrong upgrade cost for {item}")
                        owned.remove(step["from"])
                    elif step["cost"] != ITEMS[item]["cost"]:
                        raise AssertionError(f"{key}: wrong price for {item}")
                    if item in owned:
                        raise AssertionError(f"{key}: buys duplicate {item}")
                    owned.append(item)
                    spent += step["cost"]
                if spent - refunds > nw + 1:
                    raise AssertionError(f"{key}: spends {spent - refunds:.0f} of {nw} souls")
                if len(owned) > slots_at(nw):
                    raise AssertionError(f"{key}: {len(owned)} items with {slots_at(nw)} slots at {nw}")
                if sum(ITEMS[x]["is_active"] for x in owned) > MAX_ACTIVES:
                    raise AssertionError(f"{key}: more than {MAX_ACTIVES} actives")
                stage_owned[step["stage"]] = sorted(owned)
            for cp in route["checkpoints"]:
                if stage_owned.get(cp["stage"]) != sorted(cp["items"]):
                    raise AssertionError(f"{key}: checkpoint {cp['stage']} does not match the replay")
            full = next(r for r in tables[objective]["full"] if r["hero"] == hero)["items"]
            if sorted(owned) != sorted(full) or sorted(route["final_items"]) != sorted(full):
                raise AssertionError(f"{key}: route does not end in the solved full build")
            if tiers != [3] * len(tiers) or route["final_abilities"] != tiers:
                raise AssertionError(f"{key}: abilities not all maxed at the end ({tiers})")


def _deep_one(task):
    hero, stage, budget, ref, items, score, objective = task
    search = Search(hero, budget, ref, objective, search_pool(hero), random.Random(0))
    climbed, climbed_score = search.climb(items)
    return hero, stage, objective, climbed_score, score, sorted(climbed) == sorted(items)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--deep", action="store_true",
                        help="also exhaust every legal add/drop/swap neighbour")
    args = parser.parse_args()
    with open(os.path.join(ROOT, "data", "optimization.json"), encoding="utf-8") as f:
        data = json.load(f)
    refs = data["refs"]

    tables = [("allround", data["stages"], data["overall"], "")]
    if data.get("teamfight"):
        tables.append(("teamfight", data["teamfight"]["stages"],
                       data["teamfight"]["overall"], "|teamfight"))

    orders_path = os.path.join(ROOT, "data", "orders.json")
    orders = json.load(open(orders_path, encoding="utf-8")) if os.path.exists(orders_path) else None

    all_rows = []
    for objective, stages, overall, suffix in tables:
        rows = check_table(stages, overall, refs, objective)
        print(f"PASS: {objective}: recomputed {len(rows)} builds for {len(HEROES)} heroes")
        if orders is not None:
            check_orders(orders, rows, suffix)
            print(f"PASS: {objective}: replayed {len(rows)} purchase orders")
        all_rows += [(objective, row) for row in rows.values()]

    routes_path = os.path.join(ROOT, "data", "routes.json")
    if os.path.exists(routes_path):
        routes = json.load(open(routes_path, encoding="utf-8"))
        stage_tables = {obj: st for obj, st, _, _ in tables}
        check_routes(routes, stage_tables)
        n = sum(len(v) for v in routes.values())
        print(f"PASS: replayed {n} full-game routes (souls, slots, sells, components, all abilities maxed)")

    if args.deep:
        tasks = [(r["hero"], r["stage"], r["budget"], refs[r["stage"]], r["items"], r["score"], obj)
                 for obj, r in all_rows]
        workers = max(1, (os.cpu_count() or 2) - 2)
        with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as ex:
            for hero, stage, obj, climbed, stored, same in ex.map(_deep_one, tasks, chunksize=2):
                if not same or climbed > stored * (1 + 1e-9):
                    raise AssertionError(
                        f"{obj}:{hero}|{stage}: a one-item exchange improves "
                        f"{stored:.6f} -> {climbed:.6f}")
        print(f"PASS: all {len(tasks)} builds are one-exchange local optima")


if __name__ == "__main__":
    main()
