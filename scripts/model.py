"""
Deadlock combat model.

Every formula here is sourced from either the shipped game files (dataset.json)
or a verified wiki mechanic page. Verified facts, patch 09-16-2026 (still the
live patch on 2026-09-25):

  * Boons come from NET WORTH thresholds, not spending. Buying items never
    changes your boon count. Max boon 35.
  * Per-boon scaling is per hero (health/bullet/melee) except Spirit Power,
    which is 1.1 for most heroes (Grey Talon 1.6, Haze 0.5, a few at 1.2-1.3).
  * Spirit damage is LINEAR:  dmg = base + SpiritPower * coefficient
  * Resistances stack MULTIPLICATIVELY: total = 1 - prod(1 - Ri)
    Resist REDUCTION is pooled the same way, then SUBTRACTED from total resist.
  * Lifesteal stacks multiplicatively (deadlock.wiki/Lifesteal worked example).
  * "Investments": bonuses scale off CUMULATIVE SOULS SPENT PER CATEGORY
    (not per item tier). Caps at 28,800/category for +115% weapon damage,
    +66% health, +100 flat Spirit. Big discontinuity at 4,800 ("the 4.8k spike").
  * 12 item slots max: 9 universal slots plus 3 Extra Slots unlocked by
    destroying Walkers. Slots accept any category (deadlock.wiki/Items,
    steamdb flex-slots page, build client-6698). Max 4 ACTIVE items.
  * Tier costs: 800 / 1600 / 3200 / 6400. Tier 5 is Street Brawl only.

Scoring is a scenario ensemble (see SCENARIOS). Each scenario resolves a fight
against a reference opponent as score = time-to-die / time-to-kill, and the
ensemble score is the weighted geometric mean. One legal ability-upgrade
allocation is held across every scenario.
"""

import itertools
import json
import math
import os
from collections import namedtuple
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")

with open(os.path.join(DATA, "dataset.json"), encoding="utf-8") as f:
    DATASET = json.load(f)

HEROES = DATASET["heroes"]
ITEMS = DATASET["items"]

# Investments table (cumulative souls spent per category -> bonus).
# Verified identical across all 38 heroes and against deadlock.wiki/Investments.
INVEST = {
    "weapon":   [(800, 9), (1600, 12), (2400, 15), (3200, 18), (4800, 46),
                 (6400, 54), (8000, 62), (11200, 74), (16000, 86),
                 (22400, 100), (28800, 115)],
    "vitality": [(800, 9), (1600, 12), (2400, 15), (3200, 20), (4800, 38),
                 (6400, 42), (8000, 46), (11200, 50), (16000, 54),
                 (22400, 60), (28800, 66)],
    "spirit":   [(800, 7), (1600, 11), (2400, 15), (3200, 19), (4800, 38),
                 (6400, 45), (8000, 52), (11200, 59), (16000, 66),
                 (22400, 75), (28800, 100)],
}

MAX_SLOTS = 12
BASE_SLOTS = 9
# Extra slots unlock one per enemy Walker destroyed (deadlock.wiki/Extra_Slots,
# since 11-21-2025). The files do not say when Walkers fall, so this is an
# assumption: net worth at which the 1st / 2nd / 3rd Walker is typically down.
WALKER_NET_WORTH = (16000, 26000, 36000)


def slots_at(net_worth):
    """Item slots available at a net worth: 9, plus one per Walker destroyed."""
    return BASE_SLOTS + sum(1 for nw in WALKER_NET_WORTH if net_worth >= nw)
MAX_ACTIVES = 4
ENGAGEMENT_RANGE_M = 18.0
CONDITIONAL_UPTIME = 0.75
ABILITY_TIER_COST = (0, 1, 3, 8)

# Healing cannot cancel more than this share of post-mitigation incoming
# damage. Real sustain is not steady-state: lifesteal stops while you are
# stunned, silenced, repositioning or between targets, and burst arrives
# faster than healing ticks. The old 8% floor let a build that out-healed a
# steady DPS number score 12.5x and read as "unkillable".
NET_INCOMING_FLOOR = 0.25
# Damage splashed onto enemies other than your target (Ricochet bounces, AoE
# abilities and procs) is worth half as much as focused damage.
CLEAVE_VALUE = 0.5
# Share of an enemy's bullet-damage cycle spent reloading; fire-rate slows
# do not shorten a reload.
RELOAD_SHARE = 0.15
# Average current health of a target across a fight, for %current-HP effects.
AVG_CURRENT_HP = 0.6
# Every scenario is ONE engagement of this many seconds, entered with all
# cooldowns ready (you open a teamfight with your actives and ultimate).
# Anything with a longer cooldown is used once per fight: its uptime and
# damage are amortised over the window, not over its full cooldown. The old
# whole-game average credited Vampiric Burst with 17% uptime and Drifter's
# Eternal Night with 6%, which undervalued every burst kit and active item.
FIGHT_WINDOW = 20.0


def window_cd(cd):
    """Effective cooldown inside one engagement."""
    return min(cd, FIGHT_WINDOW) if cd > 0 else cd

Scenario = namedtuple(
    "Scenario",
    "name weight focus antiheal bullet_frac distances isolation headshot")

# distances: (metres, share of the fight) -- a spread, not one point, so a
# close-range item gets partial credit instead of a 0/1 cliff at its radius.
# isolation: share of the fight your target has no ally within 20m (Bloodscent).
SCENARIOS = (
    Scenario("pick", 0.15, 1.0, 20, 0.65, ((8, .30), (15, .45), (25, .25)), 1.00, 0.25),
    Scenario("skirmish", 0.30, 1.6, 35, 0.60, ((8, .25), (18, .50), (28, .25)), 0.25, 0.25),
    Scenario("teamfight", 0.35, 2.4, 50, 0.55, ((10, .25), (20, .50), (30, .25)), 0.0, 0.25),
    Scenario("bullet_team", 0.10, 2.2, 40, 0.80, ((10, .25), (18, .50), (28, .25)), 0.0, 0.25),
    Scenario("spirit_team", 0.10, 2.2, 40, 0.30, ((10, .25), (18, .50), (28, .25)), 0.0, 0.25),
)
SCENARIO_BY_NAME = {s.name: s for s in SCENARIOS}

# Objective = scenario weights. "allround" is the published ranking;
# "teamfight" drops the isolated pick and skirmish entirely.
OBJECTIVES = {
    "allround": {s.name: s.weight for s in SCENARIOS},
    "teamfight": {"teamfight": 0.6, "bullet_team": 0.2, "spirit_team": 0.2},
}

# Items whose effect exists only within a radius of the holder.
# name -> (radius property, properties that are gated)
RANGE_GATED = {
    "Stalker": ("ProcRadius", ("BulletResistReduction", "DPS")),
    "Hunter's Aura": ("Radius", ("BulletArmorReduction", "FireRateSlow")),
}
# Items whose negative OutgoingDamagePenaltyPercent is on YOUR damage.
SELF_DAMAGE_PENALTY = ("Golden Goose Egg", "Cursed Relic")
# Ultimates that make their targets count as Isolated (deadlock.wiki/Drifter:
# Eternal Night "affected enemies are considered isolated for the duration").
ISOLATING_ULTIMATES = ("drifter_darkness",)


def investment_bonus(category, souls_spent):
    """Step function: total bonus at a given cumulative category spend."""
    bonus = 0.0
    for threshold, value in INVEST[category]:
        if souls_spent >= threshold:
            bonus = float(value)
        else:
            break
    return bonus


def boons_for_networth(hero, net_worth):
    """Boon count from net worth, using the hero's shipped gold table."""
    li = hero["level_info"]
    count = 0
    for lvl in sorted(int(k) for k in li):
        req = li[str(lvl)]["required_gold"] if str(lvl) in li else li[lvl]["required_gold"]
        if req is None:
            continue
        if net_worth >= req:
            count = lvl - 1   # level 1 == 0 boons
        else:
            break
    return min(count, 35)


def ability_points_for_networth(hero, net_worth):
    """Ability points actually unlocked at a net-worth checkpoint."""
    return sum(
        1 for info in hero["level_info"].values()
        if info.get("required_gold") is not None
        and net_worth >= info["required_gold"]
        and "EAbilityPoints" in (info.get("bonus") or [])
    )


@lru_cache(maxsize=None)
def _hero_progress(hero_name, net_worth):
    hero = HEROES[hero_name]
    return boons_for_networth(hero, net_worth), ability_points_for_networth(hero, net_worth)


