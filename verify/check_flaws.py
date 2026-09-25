"""Human-readable audit of the ranking-sensitive model corrections."""

import os
import sys


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from model import HEROES, ITEMS, Loadout, pooled  # noqa: E402


REF = {"ehp": 9851, "dps": 462, "bullet_resist": 17, "tech_resist": 72}


def check(label, condition, detail):
    mark = "PASS" if condition else "FAIL"
    print(f"[{mark}] {label}: {detail}")
    if not condition:
        raise AssertionError(label)


base = Loadout("Drifter", [], 50000)
far = base.weapon_dps_vs(0, 0, distance_m=30)
check("range falloff", abs(far / base.weapon_dps - 0.6) < 1e-9,
      f"Drifter retains {far / base.weapon_dps:.1%} at 30m")

life = Loadout("Drifter", ["Bullet Lifesteal", "Fury Trance"], 50000)
expected_life = pooled([13, 14])
check("lifesteal pooling", abs(life.bullet_lifesteal - expected_life) < 1e-9,
      f"13% + 14% -> {life.bullet_lifesteal:.2f}%")

glass = Loadout("Drifter", ["Glass Cannon"], 50000)
check("health penalties", abs(glass.health / base.health - 0.87) < 1e-9,
      f"Glass Cannon leaves {glass.health / base.health:.0%} max health")

tempo = Loadout("Drifter", ["Healing Tempo"], 50000)
check("trigger-gated buffs", tempo.firerate_pct == 0,
      "Healing Tempo grants no fire rate without an applied-heal trigger")

cdr = Loadout("Yamato", ["Compress Cooldown", "Superior Cooldown",
                          "Transcendent Cooldown"], 50000)
expected_cdr = pooled([18, 20, 25])
check("cooldown pooling", abs(cdr.cdr - expected_cdr) < 1e-9,
      f"18% + 20% + 25% -> {cdr.cdr:.2f}% ability CDR")
check("item cooldown separation", cdr.item_cdr == 25,
      f"item CDR is {cdr.item_cdr:.0f}%, not {cdr.cdr:.2f}%")

billy = Loadout("Billy", [], 50000)
billy.ability_levels = (3, 3, 3, 3)
billy_heal, billy_parts = billy.ability_healing()
check("healing field classification", billy_heal == 0,
      f"Melee Bonus Health is excluded from healing ({billy_parts})")

drain = Loadout("Drifter", ["Blood Tribute"], 50000).duel(REF, antiheal=35)
expected_heal = drain["gross_heal_ps"] * 0.65 - 50
check("self-drain ordering", abs(drain["heal_ps"] - expected_heal) < 1e-9,
      "anti-heal applies before the 50 HP/s self-drain, which is never clamped away")

for nw, points in ((6000, 8), (12000, 15), (20000, 21), (32000, 26), (50000, 32)):
    lo = Loadout("Drifter", [], nw)
    check(f"ability points at {nw:,}", lo.ability_points == points,
          f"{lo.ability_points} available")

probe = Loadout("Drifter", [], 0)
probe.bullet_resist = 50
probe.tech_resist = 0
raw_pool = probe.health + probe.ability_bonus_health() + probe.barrier_pool()
check("mixed EHP", abs(probe.ehp() - raw_pool / 0.7) < 1e-9,
      "60/40 incoming uses the weighted damage multiplier, not averaged EHP")
target = {"health": 1000, "ehp": 2000, "dps": 100,
          "bullet_resist": 50, "tech_resist": 0}
target_duel = Loadout("Drifter", [], 0).duel(
    target, headshot_rate=0, antiheal=0, focus=1)
check("target resistance applied once",
      abs(target_duel["ttk"] - 1000 / target_duel["total_dps"]) < 1e-9,
      "TTK uses raw target health after channel resistance reduces DPS")

viscous = Loadout("Viscous", [], 50000)
v_bullet, v_spirit = viscous.total_resists((3, 3, 3, 3))
check("ability resistance uptime", v_bullet > viscous.bullet_resist and v_spirit > viscous.tech_resist,
      "Goo Ball's upgraded timed resists enter both defensive channels")
drifter_shred, _ = base.total_shreds((3, 3, 3, 3))
check("ability shred uptime", drifter_shred > base.bullet_shred,
      "Stalker's Mark's tier-upgraded timed shred enters outgoing damage")

print(f"\nAll model audits passed for {len(HEROES)} heroes and {len(ITEMS)} extracted items.")
