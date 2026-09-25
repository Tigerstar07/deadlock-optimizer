"""
Deadlock dataset extractor.

Reads the raw game-file dumps (heroes_raw.json / items_raw.json, pulled from
assets.deadlock-api.com which parses Valve's shipped .vdata files) and emits a
normalised dataset.json plus human-readable markdown.

Patch baseline: Minor Update 09-16-2026 (verified in verify.py).
"""

import json
import os
import re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def strip_html(s):
    if not isinstance(s, str):
        return s
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", s).strip()


def num(v):
    """Coerce a game-file value to float where possible.

    Values arrive as bare numbers, numeric strings, or strings carrying a unit
    suffix ('32m', '25%'); the suffix is display metadata, not part of the value.
    """
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        m = re.match(r"^(-?[\d.]+)", v.strip())
        if m:
            try:
                return float(m.group(1))
            except ValueError:
                return None
    return None


def parse_props(raw_props):
    """Normalise a properties dict, keeping value + any scaling coefficient."""
    out = {}
    for key, val in (raw_props or {}).items():
        if not isinstance(val, dict):
            out[key] = {"value": num(val), "raw": val}
            continue
        entry = {
            "value": num(val.get("value")),
            "raw": val.get("value"),
            "label": strip_html(val.get("label") or ""),
            "css": val.get("css_class"),
        }
        sf = val.get("scale_function")
        if isinstance(sf, dict):
            entry["scale_class"] = sf.get("class_name")
            entry["scale_stat"] = sf.get("specific_stat_scale_type")
            # stat_scale is the Spirit Power coefficient for tech_damage/tech_healing
            if sf.get("stat_scale") is not None:
                entry["spirit_scale"] = num(sf.get("stat_scale"))
        out[key] = entry
    return out


def parse_upgrades(raw_upgrades):
    """Ability/item tier upgrades (T1/T2/T3) -> list of {prop: bonus} dicts."""
    tiers = []
    for u in raw_upgrades or []:
        # A LIST, not a dict keyed by name: a single tier can carry two entries
        # for the same property -- Apollo's Flawless Advance T3 has
        # PerfectDamage +65 (flat) AND PerfectDamage x1.15 (EMultiplyScale).
        # Keying by name silently dropped one of every such pair.
        entries = []
        for pu in (u or {}).get("property_upgrades", []) or []:
            name = pu.get("name")
            if not name:
                continue
            entries.append({
                "name": name,
                "bonus": num(pu.get("bonus")),
                "raw": pu.get("bonus"),
                "type": pu.get("upgrade_type"),
                "scale": num(pu.get("scale")) if pu.get("scale") is not None else None,
            })
        # convenience view for display code (last-wins, as before)
        bonuses = {e["name"]: e for e in entries}
        tiers.append({
            "entries": entries,
            "bonuses": bonuses,
            "description": strip_html((u or {}).get("description") or ""),
        })
    return tiers


def prop_sections(raw):
    """Map each property -> its tooltip section type.

    'innate' properties are always active. Properties under 'active' or
    'passive' sections are CONDITIONAL: they only apply while the item's
    buff is running (Active Reload's 16% bullet lifesteal requires hitting
    the active-reload window; Fury Trance's 40% spirit resist is only up
    during its 6.5s buff).

    A section with no ``section_type`` is the tooltip's proc/conditional block
    (Burst Fire's on-hit fire rate, Lucky Shot's proc, Stalker's wound): it is
    classified as 'passive' so its buffs are uptime-weighted. Headline innate
    stats sit in ``elevated_properties``, which must be read too, or they fall
    through to the unclassified heuristics.
    """
    out = {}
    for s in raw.get("tooltip_sections") or []:
        st = s.get("section_type") or "passive"
        for sa in s.get("section_attributes") or []:
            for key in ((sa.get("properties") or [])
                        + (sa.get("important_properties") or [])
                        + (sa.get("elevated_properties") or [])):
                # first section wins; innate always wins
                if key not in out or st == "innate":
                    out[key] = st
    return out