@lru_cache(maxsize=None)
def ability_level_candidates(point_count, ability_count=4):
    """All legal tier allocations that spend the maximum usable points.

    Ability tiers cost 1/2/5 additional points, or 0/1/3/8 cumulative.
    There are only 1-12 maximum-spend allocations at the five checkpoints,
    so evaluating every one is both cheap and deterministic.
    """
    allocations = list(itertools.product(range(4), repeat=ability_count))
    spent = [sum(ABILITY_TIER_COST[level] for level in levels)
             for levels in allocations]
    usable = max((value for value in spent if value <= point_count), default=0)
    return tuple(levels for levels, value in zip(allocations, spent)
                 if value == usable)


# Universal reload-initiation constant. Solving
#   clip*bullets*dmg / dps_with_reload  -  clip*cycle  -  reload
# gives exactly +0.2500s for 32 of the 38 heroes; the 6 deviations are exactly
# the burst/charge weapons (Lash, Seven, Paradox, Sinclair, Paige, The
# Doorman), whose shipped cycle_time is not the average shot interval. For
# those, effective_cycle() inverts the game's own DPS figure instead.
RELOAD_OVERHEAD = 0.25


@lru_cache(maxsize=None)
def effective_cycle(hero_name):
    """The weapon's true AVERAGE seconds-per-shot.

    For most heroes this equals the shipped cycle_time. For burst weapons it is
    lower, because shots inside a burst fire faster than cycle_time; for
    charge-up weapons it is higher. Derived by inverting the game's own
    damage_per_second_with_reload:

        effective_cycle = (magazine_time - reload - 0.25) / clip
    """
    w = HEROES[hero_name]["weapon"]
    clip = w.get("clip_size") or 0
    cyc = w.get("cycle_time") or 0
    rel = w.get("reload_duration") or 0
    dmg = w.get("bullet_damage") or 0
    dps = w.get("damage_per_second_with_reload") or 0
    bullets = w.get("bullets") or 1
    if not (clip and dps and dmg):
        return cyc
    mag_time = (clip * bullets * dmg) / dps
    eff = (mag_time - rel - RELOAD_OVERHEAD) / clip
    return eff if eff > 0 else cyc


def pooled(values):
    """Multiplicative pooling used for resists and resist-reduction."""
    prod = 1.0
    for v in values:
        prod *= (1.0 - v / 100.0)
    return (1.0 - prod) * 100.0


def _pval(it, key):
    return (it["properties"].get(key) or {}).get("value") or 0.0


def _pscale(it, key):
    return (it["properties"].get(key) or {}).get("spirit_scale") or 0.0


# ------------------------------------------------------------ ability cache
_RESOLVED = {}


def resolve_ability(hero_name, index, level):
    """Ability properties after applying the first ``level`` upgrade tiers.

    Pure function of (hero, ability, level) -- Spirit Power is applied later
    -- so it is cached once per process instead of once per build.
    """
    key = (hero_name, index, level)
    cached = _RESOLVED.get(key)
    if cached is not None:
        return cached
    ability = HEROES[hero_name]["abilities"][index]
    props = {k: dict(v) for k, v in (ability.get("properties") or {}).items()}
    for tier in (ability.get("upgrades") or [])[:level]:
        for entry in tier.get("entries") or []:
            name = entry.get("name")
            bonus = entry.get("bonus")
            if not name or bonus is None:
                continue
            p = props.setdefault(name, {
                "value": 0.0, "raw": None, "label": "", "css": None,
                "spirit_scale": 0.0,
            })
            kind = entry.get("type")
            if kind == "EAddToScale":
                p["spirit_scale"] = (p.get("spirit_scale") or 0.0) + bonus
            elif kind == "EMultiplyScale":
                # A zero value in the dump represents a bespoke non-Spirit
                # scale (melee, distance, etc.), which this generic model
                # deliberately does not guess at.
                if bonus:
                    p["spirit_scale"] = (p.get("spirit_scale") or 0.0) * bonus
            elif kind == "EMultiplyBase":
                p["value"] = (p.get("value") or 0.0) * (1 + bonus / 100.0)
            else:  # plain entry and EAddToBase
                p["value"] = (p.get("value") or 0.0) + bonus
    _RESOLVED[key] = props
    return props


def _is_aoe(props):
    """Radius-bearing or multi-target abilities hit more than one enemy."""
    if ((props.get("AbilityUnitTargetLimit") or {}).get("value") or 0) > 1:
        return True
    return any("Radius" in k and (p.get("value") or 0) > 0
               for k, p in props.items())


# Damage properties that are rates (per second) rather than instances.
_RATE_KEYS = ("DPS", "LifeDrainPerSecond", "TurretDPS", "DamagePerSecond")
# Percentage / self-damage / meta fields that are not raw damage numbers.
_SKIP_KEYS = frozenset((
    "SelfDamagePct", "OutgoingTechDamagePercent", "DotHealthPercent",
    "BloodSpillDPSPercent", "MaxHealthDamage", "HealthToDamage",
    "LowHealthEnemyDamageBonus", "SpadeDamageBonus", "HeadshotBonus",
    "BonusSpirit", "MinimumDamage",
    # Paradox's Kinetic Carbine values are % bullet amplification.
    "MaxBonusBulletDamage", "MinBonusBulletDamage",
    "DamageThreshold", "SleepDamageThreshold",
    "CurrentHealthPercentDamage", "SelfDamagePercentage",
    "DamageAmplificationPerStack", "AmpDamagePercent",
    # Graves' Borrowed Decree grants Spirit Power; it is a buff, not damage.
    "TechPower",
))
# What an ability's scale coefficient multiplies. The extractor stores every
# scale as "spirit_scale"; the shipped scale type says what it really scales
# with. Venator's Ira Domini is +3.0 per BOON, Silver's Boot Kick +0.9 x light
# melee damage -- multiplying those by Spirit Power overstated them ~4x.
_SPIRIT_SCALES = (None, "", "ETechPower")
_SCALE_STATS = {"ELevelUpBoons": "boons", "ELightMeleeDamage": "light_melee",
                "EHeavyMeleeDamage": "heavy_melee"}
# Genuine spirit damage coefficients peak near 3.0 (Venator's Ira Domini).
# Anything above is a percentage/health-scaling field mis-tagged as damage.
_MAX_DAMAGE_COEF = 3.2
# A per-tick drip is small; anything larger next to a TickRate is a per-hit
# instance (Graves' Grasping Hands). Total ticks are capped.
_MAX_TICK_BASE = 40.0
_MAX_TICKS = 16.0


