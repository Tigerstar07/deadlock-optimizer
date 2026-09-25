"""
Build optimiser: every hero, every stage, two objectives.

For each hero and net-worth checkpoint, searches the legal shop for the item
set that maximises the scenario-ensemble score from model.py:

  * allround  - pick / skirmish / teamfight mix (the published ranking)
  * teamfight - teamfight scenarios only (sustain + damage under focus fire)

Constraints (deadlock.wiki/Items, steamdb flex-slot page, build client-6698):
  * <= 12 item slots, any category (9 universal + 3 from Walkers)
  * <= 4 active items
  * total spend <= net worth for that stage
  * Tier 5 (Street Brawl) and hero-restricted items excluded

Search, per hero (stages run in order, each seeded with the previous build):
  1. several greedy constructions (by score, by score-per-soul, from the
     previous stage's build)
  2. exhaustive best-improvement add / drop / swap climb -> a verified
     one-exchange local optimum
  3. iterated local search: drop 2-4 items, greedy refill, climb again; keep
     improvements. This escapes one-exchange optima that the Investments step
     function (the 4,800-soul spike) creates.
All evaluations are memoised per (hero, stage). Heroes run in parallel on
every core but two.

The reference opponent is a fixed point: the median hero running its own
optimised build, recomputed until stable.
"""

import argparse
import concurrent.futures
import json
import math
import os
import random
import statistics
import sys
import time
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import (HEROES, ITEMS, Loadout, MAX_SLOTS, MAX_ACTIVES,  # noqa: E402
                   OBJECTIVES, SCENARIOS, SCENARIO_BY_NAME, valid_build,
                   RANGE_GATED, SELF_DAMAGE_PENALTY, WALKER_NET_WORTH, slots_at)

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")

STAGES = [
    ("laning",   6000),
    ("early",   12000),
    ("mid",     20000),
    ("late",    32000),
    ("full",    50000),
]
STAGE_WEIGHT = {"laning": 0.10, "early": 0.15, "mid": 0.30, "late": 0.30, "full": 0.15}

# Item properties the model reads. Items with none of these (and no bespoke
# rule) contribute only their category Investment, so they are
# interchangeable: one representative per (category, cost, active) is kept.
_MODELLED_KEYS = set(
    Loadout.FLAT_SPIRIT + Loadout.WEAPON_PCT + Loadout.FIRERATE_PCT
    + Loadout.CLIP_PCT + Loadout.CLIP_FLAT + Loadout.HEALTH_FLAT
    + Loadout.HEALTH_PCT + Loadout.BULLET_RESIST + Loadout.TECH_RESIST
    + Loadout.BULLET_LIFESTEAL + Loadout.SPIRIT_LIFESTEAL + Loadout.CDR
    + Loadout.ITEM_CDR + Loadout.HP_REGEN + Loadout.BULLET_SHRED
    + Loadout.SPIRIT_SHRED + Loadout.BURST_HEAL + Loadout.HEAL_AMP) | {
    "CloseRangeBonusWeaponPower", "LongRangeBonusWeaponPower", "BonusBaseHealth",
    "CritDamagePercent", "CombatBarrier", "HealthStealPctHero",
    "HealthDrainedPerSecond", "BonusAttackRangePercent", "BulletResistPerStack",
}
_BESPOKE = set(RANGE_GATED) | set(SELF_DAMAGE_PENALTY) | {
    "Mystic Burst", "Quicksilver Reload", "Mercurial Magnum", "Tankbuster",
    "Torment Pulse", "Scourge", "Arctic Blast", "Cold Front", "Silence Wave",
    "Phantom Strike", "Alchemical Fire", "Spirit Burn", "Mystic Shot",
    "Tesla Bullets", "Capacitor", "Toxic Bullets", "Headshot Booster",
    "Headhunter", "Ricochet", "Inhibitor", "Rusted Barrel", "Suppressor",
    "Juggernaut", "Active Reload",
}


def legal_items(hero_name=None):
    return sorted(name for name, it in ITEMS.items()
                  if it["tier"] != 5 and not it["heroes_restricted"] and it["cost"])


def _is_modelled(name):
    it = ITEMS[name]
    if name in _BESPOKE:
        return True
    return any((p.get("value") or 0) and k in _MODELLED_KEYS
               for k, p in it["properties"].items())


def search_pool(hero_name=None):
    """Legal items with stat-less fillers collapsed to one per class."""
    pool, fillers = [], {}
    for name in legal_items(hero_name):
        if _is_modelled(name):
            pool.append(name)
        else:
            it = ITEMS[name]
            fillers.setdefault((it["slot"], it["cost"], it["is_active"]), name)
    return pool + sorted(fillers.values())


