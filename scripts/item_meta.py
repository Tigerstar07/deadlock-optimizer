"""
Real item usage at Ascendant 1+ for the current patch.

Fetches the Deadlock API's item statistics (overall and per hero) for the
same ranked match window and rank filter as pro_rank.py, and stores a
snapshot so the rest of the pipeline stays reproducible offline.

    python scripts/item_meta.py            # use the snapshot if present
    python scripts/item_meta.py --refresh  # re-fetch

-> data/item_meta_source.json
"""

import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pro_rank import MIN_AVERAGE_BADGE, PATCH, PATCH_START, fetch_json, request_url  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "item_meta_source.json")


def refresh():
    overall_url = request_url("item-stats")
    by_hero_url = overall_url + "&bucket=hero"
    payload = {
        "fetched_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "patch": PATCH,
        "patch_start": PATCH_START,
        "rank_filter": "Ascendant 1+",
        "min_average_badge": MIN_AVERAGE_BADGE,
        "overall_url": overall_url,
        "by_hero_url": by_hero_url.replace("bucket=no_bucket&", ""),
        "overall": fetch_json(overall_url),
        "by_hero": fetch_json(by_hero_url.replace("bucket=no_bucket&", "")),
        # hero match counts from the same moment, for per-hero pick rates
        "hero_stats": fetch_json(request_url("hero-stats")),
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=1)
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    if args.refresh or not os.path.exists(OUT):
        payload = refresh()
        print(f"fetched {len(payload['overall'])} items, {len(payload['by_hero'])} hero-item rows")
    else:
        with open(OUT, encoding="utf-8") as f:
            payload = json.load(f)
        print(f"using snapshot from {payload['fetched_at'][:10]}: "
              f"{len(payload['overall'])} items, {len(payload['by_hero'])} hero-item rows")


if __name__ == "__main__":
    main()