@lru_cache(maxsize=None)
def ability_digest(hero_name, idx, level):
    """Static, Spirit-Power-independent summary of one ability at one tier.

    Parsing the raw property dicts is the expensive part of an evaluation, and
    it depends only on (hero, ability, tier), so it happens once per process.
    Spirit Power, cooldown reduction and max health are applied per build.
    """
    props = resolve_ability(hero_name, idx, level)
    ability = HEROES[hero_name]["abilities"][idx]

    def g(key):
        return (props.get(key) or {}).get("value") or 0.0

    cd, dur, tick = g("AbilityCooldown"), g("AbilityDuration"), g("TickRate")
    ticks = min(dur / tick, _MAX_TICKS) if tick >= 0.25 and dur > 0 else 1.0

    damage = []
    for k, p in props.items():
        if p.get("css") not in ("tech_damage", "damage") or k in _SKIP_KEYS:
            continue
        coef = p.get("spirit_scale") or 0.0
        if coef > _MAX_DAMAGE_COEF:
            continue
        base = p.get("value") or 0.0
        if base <= 0 and coef <= 0:
            continue
        if any(r in k for r in _RATE_KEYS):
            kind = "rate"
        elif ticks > 1 and k in ("Damage", "DamagePerTick", "BurnDamage") and base <= _MAX_TICK_BASE:
            kind = "tick"
        else:
            kind = "instant"
        stype = p.get("scale_stat")
        scale_by = "spirit" if stype in _SPIRIT_SCALES else _SCALE_STATS.get(stype)
        if scale_by is None:
            coef = 0.0          # unknown scale (stack counts, ...): base only
            if base <= 0:
                continue
        damage.append((k, base, coef, kind, scale_by or "spirit"))

    # Healing rules, each checked against the shipped descriptions:
    #  * percent / multiplier / lifesteal / on-kill fields are not flat HP
    #    (Lash's HealPctVsHeroes heals 40% of damage dealt; lifesteal fields
    #    are the lifesteal channel);
    #  * Billy's melee "Bonus Health" is temporary max health, not healing;
    #  * 'MaxHealth' fields heal a % of max health per cast (Ivy Stone Form);
    #  * TotalHealthRegen is a total spread over the buff (Victor Jumpstart);
    #  * per-second / regen fields tick while the ability runs.
    heals = []
    for k, p in props.items():
        if p.get("css") != "healing" or not p.get("value"):
            continue
        label = (p.get("label") or "").lower()
        lk = k.lower()
        if "bonus health" in label or k == "MaxHealthMelee":
            continue
        if ("pct" in lk or "percent" in lk or "mult" in lk or "factor" in lk
                or "lifesteal" in lk or "perkill" in lk or "on kill" in label):
            continue
        if "maxhealth" in lk:
            mode = "maxhealth"
        elif k == "TotalHealthRegen":
            mode = "flat"
        elif "persecond" in lk or "regen" in lk or "dps" in lk:
            mode = "rate"
        else:
            mode = "flat"
        heals.append((k, p["value"], p.get("spirit_scale") or 0.0, mode))

    res_dur = dur or g("AbilityChannelTime")
    both = g("DamageResistPctWhileChanneling")
    rb = g("BulletResist") + g("BulletResistOnActive") + both
    rt = g("TechResist") + g("SpiritResist") + both
    resist = (cd, res_dur, rb, rt) if (rb > 0 or rt > 0) else None

    shred = None
    if not g("AbilityChargesConditionally"):
        generic = g("DebuffDuration") or dur
        b_dur = g("BulletResistReductionDuration") or g("DiamondResistShredDuration") or generic
        s_dur = g("TechResistReductionDuration") or g("DiamondResistShredDuration") or generic
        sb = sum(abs(g(k)) for k in ("BulletResistReduction", "BulletArmorReduction", "DiamondResistShred"))
        ss = sum(abs(g(k)) for k in ("TechResistDebuff", "MagicResistReduction",
                                     "TechArmorDamageReduction", "DiamondResistShred"))
        if sb or ss:
            shred = (cd, sb, ss, b_dur, s_dur)

    barrier = None
    bp = props.get("CombatBarrier")
    if bp and bp.get("value"):
        barrier = (bp["value"], bp.get("spirit_scale") or 0.0, cd,
                   g("MaxLifetime") or dur)

    dot = None
    dp = props.get("DotHealthPercent")
    if dp and (dp.get("value") or dp.get("spirit_scale")):
        dot = (dp.get("value") or 0.0, dp.get("spirit_scale") or 0.0)

    return {
        "cd": cd, "dur": dur, "ticks": ticks,
        "conditional": bool(g("AbilityChargesConditionally")),
        "aoe": _is_aoe(props),
        "damage": tuple(damage), "heals": tuple(heals),
        "resist": resist, "shred": shred, "barrier": barrier, "dot": dot,
        "bonus_health": g("BonusMaxHealth") + g("BonusHealth"),
        "lifesteal": g("AbilityLifestealPercentHero"),
        "iso_amp": g("AmpDamagePercent") if g("IsolationRange") else 0.0,
        "isolating_ult": ability.get("class_name") in ISOLATING_ULTIMATES,
    }