def main():
    heroes_raw = load("heroes_raw.json")
    items_raw = load("items_raw.json")

    by_class = {x["class_name"]: x for x in items_raw}

    # ---------------- items (shop upgrades) ----------------
    items = {}
    for x in items_raw:
        if x.get("type") != "upgrade":
            continue
        if x.get("disabled"):
            continue
        if not x.get("shopable", True):
            continue
        desc = x.get("description") or {}
        items[x["name"]] = {
            "id": x["id"],
            "class_name": x["class_name"],
            "name": x["name"],
            "slot": x.get("item_slot_type"),
            "tier": x.get("item_tier"),
            "cost": x.get("cost"),
            "is_active": bool(x.get("is_active_item")),
            "activation": x.get("activation"),
            "imbue": bool(x.get("imbue")),
            "components": x.get("component_items") or [],
            "heroes_restricted": x.get("heroes") or [],
            "properties": parse_props(x.get("properties")),
            "sections": prop_sections(x),
            "upgrades": parse_upgrades(x.get("upgrades")),
            "desc": strip_html(desc.get("desc") or ""),
            "desc_active": strip_html(desc.get("active") or ""),
            "desc_passive": strip_html(desc.get("passive") or ""),
        }

    # ---------------- heroes ----------------
    heroes = {}
    for h in heroes_raw:
        if h.get("disabled") or not h.get("player_selectable"):
            continue
        if h.get("in_development") or h.get("prerelease_only"):
            continue

        ss = {k: num(v.get("value")) for k, v in (h.get("starting_stats") or {}).items()}
        lvl = h.get("standard_level_up_upgrades") or {}

        # weapon
        wclass = (h.get("items") or {}).get("weapon_primary")
        wrec = by_class.get(wclass) or {}
        winfo = wrec.get("weapon_info") or {}
        weapon = {k: v for k, v in winfo.items() if not isinstance(v, (dict, list))}
        weapon["name"] = wrec.get("name")
        weapon["class_name"] = wclass
        # per-shot spirit/other props living on the weapon record
        weapon["properties"] = parse_props(wrec.get("properties"))

        # abilities
        abilities = []
        for slot in ("signature1", "signature2", "signature3", "signature4"):
            aclass = (h.get("items") or {}).get(slot)
            if not aclass:
                continue
            a = by_class.get(aclass)
            if not a:
                abilities.append({"slot": slot, "class_name": aclass, "missing": True})
                continue
            adesc = a.get("description") or {}
            abilities.append({
                "slot": slot,
                "class_name": aclass,
                "name": a.get("name"),
                "is_ultimate": slot == "signature4",
                "properties": parse_props(a.get("properties")),
                "upgrades": parse_upgrades(a.get("upgrades")),
                "desc": strip_html(adesc.get("desc") or ""),
            })

        # level / boon gold table
        level_info = {}
        for k, v in (h.get("level_info") or {}).items():
            level_info[int(k)] = {
                "required_gold": v.get("required_gold"),
                "bonus": v.get("bonus_currencies"),
            }

        heroes[h["name"]] = {
            "id": h["id"],
            "class_name": h["class_name"],
            "name": h["name"],
            "complexity": h.get("complexity"),
            "hero_type": h.get("hero_type"),
            "tags": h.get("tags") or [],
            "base": ss,
            "per_boon": {
                "health": lvl.get("MODIFIER_VALUE_BASE_HEALTH_FROM_LEVEL"),
                "bullet_damage": lvl.get("MODIFIER_VALUE_BASE_BULLET_DAMAGE_FROM_LEVEL"),
                "bullet_damage_alt": lvl.get("MODIFIER_VALUE_BASE_BULLET_DAMAGE_FROM_LEVEL_ALT_FIRE"),
                "melee_damage": lvl.get("MODIFIER_VALUE_BASE_MELEE_DAMAGE_FROM_LEVEL"),
                "spirit_power": lvl.get("MODIFIER_VALUE_TECH_POWER"),
                "bullet_resist": lvl.get("MODIFIER_VALUE_BULLET_ARMOR_DAMAGE_RESIST"),
                "tech_resist": lvl.get("MODIFIER_VALUE_TECH_RESIST"),
                "attack_range": lvl.get("MODIFIER_VALUE_BONUS_ATTACK_RANGE"),
                "boons_per_level": lvl.get("MODIFIER_VALUE_BOON_COUNT"),
            },
            "purchase_bonuses": h.get("purchase_bonuses") or {},
            "level_info": level_info,
            "weapon": weapon,
            "abilities": abilities,
        }

    dataset = {
        "meta": {
            "patch": "Minor Update 09-16-2026",
            "extracted": "2026-09-18",
            "source": "assets.deadlock-api.com (parsed Valve game files)",
            "hero_count": len(heroes),
            "item_count": len(items),
        },
        "heroes": heroes,
        "items": items,
    }

    out = os.path.join(DATA, "dataset.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=1)

    print(f"heroes : {len(heroes)}")
    print(f"items  : {len(items)}")
    by_slot = defaultdict(int)
    for i in items.values():
        by_slot[(i['slot'], i['tier'])] += 1
    for k in sorted(by_slot, key=lambda z: (str(z[0]), z[1] or 0)):
        print(f"   {k[0]:9s} T{k[1]}: {by_slot[k]}")
    print(f"\nwrote {out} ({os.path.getsize(out):,} bytes)")


if __name__ == "__main__":
    main()