def valid(items, budget):
    return valid_build(items, budget)


class Search:
    """Memoised build search for one hero / budget / reference / objective."""

    def __init__(self, hero, budget, ref, objective, pool, rng, net_worth=None):
        self.hero, self.budget, self.ref = hero, budget, ref
        self.objective, self.pool, self.rng = objective, pool, rng
        # net worth sets boons / ability points; budget caps item spend
        self.net_worth = budget if net_worth is None else net_worth
        self.max_slots = slots_at(self.net_worth)
        self.memo = {}
        self.evals = 0

    def score(self, items):
        key = frozenset(items)
        value = self.memo.get(key)
        if value is None:
            self.evals += 1
            value = Loadout(self.hero, list(items), net_worth=self.net_worth).evaluate(
                self.ref, self.objective)[0]
            self.memo[key] = value
        return value

    def _fits(self, items, extra_cost=0, extra_active=False):
        if len(items) >= self.max_slots:
            return False
        if extra_active and sum(1 for n in items if ITEMS[n]["is_active"]) >= MAX_ACTIVES:
            return False
        return sum(ITEMS[n]["cost"] for n in items) + extra_cost <= self.budget

    def greedy(self, start=(), per_soul=False):
        cur = [n for n in start if n in ITEMS]
        while not valid_build(cur, self.budget, self.net_worth):
            cur.pop()
        cur_sc = self.score(cur) if cur else 0.0
        while True:
            best, best_val, best_sc = None, None, None
            spent = sum(ITEMS[n]["cost"] for n in cur)
            actives = sum(1 for n in cur if ITEMS[n]["is_active"])
            if len(cur) >= self.max_slots:
                break
            for cand in self.pool:
                it = ITEMS[cand]
                if cand in cur or spent + it["cost"] > self.budget:
                    continue
                if it["is_active"] and actives >= MAX_ACTIVES:
                    continue
                sc = self.score(cur + [cand])
                val = (sc - cur_sc) / it["cost"] if per_soul else sc
                if best is None or val > best_val:
                    best, best_val, best_sc = cand, val, sc
            if best is None or best_sc <= cur_sc + 1e-12:
                break
            cur.append(best)
            cur_sc = best_sc
        return cur, cur_sc

    def climb(self, items):
        """Best-improvement add/drop/swap to a one-exchange local optimum."""
        cur = list(items)
        cur_sc = self.score(cur)
        while True:
            best, best_sc = None, cur_sc
            spent = sum(ITEMS[n]["cost"] for n in cur)
            actives = sum(1 for n in cur if ITEMS[n]["is_active"])
            cur_set = set(cur)
            for cand in self.pool:
                if cand in cur_set:
                    continue
                it = ITEMS[cand]
                if (len(cur) < self.max_slots and spent + it["cost"] <= self.budget
                        and not (it["is_active"] and actives >= MAX_ACTIVES)):
                    trial = cur + [cand]
                    sc = self.score(trial)
                    if sc > best_sc + 1e-12:
                        best, best_sc = trial, sc
                for i, out in enumerate(cur):
                    o = ITEMS[out]
                    if spent - o["cost"] + it["cost"] > self.budget:
                        continue
                    if (it["is_active"] and not o["is_active"]
                            and actives >= MAX_ACTIVES):
                        continue
                    trial = cur[:i] + cur[i + 1:] + [cand]
                    sc = self.score(trial)
                    if sc > best_sc + 1e-12:
                        best, best_sc = trial, sc
            for i in range(len(cur)):
                trial = cur[:i] + cur[i + 1:]
                sc = self.score(trial)
                if sc > best_sc + 1e-12:
                    best, best_sc = trial, sc
            if best is None:
                return cur, cur_sc
            cur, cur_sc = best, best_sc

    def ils(self, items, iterations):
        best, best_sc = self.climb(items)
        cur, cur_sc = best, best_sc
        for _ in range(iterations):
            k = self.rng.randint(2, min(4, max(2, len(cur))))
            kept = list(cur)
            self.rng.shuffle(kept)
            kept = kept[k:]
            trial, _ = self.greedy(kept, per_soul=self.rng.random() < 0.5)
            trial, trial_sc = self.climb(trial)
            if trial_sc >= cur_sc - 1e-12:
                cur, cur_sc = trial, trial_sc
            if trial_sc > best_sc + 1e-12:
                best, best_sc = trial, trial_sc
        return best, best_sc

    def solve(self, seeds=(), iterations=24):
        starts = [self.greedy()[0], self.greedy(per_soul=True)[0]]
        for seed in seeds:
            if seed:
                starts.append(self.greedy(seed)[0])
        climbed = [self.climb(s) for s in starts]
        items, _ = max(climbed, key=lambda pair: pair[1])
        if iterations:
            items, _ = self.ils(items, iterations)
        return sorted(items), self.score(items)


