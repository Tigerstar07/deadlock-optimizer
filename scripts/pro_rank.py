"""Build a reproducible pro-leaning hero evidence ranking.

This deliberately remains separate from the build optimizer.  Item builds are
still selected by the mechanics model; this layer asks whether high-skill
outcomes, draft pressure and a small amount of measurable macro contribution
change the cross-hero conclusion.

Run with ``--refresh`` after a patch to fetch a new Ascendant+ ranked sample
from the documented Deadlock API analytics endpoints.  The raw response and
exact query parameters are saved so future results remain auditable.
"""

from __future__ import annotations

import argparse
import bisect
import datetime as dt
import json
import math
import os
import urllib.parse
import urllib.request

from model import HEROES


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SOURCE = os.path.join(DATA, "pro_meta_source.json")
OUTPUT = os.path.join(DATA, "pro_ranking.json")
API = "https://api.deadlock-api.com/v1/analytics"

# Current shipped-data baseline.  Keeping this explicit prevents a silent mix
# of pre- and post-patch match results.
PATCH = "Minor Update 09-16-2026"
# Exact Steam News publication timestamp from data/steamnews.json.  Midnight
# would leak roughly twenty hours of pre-patch matches into the sample.
PATCH_START = "2026-09-16T20:16:43+00:00"
MIN_AVERAGE_BADGE = 101  # Ascendant 1+
PRIOR_MATCHES = 500

WEIGHTS = {
    "combat": 0.35,
    "high_skill_outcome": 0.40,
    "draft_priority": 0.15,
    "macro_breadth": 0.10,
}

SENSITIVITY = {
    "balanced": WEIGHTS,
    "outcome_heavy": {
        "combat": 0.20, "high_skill_outcome": 0.55,
        "draft_priority": 0.15, "macro_breadth": 0.10,
    },
    "model_heavy": {
        "combat": 0.50, "high_skill_outcome": 0.30,
        "draft_priority": 0.10, "macro_breadth": 0.10,
    },
    "draft_heavy": {
        "combat": 0.25, "high_skill_outcome": 0.35,
        "draft_priority": 0.30, "macro_breadth": 0.10,
    },
}


def request_url(endpoint: str, *, min_badge=MIN_AVERAGE_BADGE, max_badge=None) -> str:
    timestamp = int(dt.datetime.fromisoformat(PATCH_START).timestamp())
    params = {
        "bucket": "no_bucket",
        "game_mode": "normal",
        "match_mode": "ranked",
        "min_unix_timestamp": timestamp,
    }
    if min_badge is not None:
        params["min_average_badge"] = min_badge
    if max_badge is not None:
        params["max_average_badge"] = max_badge
    if endpoint == "hero-ban-stats":
        params.pop("game_mode")
    return f"{API}/{endpoint}?{urllib.parse.urlencode(params)}"


