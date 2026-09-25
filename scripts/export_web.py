"""Builds the compact JSON payload the web app loads."""

import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import HEROES, ITEMS, DATASET, INVEST, effective_cycle, RELOAD_OVERHEAD

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")
WEB = os.path.join(ROOT, "web")
U = 39.37

os.makedirs(WEB, exist_ok=True)


def main():
    # hero portraits straight from the shipped asset list
    raw_heroes = json.load(open(os.path.join(DATA, "heroes_raw.json"), encoding="utf-8"))
    IMG = {}
    for x in raw_heroes:
        im = x.get("images") or {}
        IMG[x.get("name")] = {
            "card": im.get("icon_hero_card_webp") or im.get("icon_hero_card"),
            "small": im.get("icon_image_small_webp") or im.get("icon_image_small"),
            "vertical": im.get("top_bar_vertical_image_webp") or im.get("top_bar_vertical_image"),
            "bg": im.get("background_image_webp") or im.get("background_image"),
        }

    heroes = {}
    for n, h in HEROES.items():
        w = h["weapon"]
        abilities = []
        for a in h["abilities"]:
            # Keep zero-valued base properties when an ability upgrade targets
            # them.  Their metadata (especially ``css`` and Spirit scaling)
            # is still required by the browser model after the upgrade adds a
            # value.  Dropping them made the Build Lab under-count upgraded
            # damage such as Drifter's DamageHeavyMelee.
            upgraded_keys = {
                entry.get("name")
                for tier in (a.get("upgrades") or [])
                for entry in (tier.get("entries") or [])
                if entry.get("name")
            }
            props = {}
            for k, p in (a.get("properties") or {}).items():
                if p.get("value") or p.get("spirit_scale") or k in upgraded_keys:
                    props[k] = {"v": p["value"], "c": p.get("spirit_scale"),
                                "css": p.get("css"), "label": p.get("label")}
            abilities.append({
                "name": a.get("name"),
                "ult": a.get("is_ultimate"),
                "desc": a.get("desc"),
                "props": props,
                "upgrade_entries": [
                    [{"n": e.get("name"), "b": e.get("bonus"), "t": e.get("type")}
                     for e in (u.get("entries") or [])]
                    for u in (a.get("upgrades") or [])
                ],
                "upgrades": [
                    {k: v["bonus"] for k, v in (u["bonuses"] or {}).items()}
                    for u in (a.get("upgrades") or [])
                ],
            })
        heroes[n] = {
            "id": h["id"],
            "img": IMG.get(n, {}),
            "complexity": h.get("complexity"),
            "base": h["base"],
            "per_boon": h["per_boon"],
            "level_info": {str(k): v["required_gold"] for k, v in h["level_info"].items()},
            "ability_point_gold": [
                v["required_gold"] for v in h["level_info"].values()
                if "EAbilityPoints" in (v.get("bonus") or [])
            ],
            "weapon": {
                "bullet_damage": w.get("bullet_damage"),
                "bullets": w.get("bullets") or 1,
                "clip_size": w.get("clip_size"),
                "cycle_time": w.get("cycle_time"),
                "effective_cycle": effective_cycle(n),
                "reload_duration": w.get("reload_duration"),
                "dps": w.get("damage_per_second"),
                "dps_reload": w.get("damage_per_second_with_reload"),
                "headshot": w.get("crit_bonus_start"),
                "falloff_start_m": (w.get("damage_falloff_start_range") or 0) / U,
                "falloff_end_m": (w.get("damage_falloff_end_range") or 0) / U,
                "falloff_scale": w.get("damage_falloff_end_scale"),
                "burst": w.get("burst_shot_count"),
                "bullet_speed": w.get("bullet_speed"),
            },
            "abilities": abilities,
        }

    raw_items = json.load(open(os.path.join(DATA, "items_raw.json"), encoding="utf-8"))
    RAWITEM = {x.get("name"): (x.get("shop_image_webp") or x.get("shop_image")
                               or x.get("image_webp") or x.get("image"))
               for x in raw_items}

    items = {}
    for n, it in ITEMS.items():
        if it["tier"] == 5:
            continue
        props = {k: p["value"] for k, p in it["properties"].items() if p.get("value")}
        items[n] = {
            "slot": it["slot"], "tier": it["tier"], "cost": it["cost"],
            "active": it["is_active"], "components": it["components"],
            "__cls": it["class_name"],
            "desc": it["desc"] or it["desc_passive"] or it["desc_active"],
            "props": props,
            # tooltip section per property (innate = always on, active/passive =
            # conditional); the browser model needs this to weight uptime the
            # same way the Python model does.
            "sections": it.get("sections") or {},
            "img": RAWITEM.get(n),
        }

    payload = {
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        "meta": DATASET["meta"],
        "invest": INVEST,
        "reload_overhead": RELOAD_OVERHEAD,
        "heroes": heroes,
        "items": items,
    }

    # optimisation results + empirical meta, if present
    for fname, key in [("optimization.json", "optimization"),
                       ("benchmarks.json", "benchmarks"),
                       ("sensitivity.json", "sensitivity"),
                       ("orders.json", "orders"),
                       ("pro_ranking.json", "pro_ranking"),
                       ("hero_meta.json", "meta_all"),
                       ("hero_meta_high.json", "meta_high"),
                       ("hero_meta_low.json", "meta_low")]:
        p = os.path.join(DATA, fname)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                payload[key] = json.load(f)

    out = os.path.join(WEB, "data.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, separators=(",", ":"))
    print(f"wrote {out} ({os.path.getsize(out):,} bytes)")
    print(f"  heroes {len(heroes)} | items {len(items)}")


if __name__ == "__main__":
    main()
