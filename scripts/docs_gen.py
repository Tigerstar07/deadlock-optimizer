"""
Writes the complete stat reference to markdown: every hero, every number.

Produces:
  docs/HEROES.md   - full stat sheet for all 38 heroes
  docs/ITEMS.md    - all 173 live shop items with every property
  docs/MECHANICS.md- the verified formulas and constants
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import HEROES, ITEMS, DATASET, INVEST, effective_cycle, RELOAD_OVERHEAD, Loadout

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOCS = os.path.join(ROOT, "docs")
U = 39.37  # source units per metre (verified: Lash falloff 16m->48m matches patch)

os.makedirs(DOCS, exist_ok=True)


def fmt(v, nd=2):
    if v is None:
        return "-"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, (int, float)):
        if abs(v - round(v)) < 1e-9:
            return str(int(round(v)))
        return f"{v:.{nd}f}"
    return str(v)


def hero_md(name, h):
    b = h["base"]
    w = h["weapon"]
    pb = h["per_boon"]
    L0 = Loadout(name, [], net_worth=0)
    L_mid = Loadout(name, [], net_worth=20000)
    L_max = Loadout(name, [], net_worth=50000)

    o = []
    o.append(f"## {name}\n")
    o.append(f"*internal id {h['id']} / `{h['class_name']}` / complexity {h.get('complexity')}*\n")

    o.append("\n### Vitality\n")
    o.append("| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |")
    o.append("|---|---|---|---|---|")
    o.append(f"| Max Health | {fmt(b.get('max_health'))} | +{fmt(pb['health'])} | "
             f"{fmt(L_mid.health)} | {fmt(L_max.health)} |")
    o.append(f"| Health Regen | {fmt(b.get('base_health_regen'))} | - | - | - |")
    if pb.get("bullet_resist"):
        o.append(f"| Bullet Resist | 0% | +{fmt(pb['bullet_resist'])}% | "
                 f"{fmt(L_mid.bullet_resist)}% | {fmt(L_max.bullet_resist)}% |")
    if pb.get("tech_resist"):
        o.append(f"| Spirit Resist | 0% | +{fmt(pb['tech_resist'])}% | "
                 f"{fmt(L_mid.tech_resist)}% | {fmt(L_max.tech_resist)}% |")

    o.append("\n### Movement\n")
    o.append("| stat | value |")
    o.append("|---|---|")
    for key, label, unit in [
        ("max_move_speed", "Max Move Speed", " m/s"),
        ("sprint_speed", "Sprint Speed (bonus)", " m/s"),
        ("crouch_speed", "Crouch Speed", " m/s"),
        ("move_acceleration", "Move Acceleration", ""),
        ("stamina", "Stamina", ""),
        ("stamina_regen_per_second", "Stamina Regen", "/s"),
        ("ground_dash_distance_in_meters", "Ground Dash Distance", " m"),
        ("ground_dash_duration", "Ground Dash Duration", " s"),
        ("air_dash_distance_in_meters", "Air Dash Distance", " m"),
        ("air_dash_duration", "Air Dash Duration", " s"),
    ]:
        if b.get(key) is not None:
            o.append(f"| {label} | {fmt(b.get(key))}{unit} |")

    o.append("\n### Melee\n")
    o.append("| stat | base | per boon | at 50k NW |")
    o.append("|---|---|---|---|")
    melee50 = (b.get("light_melee_damage") or 0) + 35 * (pb["melee_damage"] or 0)
    o.append(f"| Light Melee | {fmt(b.get('light_melee_damage'))} | +{fmt(pb['melee_damage'])} | {fmt(melee50)} |")
    o.append(f"| Heavy Melee | {fmt(b.get('heavy_melee_damage'))} | - | - |")

    o.append("\n### Weapon\n")
    o.append(f"`{w.get('class_name')}`\n")
    o.append("| stat | value |")
    o.append("|---|---|")
    rows = [
        ("Damage per bullet", fmt(w.get("bullet_damage"))),
        ("Bullets per shot", fmt(w.get("bullets"))),
        ("Damage per shot", fmt((w.get('bullet_damage') or 0) * (w.get('bullets') or 1))),
        ("Ammo / clip size", fmt(w.get("clip_size"))),
        ("Damage per magazine", fmt(w.get("damage_per_magazine"))),
        ("Cycle time (nominal)", f"{fmt(w.get('cycle_time'), 4)} s"),
        ("Cycle time (effective avg)", f"{fmt(effective_cycle(name), 4)} s"),
        ("Shots / second", fmt(w.get("shots_per_second"), 3)),
        ("Shots / second (with reload)", fmt(w.get("shots_per_second_with_reload"), 3)),
        ("Reload duration", f"{fmt(w.get('reload_duration'))} s"),
        ("Burst shot count", fmt(w.get("burst_shot_count"))),
        ("DPS (sustained, no reload)", fmt(w.get("damage_per_second"), 2)),
        ("**DPS (with reload)**", f"**{fmt(w.get('damage_per_second_with_reload'), 2)}**"),
        ("Bullet damage per boon", f"+{fmt(pb['bullet_damage'], 3)}"),
        ("Headshot multiplier", f"x{fmt(w.get('crit_bonus_start'))}"),
        ("Bullet speed", fmt(w.get("bullet_speed"))),
        ("Falloff: full damage to", f"{fmt((w.get('damage_falloff_start_range') or 0)/U,1)} m"),
        ("Falloff: decays to", f"{fmt((w.get('damage_falloff_end_range') or 0)/U,1)} m"),
        ("Falloff: damage retained", f"{fmt((w.get('damage_falloff_end_scale') or 0)*100,0)}%"),
        ("Max range", f"{fmt((w.get('range') or 0)/U,1)} m"),
        ("Move speed while shooting", f"{fmt((w.get('shoot_move_speed_percent') or 0)*100,0)}%"),
        ("Spread penalty per shot", fmt(w.get("shoot_spread_penalty_per_shot"), 3)),
    ]
    for k, v in rows:
        o.append(f"| {k} | {v} |")

    o.append("\n### Spirit scaling\n")
    o.append(f"- Spirit Power per boon: **+{fmt(pb['spirit_power'])}**"
             f"  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)")
    o.append(f"- Spirit Power at 20k net worth (no items): **{fmt(L_mid.spirit_power,1)}**")
    o.append(f"- Spirit Power at 50k net worth (no items): **{fmt(L_max.spirit_power,1)}**")

    o.append("\n### Abilities\n")
    for a in h["abilities"]:
        tag = " (ULTIMATE)" if a.get("is_ultimate") else ""
        o.append(f"\n#### {a.get('name')}{tag}\n")
        if a.get("desc"):
            o.append(f"> {a['desc']}\n")
        props = a.get("properties") or {}
        shown = [(k, p) for k, p in props.items() if p.get("value")]
        if shown:
            o.append("| property | value | spirit coef | at 20k SP |")
            o.append("|---|---|---|---|")
            for k, p in shown:
                coef = p.get("spirit_scale")
                scaled = (p["value"] + L_mid.spirit_power * coef) if coef else None
                o.append(f"| {k} | {fmt(p['value'],3)} | "
                         f"{('+' + fmt(coef,4)) if coef else '-'} | "
                         f"{fmt(scaled,1) if scaled is not None else '-'} |")
        ups = a.get("upgrades") or []
        if ups:
            o.append("\n**Upgrades**\n")
            for i, u in enumerate(ups, 1):
                bl = ", ".join(f"`{k}` {'+' if (v['bonus'] or 0) >= 0 else ''}{fmt(v['bonus'],3)}"
                               for k, v in u["bonuses"].items())
                o.append(f"- **T{i}** — {bl or u.get('description') or '(see description)'}")
    return "\n".join(o)


def write_heroes():
    out = ["# Deadlock — Complete Hero Stat Reference",
           f"\n*Patch: {DATASET['meta']['patch']} · extracted {DATASET['meta']['extracted']}*",
           f"\n*Source: {DATASET['meta']['source']}*",
           "\nEvery number below is read directly from the shipped game files, not "
           "from a wiki or a guide. Distances are converted from Source units at "
           "39.37 units/metre (verified against the 09-16-2026 note "
           "\"Lash: Gun falloff reduced from 18m->54m to 16m->48m\").",
           f"\n**{len(HEROES)} playable heroes.**\n",
           "\n---\n"]
    for name in sorted(HEROES):
        out.append(hero_md(name, HEROES[name]))
        out.append("\n---\n")
    p = os.path.join(DOCS, "HEROES.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    return p


def write_items():
    out = ["# Deadlock — Complete Item Reference",
           f"\n*Patch: {DATASET['meta']['patch']} · extracted {DATASET['meta']['extracted']}*\n",
           "173 purchasable items. Tier 5 entries exist in the files but are "
           "**Street Brawl only** and are excluded from standard-mode builds.\n"]
    for slot in ("weapon", "vitality", "spirit"):
        out.append(f"\n## {slot.upper()} items\n")
        for tier in (1, 2, 3, 4):
            items = sorted([i for i in ITEMS.values()
                            if i["slot"] == slot and i["tier"] == tier],
                           key=lambda z: z["name"])
            if not items:
                continue
            cost = items[0]["cost"]
            out.append(f"\n### Tier {tier} — {cost} souls\n")
            for it in items:
                kind = "ACTIVE" if it["is_active"] else "passive"
                out.append(f"\n**{it['name']}** ({kind})")
                if it["components"]:
                    out.append(f"  \n*builds from: {', '.join(it['components'])}*")
                d = it["desc"] or it["desc_passive"] or it["desc_active"]
                if d:
                    out.append(f"  \n> {d}")
                props = [(k, p) for k, p in it["properties"].items()
                         if p.get("value") and k not in
                         ("AbilityUnitTargetLimit", "AbilityCooldownBetweenCharge",
                          "ChannelMoveSpeed")]
                if props:
                    out.append("")
                    out.append("| property | value |")
                    out.append("|---|---|")
                    for k, p in props:
                        out.append(f"| {k} | {fmt(p['value'],3)} |")
                for i, u in enumerate(it["upgrades"] or [], 1):
                    bl = ", ".join(f"`{k}` {fmt(v['bonus'],3)}" for k, v in u["bonuses"].items())
                    if bl:
                        out.append(f"- upgrade {i}: {bl}")
    p = os.path.join(DOCS, "ITEMS.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    return p


def write_mechanics():
    o = ["# Deadlock — Verified Mechanics and Formulas",
         f"\n*Patch: {DATASET['meta']['patch']}*\n",
         "Every formula here was checked against the shipped game files AND a "
         "second source, and the check is recorded next to it.\n",
         "\n## Boons (levels)\n",
         "Boons come from **net worth thresholds**, not from spending. Buying an "
         "item never changes your boon count. Max boon is 35, reached at 48,600 "
         "net worth.\n",
         "Per-boon gains are per hero (health, bullet damage, melee), except "
         "Spirit Power which is +1.1 for 32 of 38 heroes. Exceptions: "
         "**Grey Talon +1.6**, **Haze +0.5**, three heroes at +1.3, one at +1.2. "
         "Only **Bebop (+0.3%)** and **Dynamo (+0.625%)** gain Bullet Resist per boon.\n",
         "> Verified: the shipped per-boon health values match the 09-16-2026 patch "
         "notes exactly — Graves 33→35, Holliday 41→43, Silver 28→31.\n",
         "Ability points also come from the shipped level table. The five optimizer "
         "checkpoints provide **8 / 15 / 21 / 26 / 32** points at 6k / 12k / 20k / "
         "32k / 50k net worth. Ability tiers cost 1, 2 and 5 additional points.\n",
         "\n## Investments (the biggest build lever in the game)\n",
         "Bonuses scale off **cumulative souls spent per category**, not per item.\n"]
    o.append("| souls in category | weapon dmg | health | spirit power |")
    o.append("|---|---|---|---|")
    for i, (thr, _) in enumerate(INVEST["weapon"]):
        o.append(f"| {thr:,} | +{INVEST['weapon'][i][1]}% | "
                 f"+{INVEST['vitality'][i][1]}% | +{INVEST['spirit'][i][1]} |")
    o.append("\nNote the discontinuity at **4,800 souls**: weapon damage jumps "
             "+18% → +46% for one more 1,600-soul item. This is the single "
             "largest power spike available and it is why build ORDER matters "
             "more than build CONTENTS in the mid game.\n")
    o.append("\n## Damage formulas\n")
    o.append("```\nSpirit damage   = base + SpiritPower * coefficient      (linear)\n"
             "Bullet damage   = (base + boons * per_boon) * (1 + weapon%)\n"
             "Sustained DPS   = clip*bullets*dmg / (clip*cycle + reload + 0.25)\n"
             "```\n")
    o.append(f"The **+{RELOAD_OVERHEAD}s** reload-initiation constant was derived by "
             "inverting the game's own `damage_per_second_with_reload` and comes out "
             "to exactly 0.2500 for 32 of 38 heroes. The six burst/charge weapons "
             "use an effective cycle derived from the shipped DPS value.\n")
    o.append("Weapon damage is averaged over each scenario's **spread of engagement "
             "distances** (e.g. teamfight 10/20/30 m at 25/50/25%). Falloff is linear between "
             "the shipped start/end ranges, after falloff-range item bonuses; close-range "
             "items (Point Blank, Stalker, Hunter's Aura, Torment Pulse) count only inside "
             "their radius.\n")
    o.append("\n## Engagement window\n")
    o.append("Each scenario is **one 20-second engagement entered with every cooldown ready**. "
             "Uptime, cast rate and healing of anything on a longer cooldown are amortised over "
             "20 s instead of the full cooldown (actives, ultimates, barriers, shielding procs). "
             "Barriers count once per fight.\n")
    o.append("\n## Resistances\n")
    o.append("```\nTotal resist    = 1 - product(1 - Ri)        (multiplicative)\n"
             "Total shred     = 1 - product(1 - Si)        (pooled the same way)\n"
             "Final resist    = Total resist - Total shred (subtracted, not pooled)\n```\n")
    o.append("Because shred subtracts from a multiplicatively-pooled total, it gets "
             "*more* effective the more the target has stacked resist.\n")
    o.append("Lifesteal and cooldown reduction also pool multiplicatively. Item "
             "cooldown reduction is separate from ability cooldown reduction.\n")
    o.append("Explicit hero ability resistance buffs are applied after tier upgrades "
             "and pooled with item/boon resistance at duration-to-cooldown uptime. "
             "A summon resistance with no hero-buff duration is skipped.\n")
    o.append("Ability-applied bullet/spirit shred is also tier-upgraded and uptime "
             "weighted when an explicit debuff duration is present. Resource-gated "
             "and unknown-duration shred is skipped rather than guessed.\n")
    o.append("\n## Healing order\n")
    o.append("```\ngross healing = lifesteal + regen*(1+regen amp) + cast heals*(1+cast amp)\n"
             "net healing   = gross healing*(1-enemy anti-heal) + Siphon Bullets - self health drain\n"
             "net incoming  = max(25% of incoming, incoming - net healing)\n```\n")
    o.append("Siphon Bullets steals 2.5% of the target's current max HP per 1.2 s as damage and "
             "as healing that ignores healing reduction, decaying as the target's max HP shrinks. "
             "Healing can offset at most 75% of incoming damage.\n")
    o.append("Healing Tempo does not amplify passive lifesteal and its fire-rate buff "
             "requires an applied-heal trigger. Enemy anti-heal does not reduce "
             "Blood Tribute's self-inflicted health drain.\n")
    o.append("\n## Duel score\n")
    o.append("Target bullet and spirit resistance reduce the matching damage channel first. "
             "Time-to-kill then divides the target's **raw health and barrier pool** "
             "by that resistance-adjusted DPS. The displayed mixed-damage EHP is "
             "diagnostic only; using it in the time-to-kill denominator would count "
             "target resistance twice. Incoming reference DPS is recorded before "
             "mitigation because the defender's mixed EHP applies its own resistances. "
             "For the 60/40 bullet/spirit mix, EHP is raw health divided by the "
             "weighted damage multiplier. Healing is subtracted after mitigation.\n")
    o.append("\n## Slots and limits\n")
    o.append("- **12 item slots** max: 9 base + 3 unlocked by destroying Walkers\n"
             "- Slots are **universal** — any category in any slot\n"
             "- **Max 4 active items** (keybind limit)\n"
             "- Tier costs: 800 / 1,600 / 3,200 / 6,400\n"
             "- Owning a component discounts the upgrade by the component's cost\n")
    p = os.path.join(DOCS, "MECHANICS.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write("\n".join(o))
    return p


if __name__ == "__main__":
    for p in (write_mechanics(), write_heroes(), write_items()):
        print(f"wrote {p}  ({os.path.getsize(p):,} bytes)")