def ref_at(refs, net_worth):
    """Reference opponent at any net worth (linear between checkpoints)."""
    pts = [(budget, refs[stage]) for stage, budget in STAGES]
    if net_worth <= pts[0][0]:
        return dict(pts[0][1])
    if net_worth >= pts[-1][0]:
        return dict(pts[-1][1])
    for (b0, r0), (b1, r1) in zip(pts, pts[1:]):
        if b0 <= net_worth <= b1:
            t = (net_worth - b0) / (b1 - b0)
            return {k: r0[k] + t * (r1[k] - r0[k]) for k in r0}
    return dict(pts[-1][1])


def make_row(hero, stage, budget, ref, items, objective):
    lo = Loadout(hero, items, net_worth=budget)
    score, levels, results = lo.evaluate(ref, objective)
    weights = OBJECTIVES[objective]
    total_w = sum(weights.values())

    def weighted(field):
        return sum(w * results[name][field] for name, w in weights.items()) / total_w

    bullet_resist, tech_resist = lo.total_resists(levels)
    return {
        "hero": hero, "stage": stage, "budget": budget,
        "score": score, "items": list(items), "spend": lo.spend,
        "boons": lo.boons, "spirit_power": lo.spirit_power,
        "gun_dps": weighted("gun_dps"),
        "ability_dps": weighted("ability_dps"),
        "item_proc_dps": weighted("item_proc_dps"),
        "total_dps": weighted("total_dps"),
        "cleave_dps": weighted("cleave_dps"),
        "heal_ps": weighted("heal_ps"),
        "gross_heal_ps": weighted("gross_heal_ps"),
        "self_drain_ps": weighted("self_drain_ps"),
        "ehp": sum(w * lo.ehp(SCENARIO_BY_NAME[name].bullet_frac, levels)
                   for name, w in weights.items()) / total_w,
        "health": lo.health + lo.ability_bonus_health(levels),
        "bullet_resist": bullet_resist, "tech_resist": tech_resist,
        "bullet_lifesteal": lo.bullet_lifesteal,
        "spirit_lifesteal": lo.ability_lifesteal_total(levels),
        "ability_points": lo.ability_points,
        "ability_levels": list(levels),
        "falloff": weighted("falloff"),
        "ttk": weighted("ttk"), "ttd": weighted("ttd"),
        "sustain_ratio": weighted("sustain_ratio"),
        "unkillable": results[max(weights, key=weights.get)]["unkillable"],
        "scenario_scores": {name: results[name]["score"] for name in weights},
    }


def solve_hero(task):
    """All stages for one hero, each seeded with the previous stage's build."""
    hero, refs, objective, iterations, seeds_by_stage = task
    pool = search_pool(hero)
    rng = random.Random(zlib.crc32(f"{hero}|{objective}".encode("utf-8")))
    rows, prev = [], []
    for stage, budget in STAGES:
        search = Search(hero, budget, refs[stage], objective, pool, rng)
        seeds = [prev] + list((seeds_by_stage or {}).get(stage, []))
        items, _ = search.solve(seeds, iterations)
        rows.append(make_row(hero, stage, budget, refs[stage], items, objective))
        prev = items
    return hero, rows


def run_all(refs, objective, iterations, workers, seeds=None, label=""):
    tasks = [(hero, refs, objective, iterations, (seeds or {}).get(hero))
             for hero in sorted(HEROES)]
    out = {}
    t0 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(solve_hero, t) for t in tasks]
        for i, fut in enumerate(concurrent.futures.as_completed(futures), 1):
            hero, rows = fut.result()
            out[hero] = rows
            print(f"  {label}[{i:2d}/{len(tasks)}] {hero:12s} "
                  + " ".join(f"{r['score']:.3f}" for r in rows)
                  + f"  ({time.time() - t0:.0f}s)", flush=True)
    return out


