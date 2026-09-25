"""Regression tests for the mechanics that materially change build rankings."""

import json
import math
import os
import sys
import unittest


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from model import (  # noqa: E402
    FIGHT_WINDOW,
    HEROES,
    ITEMS,
    MAX_SLOTS,
    SCENARIO_BY_NAME,
    Loadout,
    ability_points_for_networth,
    pooled,
    valid_build,
)


REF = {"ehp": 8000.0, "dps": 450.0, "bullet_resist": 25.0, "tech_resist": 25.0}


class MechanicsTests(unittest.TestCase):
    def test_web_payload_keeps_scaled_and_upgrade_target_properties(self):
        """The browser needs zero-base scaling/css metadata after export."""
        with open(os.path.join(ROOT, "web", "data.json"), encoding="utf-8") as handle:
            web = json.load(handle)
        for hero_name, hero in HEROES.items():
            exported = {ability["name"]: ability for ability in web["heroes"][hero_name]["abilities"]}
            for ability in hero["abilities"]:
                target_keys = {
                    entry.get("name")
                    for tier in (ability.get("upgrades") or [])
                    for entry in (tier.get("entries") or [])
                    if entry.get("name")
                }
                required_keys = {
                    key for key, prop in (ability.get("properties") or {}).items()
                    if prop.get("value") or prop.get("spirit_scale") or key in target_keys
                }
                for key in required_keys:
                    with self.subTest(hero=hero_name, ability=ability["name"], prop=key):
                        self.assertIn(key, exported[ability["name"]]["props"])

    def test_base_weapon_dps_matches_game_for_every_hero(self):
        for name, hero in HEROES.items():
            with self.subTest(hero=name):
                actual = Loadout(name, [], net_worth=0).weapon_dps
                expected = hero["weapon"]["damage_per_second_with_reload"]
                self.assertAlmostEqual(actual, expected, places=6)

    def test_stage_ability_point_schedule(self):
        hero = HEROES["Drifter"]
        expected = {6000: 8, 12000: 15, 20000: 21, 32000: 26, 50000: 32}
        self.assertEqual(
            {nw: ability_points_for_networth(hero, nw) for nw in expected},
            expected,
        )

    def test_full_build_applies_all_ability_tiers(self):
        loadout = Loadout("Celeste", [], net_worth=50000)
        result = loadout.duel(REF)
        self.assertEqual(result["ability_levels"], [3, 3, 3, 3])

    def test_duel_can_hold_one_allocation_across_scenarios(self):
        loadout = Loadout("Celeste", [], net_worth=20000)
        allocation = loadout.ability_level_options[-1]
        result = loadout.duel(
            REF, focus=2.4, antiheal=50, incoming_bullet_frac=0.3,
            levels=allocation,
        )
        self.assertEqual(result["ability_levels"], list(allocation))
        self.assertEqual(result["incoming_bullet_fraction"], 0.3)

    def test_range_falloff_is_applied(self):
        loadout = Loadout("Drifter", [], net_worth=50000)
        near = loadout.weapon_dps_vs(0, 0, distance_m=18)
        far = loadout.weapon_dps_vs(0, 0, distance_m=30)
        self.assertAlmostEqual(near, loadout.weapon_dps, places=6)
        self.assertAlmostEqual(far / near, 0.6, places=6)

    def test_lifesteal_is_multiplicatively_pooled(self):
        loadout = Loadout("Drifter", ["Bullet Lifesteal", "Fury Trance"], 50000)
        self.assertAlmostEqual(loadout.bullet_lifesteal, pooled([13, 14]), places=6)

    def test_target_spirit_shred_is_not_counted_as_negative_self_resist(self):
        loadout = Loadout("Drifter", ["Spirit Shredder Bullets"], 50000)
        self.assertGreater(loadout.spirit_shred, 0)
        self.assertEqual(loadout.tech_resist, 0)

    def test_glass_cannon_health_penalty(self):
        base = Loadout("Drifter", [], 50000)
        glass = Loadout("Drifter", ["Glass Cannon"], 50000)
        self.assertAlmostEqual(glass.health / base.health, 0.87, places=6)

    def test_healing_tempo_requires_an_applied_heal(self):
        drifter = Loadout("Drifter", ["Healing Tempo"], 50000)
        victor = Loadout("Victor", ["Healing Tempo"], 50000)
        self.assertFalse(drifter.has_cast_heal)
        self.assertEqual(drifter.firerate_pct, 0)
        self.assertTrue(victor.has_cast_heal)
        self.assertGreater(victor.firerate_pct, 0)

    def test_buff_duration_and_condition_uptimes(self):
        # one engagement of FIGHT_WINDOW seconds: a 20s buff on a 40s
        # cooldown covers the whole fight; 12s on 15s is unchanged
        self.assertAlmostEqual(Loadout.item_uptime(ITEMS["Diviner's Kevlar"]),
                               min(1.0, 20 / min(40, FIGHT_WINDOW)))
        self.assertAlmostEqual(Loadout.item_uptime(ITEMS["Mercurial Magnum"]), 0.8)
        self.assertAlmostEqual(Loadout.item_uptime(ITEMS["Vampiric Burst"]), 5 / FIGHT_WINDOW)
        self.assertAlmostEqual(Loadout.item_uptime(ITEMS["Kinetic Dash"]), 0.75)

    def test_cooldown_reduction_pools_and_item_cdr_is_separate(self):
        loadout = Loadout(
            "Yamato", ["Compress Cooldown", "Superior Cooldown", "Transcendent Cooldown"], 50000
        )
        self.assertAlmostEqual(loadout.cdr, pooled([18, 20, 25]), places=6)
        self.assertAlmostEqual(loadout.item_cdr, 25, places=6)

    def test_billy_melee_bonus_health_is_not_flat_healing(self):
        loadout = Loadout("Billy", [], 50000)
        loadout.ability_levels = (3, 3, 3, 3)
        healing, parts = loadout.ability_healing()
        self.assertFalse(any(key == "MaxHealthMelee" for _, key, _ in parts))
        self.assertEqual(healing, 0)

    def test_heal_amp_does_not_inflate_passive_lifesteal(self):
        base = Loadout("Drifter", ["Bullet Lifesteal"], 50000)
        amp = Loadout("Drifter", ["Bullet Lifesteal", "Healing Tempo"], 50000)
        gun = 500.0
        self.assertAlmostEqual(
            base.healing_per_second(gun, 0) - base.hp_regen,
            amp.healing_per_second(gun, 0) - amp.hp_regen * 1.25,
            places=6,
        )

    def test_self_drain_is_not_reduced_by_enemy_antiheal(self):
        # Self-drain is a real HP cost: it is not clamped away when healing
        # is low (the old max(0, ...) made Blood Tribute's drain free).
        loadout = Loadout("Drifter", ["Blood Tribute"], 50000)
        no_anti = loadout.duel(REF, antiheal=0)
        anti = loadout.duel(REF, antiheal=35)
        expected = anti["gross_heal_ps"] * 0.65 - 50.0
        self.assertAlmostEqual(anti["heal_ps"], expected, places=6)
        self.assertEqual(no_anti["self_drain_ps"], 50.0)

    def test_instant_item_heal_is_not_double_uptime_weighted(self):
        loadout = Loadout("Drifter", ["Dispel Magic"], 50000)
        self.assertAlmostEqual(loadout.item_heal_ps, 250 / min(45, FIGHT_WINDOW), places=6)

    def test_target_resistance_is_not_counted_twice(self):
        loadout = Loadout("Drifter", [], 0)
        ref = {
            "health": 1000.0,
            "ehp": 2000.0,  # display-only mixed EHP must not enter TTK
            "dps": 100.0,
            "bullet_resist": 50.0,
            "tech_resist": 0.0,
        }
        result = loadout.duel(ref, headshot_rate=0, antiheal=0, focus=1)
        self.assertAlmostEqual(result["ttk"], 1000.0 / result["total_dps"], places=6)
        self.assertNotAlmostEqual(result["ttk"], 2000.0 / result["total_dps"], places=6)
        self.assertGreater(result["raw_total_dps"], result["total_dps"])

    def test_mixed_resistance_and_healing_order(self):
        loadout = Loadout("Drifter", [], 0)
        loadout.bullet_resist = 50.0
        loadout.tech_resist = 0.0
        pool = loadout.health + loadout.ability_bonus_health() + loadout.barrier_pool()
        self.assertAlmostEqual(loadout.ehp(), pool / 0.7, places=6)
        ref = {
            "health": 1000.0,
            "ehp": 1000.0,
            "dps": 100.0,
            "bullet_resist": 0.0,
            "tech_resist": 0.0,
        }
        result = loadout.duel(ref, headshot_rate=0, antiheal=0, focus=1)
        self.assertAlmostEqual(result["effective_incoming"], 70.0, places=6)
        self.assertAlmostEqual(result["ttd"], pool / (70.0 - result["heal_ps"]), places=6)

    def test_ability_resistance_is_upgrade_and_uptime_weighted(self):
        loadout = Loadout("Viscous", [], 50000)
        levels = (3, 3, 3, 3)
        ability = next(a for a in loadout.hero["abilities"] if a["name"] == "Goo Ball")
        props = loadout.resolved_ability_properties(ability, 3)
        uptime = min(1.0, props["AbilityDuration"]["value"]
                     / min(props["AbilityCooldown"]["value"], FIGHT_WINDOW))
        granted = props["BulletResist"]["value"] * uptime
        bullet, spirit = loadout.total_resists(levels)
        self.assertAlmostEqual(bullet, pooled([loadout.bullet_resist, granted]), places=6)
        self.assertAlmostEqual(spirit, pooled([loadout.tech_resist, granted]), places=6)

    def test_ability_shred_is_upgrade_and_uptime_weighted(self):
        loadout = Loadout("Drifter", [], 50000)
        levels = (3, 3, 3, 3)
        ability = next(a for a in loadout.hero["abilities"] if a["name"] == "Stalker's Mark")
        props = loadout.resolved_ability_properties(ability, 3)
        uptime = min(1.0, props["AbilityDuration"]["value"]
                     / min(props["AbilityCooldown"]["value"], FIGHT_WINDOW))
        granted = abs(props["BulletResistReduction"]["value"]) * uptime
        bullet, spirit = loadout.total_shreds(levels)
        self.assertAlmostEqual(bullet, pooled([loadout.bullet_shred, granted]), places=6)
        self.assertAlmostEqual(spirit, loadout.spirit_shred, places=6)