class Loadout:
    """A hero + item set at a given net worth, with all derived stats."""

    # item property -> internal stat bucket
    FLAT_SPIRIT = ("TechPower", "SpiritPower", "BonusSpirit")
    WEAPON_PCT = ("BaseAttackDamagePercent",)
    FIRERATE_PCT = ("BonusFireRate", "ActiveBonusFireRate", "ActivatedFireRate",
                    "FervorFireRate")
    CLIP_PCT = ("BonusClipSizePercent",)
    CLIP_FLAT = ("BonusClipSize",)
    HEALTH_FLAT = ("BonusHealth",)
    HEALTH_PCT = ("MaxHealthLossPercent",)
    BULLET_RESIST = ("BulletResist", "BulletResistBelowThreshold", "BuffBulletResist")
    TECH_RESIST = ("TechResist", "TechResistBelowThreshold", "BuffTechResist")
    BULLET_LIFESTEAL = ("BulletLifestealPercent", "ActiveBonusLifesteal")
    SPIRIT_LIFESTEAL = ("AbilityLifestealPercentHero",
                        "AbilityLifestealPercentHeroPassive",
                        "BonusSpiritLifesteal")
    CDR = ("CooldownReduction",)
    ITEM_CDR = ("ItemCooldownReduction",)
    HP_REGEN = ("BonusHealthRegen",)
    OOC_REGEN = ("OutOfCombatHealthRegen",)
    BULLET_SHRED = ("BulletArmorReduction", "BulletResistReduction")
    SPIRIT_SHRED = ("MagicResistReduction", "TechArmorDamageReduction")
    # healing that is not lifesteal: burst heals amortised over their cooldown
    BURST_HEAL = ("TotalHealthRegen", "LifestealHeal", "HealPerStack", "HealOnActivate")
    HEAL_AMP = ("HealAmpCastPercent", "HealAmpRegenPercent")

    # Kept for callers that build a single ad-hoc scenario through duel().
    ANTIHEAL_ASSUMED = 35.0
    FOCUS_FIRE = 1.6
    # Healing Tempo explicitly excludes passive Bullet/Spirit Lifesteal.
    AMP_ON_LIFESTEAL = False

    def __init__(self, hero_name, item_names, net_worth=None):
        self.hero_name = hero_name
        self.hero = HEROES[hero_name]
        self.item_names = list(item_names)
        self.items = [ITEMS[n] for n in self.item_names]
        self._names = set(self.item_names)

        self.spend = sum(i["cost"] or 0 for i in self.items)
        self.net_worth = net_worth if net_worth is not None else self.spend
        self.boons, self.ability_points = _hero_progress(hero_name, self.net_worth)
        self.ability_level_options = ability_level_candidates(
            self.ability_points, len(self.hero["abilities"]))
        self.ability_levels = self.ability_level_options[0]
        self.engagement_range = ENGAGEMENT_RANGE_M
        self._level_cache = {}
        self._gun_cache = {}
        self._falloff_cache = {}

        self._aggregate()
        self._derive()
        self._item_effects()

    # ---------------------------------------------------------------- stats
    @staticmethod
    def item_uptime(it, item_cdr=0.0):
        """Fraction of time an active/proc item's buff is running.

        Active items grant their headline buff for AbilityDuration on an
        AbilityCooldown. Infuser's 70% spirit lifesteal is 7s on a 30s cooldown
        = 23% uptime, NOT a permanent 70%.
        """
        dur = (_pval(it, "AbilityDuration") or _pval(it, "BuffDuration")
               or _pval(it, "BarrierDuration"))
        cd = _pval(it, "AbilityCooldown")
        if dur > 0 and cd <= 0:
            return CONDITIONAL_UPTIME
        if dur <= 0 or cd <= 0:
            return 1.0
        effective_cd = window_cd(cd * max(0.05, 1 - item_cdr / 100.0))
        return min(1.0, dur / effective_cd)

    def _has_cast_heal(self):
        """Whether this build can trigger effects that require an applied heal."""
        for it in self.items:
            if any(_pval(it, k) for k in self.BURST_HEAL):
                return True
        for ability in self.hero["abilities"]:
            for p in (ability.get("properties") or {}).values():
                if p.get("css") == "healing" and p.get("value"):
                    key = (p.get("label") or "").lower()
                    if "lifesteal" not in key and "regen" not in key:
                        return True
        return False

    def _prop_value(self, it, key):
        """Uptime-weighted value of one property on one item.

        Classification comes from the item's own tooltip sections:
          innate           -> always on, full value
          active / passive -> conditional buff, weighted by duration/cooldown
        Untyped proc sections are classified as passive by extract.py.
        """
        name = it["name"]
        # Healing Tempo only grants these buffs after an applied heal. Passive
        # lifesteal and innate regen explicitly do not trigger it.
        if (name == "Healing Tempo"
                and key in ("BonusFireRate", "BonusMoveSpeed")
                and not self.has_cast_heal):
            return 0.0
        # Radius-gated effects are applied per engagement distance instead.
        gate = RANGE_GATED.get(name)
        if gate and key in gate[1]:
            return 0.0
        if key == "OutgoingDamagePenaltyPercent":
            return 0.0  # routed explicitly (self vs enemy) in _item_effects
        props = it["properties"]
        if key == "BulletResist" and "BulletResistPerStack" in props:
            # Escalating Resilience: MaxArmorStacks is labelled "Max Bullet
            # Resist" -- it is the 30% cap, not a stack count
            # (deadlock.wiki: 2%/stack, 30% max). Stacks decay between
            # exchanges, so average 85% of the cap.
            cap = _pval(it, "MaxArmorStacks")
            return cap * 0.85
        p = props.get(key)
        if not p or not p.get("value"):
            return 0.0
        val = p["value"]
        sec = (it.get("sections") or {}).get(key)
        if sec == "innate":
            return val
        uptime = self.item_uptime(it, getattr(self, "item_cdr", 0.0))
        # Above/below-health passives are present for only the corresponding
        # fraction of a full-health-to-zero exchange.
        threshold = _pval(it, "LifeThreshold")
        below = _pval(it, "HealthThreshold")
        if sec == "passive" and threshold:
            uptime *= max(0.0, min(1.0, 1.0 - threshold / 100.0))
        elif sec == "passive" and below and "BelowThreshold" in key:
            uptime *= max(0.0, min(1.0, below / 100.0))
        if sec in ("active", "passive"):
            return val * uptime
        # Not listed in any tooltip section: fall back to name/sibling heuristics.
        if key.startswith("Active") or (key + "Passive") in props:
            return val * uptime
        return val

    def _sum_prop(self, keys):
        total = 0.0
        for it in self.items:
            for k in keys:
                total += self._prop_value(it, k)
        return total

    def _pool_prop(self, keys, extra=()):
        vals = [abs(v) for it in self.items for k in keys
                for v in (self._prop_value(it, k),) if v]
        vals.extend(e for e in extra if e)
        return pooled(vals) if vals else 0.0

    def _aggregate(self):
        self.has_cast_heal = self._has_cast_heal()
        self.spend_by_cat = {"weapon": 0, "vitality": 0, "spirit": 0}
        for it in self.items:
            if it["slot"] in self.spend_by_cat:
                self.spend_by_cat[it["slot"]] += it["cost"] or 0

        self.inv_weapon = investment_bonus("weapon", self.spend_by_cat["weapon"])
        self.inv_vit = investment_bonus("vitality", self.spend_by_cat["vitality"])
        self.inv_spirit = investment_bonus("spirit", self.spend_by_cat["spirit"])

        pb = self.hero["per_boon"]
        # Item cooldown is a separate stat. Compute it first so uptime-weighted
        # item properties can use the effective item cooldown.
        item_cdr_values = [abs(_pval(it, k)) for it in self.items
                           for k in self.ITEM_CDR if _pval(it, k)]
        self.item_cdr = pooled(item_cdr_values) if item_cdr_values else 0.0

        self.spirit_power = (
            self.boons * (pb["spirit_power"] or 0)
            + self._sum_prop(self.FLAT_SPIRIT)
            + self.inv_spirit
        )
        melee_boon = self.boons * (pb.get("melee_damage") or 0)
        base = self.hero["base"]
        self.scale_stats = {
            "spirit": self.spirit_power, "boons": float(self.boons),
            "light_melee": (base.get("light_melee_damage") or 0) + melee_boon,
            "heavy_melee": (base.get("heavy_melee_damage") or 0) + melee_boon,
        }
        self.weapon_pct = self._sum_prop(self.WEAPON_PCT) + self.inv_weapon
        self.firerate_pct = self._sum_prop(self.FIRERATE_PCT)
        self.clip_pct = self._sum_prop(self.CLIP_PCT)
        self.clip_flat = self._sum_prop(self.CLIP_FLAT)
        self.cdr = self._pool_prop(self.CDR)

        # health: (base + boons) scaled by vitality investment, then flats
        base_hp = (self.hero["base"].get("max_health") or 0) + self.boons * (pb["health"] or 0)
        self.health = base_hp * (1 + self.inv_vit / 100.0) + self._sum_prop(self.HEALTH_FLAT)
        # Colossus exposes its temporary base-health increase outside the
        # tooltip section map, so weight it explicitly by the active uptime.
        base_health_pct = sum(_pval(it, "BonusBaseHealth") * self.item_uptime(it, self.item_cdr)
                              for it in self.items if _pval(it, "BonusBaseHealth"))
        self.health *= 1 + base_health_pct / 100.0
        self.health *= max(0.05, 1 + self._sum_prop(self.HEALTH_PCT) / 100.0)

        self.bullet_resist = self._pool_prop(
            self.BULLET_RESIST,
            [self.boons * pb["bullet_resist"]] if pb.get("bullet_resist") else [])
        self.tech_resist = self._pool_prop(
            self.TECH_RESIST,
            [self.boons * pb["tech_resist"]] if pb.get("tech_resist") else [])

        # Lifesteal stacks MULTIPLICATIVELY (deadlock.wiki/Lifesteal).
        self.bullet_lifesteal = self._pool_prop(self.BULLET_LIFESTEAL)
        self.spirit_lifesteal = self._pool_prop(self.SPIRIT_LIFESTEAL)
        self.hp_regen = (self.hero["base"].get("base_health_regen") or 0) + self._sum_prop(self.HP_REGEN)
        # HealAmpCastPercent and HealAmpRegenPercent are the two channels of
        # ONE amplification value, not additive bonuses.
        self.heal_amp_cast = self._sum_prop(("HealAmpCastPercent",))
        self.heal_amp_regen = self._sum_prop(("HealAmpRegenPercent",))
        self.heal_amp = max(self.heal_amp_cast, self.heal_amp_regen)

        # burst heals from items, amortised over their own cooldown
        self.item_heal_ps = 0.0
        for it in self.items:
            cd = _pval(it, "AbilityCooldown")
            for k in self.BURST_HEAL:
                v = _pval(it, k)
                if v and cd > 0:
                    # stack-based heals heal value PER STACK (Restorative Locket)
                    stacks = _pval(it, "MaxStacks") if k == "HealPerStack" else 0.0
                    eff_cd = window_cd(cd * max(0.05, 1 - self.item_cdr / 100.0))
                    self.item_heal_ps += v * (stacks or 1.0) / eff_cd

        self.bullet_shred = self._pool_prop(self.BULLET_SHRED)
        self.spirit_shred = self._pool_prop(self.SPIRIT_SHRED)
        self.self_drain = self._sum_prop(("HealthDrainedPerSecond",))
        self.n_actives = sum(1 for i in self.items if i["is_active"])

    # ------------------------------------------------------------- weapon
    def _derive(self):
        w = self.hero["weapon"]
        pb = self.hero["per_boon"]

        base_bullet = (w.get("bullet_damage") or 0) + self.boons * (pb["bullet_damage"] or 0)
        self.base_bullet_damage = base_bullet
        self.pellets = w.get("bullets") or 1
        self.bullet_damage = base_bullet * (1 + self.weapon_pct / 100.0)

        # Lucky Shot style procs: chance x bonus = average multiplier
        # (deadlock.wiki/Lucky_Shot: "functions as a 1.25x multiplier").
        crit_mult = 1.0
        for it in self.items:
            pc, cdmg = _pval(it, "ProcChance"), _pval(it, "CritDamagePercent")
            if pc > 0 and cdmg > 0:
                crit_mult += (pc / 100.0) * (cdmg / 100.0)
        self.bullet_damage *= crit_mult

        cycle = effective_cycle(self.hero_name) / (1 + self.firerate_pct / 100.0)
        clip = (w.get("clip_size") or 1) * (1 + self.clip_pct / 100.0) + self.clip_flat
        reload_t = w.get("reload_duration") or 0
        # Active Reload: hitting the timing window finishes the reload early.
        # Assume a ~45% skip on the 7s-per-12s windows it is available.
        if "Active Reload" in self._names:
            reload_t *= (1.0 - 0.45 * (7.0 / 12.0))
        bullets = w.get("bullets") or 1

        self.clip_size = clip
        self.cycle_time = cycle
        self.reload_time = reload_t

        mag_damage = clip * bullets * self.bullet_damage
        mag_time = clip * cycle + reload_t + RELOAD_OVERHEAD
        self.weapon_dps = mag_damage / mag_time if mag_time > 0 else 0.0
        self.weapon_dps_noreload = (bullets * self.bullet_damage / cycle) if cycle else 0.0
        # shots per second including reload time (for per-shot proc items)
        self.shots_per_second = clip / mag_time if mag_time > 0 else 0.0

        self.headshot_mult = w.get("crit_bonus_start") or 1.0

    def falloff_at(self, distance_m=None):
        """Linear weapon falloff at a real-world distance in metres."""
        if distance_m is None:
            distance_m = self.engagement_range
        cached = self._falloff_cache.get(distance_m)
        if cached is None:
            cached = self._falloff_cache[distance_m] = self._falloff(distance_m)
        return cached

    def _falloff(self, distance_m):
        w = self.hero["weapon"]
        units_per_metre = 39.37
        range_scale = 1 + self._sum_prop(("BonusAttackRangePercent",)) / 100.0
        start = (w.get("damage_falloff_start_range") or 0) / units_per_metre * range_scale
        end = (w.get("damage_falloff_end_range") or 0) / units_per_metre * range_scale
        end_scale = w.get("damage_falloff_end_scale")
        end_scale = 1.0 if end_scale is None else end_scale
        if distance_m <= start or end <= start:
            return 1.0
        if distance_m >= end:
            return end_scale
        return 1 + (end_scale - 1) * ((distance_m - start) / (end - start))

    def _gun_at(self, distance_m):
        """Raw weapon DPS at a distance: range-conditional power x falloff."""
        cached = self._gun_cache.get(distance_m)
        if cached is not None:
            return cached
        conditional = 0.0
        for it in self.items:
            close = _pval(it, "CloseRangeBonusDamageRange")
            far = _pval(it, "LongRangeBonusWeaponPowerMinRange")
            if close and distance_m <= close:
                conditional += self._prop_value(it, "CloseRangeBonusWeaponPower")
            if far and distance_m >= far:
                conditional += self._prop_value(it, "LongRangeBonusWeaponPower")
        scale = ((1 + (self.weapon_pct + conditional) / 100.0)
                 / max(0.05, 1 + self.weapon_pct / 100.0))
        value = self.weapon_dps * scale * self.falloff_at(distance_m)
        self._gun_cache[distance_m] = value
        return value

    def weapon_dps_vs(self, target_bullet_resist=0.0, headshot_rate=0.0,
                      distance_m=None):
        """Weapon DPS against a target, applying range, shred, then resist."""
        if distance_m is None:
            distance_m = self.engagement_range
        eff_resist = max(-100.0, target_bullet_resist - self.bullet_shred)
        hs = 1 + headshot_rate * (self.headshot_mult - 1)
        return self._gun_at(distance_m) * hs * (1 - eff_resist / 100.0)

    # ------------------------------------------------------- item effects
    def _item_effects(self):
        """Item procs, enemy debuffs and self penalties the stat buckets miss.

        Every value is read from the item's shipped properties; the formulas
        follow the item descriptions and the deadlock.wiki pages. Melee-only
        procs (Spirit Snatch, Crushing Fists, ...) are not modelled because the
        model has no melee routing.
        """
        sp = self.spirit_power
        cdr_mult = max(0.05, 1 - self.item_cdr / 100.0)
        shots = self.shots_per_second

        def item_cd(it, key="AbilityCooldown", scaled=True):
            return window_cd(_pval(it, key) * (cdr_mult if scaled else 1.0))
        # each proc: (kind, dps, pct_target_hp_per_s, radius_m, needs_ability, aoe)
        procs = []

        def add(kind, dps=0.0, pct=0.0, radius=None, needs_ability=False, aoe=False):
            if dps > 0 or pct > 0:
                procs.append((kind, dps, pct, radius, needs_ability, aoe))

        n = self._names
        I = {name: ITEMS[name] for name in n}
        if "Mystic Burst" in n:
            it = I["Mystic Burst"]
            add("spirit", _pval(it, "Damage") / (item_cd(it, scaled=False) or 14),
                needs_ability=True)
        for name in ("Quicksilver Reload", "Mercurial Magnum"):
            if name in n:
                it = I[name]
                cd = window_cd(_pval(it, "AbilityChargeUpTime") or _pval(it, "AbilityCooldown"))
                dmg = _pval(it, "Damage") + sp * _pscale(it, "Damage")
                # Mercurial Magnum: bonus spirit damage on every bullet after
                # the imbued cast (which reloads) until the next reload or 12s.
                # The shipped field is "+20% Base Bullet Damage" (+0.38%/SP):
                # a percentage of the hero's base bullet damage, NOT flat
                # damage -- read flat it gave Bebop's 5-damage bullets 80 each.
                pct = _pval(it, "BulletsBonusMagicDamage") + sp * _pscale(it, "BulletsBonusMagicDamage")
                per_bullet = pct / 100.0 * self.base_bullet_damage * self.pellets
                window = _pval(it, "BuffDuration") or cd
                bullets = min(self.clip_size, window / self.cycle_time) if self.cycle_time else 0.0
                add("spirit", (dmg + per_bullet * bullets) / cd, needs_ability=True)
        if "Tankbuster" in n:
            it = I["Tankbuster"]
            cd = window_cd(_pval(it, "AbilityChargeUpTime") or 14)
            add("spirit", _pval(it, "Damage") / cd,
                pct=_pval(it, "CurrentHealthDamage") * AVG_CURRENT_HP / cd,
                needs_ability=True)
        if "Torment Pulse" in n:
            it = I["Torment Pulse"]
            add("spirit", (_pval(it, "DamagePulseAmount") + sp * _pscale(it, "DamagePulseAmount"))
                / _pval(it, "AbilityCooldown"), radius=_pval(it, "DamagePulseRadius"), aoe=True)
        if "Scourge" in n:
            it = I["Scourge"]
            pct = _pval(it, "MaxHealthPercentAsDPS") + sp * _pscale(it, "MaxHealthPercentAsDPS")
            up = _pval(it, "AbilityDuration") / item_cd(it)
            add("spirit", pct=pct * min(1.0, up), radius=_pval(it, "AuraRadius"), aoe=True)
        for name in ("Arctic Blast", "Cold Front", "Silence Wave", "Phantom Strike"):
            if name in n:
                it = I[name]
                key = "ImpactDamage" if name == "Phantom Strike" else "Damage"
                dmg = _pval(it, key) + sp * _pscale(it, key)
                add("spirit", dmg / item_cd(it), aoe=name != "Phantom Strike")
        if "Alchemical Fire" in n:
            it = I["Alchemical Fire"]
            lo = _pval(it, "DPS") + sp * _pscale(it, "DPS")
            hi = _pval(it, "DPSMax") + sp * _pscale(it, "DPSMax")
            dur = _pval(it, "AbilityDuration")
            add("spirit", (lo + hi) / 2 * dur / item_cd(it), aoe=True)
        if "Spirit Burn" in n:
            it = I["Spirit Burn"]
            burn = _pval(it, "DPS") + sp * _pscale(it, "DPS")
            per = _pval(it, "ExplosionDamage") + burn * _pval(it, "DebuffDuration")
            add("spirit", per / window_cd(_pval(it, "ImmunityDuration")), needs_ability=True)
        if "Stalker" in n:
            it = I["Stalker"]
            add("spirit", _pval(it, "DPS") * min(1.0, _pval(it, "AbilityDuration") / _pval(it, "AbilityCooldown")),
                radius=_pval(it, "ProcRadius"))
        if "Mystic Shot" in n:
            it = I["Mystic Shot"]
            add("spirit", (_pval(it, "ProcBonusMagicDamage") + sp * _pscale(it, "ProcBonusMagicDamage"))
                / _pval(it, "AbilityCooldown"))
        for name in ("Tesla Bullets", "Capacitor"):
            if name in n:
                it = I[name]
                rate = min(shots * _pval(it, "ProcChance") / 100.0,
                           1.0 / max(0.05, _pval(it, "ProcCooldown")))
                add("spirit", rate * (_pval(it, "DamagePerChain") + sp * _pscale(it, "DamagePerChain")),
                    aoe=True)
        if "Capacitor" in n:
            it = I["Capacitor"]
            add("spirit", _pval(it, "Damage") / item_cd(it))
        if "Toxic Bullets" in n:
            it = I["Toxic Bullets"]
            # bleed of (1.9 + 0.006*SP)% max HP per second while re-applied;
            # needs a few shots of build-up, so 85% uptime while shooting.
            pct = _pval(it, "DotHealthPercent") + sp * _pscale(it, "DotHealthPercent")
            add("spirit", pct=pct * 0.85)
        for name in ("Headshot Booster", "Headhunter"):
            if name in n:
                it = I[name]
                # Headhunter's bonus also scales +4 per boon (ELevelUpBoons)
                bonus = _pval(it, "HeadShotBonusDamage") + self.boons * _pscale(it, "HeadShotBonusDamage")
                add("weapon", bonus / _pval(it, "AbilityCooldown"))
        self.procs = procs

        # Headhunter heals a share of max health on each proc.
        if "Headhunter" in n:
            it = I["Headhunter"]
            self.item_heal_ps += (_pval(it, "HealPercentPerHeadshot") / 100.0 * self.health
                                  / item_cd(it, scaled=False))

        # --- your own outgoing damage penalties (uptime weighted)
        own_penalties = []
        for name in SELF_DAMAGE_PENALTY:
            if name in n:
                it = I[name]
                sec = (it.get("sections") or {}).get("OutgoingDamagePenaltyPercent")
                up = 1.0 if sec == "innate" else self.item_uptime(it, self.item_cdr)
                own_penalties.append(abs(_pval(it, "OutgoingDamagePenaltyPercent")) * up)
        self.own_damage_mult = 1 - pooled(own_penalties) / 100.0 if own_penalties else 1.0

        # --- enemy debuffs: (damage penalty %, fire-rate slow %) per group
        self.has_ricochet = "Ricochet" in n
        self.ricochet_pct = _pval(I["Ricochet"], "RicochetDamagePercent") if self.has_ricochet else 0.0
        self.inhibitor = abs(_pval(I["Inhibitor"], "OutgoingDamagePenaltyPercent")) if "Inhibitor" in n else 0.0
        self.disarm_uptime = 0.0
        if "Cursed Relic" in n:
            it = I["Cursed Relic"]
            self.disarm_uptime = min(1.0, _pval(it, "AbilityDuration") / item_cd(it))
        self.primary_slow = []
        if "Rusted Barrel" in n:
            it = I["Rusted Barrel"]
            self.primary_slow.append(_pval(it, "FireRateSlow") * self.item_uptime(it, self.item_cdr))
        self.suppressor = _pval(I["Suppressor"], "FireRateSlow") if "Suppressor" in n else 0.0
        self.juggernaut = _pval(I["Juggernaut"], "FireRateSlow") if "Juggernaut" in n else 0.0
        if "Hunter's Aura" in n:
            it = I["Hunter's Aura"]
            self.hunter = (_pval(it, "Radius"), abs(_pval(it, "BulletArmorReduction")),
                           _pval(it, "FireRateSlow"), _pval(it, "SingleTargetPlayerMultiplier") or 2.0)
        else:
            self.hunter = None
        if "Stalker" in n:
            it = I["Stalker"]
            self.stalker = (_pval(it, "ProcRadius"),
                            abs(_pval(it, "BulletResistReduction")) * self.item_uptime(it))
        else:
            self.stalker = None

        # Siphon Bullets (deadlock.wiki): steals 2.5% of the target's current
        # max HP per proc (1.2s), as damage and as healing that ignores
        # healing reduction; decays as the target's max HP shrinks.
        self.health_steal_pct = 0.0
        self.health_steal_cooldown = 1.2
        for it in self.items:
            pct = _pval(it, "HealthStealPctHero")
            if pct > 0:
                self.health_steal_pct += pct
                self.health_steal_cooldown = _pval(it, "ProcCooldown") or 1.2

    def _gated_bullet_shred(self, distance_m, single_enemy):
        out = []
        if self.stalker and distance_m <= self.stalker[0]:
            out.append(self.stalker[1])
        if self.hunter and distance_m <= self.hunter[0]:
            out.append(self.hunter[1] * (self.hunter[3] if single_enemy else 1.0))
        return out

    # ----------------------------------------------------------- abilities
    def resolved_ability_properties(self, ability, level=0):
        index = self.hero["abilities"].index(ability)
        return resolve_ability(self.hero_name, index, level)

    def ability_damage(self, ability, prop_key, level=0):
        """Resolve one ability damage property at current Spirit Power."""
        p = self.resolved_ability_properties(ability, level).get(prop_key)
        if not p:
            return None
        return (p.get("value") or 0.0) + self.spirit_power * (p.get("spirit_scale") or 0.0)

    def ability_burst(self, levels=None):
        """Sum of the largest single damage instance from each ability."""
        total = 0.0
        parts = []
        levels = self.ability_levels if levels is None else levels
        for idx, a in enumerate(self.hero["abilities"]):
            inst = self._instances(idx, levels[idx])
            if not inst:
                continue
            key, dmg, _, _ = max(inst, key=lambda z: z[1])
            total += dmg
            parts.append((a.get("name"), key, round(dmg, 1)))
        return total, parts

    def _instances(self, idx, level):
        """Damage per CAST for each damage property on ability ``idx``."""
        d = ability_digest(self.hero_name, idx, level)
        stat = self.scale_stats
        out = []
        for key, base, coef, kind, scale_by in d["damage"]:
            val = base + stat[scale_by] * coef
            if val <= 0:
                continue
            if kind == "rate":
                out.append((key, val * d["dur"] if d["dur"] > 0 else val, "rate", d["dur"]))
            elif kind == "tick":
                out.append((key, val * d["ticks"], "tick", d["dur"]))
            else:
                out.append((key, val, "instant", 0.0))
        return out

    def ability_instances(self, ability, level=0):
        return self._instances(self.hero["abilities"].index(ability), level)

    def _ability_dps_split(self, levels):
        """(single-target DPS, AoE DPS, %current-HP per second) from abilities.

        Takes the single largest damage component per ability (conservative).
        Resource-gated abilities (AbilityChargesConditionally) are skipped:
        their nominal cooldown is not a cast rate.
        """
        single = aoe = pct = 0.0
        cdr_mult = 1 - self.cdr / 100.0
        sp = self.spirit_power
        for idx in range(len(self.hero["abilities"])):
            d = ability_digest(self.hero_name, idx, levels[idx])
            if d["conditional"] or not d["cd"]:
                continue
            eff_cd = window_cd(d["cd"] * cdr_mult)
            if eff_cd <= 0:
                continue
            best = 0.0
            for key, dmg, kind, dur in self._instances(idx, levels[idx]):
                contrib = dmg / max(eff_cd, dur) if kind in ("rate", "tick") and dur > 0 else dmg / eff_cd
                if contrib > best:
                    best = contrib
            if d["aoe"]:
                aoe += best
            else:
                single += best
            # Bleeds of X% CURRENT health per second (Stalker's Mark,
            # Vindicta's Crow Familiar; deadlock.wiki/Drifter).
            if d["dot"] and d["dur"] > 0:
                rate = d["dot"][0] + sp * d["dot"][1]
                pct += rate * AVG_CURRENT_HP * min(d["dur"], eff_cd) / eff_cd
        return single, aoe, pct

    def ability_sustained_dps(self, levels=None):
        levels = self.ability_levels if levels is None else levels
        single, aoe, _ = self._ability_dps_split(levels)
        return single + aoe

    def ability_healing(self, levels=None):
        """Healing per second from abilities, each property amortised over its
        OWN ability's cooldown (css_class 'healing'). Field rules live in
        ability_digest()."""
        total = 0.0
        parts = []
        levels = self.ability_levels if levels is None else levels
        cdr_mult = 1 - self.cdr / 100.0
        sp = self.spirit_power
        for idx, a in enumerate(self.hero["abilities"]):
            d = ability_digest(self.hero_name, idx, levels[idx])
            if d["conditional"] or not d["heals"]:
                continue
            eff_cd = window_cd(d["cd"] * cdr_mult) if d["cd"] else 0.0
            if eff_cd <= 0:
                continue
            for key, base, coef, mode in d["heals"]:
                scaled = base + sp * coef
                if mode == "maxhealth":
                    amount = scaled / 100.0 * self.health / eff_cd
                elif mode == "rate":
                    if d["dur"] <= 0:
                        continue
                    amount = scaled * min(d["dur"], eff_cd) / eff_cd
                else:  # flat per cast, including TotalHealthRegen totals
                    amount = scaled / eff_cd
                if amount > 0:
                    total += amount
                    parts.append((a.get("name"), key, round(amount, 2)))
        return total, parts

    # ------------------------------------------------------- survivability
    BARRIER_KEYS = ("CombatBarrier", "GuardianWardCombatBarrier", "VexBarrierCombatBarrier")

    def barrier_pool(self, levels=None):
        """Barrier HP gained per engagement from items and abilities.

        A barrier on a cooldown longer than the fight window is gained once
        per fight; shorter cooldowns recast (capped at 3 per fight). Barriers
        are absorbed quickly under focus fire, so their lifetime does not
        discount them.
        """
        total = 0.0
        for it in self.items:
            for key in self.BARRIER_KEYS:
                v = _pval(it, key)
                if not v:
                    continue
                cd = _pval(it, "AbilityCooldown") * max(0.05, 1 - self.item_cdr / 100.0)
                total += v * (min(3.0, FIGHT_WINDOW / cd) if 0 < cd < FIGHT_WINDOW else 1.0)
        levels = self.ability_levels if levels is None else levels
        for idx in range(len(self.hero["abilities"])):
            b = ability_digest(self.hero_name, idx, levels[idx])["barrier"]
            if not b:
                continue
            base, coef, cd, life = b
            val = base + self.spirit_power * coef
            eff_cd = cd * (1 - self.cdr / 100.0)
            if 0 < eff_cd < FIGHT_WINDOW:
                val *= min(3.0, FIGHT_WINDOW / eff_cd)
            total += val
        return total

    def ability_lifesteal_total(self, levels=None):
        """Spirit lifesteal from items PLUS lifesteal baked into abilities."""
        levels = self.ability_levels if levels is None else levels
        values = [self.spirit_lifesteal] if self.spirit_lifesteal else []
        for idx in range(len(self.hero["abilities"])):
            v = ability_digest(self.hero_name, idx, levels[idx])["lifesteal"]
            if v:
                values.append(v)
        return pooled(values) if values else 0.0

    def ability_bonus_health(self, levels=None):
        """Uptime-weighted max-health bonuses granted by abilities."""
        levels = self.ability_levels if levels is None else levels
        total = 0.0
        for idx in range(len(self.hero["abilities"])):
            d = ability_digest(self.hero_name, idx, levels[idx])
            bonus = d["bonus_health"]
            if not bonus:
                continue
            if d["cd"] > 0:
                bonus *= (min(1.0, d["dur"] / max(0.05, window_cd(d["cd"] * (1 - self.cdr / 100.0))))
                          if d["dur"] > 0 else 0.0)
            total += bonus
        return total

    def total_resists(self, levels=None):
        """Item/boon resistance pooled with uptime-weighted ability buffs."""
        levels = self.ability_levels if levels is None else levels
        bullet = [self.bullet_resist] if self.bullet_resist else []
        spirit = [self.tech_resist] if self.tech_resist else []
        for idx in range(len(self.hero["abilities"])):
            r = ability_digest(self.hero_name, idx, levels[idx])["resist"]
            if not r:
                continue
            cd, duration, b, t = r
            if cd > 0:
                if duration <= 0:
                    continue
                uptime = min(1.0, duration / max(0.05, window_cd(cd * (1 - self.cdr / 100.0))))
            else:
                uptime = 1.0
            if b > 0:
                bullet.append(b * uptime)
            if t > 0:
                spirit.append(t * uptime)
        return (pooled(bullet) if bullet else 0.0,
                pooled(spirit) if spirit else 0.0)

    def total_shreds(self, levels=None):
        """Item shred pooled with ability debuffs of known uptime."""
        levels = self.ability_levels if levels is None else levels
        bullet = [self.bullet_shred] if self.bullet_shred else []
        spirit = [self.spirit_shred] if self.spirit_shred else []
        for idx in range(len(self.hero["abilities"])):
            s = ability_digest(self.hero_name, idx, levels[idx])["shred"]
            if not s:
                continue
            cd, b, s_, b_dur, s_dur = s
            if cd > 0:
                eff_cd = max(0.05, window_cd(cd * (1 - self.cdr / 100.0)))
                if b and b_dur > 0:
                    bullet.append(b * min(1.0, b_dur / eff_cd))
                if s_ and s_dur > 0:
                    spirit.append(s_ * min(1.0, s_dur / eff_cd))
            else:
                if b:
                    bullet.append(b)
                if s_:
                    spirit.append(s_)
        return (pooled(bullet) if bullet else 0.0,
                pooled(spirit) if spirit else 0.0)

    def _isolation(self, levels):
        """(isolated damage amp %, ult uptime that forces isolation)."""
        amp = ult = 0.0
        for idx in range(len(self.hero["abilities"])):
            d = ability_digest(self.hero_name, idx, levels[idx])
            amp += d["iso_amp"]
            if d["isolating_ult"] and d["cd"] > 0 and d["dur"] > 0:
                ult = min(1.0, d["dur"] / window_cd(d["cd"] * (1 - self.cdr / 100.0)))
        return amp, ult

    def _level_stats(self, levels):
        """Everything that depends on the ability allocation, computed once."""
        levels = tuple(levels)
        cached = self._level_cache.get(levels)
        if cached is not None:
            return cached
        single, aoe, dot_pct = self._ability_dps_split(levels)
        cast_heal, _ = self.ability_healing(levels)
        br, sr = self.total_resists(levels)
        bshred, sshred = self.total_shreds(levels)
        iso_amp, ult_iso = self._isolation(levels)
        stats = {
            "abil_single": single, "abil_aoe": aoe, "dot_pct": dot_pct,
            "cast_heal": cast_heal,
            "abil_lifesteal": self.ability_lifesteal_total(levels),
            "bullet_resist": br, "spirit_resist": sr,
            "bullet_shred": bshred, "spirit_shred": sshred,
            "pool": self.health + self.ability_bonus_health(levels) + self.barrier_pool(levels),
            "iso_amp": iso_amp, "ult_iso": ult_iso,
        }
        self._level_cache[levels] = stats
        return stats

    def ehp(self, incoming_bullet_frac=0.6, levels=None):
        """Effective HP against a mixed damage profile, including barriers."""
        levels = self.ability_levels if levels is None else levels
        L = self._level_stats(levels)
        mixed = (incoming_bullet_frac * max(0.05, 1 - L["bullet_resist"] / 100.0)
                 + (1 - incoming_bullet_frac) * max(0.05, 1 - L["spirit_resist"] / 100.0))
        return L["pool"] / mixed

    def ability_dps_vs(self, target_tech_resist=0.0, levels=None):
        eff = max(-100.0, target_tech_resist - self.spirit_shred)
        return self.ability_sustained_dps(levels) * (1 - eff / 100.0)

    def healing_per_second(self, gun_dps=None, abil_dps=None,
                           amp_on_lifesteal=None, levels=None):
        """Sustain throughput: lifesteal on damage dealt + regen + cast heals."""
        if amp_on_lifesteal is None:
            amp_on_lifesteal = self.AMP_ON_LIFESTEAL
        gun = self.weapon_dps if gun_dps is None else gun_dps
        levels = self.ability_levels if levels is None else levels
        L = self._level_stats(levels)
        abil = L["abil_single"] + L["abil_aoe"] if abil_dps is None else abil_dps
        ls_heal = gun * self.bullet_lifesteal / 100.0 + abil * L["abil_lifesteal"] / 100.0
        heal = self.hp_regen * (1 + self.heal_amp_regen / 100.0)
        heal += (self.item_heal_ps + L["cast_heal"]) * (1 + self.heal_amp_cast / 100.0)
        heal += ls_heal * (1 + self.heal_amp / 100.0) if amp_on_lifesteal else ls_heal
        return max(0.0, heal)

    # -------------------------------------------------------------- combat
    def _enemy_damage_mult(self, sc, L, bounces, spirit_active):
        """Multiplier on incoming damage from debuffs you place on enemies.

        Attackers are split into your primary target, the ones your Ricochet
        bounces reach, and the rest. Inhibitor/Cursed Relic/Rusted Barrel/
        Suppressor only reach who you hit; Juggernaut slows everyone who shoots
        you; Hunter's Aura reaches enemies inside its radius and is doubled
        when a single enemy is nearby.
        """
        focus = sc.focus
        bf = sc.bullet_frac
        aura = 0.0
        if self.hunter:
            radius, _, slow, mult = self.hunter
            share = sum(w for d, w in sc.distances if d <= radius)
            aura = slow * share * (mult if focus <= 1.0 else 1.0)
        common_slow = [s for s in (aura, self.juggernaut) if s]

        def group(dmg_pen, slows):
            fr = pooled(slows) / 100.0 if slows else 0.0
            return ((1 - pooled(dmg_pen) / 100.0 if dmg_pen else 1.0)
                    * (bf * (1 - fr * (1 - RELOAD_SHARE)) + (1 - bf)))

        primary_pen = [p for p in (self.inhibitor, 100.0 * self.disarm_uptime) if p]
        primary_slow = common_slow + self.primary_slow
        if self.suppressor and spirit_active:
            primary_slow.append(self.suppressor * CONDITIONAL_UPTIME)
        m_primary = group(primary_pen, primary_slow)
        others = max(0.0, focus - 1.0)
        nb = min(bounces, others)
        m_bounce = group([self.inhibitor] if self.inhibitor else [], common_slow)
        m_rest = group([], common_slow)
        return (m_primary + nb * m_bounce + (others - nb) * m_rest) / focus

    def scenario_result(self, ref, sc, levels):
        """Resolve one scenario for one ability allocation."""
        L = self._level_stats(levels)
        target_hp = ref.get("health", ref.get("ehp", 0.0))
        focus = sc.focus
        single_enemy = focus <= 1.0

        iso = sc.isolation + (1 - sc.isolation) * L["ult_iso"]
        amp = (1 + L["iso_amp"] / 100.0 * iso) * self.own_damage_mult

        # --- weapon, averaged over the engagement-distance spread
        hs = 1 + sc.headshot * (self.headshot_mult - 1)
        gun = gun_body = raw_gun = falloff = 0.0
        for d, w in sc.distances:
            raw = self._gun_at(d)
            gated = self._gated_bullet_shred(d, single_enemy)
            shred = pooled([L["bullet_shred"]] + gated) if gated else L["bullet_shred"]
            mult = 1 - max(-100.0, ref["bullet_resist"] - shred) / 100.0
            raw_gun += w * raw * hs
            gun += w * raw * hs * mult
            gun_body += w * raw * mult
            falloff += w * self.falloff_at(d)
        gun *= amp
        gun_body *= amp

        spirit_mult = (1 - max(-100.0, ref["tech_resist"] - L["spirit_shred"]) / 100.0) * amp
        bullet_mult = (1 - max(-100.0, ref["bullet_resist"] - L["bullet_shred"]) / 100.0) * amp
        raw_abil = L["abil_single"] + L["abil_aoe"]
        abil = raw_abil * spirit_mult
        abil_aoe = L["abil_aoe"] * spirit_mult
        dot = L["dot_pct"] / 100.0 * target_hp * spirit_mult

        # --- item procs
        has_ability_damage = raw_abil > 0 or L["dot_pct"] > 0
        proc_spirit = proc_weapon = proc_aoe = raw_procs = 0.0
        for kind, dps, pct, radius, needs_ability, aoe in self.procs:
            if needs_ability and not has_ability_damage:
                continue
            share = sum(w for d, w in sc.distances if d <= radius) if radius else 1.0
            value = (dps + pct / 100.0 * target_hp) * share
            if kind == "weapon":
                if sc.headshot <= 0:
                    continue
                raw_procs += value
                proc_weapon += value * bullet_mult
            else:
                raw_procs += value
                value *= spirit_mult
                proc_spirit += value
                if aoe:
                    proc_aoe += value

        base_dps = gun + proc_weapon + abil + dot + proc_spirit

        # --- Siphon Bullets: decaying max-HP steal, unaffected by anti-heal
        siphon = 0.0
        if self.health_steal_pct > 0 and target_hp > 0 and base_dps > 0:
            p = self.health_steal_pct / 100.0
            procs = max(1.0, (target_hp / base_dps) / self.health_steal_cooldown)
            decay = (1 - (1 - p) ** procs) / (procs * p)
            siphon = target_hp * p / self.health_steal_cooldown * decay
        siphon_dps = siphon * amp

        dps = base_dps + siphon_dps

        # --- damage splashed onto other enemies
        others = max(0.0, focus - 1.0)
        bounces = min(2.0, others) if self.has_ricochet else 0.0
        ricochet_extra = gun_body * self.ricochet_pct / 100.0 * bounces
        aoe_extra = (abil_aoe + proc_aoe) * min(2.0, 0.5 * others)
        cleave = ricochet_extra + aoe_extra
        score_dps = dps + CLEAVE_VALUE * cleave
        ttk = target_hp / score_dps if score_dps > 0 else float("inf")

        # --- sustain
        ls = ((gun + proc_weapon + ricochet_extra) * self.bullet_lifesteal / 100.0
              + (abil + dot + proc_spirit + aoe_extra) * L["abil_lifesteal"] / 100.0)
        gross = (self.hp_regen * (1 + self.heal_amp_regen / 100.0)
                 + (self.item_heal_ps + L["cast_heal"]) * (1 + self.heal_amp_cast / 100.0)
                 + ls)
        self_drain = self.self_drain
        heal = gross * (1 - sc.antiheal / 100.0) + siphon - self_drain

        # --- incoming
        enemy_mult = self._enemy_damage_mult(sc, L, bounces, has_ability_damage)
        incoming = ref["dps"] * focus * enemy_mult
        # the reference opponent's own resist shred applies to you, exactly
        # as your shred applies to it
        my_br = max(-100.0, L["bullet_resist"] - ref.get("bullet_shred", 0.0))
        my_sr = max(-100.0, L["spirit_resist"] - ref.get("spirit_shred", 0.0))
        mixed = (sc.bullet_frac * max(0.05, 1 - my_br / 100.0)
                 + (1 - sc.bullet_frac) * max(0.05, 1 - my_sr / 100.0))
        effective_incoming = incoming * mixed
        net_in = max(effective_incoming * NET_INCOMING_FLOOR, effective_incoming - heal)
        ttd = L["pool"] / net_in if net_in > 0 else float("inf")
        score = ttd / ttk if 0 < ttk < float("inf") else 0.0
        return {
            "gun_dps": gun + proc_weapon, "ability_dps": abil + dot,
            "item_proc_dps": proc_spirit, "siphon_dps": siphon_dps,
            "total_dps": dps, "cleave_dps": cleave, "score_dps": score_dps,
            "raw_gun_dps": raw_gun, "raw_ability_dps": raw_abil,
            # everything you deal before the target's resists (reference DPS)
            "raw_total_dps": (raw_gun + raw_abil + L["dot_pct"] / 100.0 * target_hp
                              + raw_procs) * amp + siphon_dps,
            "heal_ps": heal, "gross_heal_ps": gross + siphon,
            "siphon_heal_ps": siphon, "self_drain_ps": self_drain,
            "raw_incoming": ref["dps"] * focus, "enemy_damage_mult": enemy_mult,
            "effective_incoming": effective_incoming, "net_incoming": net_in,
            "ttk": ttk, "ttd": ttd, "score": score,
            "sustain_ratio": heal / effective_incoming if effective_incoming else 0.0,
            "unkillable": heal >= effective_incoming,
            "isolation": iso,
            "ability_levels": list(levels), "ability_points": self.ability_points,
            "falloff": falloff, "incoming_bullet_fraction": sc.bullet_frac,
        }

    def evaluate(self, ref, objective="allround"):
        """Weighted geometric mean over scenarios, best fixed ability allocation.

        Returns (score, levels, {scenario name: result}).
        """
        weights = OBJECTIVES[objective] if isinstance(objective, str) else objective
        best = None
        for levels in self.ability_level_options:
            results = {}
            log_score = 0.0
            for name, weight in weights.items():
                r = self.scenario_result(ref, SCENARIO_BY_NAME[name], levels)
                results[name] = r
                log_score += weight * math.log(max(r["score"], 1e-9))
            score = math.exp(log_score / sum(weights.values()))
            if best is None or score > best[0]:
                best = (score, tuple(levels), results)
        self.ability_levels = best[1]
        return best

    def duel(self, ref, headshot_rate=0.25, antiheal=None, focus=None,
             amp_on_lifesteal=None, distance_m=None,
             incoming_bullet_frac=0.6, levels=None, isolation=None):
        """One ad-hoc scenario at a single distance (best allocation unless
        ``levels`` is given). Kept for tools and tests."""
        antiheal = self.ANTIHEAL_ASSUMED if antiheal is None else antiheal
        focus = self.FOCUS_FIRE if focus is None else focus
        distance_m = self.engagement_range if distance_m is None else distance_m
        if isolation is None:
            isolation = 1.0 if focus <= 1.0 else 0.0
        sc = Scenario("adhoc", 1.0, focus, antiheal, incoming_bullet_frac,
                      ((distance_m, 1.0),), isolation, headshot_rate)
        options = [tuple(levels)] if levels is not None else self.ability_level_options
        best = None
        for lv in options:
            r = self.scenario_result(ref, sc, lv)
            if best is None or r["score"] > best["score"]:
                best = r
        self.ability_levels = tuple(best["ability_levels"])
        return best

    def summary(self):
        burst, _ = self.ability_burst(self.ability_levels)
        heal, _ = self.ability_healing(self.ability_levels)
        return {
            "hero": self.hero_name,
            "net_worth": self.net_worth,
            "spend": self.spend,
            "boons": self.boons,
            "spirit_power": round(self.spirit_power, 1),
            "weapon_pct": round(self.weapon_pct, 1),
            "bullet_damage": round(self.bullet_damage, 2),
            "weapon_dps": round(self.weapon_dps, 1),
            "health": round(self.health + self.ability_bonus_health()),
            "ehp": round(self.ehp()),
            "bullet_resist": round(self.bullet_resist, 1),
            "tech_resist": round(self.tech_resist, 1),
            "ability_burst": round(burst, 1),
            "ability_dps": round(self.ability_sustained_dps(), 1),
            "ability_heal": round(heal, 1),
            "ability_points": self.ability_points,
            "ability_levels": list(self.ability_levels),
            "actives": self.n_actives,
            "slots": len(self.items),
        }


def valid_build(items, budget=None, net_worth=None):
    """Shop legality: slots unlocked at this net worth (9-12), 4 actives,
    unique, within budget. Net worth defaults to the budget."""
    nw = net_worth if net_worth is not None else budget
    slots = slots_at(nw) if nw is not None else MAX_SLOTS
    if len(items) > slots or len(set(items)) != len(items):
        return False
    if sum(1 for n in items if ITEMS[n]["is_active"]) > MAX_ACTIVES:
        return False
    if budget is not None and sum(ITEMS[n]["cost"] for n in items) > budget:
        return False
    return True