def reference_from(solved, refs_in):
    """Median stats of every hero's solved build, per stage."""
    refs = {}
    for stage, budget in STAGES:
        healths, ehps, dpss, brs, trs, bss, sss = [], [], [], [], [], [], []
        for hero, rows in solved.items():
            row = next(r for r in rows if r["stage"] == stage)
            lo = Loadout(hero, row["items"], net_worth=budget)
            levels = tuple(row["ability_levels"])
            br, tr = lo.total_resists(levels)
            bs, ss = lo.total_shreds(levels)
            bss.append(bs)
            sss.append(ss)
            healths.append(lo.health + lo.ability_bonus_health(levels) + lo.barrier_pool(levels))
            ehps.append(lo.ehp(0.6, levels))
            # pre-mitigation damage: the defender's own resists apply later
            res = lo.scenario_result(refs_in[stage], SCENARIO_BY_NAME["skirmish"], levels)
            dpss.append(res["raw_total_dps"])
            brs.append(br)
            trs.append(tr)
        refs[stage] = {
            "health": statistics.median(healths), "ehp": statistics.median(ehps),
            "dps": statistics.median(dpss),
            "bullet_resist": statistics.median(brs),
            "tech_resist": statistics.median(trs),
            "bullet_shred": statistics.median(bss),
            "spirit_shred": statistics.median(sss),
        }
    return refs


def stage_tables(solved):
    stages = {}
    for stage, _ in STAGES:
        rows = [next(r for r in solved[h] if r["stage"] == stage) for h in solved]
        rows.sort(key=lambda r: -r["score"])
        stages[stage] = rows
    overall = {hero: sum(STAGE_WEIGHT[r["stage"]] * r["score"] for r in rows)
               for hero, rows in solved.items()}
    return stages, overall


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 2))
    parser.add_argument("--iterations", type=int, default=24,
                        help="iterated-local-search rounds per hero-stage")
    parser.add_argument("--ref-passes", type=int, default=3)
    args = parser.parse_args()

    t0 = time.time()
    refs = {stage: {"health": 900 + budget * 0.09, "ehp": 1500 + budget * 0.15,
                    "dps": 90 + budget * 0.012, "bullet_resist": 15.0, "tech_resist": 15.0,
                    "bullet_shred": 0.0, "spirit_shred": 0.0}
            for stage, budget in STAGES}
    history = []
    for p in range(args.ref_passes):
        print(f"\n=== reference pass {p + 1}/{args.ref_passes} ===", flush=True)
        quick = run_all(refs, "allround", 4 if p else 0, args.workers, label="ref ")
        new_refs = reference_from(quick, refs)
        drift = max(abs(new_refs[s][k] - refs[s][k]) / max(1.0, abs(refs[s][k]))
                    for s, _ in STAGES for k in ("health", "dps"))
        refs = new_refs
        history.append(drift)
        for stage, _ in STAGES:
            r = refs[stage]
            print(f"  {stage:6s} HP {r['health']:6.0f}  DPS {r['dps']:5.0f}  "
                  f"BR {r['bullet_resist']:4.1f}%  SR {r['tech_resist']:4.1f}%  "
                  f"shred B {r['bullet_shred']:4.1f}% S {r['spirit_shred']:4.1f}%")
        print(f"  max drift {drift:.1%}")

    results = {}
    for objective in ("allround", "teamfight"):
        print(f"\n=== solving objective: {objective} ===", flush=True)
        solved = run_all(refs, objective, args.iterations, args.workers, label=objective[:4] + " ")
        stages, overall = stage_tables(solved)
        results[objective] = {"stages": stages, "overall": overall}
        top = sorted(overall.items(), key=lambda kv: -kv[1])[:10]
        print(f"  top: " + ", ".join(f"{h} {s:.3f}" for h, s in top))

    out = {
        "stages": results["allround"]["stages"],
        "overall": results["allround"]["overall"],
        "teamfight": results["teamfight"],
        "refs": refs,
        "stage_weight": STAGE_WEIGHT,
        "model": {
            "score": "weighted geometric mean of combat scenarios",
            "objectives": OBJECTIVES,
            "scenarios": {s.name: s._asdict() for s in SCENARIOS},
            "max_slots": MAX_SLOTS, "max_actives": MAX_ACTIVES,
            "slots_by_stage": {stage: slots_at(budget) for stage, budget in STAGES},
            "walker_net_worth": list(WALKER_NET_WORTH),
            "reference": "median hero on its own solved build (fixed point)",
            "reference_drift": history,
            "optimization": (f"greedy x3 + exhaustive add/drop/swap climb + "
                             f"{args.iterations}-round iterated local search"),
            "runtime_s": round(time.time() - t0, 1),
        },
    }
    with open(os.path.join(DATA, "optimization.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print(f"\nwrote data/optimization.json in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