def fetch_json(url: str):
    request = urllib.request.Request(url, headers={"User-Agent": "deadlock-math-audit/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def refresh_source():
    stats_url = request_url("hero-stats")
    bans_url = request_url("hero-ban-stats")
    all_url = request_url("hero-stats", min_badge=None)
    low_url = request_url("hero-stats", min_badge=None, max_badge=86)
    payload = {
        "fetched_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "patch": PATCH,
        "patch_start": PATCH_START,
        "rank_filter": "Ascendant 1+",
        "min_average_badge": MIN_AVERAGE_BADGE,
        "stats_url": stats_url,
        "bans_url": bans_url,
        "all_url": all_url,
        "low_url": low_url,
        "hero_stats": fetch_json(stats_url),
        "hero_bans": fetch_json(bans_url),
        "all_stats": fetch_json(all_url),
        "low_stats": fetch_json(low_url),
    }
    with open(SOURCE, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=1)
    # Keep the site's contextual win-rate columns on the same exact patch
    # window instead of silently mixing in older snapshots.
    for filename, rows in (
        ("hero_meta.json", payload["all_stats"]),
        ("hero_meta_high.json", payload["hero_stats"]),
        ("hero_meta_low.json", payload["low_stats"]),
        ("hero_meta_post.json", payload["all_stats"]),
    ):
        with open(os.path.join(DATA, filename), "w", encoding="utf-8") as handle:
            json.dump(rows, handle, indent=1)
    return payload


def percentile_map(values: dict[str, float]) -> dict[str, float]:
    """Average-tie percentile in [0, 100], where larger is better."""
    ordered = sorted(values.values())
    count = len(ordered)
    if count <= 1:
        return {name: 50.0 for name in values}
    out = {}
    for name, value in values.items():
        left = bisect.bisect_left(ordered, value)
        right = bisect.bisect_right(ordered, value)
        average_index = (left + right - 1) / 2
        out[name] = average_index / (count - 1) * 100
    return out


def score_components(source, optimization):
    id_to_name = {hero["id"]: name for name, hero in HEROES.items()}
    stats = {
        id_to_name[row["hero_id"]]: row
        for row in source["hero_stats"]
        if row.get("hero_id") in id_to_name and row.get("matches")
    }
    bans = {
        id_to_name[row["hero_id"]]: row.get("bans", 0)
        for row in source["hero_bans"]
        if row.get("hero_id") in id_to_name
    }
    heroes = sorted(set(optimization["overall"]) & set(stats))
    if len(heroes) != len(optimization["overall"]):
        missing = sorted(set(optimization["overall"]) - set(stats))
        raise RuntimeError(f"high-skill sample is missing heroes: {missing}")

    total_matches = sum(stats[name]["matches"] for name in heroes)
    total_wins = sum(stats[name]["wins"] for name in heroes)
    global_win = total_wins / total_matches

    raw = {}
    for name in heroes:
        row = stats[name]
        matches = row["matches"]
        networth = max(1, row.get("total_net_worth", 0))
        posterior_win = (
            row["wins"] + PRIOR_MATCHES * global_win
        ) / (matches + PRIOR_MATCHES)
        raw[name] = {
            "combat_log": math.log(max(optimization["overall"][name], 1e-9)),
            "posterior_win": posterior_win,
            "pick_share": matches / total_matches,
            "ban_share": bans.get(name, 0) / max(1, sum(bans.values())),
            "assist_eff": row.get("total_assists", 0) / networth * 1000,
            "objective_eff": row.get("total_boss_damage", 0) / networth * 1000,
            "farm_eff": (
                row.get("total_creep_damage", 0) + row.get("total_neutral_damage", 0)
            ) / networth * 1000,
            "damage_eff": row.get("total_player_damage", 0) / networth * 1000,
        }

    combat_pct = percentile_map({n: v["combat_log"] for n, v in raw.items()})
    outcome_pct = percentile_map({n: v["posterior_win"] for n, v in raw.items()})
    pick_pct = percentile_map({n: v["pick_share"] for n, v in raw.items()})
    ban_pct = percentile_map({n: v["ban_share"] for n, v in raw.items()})
    assist_pct = percentile_map({n: v["assist_eff"] for n, v in raw.items()})
    objective_pct = percentile_map({n: v["objective_eff"] for n, v in raw.items()})
    farm_pct = percentile_map({n: v["farm_eff"] for n, v in raw.items()})
    damage_pct = percentile_map({n: v["damage_eff"] for n, v in raw.items()})

    results = []
    for name in heroes:
        row = stats[name]
        components = {
            "combat": combat_pct[name],
            "high_skill_outcome": outcome_pct[name],
            "draft_priority": 0.65 * pick_pct[name] + 0.35 * ban_pct[name],
            "macro_breadth": (
                assist_pct[name] + objective_pct[name] + farm_pct[name] + damage_pct[name]
            ) / 4,
        }
        score = sum(WEIGHTS[key] * value for key, value in components.items())
        results.append({
            "hero": name,
            "score": score,
            "combat_score": optimization["overall"][name],
            "components": components,
            "matches": row["matches"],
            "wins": row["wins"],
            "raw_win_rate": row["wins"] / row["matches"] * 100,
            "adjusted_win_rate": raw[name]["posterior_win"] * 100,
            "pick_share": raw[name]["pick_share"] * 100,
            "ban_share": raw[name]["ban_share"] * 100,
            "macro_raw": {
                "assists_per_1k_networth": raw[name]["assist_eff"],
                "boss_damage_per_1k_networth": raw[name]["objective_eff"],
                "farm_damage_per_1k_networth": raw[name]["farm_eff"],
                "player_damage_per_1k_networth": raw[name]["damage_eff"],
            },
        })

    results.sort(key=lambda row: (-row["score"], row["hero"]))
    for index, row in enumerate(results, 1):
        row["rank"] = index

    profile_ranks = {}
    for profile, weights in SENSITIVITY.items():
        ordered = sorted(
            results,
            key=lambda row: -sum(
                weights[key] * row["components"][key] for key in weights
            ),
        )
        profile_ranks[profile] = {row["hero"]: i for i, row in enumerate(ordered, 1)}
    for row in results:
        ranks = [profile_ranks[p][row["hero"]] for p in SENSITIVITY]
        row["sensitivity_rank_min"] = min(ranks)
        row["sensitivity_rank_max"] = max(ranks)

    combat_ranks = [row["components"]["combat"] for row in results]
    outcome_ranks = [row["components"]["high_skill_outcome"] for row in results]
    combat_mean = sum(combat_ranks) / len(combat_ranks)
    outcome_mean = sum(outcome_ranks) / len(outcome_ranks)
    covariance = sum(
        (combat - combat_mean) * (outcome - outcome_mean)
        for combat, outcome in zip(combat_ranks, outcome_ranks)
    )
    denominator = math.sqrt(
        sum((combat - combat_mean) ** 2 for combat in combat_ranks)
        * sum((outcome - outcome_mean) ** 2 for outcome in outcome_ranks)
    )
    spearman = covariance / denominator if denominator else 0.0

    return results, {
        "global_win_rate": global_win * 100,
        "player_hero_appearances": total_matches,
        "estimated_matches": total_matches / 12,
        "total_bans": sum(bans.values()),
        "combat_outcome_spearman": spearman,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="fetch a fresh patch/rank sample")
    args = parser.parse_args()

    if args.refresh or not os.path.exists(SOURCE):
        source = refresh_source()
    else:
        with open(SOURCE, encoding="utf-8") as handle:
            source = json.load(handle)
    with open(os.path.join(DATA, "optimization.json"), encoding="utf-8") as handle:
        optimization = json.load(handle)

    ranking, sample = score_components(source, optimization)
    output = {
        "meta": {
            "name": "pro-leaning evidence index",
            "patch": PATCH,
            "fetched_at": source["fetched_at"],
            "rank_filter": source["rank_filter"],
            "match_mode": "ranked",
            "prior_matches": PRIOR_MATCHES,
            "weights": WEIGHTS,
            "sensitivity_profiles": SENSITIVITY,
            "source_urls": [source["stats_url"], source["bans_url"]],
            "warning": (
                "High-skill ranked evidence, not a tournament draft model. "
                "Percentile components are intentionally small and auditable."
            ),
        },
        "sample": sample,
        "ranking": ranking,
    }
    with open(OUTPUT, "w", encoding="utf-8") as handle:
        json.dump(output, handle, indent=1)

    print(f"source: {SOURCE}")
    print(f"wrote {OUTPUT}")
    print(
        f"sample: {sample['estimated_matches']:.0f} Ascendant+ ranked matches, "
        f"{sample['total_bans']} extracted bans"
    )
    for row in ranking[:15]:
        spread = f"#{row['sensitivity_rank_min']}-#{row['sensitivity_rank_max']}"
        print(
            f"{row['rank']:2d}. {row['score']:6.2f} {row['hero']:12s} "
            f"WR {row['adjusted_win_rate']:5.2f}% combat {row['combat_score']:5.3f} "
            f"sensitivity {spread}"
        )


if __name__ == "__main__":
    main()