class ShopAndItemTests(unittest.TestCase):
    """Mechanics re-verified against deadlock.wiki on 2026-09-25."""

    def test_twelve_universal_slots(self):
        self.assertEqual(MAX_SLOTS, 12)
        weapons = sorted(n for n, it in ITEMS.items()
                         if it["slot"] == "weapon" and it["tier"] == 1
                         and not it["is_active"] and not it["heroes_restricted"])
        spirits = sorted(n for n, it in ITEMS.items()
                         if it["slot"] == "spirit" and not it["is_active"]
                         and it["tier"] != 5 and not it["heroes_restricted"])
        twelve = (weapons + spirits)[:12]
        self.assertTrue(valid_build(twelve))            # any category mix
        self.assertFalse(valid_build((weapons + spirits)[:13]))

    def test_escalating_resilience_caps_at_thirty_percent(self):
        loadout = Loadout("Drifter", ["Escalating Resilience"], 0)
        self.assertAlmostEqual(loadout.bullet_resist, 30 * 0.85, places=6)

    def test_burst_fire_on_hit_rate_is_uptime_weighted(self):
        loadout = Loadout("Drifter", ["Burst Fire"], 0)
        self.assertAlmostEqual(loadout.firerate_pct, 10 + 32 * 4.5 / 9, places=6)

    def test_golden_goose_egg_penalises_own_damage_not_enemies(self):
        base = Loadout("Haze", [], 20000)
        egg = Loadout("Haze", ["Golden Goose Egg"], 20000)
        sc = SCENARIO_BY_NAME["skirmish"]
        levels = base.ability_level_options[0]
        a = base.scenario_result(REF, sc, levels)
        b = egg.scenario_result(REF, sc, levels)
        self.assertAlmostEqual(b["enemy_damage_mult"], 1.0, places=9)
        self.assertLess(b["gun_dps"], a["gun_dps"])

    def test_bloodscent_amp_needs_isolation(self):
        lo = Loadout("Drifter", [], 50000)
        levels = (3, 3, 3, 3)
        pick = lo.scenario_result(REF, SCENARIO_BY_NAME["pick"], levels)
        team = lo.scenario_result(REF, SCENARIO_BY_NAME["teamfight"], levels)
        self.assertAlmostEqual(pick["isolation"], 1.0)
        # teamfight isolation comes only from Eternal Night's uptime
        props = lo.resolved_ability_properties(lo.hero["abilities"][3], 3)
        ult = props["AbilityDuration"]["value"] / min(props["AbilityCooldown"]["value"], FIGHT_WINDOW)
        self.assertAlmostEqual(team["isolation"], ult, places=6)

    def test_siphon_healing_ignores_antiheal(self):
        lo = Loadout("Drifter", ["Siphon Bullets"], 50000)
        ref = dict(REF, health=4000.0)
        none = lo.duel(ref, antiheal=0, focus=1.0)
        full = lo.duel(ref, antiheal=100, focus=1.0)
        self.assertGreater(full["siphon_heal_ps"], 0)
        self.assertAlmostEqual(full["heal_ps"], full["siphon_heal_ps"] - full["self_drain_ps"], places=6)
        self.assertGreater(none["heal_ps"], full["heal_ps"])

    def test_hunters_aura_is_range_gated(self):
        lo = Loadout("Haze", ["Hunter's Aura"], 20000)
        self.assertEqual(lo.bullet_shred, 0)            # not a global shred
        self.assertTrue(lo._gated_bullet_shred(10, False))
        self.assertFalse(lo._gated_bullet_shred(20, False))
        doubled = lo._gated_bullet_shred(10, True)[0]
        self.assertAlmostEqual(doubled, 2 * lo._gated_bullet_shred(10, False)[0])

    def test_juggernaut_slows_attackers(self):
        base = Loadout("Abrams", [], 32000)
        jug = Loadout("Abrams", ["Juggernaut"], 32000)
        sc = SCENARIO_BY_NAME["teamfight"]
        levels = base.ability_level_options[0]
        self.assertLess(jug.scenario_result(REF, sc, levels)["enemy_damage_mult"],
                        base.scenario_result(REF, sc, levels)["enemy_damage_mult"])

    def test_weapon_shielding_resist_only_during_barrier(self):
        lo = Loadout("Haze", ["Weapon Shielding"], 20000)
        # +18% bullet resist for the 8s barrier (deadlock.wiki, 05-22-2026 patch)
        self.assertAlmostEqual(lo.bullet_resist, 18 * 8 / min(35, FIGHT_WINDOW), places=6)
        self.assertAlmostEqual(lo.barrier_pool(), 300.0, places=6)   # once per fight

    def test_mercurial_magnum_is_percent_of_base_bullet(self):
        # shipped field: "+20% Base Bullet Damage" (+0.38% per Spirit Power)
        lo = Loadout("Bebop", ["Mercurial Magnum"], 50000)
        it = ITEMS["Mercurial Magnum"]["properties"]
        pct = it["BulletsBonusMagicDamage"]["value"] + lo.spirit_power * it["BulletsBonusMagicDamage"]["spirit_scale"]
        per_bullet = pct / 100 * lo.base_bullet_damage * lo.pellets
        window = min(lo.clip_size, it["BuffDuration"]["value"] / lo.cycle_time)
        flat = it["Damage"]["value"] + lo.spirit_power * it["Damage"]["spirit_scale"]
        expected = (flat + per_bullet * window) / min(it["AbilityChargeUpTime"]["value"], FIGHT_WINDOW)
        self.assertAlmostEqual(lo.procs[0][1], expected, places=6)
        self.assertLess(lo.procs[0][1], 150)      # was ~976 when read as flat damage

    def test_ability_scale_types(self):
        lo = Loadout("Venator", [], 50000)
        ira = next(i for i, a in enumerate(lo.hero["abilities"]) if a["name"] == "Ira Domini")
        inst = dict((k, v) for k, v, _, _ in lo._instances(ira, 0))
        self.assertAlmostEqual(inst["BonusDamage"], 115 + 3.0 * lo.boons, places=6)   # per boon, not per SP
        graves = Loadout("Graves", [], 50000)
        dec = next(i for i, a in enumerate(graves.hero["abilities"]) if a["name"] == "Borrowed Decree")
        self.assertNotIn("TechPower", [k for k, *_ in graves._instances(dec, 3)])

    def test_no_hero_specific_engagement_range(self):
        ranges = {Loadout(h, [], 0).engagement_range for h in HEROES}
        self.assertEqual(len(ranges), 1)


if __name__ == "__main__":
    unittest.main()
