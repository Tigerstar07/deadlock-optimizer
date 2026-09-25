# Deadlock — Complete Hero Stat Reference

*Patch: Minor Update 09-16-2026 · extracted 2026-09-18*

*Source: assets.deadlock-api.com (parsed Valve game files)*

Every number below is read directly from the shipped game files, not from a wiki or a guide. Distances are converted from Source units at 39.37 units/metre (verified against the 09-16-2026 note "Lash: Gun falloff reduced from 18m->54m to 16m->48m").

**38 playable heroes.**


---

## Abrams

*internal id 6 / `hero_atlas` / complexity 1*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 800 | +49 | 1976 | 2515 |
| Health Regen | 1.50 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.40 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.72 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.51 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.74 | 110.83 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_bull_set`

| stat | value |
|---|---|
| Damage per bullet | 3.60 |
| Bullets per shot | 9 |
| Damage per shot | 32.40 |
| Ammo / clip size | 9 |
| Damage per magazine | 291.60 |
| Cycle time (nominal) | 0.6300 s |
| Cycle time (effective avg) | 0.6300 s |
| Shots / second | 1.587 |
| Shots / second (with reload) | 1.435 |
| Reload duration | 0.35 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 51.43 |
| **DPS (with reload)** | **46.49** |
| Bullet damage per boon | +0.100 |
| Headshot multiplier | x1.65 |
| Bullet speed | 24000 |
| Falloff: full damage to | 17.0 m |
| Falloff: decays to | 40 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.200 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Siphon Life

> Drain health from nearby enemies, dealing spirit damage over time and healing for a portion of the damage dealt.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 42 | - | - |
| AbilityDuration | 4 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 8 | - | - |
| HealingFactor | 70 | - | - |
| NonHeroHealingFactor | 35 | - | - |
| DPS | 22 | +0.6000 | 37.8 |
| TickRate | 0.250 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -20
- **T2** — `AbilityDuration` +2
- **T3** — `DPS` +0.120, `Radius` +2

#### Shoulder Charge

> Charge forward, pulling enemies you hit. Pushing a hero into a wall applies stun.If you collide with a hero you move faster during your charge.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 33 | - | - |
| AbilityDuration | 1.400 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 30 | +1.4000 | 67.0 |
| SpeedInitial | 18.750 | - | - |
| ChargeSpeedMax | 30 | - | - |
| ChargeDragVerticalOffset | 30 | - | - |
| TossUpMagnitude | 0.500 | - | - |
| SideMoveSpeedReduction | -65 | - | - |
| TurnRateMax | 140 | - | - |
| CameraTurnRateMax | 200 | - | - |
| ChargeRadius | 2.200 | - | - |
| CollidePlayersStopTime | 0.300 | - | - |
| StunDuration | 0.300 | - | - |

**Upgrades**

- **T1** — `SlowPercent` +32, `SlowDuration` +3
- **T2** — `StunDuration` +0.800
- **T3** — `AbilityCooldown` -18, `WeaponDamageBonus` +1.500, `WeaponPowerIncreaseDuration` +6

#### Infernal Resilience

> Gain bonus defensive attributes. Taking damage grants temporary regeneration for a portion of the damage taken.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| RegenIncomingDamagePercent | 13 | - | - |
| RegenIncomingDamageDuration | 20 | - | - |
| RegenDamageInterval | 1 | - | - |
| BonusHealthRegen | 1 | - | - |
| NonHeroHealPct | 40 | - | - |

**Upgrades**

- **T1** — `BonusMaxHealth` +200
- **T2** — `MeleeLifesteal` +18
- **T3** — `RegenIncomingDamagePercent` +9, `StatusResistancePercent` +20

#### Seismic Impact (ULTIMATE)

> Leap high into the air before crashing into the ground, dealing spirit damage and applying stun.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 215 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| ImpactRadius | 9 | - | - |
| ImpactHeight | 6 | - | - |
| Damage | 100 | +2.3250 | 161.4 |
| StunDuration | 1.600 | - | - |
| TossSpeed | 450 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -30
- **T2** — `StunDuration` +0.800
- **T3** — `ImmunityDuration` +5, `ImpactRadius` +6

---

## Apollo

*internal id 77 / `hero_fencer` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 770 | +45 | 1850 | 2345 |
| Health Regen | 1 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7.20 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 63 | +1.58 | 118.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_fencer_set`

| stat | value |
|---|---|
| Damage per bullet | 18.50 |
| Bullets per shot | 1 |
| Damage per shot | 18.50 |
| Ammo / clip size | 15 |
| Damage per magazine | 277.50 |
| Cycle time (nominal) | 0.3800 s |
| Cycle time (effective avg) | 0.3800 s |
| Shots / second | 2.632 |
| Shots / second (with reload) | 1.775 |
| Reload duration | 2.50 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 48.68 |
| **DPS (with reload)** | **32.84** |
| Bullet damage per boon | +0.825 |
| Headshot multiplier | x1.65 |
| Bullet speed | 5000 |
| Falloff: full damage to | 25.4 m |
| Falloff: decays to | 25.4 m |
| Falloff: damage retained | 100% |
| Max range | 25.4 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Disengaging Sigil

> Draw a sigil sphere in front of you and then leap backwards as it explodes, damaging and slowing enemies caught in it.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 12 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.500 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| SigilRadius | 6.500 | - | - |
| Damage | 85 | +1.3000 | 119.3 |
| JumpVelocityHidden | 16 | - | - |
| SlowDuration | 4 | - | - |
| SlowPercent | 24 | - | - |
| TraceToGroundDistance | 1000 | - | - |
| FallSpeedMax | 1 | - | - |
| AirSpeedMax | 70 | - | - |
| AirDrag | 2 | - | - |

**Upgrades**

- **T1** — `BonusFireRate` +25, `BonusBulletSpeedPercent` +25, `BuffDuration` +8
- **T2** — `StaminaToRestore` +1, `ResetsAirLimit` +1
- **T3** — `RecastTime` +4

#### Riposte

> Prepare to deflect the next incoming attack. On a successful deflection, briefly become invulnerable and target an enemy hero to dash towards them, stunning them and reducing their Melee Resist.Press Ability 2 to select a target.Does not trigger against trooper or neutral damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 22 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 0.800 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DashSpeed | 3000 | - | - |
| DashRange | 35 | - | - |
| SideMoveSpeed | -100 | - | - |
| TurnRateMax | 10 | - | - |
| DashRadius | 2.200 | - | - |
| CounterattackAntiMashDelay | 0.200 | - | - |
| ParryWindow | 0.300 | - | - |
| DamageThreshold | 60 | +4 | 165.6 |
| SlashConeAngle | 90 | - | - |
| SlashRadius | 6 | - | - |
| SlashHalfWidth | 1 | - | - |
| SlowDuration | 4 | - | - |
| SlowPercent | 40 | - | - |
| AbilityLifestealPercentHero | 50 | - | - |
| StunDuration | 0.800 | - | - |
| DampingFactor | 0.500 | - | - |
| LiftHeight | 240 | - | - |
| MoveSpeedMax | 4 | - | - |
| MeleeResistReduction | -25 | - | - |
| MeleeResistReductionDuration | 3 | - | - |
| DashGraceWindow | 1.300 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -8
- **T2** — `MeleeResistReduction` -25, `StunDuration` +0.400
- **T3** — `TargetLifesteal` +75, `TargetLifestealDuration` +13

#### Flawless Advance

> Perform a series of lunges in any direction, delivering piercing stabs ahead of you. Hold your ability key to time your attacks, dealing more damage the longer it's held. Releasing your attack during the perfect window deals maximum damage.Press Ability 3 to re-cast.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 26 | - | - |
| AbilityDuration | 8 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DashAngleThreshold | 89 | - | - |
| DashSpeed | 1100 | - | - |
| AttackingDashSpeed | 2200 | - | - |
| DashRange | 5 | - | - |
| AttackDashRange | 3 | - | - |
| DashRadius | 1.850 | - | - |
| HoldDurationMin | 0.250 | - | - |
| PerfectHoldTimeStart | 0.525 | - | - |
| PerfectWindowDuration | 0.250 | - | - |
| HoldDurationMax | 1.100 | - | - |
| BaseDamage | 25 | +0.5500 | 39.5 |
| MaxDamageBeforePerfect | 40 | +0.9000 | 63.8 |
| PerfectDamage | 65 | +1.5500 | 105.9 |
| PctTravelDistanceToDamageIn | 80 | - | - |
| MaxProcBleedDamagePercent | 50 | - | - |
| SlashRadius | 1.600 | - | - |
| SlashLength | 13 | - | - |
| SlashCollisionRadius | 4.050 | - | - |
| MaxStacks | 2 | - | - |
| MaxStabs | 3 | - | - |
| RecastTime | 5 | - | - |
| ParryCooldownReduction | 5 | - | - |

**Upgrades**

- **T1** — `HealFixedHealth` +1.300
- **T2** — `AbilityCooldown` -12, `BulletResist` +60, `DashBuffDuration` +1.500
- **T3** — `BaseDamage` +1.150, `MaxDamageBeforePerfect` +1.150, `PerfectDamage` +1.150, `AttackDashRange` +3, `DashSpeed` +550

#### Itani Lo Sahn (ULTIMATE)

> Charge up and perform a long range slash. Struck enemies cannot take action or heal and are stuck in slow motion. When this effect expires, they suffer devastating damage, dealing bonus damage against half-health enemies.While in slow motion, Apollo is invulnerable and enemies take reduced damage.Hold Ability 4 or to delay the cast.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 145 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 1.500 | - | - |
| AbilityChannelTime | 9999 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| TechCleaveExpireTime | 0.350 | - | - |
| DashAngleThreshold | 89 | - | - |
| DashSpeed | 10000 | - | - |
| DashRange | 27 | - | - |
| DashRadius | 7 | - | - |
| GapDistanceToWall | 180 | - | - |
| TravelDistPctBeforeWallGapCheck | 70 | - | - |
| DebuffDuration | 1.800 | - | - |
| CasterLockDuration | 1.800 | - | - |
| TimeScaleDebuff | 70 | - | - |
| VacuumSpeed | 400 | - | - |
| ImpactDamage | 70 | +0.7700 | 90.3 |
| DelayedDamage | 200 | +2.6000 | 268.6 |
| GroundDashReductionPercent | -26 | - | - |
| MoveSpeedPenaltyMaxSpeed | 200 | - | - |
| CameraDistance | 250 | - | - |
| SideMoveSpeedReduction | -100 | - | - |
| TurnRateMaxDuringCast | 999 | - | - |
| FallSpeedMax | 1 | - | - |
| AirSpeedMax | 70 | - | - |
| LowHealthEnemyThresholdPct | 50 | - | - |
| BonusDamagePercent | 60 | - | - |
| IncomingDamageReductionPercent | 70 | - | - |
| TimerSoundDuration | 1 | - | - |

**Upgrades**

- **T1** — `DashRange` +8
- **T2** — `AbilityCooldown` -35
- **T3** — `BonusDamagePercent` +50

---

## Bebop

*internal id 15 / `hero_bebop` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 880 | +52 | 2128 | 2700 |
| Health Regen | 2.50 | - | - | - |
| Bullet Resist | 0% | +0.30% | 7.20% | 10.50% |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.45 m/s |
| Sprint Speed (bonus) | 4 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.18/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.72 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.51 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 63 | +1.58 | 118.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_bebop_set`

| stat | value |
|---|---|
| Damage per bullet | 4.98 |
| Bullets per shot | 1 |
| Damage per shot | 4.98 |
| Ammo / clip size | 66 |
| Damage per magazine | 328.68 |
| Cycle time (nominal) | 0.0840 s |
| Cycle time (effective avg) | 0.0840 s |
| Shots / second | 11.905 |
| Shots / second (with reload) | 8.104 |
| Reload duration | 2.35 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 59.29 |
| **DPS (with reload)** | **40.36** |
| Bullet damage per boon | +0.115 |
| Headshot multiplier | x1.65 |
| Bullet speed | 20000 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 50.8 m |
| Falloff: damage retained | 10% |
| Max range | 32 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Exploding Uppercut

> Deal melee damage to nearby enemies and apply knockback. When they land, they deal spirit damage and apply reduced fire rate to other nearby enemies. Exploding Uppercut can be used on allies.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| MeleeHalfAngle | 60 | - | - |
| MeleeAttackLength | 6 | - | - |
| AbilityCooldown | 22 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| EnemyHeroTossVelocity | 20 | - | - |
| TossVelocity | 25 | - | - |
| MeleeRadius | 2.500 | - | - |
| ForceReductionOnAngleDown | 0.750 | - | - |
| UppercutDamage | 0.010 | +1 | 26.4 |
| LandingDamage | 75 | +0.6000 | 90.8 |
| OnLandDamageRadius | 14 | - | - |
| BuffGunRangePercent | 100 | - | - |
| BonusFireRate | -14 | +-0.1860 | -18.9 |
| ExplodeDebuffDuration | 5 | - | - |
| TossDuration | 0.500 | - | - |
| TossDurationFriendly | 0.300 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -11
- **T2** — `UppercutBuffOnHit` +9, `BuffBaseWeaponPct` +30
- **T3** — `RestoreHookCooldown` +1, `MissingHPHeal` +18

#### Sticky Bomb

> Attach a bomb that explodes after a delay, dealing spirit damage to nearby enemies. If the bomb hits or kills a hero, you gain permanent bonus damage on Sticky Bomb. Stacks diminish by half after 60 hits and 7 kills

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 18 | - | - |
| AbilityDuration | 3.500 | - | - |
| AbilityCastRange | 6 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 8 | - | - |
| FuseTime | 3.500 | - | - |
| KillCheckWindow | 10 | - | - |
| OnHitDiminish | 60 | - | - |
| OnKillDiminish | 7 | - | - |
| SelfDamagePercent | 20 | - | - |
| Damage | 85 | +1.5000 | 124.6 |
| BonusDamagePctPerPlayerKilled | 2.500 | +0.0100 | 2.8 |
| BonusDamagePctPerPlayerHit | 1 | +0.0015 | 1.0 |

**Upgrades**

- **T1** — `AbilityCooldown` -8
- **T2** — `Damage` +85
- **T3** — `MovementSpeedBonus` +5, `StatusResistancePercent` +25, `MovementSpeedBonusDuration` +6

#### Grapple Arm

> Launch out a mechanical hand that pulls the first character it hits, reeling them in. Grapple Arm can be used on allies.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 23 | - | - |
| AbilityCastRange | 30 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| HookingSlowSpeedLimit | 5 | - | - |
| SlowPercent | 72 | - | - |
| RestrictionDuration | 0.500 | - | - |
| FriendlyHookIgnoreRange | 8 | - | - |
| CancelHookDuration | 0.200 | - | - |
| HookImpactDelay | 0.500 | - | - |

**Upgrades**

- **T1** — `BulletAmp` +20, `BulletAmpDuration` +6
- **T2** — `AbilityCastRange` +30
- **T3** — `AbilityCooldown` -11.500

#### Hyper Beam (ULTIMATE)

> Channel a powerful torrent of energy that deals spirit damage and applies slow.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 120 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 1 | - | - |
| AbilityChannelTime | 11 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.800 | - | - |
| DPS | 160 | +2.5110 | 226.3 |
| BeamLength | 70 | - | - |
| BeamWidth | 2.900 | - | - |
| BeamCloseRadius | 5 | - | - |
| BeamEndRadius | 4 | - | - |
| BeamCloseDamagePercent | 75 | - | - |
| Interval | 0.100 | - | - |
| TrackingSpeed | 55 | - | - |
| ZoomTime | 0.100 | - | - |
| ZoomBias | 0.500 | - | - |
| FallSpeedMax | 1 | - | - |
| AirSpeedMax | 70 | - | - |
| SlowTargetDuration | 0.500 | - | - |
| SlowPercent | 20 | - | - |
| GroundDashReductionPercent | -36 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -20
- **T2** — `DPS` +108
- **T3** — `BeamLifesteal` +65, `BeamLifestealNonHeroPercent` +20

---

## Billy

*internal id 72 / `hero_punkgoat` / complexity 3*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 820 | +53 | 2092 | 2675 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_punkgoat_set`

| stat | value |
|---|---|
| Damage per bullet | 6.30 |
| Bullets per shot | 1 |
| Damage per shot | 6.30 |
| Ammo / clip size | 30 |
| Damage per magazine | 189 |
| Cycle time (nominal) | 0.0850 s |
| Cycle time (effective avg) | 0.0850 s |
| Shots / second | 11.765 |
| Shots / second (with reload) | 5.263 |
| Reload duration | 2.90 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 74.12 |
| **DPS (with reload)** | **33.16** |
| Bullet damage per boon | +0.127 |
| Headshot multiplier | x1.65 |
| Bullet speed | 20200 |
| Falloff: full damage to | 14.0 m |
| Falloff: decays to | 31.8 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.200 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Bashdown

> Slam your bat into the ground, pulling enemies down and dealing melee damage.The slam creates a shockwave that deals spirit damage and applies knockup.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 35 | - | - |
| AbilityCastRange | 4 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 0.300 | - | - |
| AbilityPostCastDuration | 0.300 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 8 | - | - |
| ChannelMoveSpeed | 190 | - | - |
| CameraTurnRateMax | 2000 | - | - |
| PlaceDistanceInFrontOfCaster | 6.200 | - | - |
| Damage | 35 | +1.1000 | 64.0 |
| TossForce | 350 | - | - |
| ExplodeDelay | 0.500 | - | - |
| CountsAsLightMelee | 1 | - | - |
| TossDuration | 0.400 | - | - |
| PullDownDuration | 0.750 | - | - |
| PullDownRange | 3 | - | - |
| WaveThickness | 1 | - | - |
| WaveStartRadius | 0.500 | - | - |
| WaveEndRadius | 8 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -10
- **T2** — `AbilityCastRange` +2, `AbilityCharges` +1
- **T3** — `CountsAsLightMelee` -1, `CountsAsHeavyMelee` +1, `HeavyMeleeDamage` +0, `MeleeDamage` +0, `AbilityCooldownBetweenCharge` -3

#### Rising Ram

> Charge head-first into an enemy and send them into the air along with Billy.Cooldown reduced by 50% on impact.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 32 | - | - |
| AbilityDuration | 0.300 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.350 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChargeRadius | 2.540 | - | - |
| ChargeMultiHitRadius | 1.500 | - | - |
| ChargeSpeed | 1200 | - | - |
| ChargeStrikeDistance | 165 | - | - |
| CameraTurnRateMax | 188 | - | - |
| GoingUpSpeed | 430 | - | - |
| GoingUpDistance | 3.100 | - | - |
| GoingUpEnemyDistancePercent | 95 | - | - |
| GoingBackAwaySpeed | -100 | - | - |
| KnockAwaySpeed | 170 | - | - |
| TimeBeforeGoUpForLagComp | 0.100 | - | - |
| TimeGoingUpEnemy | 0.200 | - | - |
| HoverGravityScale | 0.750 | - | - |
| AirControlDebuffDuration | 1.500 | - | - |
| AirControlDashReductionPct | -70 | - | - |
| AirControlAccelPercent | 50 | - | - |
| AirControlPercent | 50 | - | - |
| WorldImpactRadius | 25 | - | - |
| AllowRamMultiple | 1 | - | - |
| NearbyHeroKillDistance | 10 | - | - |
| ReduceCooldownOnHitPct | 50 | - | - |
| Damage | 40 | +1.9000 | 90.2 |

**Upgrades**

- **T1** — `WeaponDamageBurst` +25, `WeaponDamageBurstDuration` +5
- **T2** — `AbilityDuration` +0.400
- **T3** — `MaxHealthBuffPct` +10, `MaxHealthBuffDuration` +16, `AbilityCooldown` -13

#### Blasted

> Passive: Melee hits restore ammo and inflict wrecked on the victim for 7.0s.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 27 | - | - |
| AbilityDuration | 8 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.280 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DurationPerHeavyMelee | 4.500 | - | - |
| DurationPerLightMelee | 2.800 | - | - |
| NonPlayerResourceScalePct | 25 | - | - |
| LightMeleeScalePct | 40 | - | - |
| MaxDuration | 35 | - | - |
| BulletsReloadedPerLightMeleePct | 35 | - | - |
| BulletsReloadedPerHeavyMeleePct | 100 | - | - |
| BulletDamageAmp | 10 | - | - |
| BulletDamageAmpDuration | 7 | - | - |
| MaxHealthMelee | 70 | +0.6000 | 85.8 |
| HealthBoostDuration | 11 | - | - |
| BlastedRateOnBulletPct | 50 | - | - |

**Upgrades**

- **T1** — `BonusMoveSpeed` +2.250
- **T2** — `GainSlamOnUse` +1, `BulletDamageAmp` +7
- **T3** — `MaxHealthMelee` +0.600

#### Chain Gang (ULTIMATE)

> Chain nearby enemies to you. Chained enemies cannot use movement abilities and receive a heavy slow when they pull on the chain.After a delay, yank everyone towards Billy and deal spirit damage.The chain breaks if you lose line of sight for a short while.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 175 | - | - |
| AbilityDuration | 2.800 | - | - |
| AbilityCastRange | 12 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| RopeLength | 2 | - | - |
| RopeSnapNoLOSDuration | 0.500 | - | - |
| RopeSnapDistance | 45 | - | - |
| RopeSoftEdgeLength | 4.500 | - | - |
| MoveSpeedSlowMaxPct | 35 | - | - |
| MoveSpeedSlowMinPct | 25 | - | - |
| Damage | 120 | +0.7000 | 138.5 |
| DPS | 45 | +0.9000 | 68.8 |
| TickRate | 0.250 | - | - |
| PullForceMax | 2000 | - | - |
| PullDistance | 4 | - | - |
| PullDuration | 0.800 | - | - |
| PullTrackCasterDuration | 0.500 | - | - |

**Upgrades**

- **T1** — `BulletResist` +40, `TechResist` +40
- **T2** — `AbilityCooldown` -40
- **T3** — `UnstoppablePerHero` +1.300, `AbilityCastRange` +5

---

## Calico

*internal id 16 / `hero_nano` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 730 | +37 | 1618 | 2025 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.80 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.62 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.43 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 63 | +1.58 | 118.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_nano_set`

| stat | value |
|---|---|
| Damage per bullet | 1.84 |
| Bullets per shot | 9 |
| Damage per shot | 16.56 |
| Ammo / clip size | 12 |
| Damage per magazine | 198.72 |
| Cycle time (nominal) | 0.2100 s |
| Cycle time (effective avg) | 0.2100 s |
| Shots / second | 4.762 |
| Shots / second (with reload) | 2.235 |
| Reload duration | 2.60 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 78.86 |
| **DPS (with reload)** | **37.01** |
| Bullet damage per boon | +0.043 |
| Headshot multiplier | x1.65 |
| Bullet speed | 12500 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 1 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Gloom Bombs

> Throw a cluster of bombs that detonate after a delay, dealing spirit damage.Enemies hit by multiple bombs take 65% damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 14 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 45 | +0.6440 | 62.0 |
| Radius | 3 | - | - |
| TossSpeed | 400 | - | - |
| GrenadeCount | 4 | - | - |
| Lifetime | 0.750 | - | - |
| GrenadeAngleVariance | 0.080 | - | - |
| TimeBetweenGrenades | 0.050 | - | - |
| MultiHitPenaltyPercentage | 65 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -3
- **T2** — `MeleeResistReduction` -6, `MeleeResistReductionDuration` +6
- **T3** — `GrenadeCount` +3

#### Leaping Slash

> Dash forward before slashing all enemies in a circle, dealing melee damage. If the ability hits at least one hero, heal a small amount of health.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 13 | - | - |
| AbilityCastRange | 9 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DashAngleThreshold | 89 | - | - |
| DashSpeed | 2400 | - | - |
| DashRadius | 2 | - | - |
| ImpactDamage | 10 | +0.8000 | 31.1 |
| MoveSpeedPenaltyMaxSpeed | 200 | - | - |
| CameraDistance | 550 | - | - |
| SideMoveSpeedReduction | -90 | - | - |
| SlashRadius | 4 | - | - |
| SlashHeight | 2.500 | - | - |
| HealAmount | 40 | +1.4000 | 77.0 |
| PostDashMaintainedVelocityRatio | 0.150 | - | - |
| SlashForwardOffset | 1.500 | - | - |

**Upgrades**

- **T1** — `HealAmount` +25
- **T2** — `BonusGoldOnKill` +200, `BountyDuration` +3
- **T3** — `CooldownRefundPercent` +50, `ImpactDamage` +60

#### Ava

> Turn to shadows and possess Ava. You gain bonus move speed that increases over time, and become hidden on the minimap. Taking damage from an enemy hero resets your bonus move speed and puts Ava on a brief cooldown.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 30 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| BuffDuration | 15 | - | - |
| InterruptCooldown | 6 | - | - |
| SpeedBuildDuration | 4 | - | - |
| EnemyDamageSpeedPenalty | 65 | - | - |
| CatFormDamageDealtReduction | -100 | - | - |
| MinBonusMoveSpeedPercent | 30 | - | - |
| MaxBonusMoveSpeedPercent | 65 | - | - |

**Upgrades**

- **T1** — `BuffDuration` +15
- **T2** — `MaxBonusMoveSpeedPercent` +40, `HealthRegen` +15
- **T3** — `OutgoingDamagePercent` +18, `DamageAmpDuration` +6, `DamageAmpBuildDuration` +10

#### Return to Shadows (ULTIMATE)

> Instantly turn to shadows, becoming untargetable, gaining bonus move speed, and dealing spirit damage. After a delay, return from the shadows, dealing spirit damage again.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 115 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 3 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 7.500 | - | - |
| Damage | 150 | +0.6093 | 166.1 |
| FallSpeedMax | 10 | - | - |
| BonusMoveSpeedPercent | 20 | - | - |
| AirSpeedMax | 100 | - | - |
| AirDrag | 4 | - | - |
| ZAcceleration | 800 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -20
- **T2** — `Damage` +75, `BonusMoveSpeedPercent` +20
- **T3** — `RefundCooldowns` +1, `HealAmount` +450

---

## Celeste

*internal id 81 / `hero_unicorn` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 690 | +33 | 1482 | 1845 |
| Health Regen | 1 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.20 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 4 |
| Stamina Regen | 0.19/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.62 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.43 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_unicorn_set`

| stat | value |
|---|---|
| Damage per bullet | 18 |
| Bullets per shot | 1 |
| Damage per shot | 18 |
| Ammo / clip size | 8 |
| Damage per magazine | 144 |
| Cycle time (nominal) | 0.5800 s |
| Cycle time (effective avg) | 0.5800 s |
| Shots / second | 1.724 |
| Shots / second (with reload) | 1.161 |
| Reload duration | 2 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 31.03 |
| **DPS (with reload)** | **20.90** |
| Bullet damage per boon | +0.820 |
| Headshot multiplier | x1.65 |
| Bullet speed | 1968.50 |
| Falloff: full damage to | 22.0 m |
| Falloff: decays to | 60 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.500 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Light Eater

> Blast enemies in a cone in front of you with a flare of light. Blasted enemies take spirit damage when attacked by Celeste and provides her spirit lifesteal.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 20 | - | - |
| AbilityDuration | 8 | +0.0500 | 9.3 |
| AbilityCastRange | 10 | - | - |
| AbilityUnitTargetLimit | 100 | - | - |
| AbilityCastDelay | 0.300 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| FlareDamage | 40 | +0.4700 | 52.4 |
| Damage | 15 | +0.3400 | 24.0 |
| TickRate | 0.500 | - | - |
| TargetingConeAngle | 70 | - | - |
| ExtraSweepRadius | 2 | - | - |
| AbilityLifestealPercentHero | 18 | - | - |

**Upgrades**

- **T1** — `AbilityLifestealPercentHero` +15
- **T2** — `AbilityCastRange` +3, `AbilityCooldown` -10
- **T3** — `Damage` +0.200

#### Dazzling Trick

> Surround yourself in a protective prism. If the barrier is destroyed, it silences nearby enemies and deals a portion of the barrier as damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 38 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| MaxLifetime | 4 | - | - |
| BuffDuration | 4 | - | - |
| ExplodeRadius | 14 | - | - |
| DebuffDuration | 1.750 | - | - |
| CombatBarrier | 100 | +0.8000 | 121.1 |
| BarrierDamagePercentage | 50 | - | - |

**Upgrades**

- **T1** — `BonusMoveSpeed` +3.500
- **T2** — `CombatBarrier` +0.760
- **T3** — `DebuffDuration` +1.250, `AbilityCooldown` -20

#### Radiant Daggers

> Call down a beam of light from the sky. After a short duration, the beam will fully form, causing an explosion that deals spirit damage to all targets in the area. Celeste will receive a stacking buff that increases her spirit damage anytime this hits an enemy hero.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 33 | - | - |
| AbilityCastRange | 30 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 2 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| ExplosionInterval | 0.700 | - | - |
| PreExplosionDuration | 1.400 | - | - |
| ExplosionRadius | 8 | - | - |
| ImpactDamage | 55 | +0.6300 | 71.6 |
| ClimbHeight | 50 | - | - |
| TickRate | 0.500 | - | - |
| BuffMaxStacks | 6 | - | - |
| BuffDuration | 30 | - | - |
| MagicIncreasePerStack | 7 | - | - |
| BuffDelay | 0.750 | - | - |
| PostExplosionDuration | 0.800 | - | - |

**Upgrades**

- **T1** — `AbilityCharges` +2
- **T2** — `ImpactDamage` +70, `AbilityCooldown` -22
- **T3** — `MagicIncreasePerStack` +4, `FireRatePerStack` +9

#### Shining Wonder (ULTIMATE)

> Launch a deadly orb of light that deals spirit damage and applies slow and reduces Dash Distance on impact. The orb then bounces to the enemies within range. If no target is found, the orb will linger for a short duration while continuing to look for targets.Prioritizes enemy heroes when picking targets.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 160 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.750 | - | - |
| AbilityChannelTime | 9999 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 140 | +0.6000 | 155.8 |
| SlowDuration | 1.500 | - | - |
| SlowPercent | 32 | - | - |
| GroundDashReductionPercent | -22 | - | - |
| MaxBounces | 8 | - | - |
| BounceRadius | 15.500 | - | - |
| PriorityBounceRadius | 13.500 | - | - |
| BounceGrace | 3.250 | - | - |
| NextTargetDuration | 4 | - | - |

**Upgrades**

- **T1** — `GroundDashReductionPercent` -14, `SlowPercent` +16
- **T2** — `Damage` +0.450
- **T3** — `MaxBounces` +6, `AbilityCooldown` -30

---

## Drifter

*internal id 64 / `hero_drifter` / complexity 3*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 755 | +41 | 1739 | 2190 |
| Health Regen | 3.50 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.90 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 51.50 | +1.58 | 106.80 |
| Heavy Melee | 120 | - | - |

### Weapon

`citadel_weapon_drifter_set`

| stat | value |
|---|---|
| Damage per bullet | 19.50 |
| Bullets per shot | 3 |
| Damage per shot | 58.50 |
| Ammo / clip size | 12 |
| Damage per magazine | 702 |
| Cycle time (nominal) | 0.4410 s |
| Cycle time (effective avg) | 0.4410 s |
| Shots / second | 2.268 |
| Shots / second (with reload) | 1.503 |
| Reload duration | 2.44 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 132.65 |
| **DPS (with reload)** | **87.90** |
| Bullet damage per boon | +0.490 |
| Headshot multiplier | x1.65 |
| Bullet speed | 20000 |
| Falloff: full damage to | 22.0 m |
| Falloff: decays to | 27.0 m |
| Falloff: damage retained | 60% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.250 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Rend

> Swipe at enemies in a cone ahead of you, dealing spirit damage. If the enemy is in close range, deal bonus melee damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 16 | - | - |
| AbilityCastRange | 16 | - | - |
| AbilityUnitTargetLimit | 30 | - | - |
| AbilityCastDelay | 0.400 | - | - |
| AbilityPostCastDuration | 0.400 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| RangeForBonusDamage | 8 | - | - |
| TargetingConeAngle | 50 | - | - |
| ExtraSweepConeAngle | 60 | - | - |
| ExtraSweepRange | 3 | - | - |
| ExtraSweepOffsetBehindCaster | 80 | - | - |
| BonusDamage | 40 | +1.4000 | 77.0 |
| FallSpeedMax | 1 | - | - |
| AirSpeedMax | 70 | - | - |

**Upgrades**

- **T1** — `BonusDamage` +40
- **T2** — `AbilityCooldown` -8
- **T3** — `DebuffDuration` +2, `UseHeavyMelee` +1, `DamageHeavyMelee` +0.550, `Damage` +0

#### Stalker's Mark

> Send out a mark that bleeds the first target it hits, dealing spirit damage over time.While the enemy is bleeding you can re-activate Stalker's Mark to instantly appear behind their back.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 26 | - | - |
| AbilityDuration | 5 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DotHealthPercent | 2 | +0.0150 | 2.4 |
| TickRate | 0.500 | - | - |
| TeleportBackOffsetFromTarget | 135 | - | - |
| FallSpeedMax | 0.300 | - | - |
| AirDrag | 3 | - | - |
| VerticalDrag | 1 | - | - |

**Upgrades**

- **T1** — `BulletResistReduction` -8
- **T2** — `AbilityDuration` +3, `AbilityCooldown` -10
- **T3** — `DotHealthPercent` +1.500, `HealAmpReceivePenaltyPercent` -40, `HealAmpRegenPenaltyPercent` -40

#### Bloodscent

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCastRange | 80 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| IsolationRange | 20 | - | - |
| AmpDamagePercent | 15 | - | - |
| LowHealthThreshold | 30 | - | - |
| InvisFadeToDuration | 0.300 | - | - |
| SpottedRadius | 15 | - | - |
| RevealOnSpottedDuration | 1.500 | - | - |
| RevealOnDamageDuration | 0.250 | - | - |
| DelayBeforeInvisStarts | 0.600 | - | - |
| TrailDuration | 10 | - | - |
| MaxTrailTargets | 2 | - | - |
| TargetLingerDuration | 3 | - | - |
| TickRate | 1 | - | - |
| KillDuration | 300 | - | - |
| WeaponDmgPerIsolationKill | 3 | - | - |
| IsolationAssistPercentValue | 100 | - | - |

**Upgrades**

- **T1** — `BonusMoveSpeed` +3
- **T2** — `HealOnKillPct` +24, `StaminaToRestore` +2
- **T3** — `AmpDamagePercent` +11

#### Eternal Night (ULTIMATE)

> Surround nearby enemy heroes in darkness, severely limiting their vision of other units. Affected enemies are briefly revealed to you and are considered isolated for the duration.You gain bonus sprint speed.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 145 | - | - |
| AbilityDuration | 6.500 | - | - |
| AbilityCastRange | 100 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| SmallVisionDistance | 15 | - | - |
| DrifterNearbyRangeCheck | 40 | - | - |
| DarkFactor | 1 | - | - |
| PostProcessFadeInTime | 0.200 | - | - |
| PostProcessFadeOutTime | 1 | - | - |
| MinProjectileSpeed | 3000 | - | - |
| MaxProjectileSpeed | 3000 | - | - |
| DistanceForMaxProjSpeed | 200 | - | - |
| BonusSprintSpeed | 2 | - | - |
| BonusSprintAcceleration | 12 | - | - |
| RevealDuration | 3 | - | - |
| MaxTargets | 2 | - | - |
| AuraLingerDuration | 0.001 | - | - |

**Upgrades**

- **T1** — `BonusSprintSpeed` +10
- **T2** — `AbilityCooldown` -40
- **T3** — `AbilityDuration` +2.500, `MaxTargets` +1

---

## Dynamo

*internal id 11 / `hero_dynamo` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 880 | +61 | 2344 | 3015 |
| Health Regen | 1.75 | - | - | - |
| Bullet Resist | 0% | +0.62% | 15% | 21.88% |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.70 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.72 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.51 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_sumo_set`

| stat | value |
|---|---|
| Damage per bullet | 12.60 |
| Bullets per shot | 1 |
| Damage per shot | 12.60 |
| Ammo / clip size | 20 |
| Damage per magazine | 252 |
| Cycle time (nominal) | 0.2625 s |
| Cycle time (effective avg) | 0.2625 s |
| Shots / second | 3.810 |
| Shots / second (with reload) | 2.548 |
| Reload duration | 2.35 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 48 |
| **DPS (with reload)** | **32.10** |
| Bullet damage per boon | +0.500 |
| Headshot multiplier | x1.65 |
| Bullet speed | 12600 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.500 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Kinetic Pulse

> Release an energy pulse that travels along the ground, dealing spirit damage and applying knockup.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 26 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.420 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 5 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| TechCleaveExpireTime | 0.200 | - | - |
| Damage | 115 | +1.5500 | 155.9 |
| ClimbHeight | 1 | - | - |
| DistanceAboveGround | 1 | - | - |
| DropDownRate | 20 | - | - |
| TossSpeed | 450 | - | - |
| ImpactInterval | 0.100 | - | - |
| StompRange | 16 | - | - |
| StompWidth | 5.500 | - | - |
| TossDuration | 1 | - | - |

**Upgrades**

- **T1** — `AbilityCharges` +1
- **T2** — `BulletResistReduction` -15, `SlowPercent` +24, `SlowDuration` +4
- **T3** — `Damage` +135, `StompRange` +20

#### Quantum Entanglement

> Briefly become untargetable while teleporting to the target location. Restores stamina upon use. : Bring nearby allies with you.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 20 | - | - |
| AbilityDuration | 1.400 | - | - |
| AbilityCastRange | 10 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| AllyDistance | 13 | - | - |
| TrailInterval | 0.010 | - | - |
| StaminaRestore | 1 | - | - |

**Upgrades**

- **T1** — `AbilityCastRange` +6
- **T2** — `AbilityCooldown` -6
- **T3** — `ReduceDebuffs` +50, `ChargeReplenish` +1

#### Rejuvenating Aurora

> While channeling, restore health over time to you and any allies nearby.You can dash and melee without breaking the channel.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 48 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 5 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| HealingPerSecond | 30 | +0.4000 | 40.6 |
| AuraLingerDuration | 1 | - | - |
| ShareWithFriendsRadius | 8 | - | - |

**Upgrades**

- **T1** — `MovementSpeedBonus` +4, `MovementSpeedBonusDuration` +8
- **T2** — `AbilityCooldown` -20, `AbilityChannelTime` +1
- **T3** — `NoChannel` +1, `HealMaxHealthPercent` +2.500

#### Singularity (ULTIMATE)

> Create a singularity in your hands, dealing spirit damage over time, applying stun, and pulling in nearby enemies.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 250 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityChannelTime | 2.750 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| VacuumRadius | 7 | - | - |
| Speed | 200 | - | - |
| TossSpeed | 350 | - | - |
| TossAngle | 45 | - | - |
| DPS | 75 | +0.2800 | 82.4 |
| TickRate | 0.250 | - | - |
| CameraDistance | 400 | - | - |

**Upgrades**

- **T1** — `VacuumRadius` +2
- **T2** — `AbilityChannelTime` +0.750
- **T3** — `DPSPercentHealth` +6

---

## Graves

*internal id 76 / `hero_necro` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 730 | +35 | 1570 | 1955 |
| Health Regen | 1 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7 m/s |
| Sprint Speed (bonus) | 2.20 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 2 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_necro_set`

| stat | value |
|---|---|
| Damage per bullet | 3.60 |
| Bullets per shot | 1 |
| Damage per shot | 3.60 |
| Ammo / clip size | 40 |
| Damage per magazine | 144 |
| Cycle time (nominal) | 0.1020 s |
| Cycle time (effective avg) | 0.1020 s |
| Shots / second | 9.804 |
| Shots / second (with reload) | 5.610 |
| Reload duration | 2.80 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 35.29 |
| **DPS (with reload)** | **20.20** |
| Bullet damage per boon | +0.054 |
| Headshot multiplier | x1.65 |
| Bullet speed | 25000 |
| Falloff: full damage to | 7.6 m |
| Falloff: decays to | 17.0 m |
| Falloff: damage retained | 50% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 1 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Jar of Dead

> Passive: Collect death when anything dies nearby and store it in your Jar of Dead.Active: Throw a jar to summon Deadheads that repeatedly deal spirit damage to enemies. Deadheads follow you instead if there's no nearby enemies, and prioritize the target of your weapon.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityCharges | 4 | - | - |
| AbilityCooldownBetweenCharge | 13 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| SkullCount | 4 | - | - |
| SkullLifetime | 10 | - | - |
| TickRate | 0.200 | - | - |
| TargetSearchRadius | 7 | - | - |
| TargetSearchDelayMax | 1.250 | - | - |
| Damage | 16 | +0.2500 | 22.6 |
| TargetSearchDelayMin | 1.500 | - | - |
| MaxHits | -1 | - | - |
| SummonHealth | 20 | +1.3000 | 54.3 |
| SkullImmuneDuration | 0.150 | - | - |
| SpawnRadius | 2 | - | - |
| DelayBeforeRespawning | 1 | - | - |
| TargetDashRadius | 15 | +1 | 41.4 |
| SummonTakesDamage | 1 | - | - |
| ResourceCost | 120 | +1 | 146.4 |
| ResourceGenerationPercent | 100 | - | - |
| ResourceRadius | 40 | - | - |
| PickupsPerDeath | 1 | - | - |
| PickupsPerHeroDeath | 5 | - | - |
| AbilityChargesConditionally | 1 | - | - |
| KillTime | 0.200 | - | - |
| ResourcePerPickup | 10 | - | - |
| PickupsPerBossDeath | 5 | - | - |
| PickupsPerNeutralTrooperDeath | 3 | - | - |
| SkullKillGold | 7 | +0.5000 | 20.2 |
| TargetSearchInitialDelayMin | 0.150 | - | - |
| TargetSearchInitialDelayMax | 0.200 | - | - |
| TargetSearchInitialStagger | 0.125 | - | - |

**Upgrades**

- **T1** — `HealPerPickup` +0.160
- **T2** — `SlowPercent` +24, `SlowDuration` +1
- **T3** — `SkullCount` +2, `SkullLifetime` +4

#### Grasping Hands

> Unearth a line of grasping hands, summoning a Ghoul and leaving behind a rift. Enemies who pass through take spirit damage and receive immobilize. Alt-Cast rotates the orientation of the wall.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 34 | - | - |
| AbilityDuration | 5 | - | - |
| AbilityCastRange | 24 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| ZombieWallLength | 14 | +0.0500 | 15.3 |
| AuraRadius | 0.750 | - | - |
| DebuffDuration | 0.500 | - | - |
| GroundAuraSpacing | 1 | - | - |
| SlowPercent | 40 | - | - |
| ZombieWallHeight | 2.500 | - | - |
| Damage | 90 | +1.6000 | 132.2 |
| TickRate | 0.100 | - | - |
| ImmobilizeDuration | 1 | - | - |
| GroundAuraPopDelay | 1.100 | - | - |
| ZombieWallDeployTime | 0.600 | - | - |
| TetherDuration | 1 | - | - |
| TetherRadius | 0.100 | - | - |
| SummonCount | 1 | - | - |

**Upgrades**

- **T1** — `AbilityDuration` +2
- **T2** — `Damage` +90, `ZombieWallLength` +10
- **T3** — `ImmobilizeDuration` +0.750, `SummonCount` +1, `AbilityCooldown` -14

#### Essence Theft

> Your weapon steals weapon damage and spirit resist over time, up to a maximum amount per target.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityDuration | 4 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| MaxStolenAttackDamage | 25 | +0.2500 | 31.6 |
| ShootDurationForMax | 4 | - | - |
| ProgressLossPerSecond | 1 | - | - |
| TickInterval | 0.150 | - | - |
| DelayBeforeLoss | 0.500 | - | - |
| ProgressLossMultiplier | 2.300 | - | - |
| MaxStolenSpiritResist | 10 | - | - |
| MaxStolenTargets | 3 | - | - |
| MeleeBuildUp | 0.200 | - | - |

**Upgrades**

- **T1** — `MaxStolenSpiritResist` +5
- **T2** — `MaxStolenAttackDamage` +20
- **T3** — `SkullBuildUp` +0.150, `ZombieMeleeBuildUp` +0.150, `ZombieExplosionBuildUp` +1, `MaxStolenTargets` +1

#### Borrowed Decree (ULTIMATE)

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 140 | - | - |
| AbilityDuration | 16 | +0.0400 | 17.1 |
| AbilityCastRange | 20 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 0.660 | - | - |
| GrowTime | 0.100 | - | - |
| BlockerScaleFactor | 1 | - | - |
| KnockupSpeed | 240 | - | - |
| KnockupRadius | 4 | - | - |
| KnockupSideRatio | 1 | - | - |
| GravestoneHealth | 100 | - | - |
| AuraRadius | 8 | - | - |
| TickRate | 0.400 | - | - |
| SlowPercent | 64 | - | - |
| SlowDuration | 1.250 | - | - |
| PushForce | 300 | - | - |
| MaxGravestones | 3 | - | - |
| SummonInitialDelay | 0.300 | - | - |
| SummonFrequency | 4 | - | - |
| BuffDuration | -1 | - | - |
| StackingDebuffTickRate | 0.250 | - | - |
| Damage | 115 | +1.2700 | 148.5 |
| GravestoneTakesDamage | 1 | - | - |
| MaxStacks | 40 | - | - |
| StackDuration | 5 | - | - |
| SlowPercentPerStack | 0.500 | - | - |
| TechArmorDamageReductionPerStack | -0.500 | - | - |
| ReplicateZombieCast | 1 | - | - |
| SummonLifetime | 20 | - | - |
| DecayTickRate | 0.100 | - | - |
| DecayDuration | 1 | - | - |
| SummonMeleeDamage | 40 | +0.5000 | 53.2 |
| SummonHealth | 180 | +8 | 391.2 |
| BonusSpiritDamagePercentage | 15 | - | - |
| SummonSearchRadius | 4 | - | - |
| SummonMaxCount | 32 | - | - |
| ExplodeDelay | 0.230 | - | - |
| SpawnDuration | 1.500 | - | - |
| ExplosionRadius | 6.500 | - | - |
| BulletResist | 12.500 | - | - |
| SummonBurstCount | 2 | - | - |
| SummonBurstFrequency | 0.100 | - | - |
| DamageSlowPercent | 20 | - | - |
| DamageSlowDuration | 0.500 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -15, `MoveSpeedPercent` +25
- **T2** — `AbilityDuration` +10, `SummonFrequency` -0.300
- **T3** — `CurrentHealthDamagePercentage` +5

---

## Grey Talon

*internal id 17 / `hero_orion` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 780 | +38 | 1692 | 2110 |
| Health Regen | 1.50 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.30 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 4 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.62 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.43 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_archer_set`

| stat | value |
|---|---|
| Damage per bullet | 23.51 |
| Bullets per shot | 1 |
| Damage per shot | 23.51 |
| Ammo / clip size | 17 |
| Damage per magazine | 399.67 |
| Cycle time (nominal) | 0.6000 s |
| Cycle time (effective avg) | 0.6000 s |
| Shots / second | 1.667 |
| Shots / second (with reload) | 1.328 |
| Reload duration | 2.35 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 39.18 |
| **DPS (with reload)** | **31.22** |
| Bullet damage per boon | +0.850 |
| Headshot multiplier | x1.65 |
| Bullet speed | 19500 |
| Falloff: full damage to | 18.0 m |
| Falloff: decays to | 54 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.300 |

### Spirit scaling

- Spirit Power per boon: **+1.60**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **38.4**
- Spirit Power at 50k net worth (no items): **56**

### Abilities


#### Charged Shot

> Charge up a powerful shot that pierces through enemies. Hold Ability 1 or to hold the shot.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 17 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.500 | - | - |
| AbilityChannelTime | 9999 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 4 | - | - |
| ChannelMoveSpeed | 1.500 | - | - |
| TechCleaveExpireTime | 0.200 | - | - |
| FallSpeedMax | 60 | - | - |
| AirSpeedMax | 161.417 | - | - |
| Damage | 80 | +1 | 118.4 |
| CameraHeightOffset | 20 | - | - |
| CameraHorizontalOffset | 15 | - | - |

**Upgrades**

- **T1** — `AbilityCharges` +1
- **T2** — `Damage` +54
- **T3** — `AbilityCooldownBetweenCharge` -3, `Damage` +1

#### Rain of Arrows

> Launches you high in the air, allowing you to glide slowly. While airborne, you gain Weapon Damage and multishot on your weapon. for reduced jump height. Press Jump / mantle to cancel the glide.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 25 | - | - |
| AbilityDuration | 4 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| JumpPitch | -60 | - | - |
| JumpSpeed | 27.500 | - | - |
| AltJumpSpeed | 12 | - | - |
| WeaponDamageBonus | 3 | - | - |
| FallSpeedMax | 25 | - | - |
| AirSpeedMax | 261.417 | - | - |
| BulletSplitShot | 5 | - | - |
| FxRadius | 4 | - | - |
| AirMoveIncreasePercent | 25 | - | - |

**Upgrades**

- **T1** — `WeaponDamageBonus` +3, `SlowPercent` +24, `SlowDuration` +1.500
- **T2** — `AbilityCooldown` -12
- **T3** — `BulletLifestealPercent` +30, `TechLifestealPercent` +30, `EvasionPercent` +30

#### Spirit Snare

> Throw out a trap that begins to arm itself. Once armed, the trap will trigger when an enemy enters its radius, applying Curse and Movement Slow that interrupts, Silences, Disarms, and prevents item usage.Hit the trap with a Charged Shot to detonate early with increased radius.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 34 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| TetherRadius | 6 | - | - |
| Radius | 6.500 | - | - |
| TrapHeight | 2 | - | - |
| Lifetime | 22 | - | - |
| Damage | 25 | - | - |
| TetherDuration | 2.250 | - | - |
| TripTime | 0.500 | - | - |
| ArmTime | 2 | - | - |
| TripUpSpeed | 250 | - | - |
| TripGravity | 0.400 | - | - |
| SkipFrames | 6 | - | - |
| SlowPercent | 24 | - | - |
| ChargedShotHitRadiusScale | 30 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -20
- **T2** — `BulletArmorReduction` -15, `DebuffDuration` +10
- **T3** — `TetherDuration` +1, `Radius` +1.500

#### Guided Owl (ULTIMATE)

> After 1.5s cast time, launch a spirit owl that you control and which explodes on impact, damaging and stunning enemies. Hold [W] to accelerate the owl.Press Jump / mantle to release control. Gain permanent Spirit Power for each enemy hero killed with Guided Owl.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 125 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 1.500 | - | - |
| AbilityChannelTime | 20 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ExplosionRadius | 12 | - | - |
| Damage | 230 | +0.9374 | 266.0 |
| StunDuration | 0.750 | - | - |
| BonusTechPowerPerKill | 8 | - | - |

**Upgrades**

- **T1** — `Damage` +85
- **T2** — `AbilityCooldown` -40
- **T3** — `LowHealthEnemyThresholdPct` +22

---

## Haze

*internal id 13 / `hero_haze` / complexity 1*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 730 | +33 | 1522 | 1885 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 8.20 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.62 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.43 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_haze_set`

| stat | value |
|---|---|
| Damage per bullet | 5.26 |
| Bullets per shot | 1 |
| Damage per shot | 5.26 |
| Ammo / clip size | 25 |
| Damage per magazine | 131.50 |
| Cycle time (nominal) | 0.1050 s |
| Cycle time (effective avg) | 0.1050 s |
| Shots / second | 9.524 |
| Shots / second (with reload) | 4.785 |
| Reload duration | 2.35 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 50.10 |
| **DPS (with reload)** | **25.17** |
| Bullet damage per boon | +0.143 |
| Headshot multiplier | x1.65 |
| Bullet speed | 30000 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 46.0 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.400 |

### Spirit scaling

- Spirit Power per boon: **+0.50**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **12**
- Spirit Power at 50k net worth (no items): **17.5**

### Abilities


#### Sleep Dagger

> Throw a dagger that damages and sleeps the target. Sleeping targets wake up shortly after being damaged. Throwing a Dagger does not break your invisibility. Sleep Dagger does not interrupt enemies' channeling abilities.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 30 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| Damage | 65 | +2.2000 | 91.4 |
| SleepDuration | 2.750 | - | - |
| SleepWakeUpDelay | 0.100 | +0.0020 | 0.1 |
| MinimumSleepTime | 0.200 | - | - |
| SleepMoveSpeed | 1.500 | - | - |
| DoesNotBreakInvis | 1 | - | - |

**Upgrades**

- **T1** — `BulletResistReduction` -10, `BulletResistReductionDuration` +6
- **T2** — `SleepDuration` +1, `FixationStacks` +15
- **T3** — `AbilityCooldown` -17, `SlowPercent` +40, `GroundDashReductionPercent` -45, `DebuffDuration` +3

#### Smoke Bomb

> Fade out of sight, becoming invisible and gaining sprint speed. Attacking removes invisibility, but using items does not. Close enemies can see through your invisibility.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 33 | - | - |
| AbilityDuration | 8 | +0.1000 | 9.2 |
| AbilityUnitTargetLimit | 1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| InvisAlertWhenFading | 1 | - | - |
| InvisFadeToDuration | 1.500 | - | - |
| SpottedRadius | 18 | - | - |
| RevealOnDamageDuration | 1.500 | - | - |
| RevealOnSpottedDuration | 0.500 | - | - |
| FullInvisDistance | 50 | - | - |

**Upgrades**

- **T1** — `InvisMoveSpeedMod` +7
- **T2** — `AbilityCharges` +2, `AbilityCooldownBetweenCharge` +7
- **T3** — `BulletLifesteal` +50, `PostInvisBuffDuration` +5, `DispelOnUse` +1

#### Fixation

> Shooting a target increases your bullet damage on that target. Gain one stack per bullet hit, three if the hit is a headshot.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityDuration | 6 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| MaxStacks | 40 | - | - |
| HeadshotStacks | 3 | - | - |
| DamageBonusFixedPerStack | 0.200 | - | - |

**Upgrades**

- **T1** — `ProcDamage` +0.800, `ProcDamageStackCount` +20, `SlowPercent` +12, `SlowDuration` +2
- **T2** — `AbilityDuration` +5, `MaxStacks` +40
- **T3** — `DamageBonusFixedPerStack` +0.000

#### Bullet Dance (ULTIMATE)

> Enter a flurry, firing your weapon at nearby enemies with perfect accuracy and added Bullet Damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 165 | - | - |
| AbilityDuration | 3.500 | +0.0300 | 3.9 |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.400 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 4 | - | - |
| Radius | 16 | - | - |
| RadiusMin | 0.750 | - | - |
| TargetsPerTick | 1 | - | - |
| BonusFireRate | 25 | - | - |
| WeaponDamageBonus | 7 | - | - |
| ProcChance | 100 | - | - |
| EvasionPercent | 30 | - | - |
| OverrideBulletRadius | 10 | - | - |

**Upgrades**

- **T1** — `WeaponDamageBonus` +7
- **T2** — `BonusFireRate` +10, `ChannelMoveSpeed` +3
- **T3** — `EvasionPercent` +40, `AbilityCooldown` -65

---

## Holliday

*internal id 14 / `hero_astro` / complexity 3*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 780 | +43 | 1812 | 2285 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 8.20 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 2 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.62 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.43 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_astro_set`

| stat | value |
|---|---|
| Damage per bullet | 19.70 |
| Bullets per shot | 1 |
| Damage per shot | 19.70 |
| Ammo / clip size | 10 |
| Damage per magazine | 197 |
| Cycle time (nominal) | 0.4725 s |
| Cycle time (effective avg) | 0.4725 s |
| Shots / second | 2.116 |
| Shots / second (with reload) | 1.294 |
| Reload duration | 2.75 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 41.69 |
| **DPS (with reload)** | **25.50** |
| Bullet damage per boon | +1.144 |
| Headshot multiplier | x1.65 |
| Bullet speed | 45500 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 1 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Powder Keg

> Throw a barrel that explodes after a delay, dealing spirit damage, setting enemies on fire and applying knockup. The barrel can be detonated early by being shot, melee'd, or detonated by another barrel. The burn stacks, so overlapping barrels burn for their combined damage.Can be Alt-Cast to place the barrel infront of Holliday.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 28 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.125 | - | - |
| AbilityCharges | 2 | - | - |
| AbilityCooldownBetweenCharge | 7.500 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 6 | - | - |
| BarrelLifetime | 8 | - | - |
| ImpactDamage | 40 | +0.5250 | 53.9 |
| DPS | 13.333 | +0.1750 | 18.0 |
| BurnDuration | 3 | - | - |
| TickRate | 0.500 | - | - |
| BarrelRollSpeedMoveMin | 20 | - | - |
| BarrelPitchMin | 2 | - | - |
| BarrelPitchMax | 90 | - | - |
| BarrelRollSpeedMoveAir | 10 | - | - |
| BarrelLightMeleeForceForward | 1400 | - | - |
| BarrelLightMeleeForceUp | 300 | - | - |
| BarrelHeavyMeleeForceForward | 1800 | - | - |
| BarrelHeavyMeleeForceUp | 300 | - | - |
| BarrelScale | 1.300 | - | - |
| TossSpeed | 140 | - | - |
| ArmTime | 0.100 | - | - |
| MinTimeBeforeDestroy | 0.100 | - | - |
| TossDuration | 0.400 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -10
- **T2** — `AbilityCharges` +1
- **T3** — `ImpactDamage` +0.250, `DPS` +0.083, `AbilityCooldownBetweenCharge` -5

#### Bounce Pad

> Drop a bounce pad in the world that launches any hero. You explode on landing, dealing Damage to any nearby enemies. The explosion can only occur once per person per Bounce Pad.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 41 | - | - |
| AbilityDuration | 22 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.080 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 3.500 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| BounceVelocity | 750 | - | - |
| UpFactor | 1.200 | - | - |
| BarrelBounceVelocity | 800 | - | - |
| BarrelUpFactor | 1 | - | - |
| Scale | 1 | - | - |
| PlaceDistance | 200 | - | - |
| AirControlPercent | 100 | - | - |
| AirControlAccelPercent | 50 | - | - |
| MinAirTimeForStomp | 0.200 | - | - |
| Radius | 9 | - | - |
| VerticalDifferenceTolerance | 60 | - | - |
| TossSpeed | 500 | - | - |
| StompDamage | 60 | +0.3720 | 69.8 |

**Upgrades**

- **T1** — `AbilityCooldown` -10
- **T2** — `SpeedOnLand` +4, `SpeedOnLandDuration` +4
- **T3** — `StompStunDuration` +0.700

#### Crackshot

> Headshots deal bonus Damage and applies a Fading Move Speed penalty. This effect can only occur when off cooldown. Cooldown is reduced by 50% on NPC hits. Crackshot ignores range damage fall-off and does not apply to objectives.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 20 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ExplosionRadius | 2 | - | - |
| Damage | 55 | +1.1160 | 84.5 |
| DebuffDuration | 2 | - | - |
| FadingSlowPercent | 40 | - | - |
| CrackshotNPCCDReduction | 50 | - | - |

**Upgrades**

- **T1** — `FadingSlowPercent` +20
- **T2** — `Damage` +49.500, `BulletResistReduction` -6, `BulletResistReductionDuration` +5
- **T3** — `AbilityCooldownPerHeadshot` -6, `AbilityCooldownPerHeadshotNPC` -3

#### Spirit Lasso (ULTIMATE)

> Throw out your lasso, dealing spirit damage, pulling, and applying stun.Using a Bounce Pad extends the duration of Spirit Lasso.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 130 | - | - |
| AbilityDuration | 2.250 | - | - |
| AbilityCastRange | 20 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.500 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| BouncePadExtendDuration | 1.250 | - | - |
| LiftHeight | 7 | - | - |
| LiftHorizontal | -30 | - | - |
| FollowDampingFactor | 8 | - | - |
| GrabExtraTargetsRadiusMult | 2 | - | - |
| ExtraTargetConeAngle | 60 | - | - |
| ExtraTargetHorizontalOffset | 30 | - | - |
| FollowDistance | 60 | - | - |
| CameraPreviewOffset | 25 | - | - |
| CameraPreviewSpeed | 0.600 | - | - |
| CameraPreviewDistance | 200 | - | - |
| LassoTargetMaxSpeed | 55 | - | - |
| LiftInitialDelay | 0.500 | - | - |
| LiftInitialVelocityStart | 500 | - | - |
| LiftInitialRisingSpeed | 100 | - | - |
| Damage | 80 | +0.9300 | 104.6 |

**Upgrades**

- **T1** — `Damage` +80
- **T2** — `AbilityDuration` +0.750
- **T3** — `AbilityCooldown` -40

---

## Infernus

*internal id 1 / `hero_inferno` / complexity 1*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 830 | +39 | 1766 | 2195 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.70 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_inferno_set`

| stat | value |
|---|---|
| Damage per bullet | 5.50 |
| Bullets per shot | 1 |
| Damage per shot | 5.50 |
| Ammo / clip size | 27 |
| Damage per magazine | 148.50 |
| Cycle time (nominal) | 0.1050 s |
| Cycle time (effective avg) | 0.1050 s |
| Shots / second | 9.524 |
| Shots / second (with reload) | 5.061 |
| Reload duration | 2.25 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 52.38 |
| **DPS (with reload)** | **27.84** |
| Bullet damage per boon | +0.088 |
| Headshot multiplier | x1.65 |
| Bullet speed | 26000 |
| Falloff: full damage to | 18.0 m |
| Falloff: decays to | 55 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.150 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Napalm

> Spew an incendiary mixture, dealing spirit damage, applying slow, and coating targets in napalm.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 25 | - | - |
| AbilityCastRange | 20 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 6 | - | - |
| ChannelMoveSpeed | 18 | - | - |
| TickRate | 0.500 | - | - |
| ParticleRadiusMultiplier | 1.150 | - | - |
| IncomingDamagePercentFromCaster | 16 | - | - |
| DebuffDuration | 8 | - | - |
| Damage | 40 | +0.6000 | 55.8 |
| HeightOffGround | 50 | - | - |
| GrowthPerMeter | 0.500 | - | - |
| InitialWidth | 1 | - | - |
| SlowDuration | 4 | - | - |
| SlowPercent | 28 | - | - |

**Upgrades**

- **T1** — `AbilityCharges` +1
- **T2** — `LifestealPercentHero` +15
- **T3** — `IncomingDamagePercentFromCaster` +17, `HealAmpReceivePenaltyPercent` -33, `HealAmpRegenPenaltyPercent` -33

#### Flame Dash

> Dash forward, gaining slow resistance while leaving a flaming trail that deals spirit damage over time. Hold [W] while active to dash farther.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 38 | - | - |
| AbilityDuration | 3 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| ChannelMoveSpeed | 18 | - | - |
| DashSpeed | 12 | - | - |
| DashAirSpeed | 8 | - | - |
| FlameAuraRadius | 4.500 | - | - |
| DPS | 30 | +0.7000 | 48.5 |
| AuraLingerDuration | 1 | - | - |
| TickRate | 0.500 | - | - |
| GroundFlameDuration | 4 | - | - |
| GroundAuraSpacing | 1 | - | - |
| SpeedBurstSpeed | 20 | - | - |
| SideMoveSpeedReduction | -65 | - | - |
| FlameDashJumpBonus | 50 | - | - |
| SlowResistance | 50 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -12
- **T2** — `DPS` +20, `GroundFlameDuration` +1
- **T3** — `AbilityCharges` +2, `AbilityCooldownBetweenCharge` +14

#### Afterburn

> Weapon hits build up a burning effect, dealing spirit damage over time. Abilities refresh to the base burn duration and weapon hits extend it.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| BuildUpDuration | 17 | - | - |
| BuildUpBulletPercentPerHit | 8.100 | - | - |
| CritBuildup | 15.400 | - | - |
| RefillDuration | 0.500 | - | - |
| RefillDurationCrit | 1 | - | - |
| TickRate | 0.500 | - | - |
| BurnDurationBase | 3 | - | - |
| BurnDuration | 3 | - | - |
| DPS | 14 | +0.6600 | 31.4 |

**Upgrades**

- **T1** — `DPS` +16
- **T2** — `OutgoingTechDamagePercent` -35
- **T3** — `BurnDuration` +3

#### Concussive Combustion (ULTIMATE)

> Become a living bomb, dealing spirit damage and applying stun to all nearby enemies after a delay.Once cast, Concussive Combustion cannot be interrupted.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 190 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| ExplodeDelay | 3.250 | - | - |
| StunDuration | 1.250 | - | - |
| Damage | 125 | +0.9749 | 150.7 |
| Radius | 12 | - | - |

**Upgrades**

- **T1** — `Damage` +100
- **T2** — `AbilityCooldown` -65, `LifeStealPercentOnHit` +100
- **T3** — `StunDuration` +0.900, `Radius` +10

---

## Ivy

*internal id 20 / `hero_tengu` / complexity 3*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 755 | +45 | 1835 | 2330 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7.20 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 4 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.62 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.43 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_tengu_set`

| stat | value |
|---|---|
| Damage per bullet | 4.45 |
| Bullets per shot | 1 |
| Damage per shot | 4.45 |
| Ammo / clip size | 33 |
| Damage per magazine | 146.85 |
| Cycle time (nominal) | 0.0735 s |
| Cycle time (effective avg) | 0.0735 s |
| Shots / second | 13.605 |
| Shots / second (with reload) | 6.446 |
| Reload duration | 2.44 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 60.54 |
| **DPS (with reload)** | **28.68** |
| Bullet damage per boon | +0.080 |
| Headshot multiplier | x1.65 |
| Bullet speed | 22500 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.500 |

### Spirit scaling

- Spirit Power per boon: **+1.20**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **28.8**
- Spirit Power at 50k net worth (no items): **42**

### Abilities


#### Entangling Thorns

> Summon a patch of choking thorns that damage and slows enemies in its radius.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 32 | - | - |
| AbilityDuration | 4 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 5 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| TickRate | 0.250 | - | - |
| Radius | 6 | - | - |
| Height | 2 | - | - |
| DPS | 40 | +0.5500 | 55.8 |
| SlowPercent | 28 | - | - |

**Upgrades**

- **T1** — `AbilityCharges` +1
- **T2** — `Radius` +2, `DPS` +0.500
- **T3** — `TimeToEntangle` +2, `EntangleDuration` +1.600

#### Kudzu Connection

> Connect with a nearby ally to gain bonuses, replicated healing, and ignore the move speed penalty while shooting.Receive 50% of Bonuses with no connectionConnection requires line of sight.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 37 | - | - |
| AbilityDuration | 12 | - | - |
| AbilityCastRange | 16 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| BonusFireRate | 10 | +0.1800 | 15.2 |
| BulletLifestealPercent | 15 | +0.1500 | 19.3 |
| TickRate | 0.100 | - | - |
| TetherSharedHealPct | 35 | +0.8500 | 59.5 |
| HealingPerGlub | 20 | - | - |
| TotalTetherTargets | 1 | - | - |
| MoveWhileShootingSpeedPenaltyReductionPercent | 100 | - | - |
| MoveWhileZoomedSpeedPenaltyReductionPercent | 100 | - | - |

**Upgrades**

- **T1** — `MoveSpeedBonus` +2
- **T2** — `BonusFireRate` +8, `BulletLifestealPercent` +8
- **T3** — `AbilityDuration` -13, `AbilityCooldown` -37

#### Stone Form

> Turn yourself into impervious stone and smash into the ground, stunning and damaging enemies nearby. Heals you for a percentage of your max health.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 40 | - | - |
| AbilityDuration | 3 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.250 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DampingFactor | 0.250 | - | - |
| MoveSpeedMax | 8 | - | - |
| LiftHeight | 180 | - | - |
| LiftTime | 1 | - | - |
| MaxHealthRegen | 6 | - | - |
| Damage | 75 | +0.6000 | 92.3 |
| StunDuration | 0.750 | - | - |
| Radius | 5.750 | - | - |

**Upgrades**

- **T1** — `MaxHealthRegen` +6
- **T2** — `AbilityCooldown` -25
- **T3** — `StunDuration` +0.750, `Damage` +1.500

#### Air Drop (ULTIMATE)

> Grab an ally and take flight with them. Drop your ally to cause an explosion, dealing spirit damage. You and your ally gain increased Outgoing Damage when flying ends. Cooldown reduced by 30% when used on allies.Taking damage briefly disables using the ability.While lifted, your ally cannot attack and deals -20% damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 100 | - | - |
| AbilityDuration | 21 | - | - |
| AbilityCastRange | 22 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| CooldownReductionPctOnOthers | 30 | - | - |
| InterruptCooldown | 3.500 | - | - |
| AllyCastDelay | 0.100 | - | - |
| ExplodeDamage | 115 | +0.7000 | 135.2 |
| OnLandDamageRadiusStart | 16 | - | - |
| OnLandDamageRadius | 20 | - | - |
| SilenceBombSpeed | 12 | - | - |
| AllyOutgoingDamagePercent | -20 | - | - |
| BuffDuration | 8 | - | - |
| AirDropOutgoingDamagePercent | 20 | - | - |

**Upgrades**

- **T1** — `AirDropBulletShield` +0.700
- **T2** — `SlowPercent` +32, `DebuffDuration` +3
- **T3** — `SilenceDuration` +3, `ExplodeDamage` +1.500, `AirDropBulletShield` +1

---

## Kelvin

*internal id 12 / `hero_kelvin` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 880 | +60 | 2320 | 2980 |
| Health Regen | 1 | - | - | - |
| Spirit Resist | 0% | +0.62% | 15% | 21.88% |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.70 m/s |
| Sprint Speed (bonus) | 1.10 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.18/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.72 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.51 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_kelvin_set`

| stat | value |
|---|---|
| Damage per bullet | 18.60 |
| Bullets per shot | 1 |
| Damage per shot | 18.60 |
| Ammo / clip size | 14 |
| Damage per magazine | 260.40 |
| Cycle time (nominal) | 0.2625 s |
| Cycle time (effective avg) | 0.2625 s |
| Shots / second | 3.810 |
| Shots / second (with reload) | 2.151 |
| Reload duration | 2.58 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 70.86 |
| **DPS (with reload)** | **40** |
| Bullet damage per boon | +0.418 |
| Headshot multiplier | x1.65 |
| Bullet speed | 6300 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 1 |

### Spirit scaling

- Spirit Power per boon: **+1.30**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **31.2**
- Spirit Power at 50k net worth (no items): **45.5**

### Abilities


#### Frost Grenade

> Throw a grenade that explodes in a cloud of freezing ice that heals allies and applies spirit damage and move speed reduction to enemies.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 30 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityCharges | 2 | - | - |
| AbilityCooldownBetweenCharge | 7 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 6.500 | - | - |
| Damage | 60 | +0.6000 | 78.7 |
| SlowPercent | 32 | - | - |
| SlowDuration | 4 | - | - |
| HealAmount | 60 | +0.8000 | 85.0 |

**Upgrades**

- **T1** — `Damage` +30, `HealAmount` +30
- **T2** — `PauseStaminaRegen` +1, `AbilityCooldown` -10
- **T3** — `Radius` +2, `HealAmount` +0.900, `Damage` +0.800

#### Ice Path

> Kelvin creates a floating trail of ice and snow that gives movement bonuses to him and his allies. Kelvin gains 60% slow resistance for the duration. Enemies can also walk on the floating trail. Press Dash / Crouch / slide to travel up or down while in Ice Path.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 50 | - | - |
| AbilityDuration | 8 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| IcePathInterval | 0.500 | - | - |
| CameraDistance | 250 | - | - |
| PopupForce | 30 | - | - |
| MinHeight | 20 | - | - |
| IcePathAuraDuration | 18 | - | - |
| ModifierRadius | 5 | - | - |
| IcePathShardRadius | 1.200 | - | - |
| IcePathEdgeWidth | 0.700 | - | - |
| IcePathPullInStrength | 20 | - | - |
| MoveSpeedBonus | 2 | - | - |
| SprintSpeedBonus | 2 | - | - |
| SlowResistancePercent | 60 | - | - |
| SlideScale | 50 | - | - |
| MoveWhileShootingSpeedPenaltyReductionPercent | 100 | - | - |
| MoveWhileZoomedSpeedPenaltyReductionPercent | 100 | - | - |

**Upgrades**

- **T1** — `MoveSpeedBonus` +2, `BulletResist` +35
- **T2** — `AbilityCooldown` -25
- **T3** — `BonusSpiritPct` +35, `BonusSpirit` +20

#### Arctic Beam

> Shoot freezing cold energy out in front of you, damaging targets and progressively reducing their movement and fire rate the longer you sustain the beam on them. You have reduced move speed while using Arctic Beam. The beam may also claim Souls.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 28 | - | - |
| AbilityDuration | 5 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| ChannelSlowPercent | 8 | - | - |
| DPS | 45 | +0.3800 | 56.9 |
| TickRate | 0.100 | - | - |
| PathLength | 25 | - | - |
| PathWidth | 1.100 | - | - |
| CameraDistance | 250 | - | - |
| MinSlowPercent | 24 | - | - |
| MaxSlowPercent | 16 | - | - |
| MaxFireRateSlowPercent | 20 | - | - |
| MaxGroundDashReductionPercent | -18 | - | - |
| MaxSlowTime | 2 | - | - |
| IceBeamBuildupProcDuration | 2 | - | - |
| SlowDuration | 0.600 | - | - |

**Upgrades**

- **T1** — `MaxSlowPercent` +20, `MaxFireRateSlowPercent` +25
- **T2** — `DPS` +0.600
- **T3** — `BeamSplit` +0.930, `BeamSplitCount` +2, `AbilityCooldown` -13

#### Frozen Shelter (ULTIMATE)

> Target yourself or a Hero to freeze the air and create an impenetrable dome around them. While in the dome, allies gain rapid regeneration and enemies are slowed. Objectives becomes Invulnerable and Frozen under Frozen Shelter

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 185 | - | - |
| AbilityDuration | 5 | - | - |
| AbilityCastRange | 8 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 10 | - | - |
| BlockerScaleFactor | 115 | - | - |
| GrowTime | 0.200 | - | - |
| EnemyDragSpeed | 1000 | - | - |
| BonusHealthRegen | 90 | +0.2000 | 96.2 |
| SlowPercent | 28 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -20
- **T2** — `AbilityDuration` +1.500
- **T3** — `BonusHealthRegen` +1, `PurgeOnCast` +1

---

## Lady Geist

*internal id 4 / `hero_ghost` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 880 | +51 | 2104 | 2665 |
| Health Regen | 1 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.30 m/s |
| Sprint Speed (bonus) | 2.40 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.72 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.51 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_ghost_set`

| stat | value |
|---|---|
| Damage per bullet | 20.70 |
| Bullets per shot | 1 |
| Damage per shot | 20.70 |
| Ammo / clip size | 9 |
| Damage per magazine | 186.30 |
| Cycle time (nominal) | 0.4725 s |
| Cycle time (effective avg) | 0.4725 s |
| Shots / second | 2.116 |
| Shots / second (with reload) | 1.270 |
| Reload duration | 2.58 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 43.81 |
| **DPS (with reload)** | **26.29** |
| Bullet damage per boon | +1 |
| Headshot multiplier | x1.65 |
| Bullet speed | 32600 |
| Falloff: full damage to | 17.0 m |
| Falloff: decays to | 48 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.500 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Essence Bomb

> Sacrifice some of your health to launch a bomb that deals damage after a brief arm time.Self damage type is Spirit and can be mitigated.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 14 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| SelfDamagePct | 30 | - | - |
| Damage | 90 | +1.2200 | 122.2 |
| Radius | 7 | - | - |
| ArmingDuration | 0.650 | - | - |
| BeepSoundIntervalBias | 0.550 | - | - |
| BeepSoundMaxFrequency | 0.100 | - | - |
| BeepSoundBuildupCount | 4 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -5
- **T2** — `Damage` +50, `Radius` +2
- **T3** — `BloodSpillDPSPercent` +30, `BloodSpillDuration` +6

#### Life Drain

> Create a tether that drains enemy health over time and heals you. Target must be in line of sight and within max range to drain. You can shoot and use other abilities during the drain, but your move speed is reduced. to give health to friendly Heroes.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 34 | - | - |
| AbilityDuration | 2.500 | - | - |
| AbilityCastRange | 18 | - | - |
| AbilityUnitTargetLimit | 10 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| MaxRange | 28 | - | - |
| MoveSpeedReduction | 32 | - | - |
| LifeDrainPerSecond | 24 | +0.3225 | 32.5 |
| TickRate | 0.100 | - | - |
| LifeDrainHealthMult | 100 | - | - |

**Upgrades**

- **T1** — `LifeDrainPerSecond` +13
- **T2** — `AbilityDuration` +2.500
- **T3** — `AbilityCharges` +3, `AbilityCooldownBetweenCharge` +0.100, `LifeDrainPerSecond` +0.450

#### Malice

> Sacrifice some of your health to launch blood shards that apply a stack of Malice. Each stack slows the victim and increases the damage they take from you. The slow effect decreases over time.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 6 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.120 | - | - |
| AbilityPostCastDuration | 0.300 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| HealthToDamage | 23 | +0.5580 | 37.7 |
| NumBloodShards | 3 | - | - |
| SpreadAngleDegrees | 6 | - | - |
| MoveSpeedPenaltyPerStack | 12 | - | - |
| VulnerabilityPerStack | 7 | - | - |
| DebuffDuration | 9 | - | - |
| SlowDuration | 4 | - | - |
| MaxStacks | 5 | - | - |
| SelfDamagePct | 9 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -3
- **T2** — `HealthToDamage` +25.200, `NumBloodShards` +4, `SpreadAngleDegrees` +22
- **T3** — `VulnerabilityPerStack` +8

#### Soul Exchange (ULTIMATE)

> Swaps health levels with an enemy target. There is a minimum health percentage that enemies can be brought down to and a minimum amount of health received based on victims current health.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 220 | - | - |
| AbilityDuration | 0.250 | - | - |
| AbilityCastRange | 5.500 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 2 | - | - |
| PostCastHoldTime | 0.200 | - | - |
| InitialUpSpeed | 150 | - | - |
| EnemyMinHealthPct | 30 | - | - |
| MinHealthTakenPct | 30 | - | - |
| MinDiffToCast | 0.100 | - | - |
| EnemySlowPct | 56 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -50
- **T2** — `SilenceDuration` +3, `SilenceRadius` +25
- **T3** — `SelfBuffDuration` +8, `TechResist` +50, `BonusFireRate` +40, `BonusSpirit` +60

---

## Lash

*internal id 31 / `hero_lash` / complexity 3*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 780 | +50 | 1980 | 2530 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7.20 m/s |
| Sprint Speed (bonus) | 2.10 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_lash_set`

| stat | value |
|---|---|
| Damage per bullet | 8.46 |
| Bullets per shot | 1 |
| Damage per shot | 8.46 |
| Ammo / clip size | 29 |
| Damage per magazine | 245.34 |
| Cycle time (nominal) | 0.2625 s |
| Cycle time (effective avg) | 0.1626 s |
| Shots / second | 5.831 |
| Shots / second (with reload) | 3.965 |
| Reload duration | 2.35 s |
| Burst shot count | 3 |
| DPS (sustained, no reload) | 49.33 |
| **DPS (with reload)** | **33.54** |
| Bullet damage per boon | +0.310 |
| Headshot multiplier | x1.65 |
| Bullet speed | 25000 |
| Falloff: full damage to | 16 m |
| Falloff: decays to | 48 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.200 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Ground Strike

> Stomp the ground beneath you, damaging enemies in front of you. If you perform Ground Strike while airborne, you quickly dive towards the ground. Damage grows slower after 25m.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 18 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityPostCastDuration | 0.400 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 10 | - | - |
| StrikeVelocity | 50 | - | - |
| StompDamage | 60 | +0.7905 | 80.9 |
| StompDamagePerMeterPrimary | 5.500 | +0.0400 | 6.6 |
| StompDamagePerMeterSecondary | 4.200 | +0.0081 | 4.4 |
| StompDamagePrimaryRange | 25 | - | - |
| MinAimAngle | 60 | - | - |
| StompVerticalThreshold | 118 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -10
- **T2** — `EnemySlowPct` +40, `SlowDuration` +3, `StompBounceHeight` +400, `TossDuration` +1
- **T3** — `StompDamagePerMeterPrimary` +120, `StompDamagePerMeterSecondary` +120

#### Grapple

> Pull yourself through the air toward a target. Using Grapple also resets your limit of air jumps and dashes.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 35 | - | - |
| AbilityCastRange | 30 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 2 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| JumpVelocity | 20 | - | - |
| LashFriendlies | 1 | - | - |
| JumpSlowResistance | 0.667 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -17
- **T2** — `AbilityCastRange` +20, `WeaponDamageBonus` +7, `WeaponDamageBonusDuration` +6
- **T3** — `AbilityCharges` +1, `RestoreStaminaOnUse` +1, `AirControlPercent` +60

#### Flog

> Strike enemies in front of you with your whip, healing for a portion of the damage dealt.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 26 | - | - |
| AbilityCastRange | 20 | - | - |
| AbilityUnitTargetLimit | 30 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| TargetingConeAngle | 40 | - | - |
| HealPctVsNonHeroes | 16 | - | - |
| HealPctVsHeroes | 40 | - | - |
| Damage | 65 | +0.8500 | 87.4 |

**Upgrades**

- **T1** — `EnemySlowDuration` +3, `EnemySlowPct` +28
- **T2** — `AbilityCooldown` -16, `FireRateSlow` +30
- **T3** — `Damage` +80, `TargetingConeAngle` +25, `HealPctVsHeroes` +15, `HealPctVsNonHeroes` +6

#### Death Slam (ULTIMATE)

> Focus on enemies to connect whips to them. After channeling, connected enemies are lifted and stunned then slammed into the ground. Your victims and any enemies in the landing zone will be damaged and slowed. Press to throw connected enemies early. Enemies that are not in line of sight or go out of range during the latch time will not be grabbed.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| TimeToGainLockonStack | 0.700 | - | - |
| LockonConeAngle | 40 | - | - |
| TimeToLoseLockonStack | 2 | - | - |
| LosingLockGraceTime | 0.400 | - | - |
| MaxLockonStacks | 1 | - | - |
| AbilityCooldown | 170 | - | - |
| AbilityCastRange | 20 | - | - |
| AbilityUnitTargetLimit | 6 | - | - |
| AbilityCastDelay | 0.300 | - | - |
| AbilityChannelTime | 2.300 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| ImpactDamage | 105 | +0.9749 | 130.7 |
| UpBoostSpeed | 400 | - | - |
| LiftHeight | 6 | - | - |
| BoostTime | 1 | - | - |
| HangTime | 0.600 | - | - |
| ThrowDistance | 14 | +0.1400 | 17.7 |
| SlamSpeed | 1600 | - | - |
| ThrowStraightDuration | 1.500 | - | - |
| SlowDuration | 4 | - | - |
| SlowPercent | 40 | - | - |
| ImpactRadius | 6 | - | - |
| NotInConeLosesLock | 1 | - | - |

**Upgrades**

- **T1** — `ThrowDistance` +12
- **T2** — `AbilityCooldown` -35
- **T3** — `StunDuration` +1.200, `AbilityCastRange` +6

---

## McGinnis

*internal id 8 / `hero_forge` / complexity 1*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 780 | +52 | 2028 | 2600 |
| Health Regen | 2 | - | - | - |
| Spirit Resist | 0% | +0.35% | 8.40% | 12.25% |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.70 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 2 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_engineer_set`

| stat | value |
|---|---|
| Damage per bullet | 6.08 |
| Bullets per shot | 1 |
| Damage per shot | 6.08 |
| Ammo / clip size | 66 |
| Damage per magazine | 401.28 |
| Cycle time (nominal) | 0.2100 s |
| Cycle time (effective avg) | 0.2100 s |
| Shots / second | 4.762 |
| Shots / second (with reload) | 3.793 |
| Reload duration | 3.29 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 28.95 |
| **DPS (with reload)** | **23.06** |
| Bullet damage per boon | +0.171 |
| Headshot multiplier | x1.65 |
| Bullet speed | 25590.60 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.450 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Mini Turret

> Deploy a turret that shoots enemies, dealing spirit damage over time. The turret expires after a limited lifetime.Turrets deal reduced damage to troopers and objectives.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 18 | - | - |
| AbilityCastRange | 20 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 3 | - | - |
| ModelScale | 0.800 | - | - |
| TickRate | 0.500 | - | - |
| TrackingSpeed | 430 | - | - |
| AttackConeAngle | 10 | - | - |
| TurretDeployTime | 0.250 | - | - |
| TurretBaseHealth | 100 | +9 | 337.6 |
| TurretAttackRange | 30 | - | - |
| TurretAttackFalloffStart | 20 | - | - |
| TurretAttackFalloffEnd | 30 | - | - |
| TurretAttackDelay | 0.200 | - | - |
| TurretDPS | 24 | +0.4200 | 35.1 |
| TurretLifetime | 35 | - | - |
| AttackSpeedMult | 100 | - | - |
| TechResist | 35 | - | - |
| MeleeResist | 35 | - | - |
| NonHeroDamagePercentOutgoing | 50 | - | - |
| BossDamagePercentOutgoing | 30 | - | - |
| BossDamagePercentIncoming | 50 | - | - |

**Upgrades**

- **T1** — `TurretAttackRange` +10, `TurretDPS` +10
- **T2** — `AbilityCharges` +2
- **T3** — `AttackSpeedMult` +25, `TurretLifetime` +12

#### Medicinal Specter

> Deploy a spirit that provides healing to nearby allies.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 50 | - | - |
| AbilityDuration | 6.500 | - | - |
| AbilityCastRange | 15 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| HealRadius | 6 | - | - |
| ExternalBonusHealthRegen | 25 | +0.3000 | 32.9 |
| TurretHealMult | 1 | - | - |
| HealInterval | 0.100 | - | - |

**Upgrades**

- **T1** — `AbilityDuration` +1.500
- **T2** — `AbilityCooldown` -20, `StaminaCooldownReduction` +100
- **T3** — `MaxHealthRegenPct` +2, `HealRadius` +3, `SpiritResist` +40

#### Spectral Wall

> Cast a wall that applies slow on enemies it passes through. Erupt the wall to divide the terrain in half and damage nearby enemies. After casting, press or Ability 3 to erupt the wall early. Can be Destroyed with Melee Attacks

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 50 | - | - |
| AbilityDuration | 6 | - | - |
| AbilityCastRange | 50 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| MinRange | 5 | - | - |
| WallImpactRange | 5 | - | - |
| PushForce | 175 | - | - |
| Damage | 60 | +0.7312 | 79.3 |
| NumWallSegments | 8 | - | - |
| TimeBetweenSegments | 0.035 | - | - |
| SegmentEmitTime | 0.100 | - | - |
| TimeToMaxDistance | 1.800 | - | - |
| SlowDuration | 2.500 | - | - |
| SlowPercent | 16 | - | - |

**Upgrades**

- **T1** — `BonusDamagePercent` +20, `DebuffDuration` +7
- **T2** — `AbilityCooldown` -20, `AbilityDuration` +2
- **T3** — `CreateTurrets` +2, `TurretLifeTime` +8, `SlowPercent` +24

#### Heavy Barrage (ULTIMATE)

> Unleashes a volley of rockets that home in on a targeted location. McGinnis is slowed and is still able to use stamina.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 200 | - | - |
| AbilityDuration | 8 | - | - |
| AbilityCastRange | 36 | - | - |
| AbilityUnitTargetLimit | 100 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DamagePerRocket | 21 | +0.2000 | 26.3 |
| GrenadesPerSecond | 6 | - | - |
| IntervalRampUpTime | 0.300 | - | - |
| IntervalRampUpStart | 0.350 | - | - |
| DetonateTimer | 5 | - | - |
| ExplosionFalloffDisabled | 1 | - | - |
| ExplosionRadius | 4.500 | - | - |
| TrackSpeedNear | 150 | - | - |
| TrackSpeedFar | 100 | - | - |
| TrackingTime | 0.400 | - | - |
| MinDistance | 8.500 | - | - |
| MaxSpread | 5 | - | - |
| ProjectileIgnoreCollisionTime | 0.200 | - | - |
| GroundDashReductionPercent | -35 | - | - |

**Upgrades**

- **T1** — `MoveSlowPercent` +24, `EnemyDashSlowPercent` -16, `MoveSlowDuration` +1
- **T2** — `AbilityCooldown` -45, `AbilityDuration` +6
- **T3** — `DamagePerRocket` +0.160, `ExplosionRadius` +2

---

## Mina

*internal id 63 / `hero_vampirebat` / complexity 3*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 660 | +27 | 1308 | 1605 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.50 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 2 |
| Stamina Regen | 0.24/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.62 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.43 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_vampirebat_set`

| stat | value |
|---|---|
| Damage per bullet | 7.31 |
| Bullets per shot | 1 |
| Damage per shot | 7.31 |
| Ammo / clip size | 12 |
| Damage per magazine | 87.72 |
| Cycle time (nominal) | 0.2520 s |
| Cycle time (effective avg) | 0.2520 s |
| Shots / second | 3.968 |
| Shots / second (with reload) | 2.413 |
| Reload duration | 1.70 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 29.01 |
| **DPS (with reload)** | **17.64** |
| Bullet damage per boon | +0.275 |
| Headshot multiplier | x1.65 |
| Bullet speed | 30000 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 46.0 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.300 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Rake

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 16 | - | - |
| AbilityCastRange | 10 | - | - |
| AbilityUnitTargetLimit | 6 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityPostCastDuration | 0.400 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 60 | +1 | 86.4 |
| TargetingConeAngle | 60 | - | - |
| TimeBetweenAttacks | 0.040 | - | - |
| MissingHealthDamagePercentage | 6 | - | - |
| MiniJumpVelocity | 200 | - | - |
| RakeHealPerKill | 25 | +0.3000 | 32.9 |
| TrooperExecuteThreshold | 60 | - | - |
| FallSpeedMax | 3 | - | - |
| AirDrag | 0.200 | - | - |
| FallingDrag | 20 | - | - |
| MaxFloatTime | 4 | - | - |

**Upgrades**

- **T1** — `Damage` +60
- **T2** — `RakeHealPerKill` +30, `AbilityCooldown` -8
- **T3** — `MissingHealthDamagePercentage` +7, `RakeHealPerKill` +1.200

#### Sanguine Retreat

> Briefly disperse, becoming untargetable and flying to a target location. Can be recast within a brief window.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 32 | - | - |
| AbilityDuration | 0.650 | - | - |
| AbilityCastRange | 9 | +0.0200 | 9.5 |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| MaxRecasts | 1 | - | - |
| RecastWindow | 4 | - | - |
| ExitVelocity | 5 | - | - |
| EndJumpVelocity | 200 | - | - |

**Upgrades**

- **T1** — `BonusFireRate` +25, `BuffDuration` +8, `BonusBullets` +8
- **T2** — `AbilityCooldown` -10
- **T3** — `MaxRecasts` +1, `AbilityCastRange` +4

#### Love Bites

> Your bullets apply additional spirit damage. Dealing damage your abilities builds up to a vicious bite, dealing a burst of bonus spirit damage. Love Bites has a unique cooldown per target.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| MagicDamagePerBullet | 4 | +0.0900 | 6.4 |
| PerTargetCooldown | 10 | - | - |
| BuildUpPerShot | 18.400 | - | - |
| BuildUpDuration | 5 | - | - |
| BonusDamage | 45 | +1.8500 | 93.8 |
| BuildUpPerBat | 20 | - | - |
| BuildUpPerDagger | 30 | - | - |
| BuildUpHeadshotBonus | 1.500 | - | - |
| EffectivenessVolumeScaleMin | 0.500 | - | - |
| EffectivenessVolumeScaleMax | 1 | - | - |

**Upgrades**

- **T1** — `SlowDuration` +3, `SlowPercent` +24
- **T2** — `MagicDamagePerBullet` +3, `BonusDamage` +45
- **T3** — `PerTargetCooldown` -5, `BonusFireRate` +25, `BuffDuration` +5

#### Nox Nostra (ULTIMATE)

> Active: Unleash a cloud of bats that seek out targets, each dealing spirit damage and applying Silence.Passive: Triggering Love Bites against heroes permanently increases the number of bats released.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| TimeToGainLockonStack | 0.010 | - | - |
| LockonConeAngle | 40 | - | - |
| TimeToLoseLockonStack | 0.300 | - | - |
| MaxLockonStacks | 1 | - | - |
| StacksCanDecay | 1 | - | - |
| AbilityCooldown | 150 | - | - |
| AbilityCastRange | 40 | - | - |
| AbilityUnitTargetLimit | 12 | - | - |
| AbilityCastDelay | 0.500 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| BatSpawnRadius | 1.500 | - | - |
| FallSpeedMax | 1 | - | - |
| BatSpawnRandomVelocity | 300 | - | - |
| AirDrag | 12 | - | - |
| Damage | 4.600 | +0.0940 | 7.1 |
| JumpPitch | -60 | - | - |
| JumpSpeed | 17 | - | - |
| BatCount | 75 | - | - |
| DebuffDuration | 1.250 | - | - |
| BatSpawnRandomAngle | 0.150 | - | - |
| BatCountPerWave | 1 | - | - |
| BonusBatsMax | 50 | - | - |
| BonusBatsPerProc | 2 | - | - |
| CurrentHealthDamageCapToBosses | 20 | - | - |
| BatPerSecond | 30 | - | - |
| JumpCeilingCheckDistance | 11 | - | - |
| NotInConeLosesLock | 1 | - | - |
| TargetingConeAngle | 20 | - | - |
| GroundAccelerationPercentage | -80 | - | - |
| GroundFrictioNpercentage | -80 | - | - |
| VerticalDrag | 1 | - | - |
| BatEffectiveness | 0.200 | - | - |
| MaxBatTargets | 2 | - | - |

**Upgrades**

- **T1** — `Damage` +1.900
- **T2** — `AbilityCooldown` -45
- **T3** — `CurrentHealthPercent` +0.500

---

## Mirage

*internal id 52 / `hero_mirage` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 730 | +45 | 1810 | 2305 |
| Health Regen | 1.50 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_mirage_set`

| stat | value |
|---|---|
| Damage per bullet | 14.80 |
| Bullets per shot | 1 |
| Damage per shot | 14.80 |
| Ammo / clip size | 16 |
| Damage per magazine | 236.80 |
| Cycle time (nominal) | 0.3675 s |
| Cycle time (effective avg) | 0.3675 s |
| Shots / second | 2.721 |
| Shots / second (with reload) | 1.833 |
| Reload duration | 2.60 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 40.27 |
| **DPS (with reload)** | **27.12** |
| Bullet damage per boon | +0.300 |
| Headshot multiplier | x1.65 |
| Bullet speed | 32600 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.500 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Fire Scarabs

> Infest an enemy with fire scarabs, stealing life from them and causing them to deal reduced damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 35 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.050 | - | - |
| AbilityCharges | 2 | - | - |
| AbilityCooldownBetweenCharge | 1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| OutgoingDamagePenaltyPercent | -20 | - | - |
| DPS | 8 | +0.1000 | 10.6 |
| StealDuration | 5 | - | - |
| MaxStacks | 100 | - | - |

**Upgrades**

- **T1** — `DPS` +7
- **T2** — `AbilityCharges` +1, `StealDuration` +2
- **T3** — `OutgoingDamagePenaltyPercent` -15, `DPS` +0.130

#### Dust Devil

> Transform yourself into a whirlwind that travels forward, damaging enemies, slowing their move speed and lifting them up in the air. After emerging from the tornado you gain bullet evasion.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 36 | - | - |
| AbilityCastRange | 20 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 4 | - | - |
| OpenHeight | 8 | - | - |
| Damage | 65 | +0.3000 | 72.9 |
| TickRate | 0.250 | - | - |
| ProjectileThinkInterval | 0.010 | - | - |
| DistanceAboveGround | 0.500 | - | - |
| ClimbHeight | 1 | - | - |
| DropDownRate | 10 | - | - |
| TornadoSpeed | 24 | - | - |
| EnemyLiftDuration | 0.200 | - | - |
| LiftHeight | 3 | - | - |
| DampingFactor | 0.100 | - | - |
| MaxDeltaMovementControl | 2 | - | - |
| HoldInPlaceDuration | 0.300 | - | - |
| WhirlwindEvasionChance | 30 | - | - |
| WhirlwindDuration | 4 | - | - |
| SlowDuration | 3 | - | - |
| SlowPercent | 24 | - | - |

**Upgrades**

- **T1** — `Damage` +60
- **T2** — `AbilityCooldown` -12, `WhirlwindEvasionChance` +30
- **T3** — `RecastWindow` +6, `Damage` +0.600

#### Djinn's Mark

> Active: Consume all Djinn Mark's to deal its damage now.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 2.750 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| ProcCooldown | 2.750 | - | - |
| ProcDamageBase | 11 | +0.3500 | 20.2 |
| ProcChance | 100 | - | - |
| ProcMaxRange | 40 | - | - |
| VictimStackDuration | 5 | - | - |
| RevealDuration | 6 | - | - |
| MaxStacks | 4 | - | - |
| DMarkMultiplierPerStack | 2 | - | - |

**Upgrades**

- **T1** — `MovementSpeedSlow` +48, `SlowDuration` +0.800
- **T2** — `ProcDamageBase` +20, `VictimStackDuration` +3
- **T3** — `AbilityCooldown` -0.750, `ProcCooldown` -0.750, `StunDuration` +0.500, `MaxStacks` +1

#### Traveler (ULTIMATE)

> Target a location on the minimap. After a brief wait, teleport to that location. Taking damage during the wait period causes the teleport to be interrupted.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 140 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| TeleportCompletedTime | 2 | - | - |
| InterruptCooldown | 4 | - | - |
| SearchRadius | 30 | - | - |

**Upgrades**

- **T1** — `BonusMoveSpeed` +3, `BonusFireRate` +20, `MovementSpeedBonusDuration` +12
- **T2** — `CombatBarrier` +0.600
- **T3** — `AbilityCooldown` -90

---

## Mo & Krill

*internal id 18 / `hero_krill` / complexity 3*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 930 | +65 | 2490 | 3205 |
| Health Regen | 1 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 8 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.72 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.51 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_digger_set`

| stat | value |
|---|---|
| Damage per bullet | 2.82 |
| Bullets per shot | 4 |
| Damage per shot | 11.28 |
| Ammo / clip size | 20 |
| Damage per magazine | 225.60 |
| Cycle time (nominal) | 0.1890 s |
| Cycle time (effective avg) | 0.1890 s |
| Shots / second | 5.291 |
| Shots / second (with reload) | 2.920 |
| Reload duration | 2.82 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 59.68 |
| **DPS (with reload)** | **32.93** |
| Bullet damage per boon | +0.085 |
| Headshot multiplier | x1.65 |
| Bullet speed | 12600 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.500 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Scorn

> Deal damage to nearby enemies and heal yourself based on the damage done. Heal is stronger against enemy heroes.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 13 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| Radius | 9 | - | - |
| Damage | 50 | +0.7500 | 69.8 |
| DamageHealMultNonHero | 0.350 | - | - |
| DamageHealMult | 1.200 | - | - |
| TickRate | 0.100 | - | - |

**Upgrades**

- **T1** — `Damage` +35
- **T2** — `AbilityCooldown` -5, `Radius` +1
- **T3** — `DamageBonus` +15, `DebuffDuration` +16

#### Burrow

> Burrow underground, moving faster, and gaining spirit and bullet armor. Damage from enemy heroes will reduce the speed bonus. When you jump out, deal spirit damage, slow, and knockup.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 40 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 1 | - | - |
| AbilityChannelTime | 5 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DPS | 75 | +1.4880 | 114.3 |
| Radius | 5 | - | - |
| BonusMoveSpeed | 5 | - | - |
| SpeedLostDuration | 1 | - | - |
| EnemyDamageSpeedPenalty | 0.500 | - | - |
| SpinDuration | 1.500 | - | - |
| SpinSlowPercent | 8 | - | - |
| SpinSlowDuration | 0.300 | - | - |
| TechResist | 30 | - | - |
| BulletResist | 60 | - | - |
| TickRate | 0.100 | - | - |
| UpForce | 250 | - | - |
| TossDuration | 1 | - | - |

**Upgrades**

- **T1** — `DPS` +50
- **T2** — `AbilityChannelTime` +4, `Radius` +2
- **T3** — `AbilityCooldown` -20, `BonusMoveSpeed` +4

#### Sand Blast

> Spray sand that disarms enemies in front of you and deals damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 40 | - | - |
| AbilityDuration | 2.500 | - | - |
| AbilityCastRange | 25 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| GrowthPerMeter | 0.500 | - | - |
| InitialWidth | 5 | - | - |
| HeightOffGround | 20 | - | - |
| Damage | 40 | - | - |

**Upgrades**

- **T1** — `Damage` +50, `AbilityCastRange` +5
- **T2** — `SlowPercent` +24, `GroundDashReductionPercent` -26
- **T3** — `AbilityCooldown` -25, `AbilityDuration` +1.500

#### Combo (ULTIMATE)

> Hold the target in place, stunning them and dealing damage during the channel. If they die during, or within 3 seconds of Combo ending, you permanently gain max health.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 150 | - | - |
| AbilityCastRange | 4 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 2.400 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| DPS | 40 | +0.6000 | 55.8 |
| BonusHealthOnKill | 40 | +2 | 92.8 |

**Upgrades**

- **T1** — `LifeStealPercentOnHit` +100
- **T2** — `AbilityCooldown` -30, `BulletResist` +50
- **T3** — `AbilityChannelTime` +0.700, `DPS` +0.400

---

## Paige

*internal id 67 / `hero_bookworm` / complexity 1*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 680 | +31 | 1424 | 1765 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.90 m/s |
| Sprint Speed (bonus) | 3.50 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.72 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.51 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 42 | +1.20 | 84 |
| Heavy Melee | 120 | - | - |

### Weapon

`citadel_weapon_bookworm_set2`

| stat | value |
|---|---|
| Damage per bullet | 35 |
| Bullets per shot | 1 |
| Damage per shot | 35 |
| Ammo / clip size | 14 |
| Damage per magazine | 490 |
| Cycle time (nominal) | 0.5000 s |
| Cycle time (effective avg) | 0.5929 s |
| Shots / second | 1.667 |
| Shots / second (with reload) | 1.267 |
| Reload duration | 2.50 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 58.33 |
| **DPS (with reload)** | **44.34** |
| Bullet damage per boon | +0.520 |
| Headshot multiplier | x1.65 |
| Bullet speed | 1710 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 1 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Bookwyrm

> Conjure a dragon that appears at the target location before flying forward, dealing spirit damage and leaving a burning path in its trail.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 33 | - | - |
| AbilityDuration | 5 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 7 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DPS | 30 | +0.3000 | 37.9 |
| TickRate | 0.300 | - | - |
| StartupDelay | 0.300 | - | - |
| DebuffDuration | 1.500 | - | - |
| DragonSearchRadius | 8.500 | - | - |
| DragonConeRange | 5 | - | - |
| DragonUpwardSpeed | 400 | - | - |
| GroundFlameDuration | 3 | - | - |
| Damage | 60 | +1.3000 | 94.3 |
| Radius | 4 | - | - |
| DragonSearchTickRate | 0.100 | - | - |
| GroundAuraSpacing | 2 | - | - |
| AuraLingerDuration | 0.100 | - | - |
| DragonTravelRange | 20 | - | - |
| DragonRangePerSecond | 500 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -12
- **T2** — `GroundFlameDuration` +2, `Radius` +1, `AbilityCharges` +1
- **T3** — `Damage` +100, `DPS` +30, `DragonTravelRange` +12

#### Plot Armor

> Grant an ally a barrier. While the barrier holds, they gain bonus weapon damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 28 | - | - |
| AbilityDuration | 5 | - | - |
| AbilityCastRange | 35 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| CombatBarrier | 125 | +1.5000 | 164.6 |
| PushForce | 900 | - | - |
| BaseAttackDamagePercent | 25 | +0.3000 | 32.9 |
| ShoveRadius | 6 | - | - |
| BonusTargetRadius | 30 | - | - |
| BonusSpiritDamagePercent | 15 | - | - |

**Upgrades**

- **T1** — `BonusFireRate` +0.160
- **T2** — `CombatBarrier` +100, `AbilityDuration` +2
- **T3** — `CombatBarrier` +0.500, `BonusTargets` +2, `BonusTargetsBarrierPercentage` +100

#### Captivating Read

> Target an area with latent magic, applying slow. The magic detonates after a delay, dealing spirit damage and applying immobilize.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 30 | - | - |
| AbilityCastRange | 30 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 90 | +1.3000 | 124.3 |
| Radius | 7.500 | - | - |
| DetonationDelay | 1.250 | - | - |
| ImmobilizeDuration | 1 | - | - |
| SlowDuration | 0.500 | - | - |
| SlowPercent | 36 | - | - |
| Height | 8 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -14
- **T2** — `ImmobilizeDuration` +1
- **T3** — `TechArmorDamageReduction` -18, `DebuffDuration` +6, `Radius` +2

#### Rallying Charge (ULTIMATE)

> Release a wave of spectral knights and steeds that charge across the entire city, healing allies and dealing spirit damage to enemies. The strength of the heal and spirit damage is amplified as the knights travel further.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 210 | - | - |
| AbilityDuration | 13 | - | - |
| AbilityCastRange | 600 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 0.700 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| Damage | 125 | +1 | 151.4 |
| GroundStickHeight | 0.050 | - | - |
| TossUpSpeed | 600 | - | - |
| KnightChargeWidth | 1.700 | - | - |
| KnightCount | 5 | - | - |
| KnightPositionSpread | 1.800 | - | - |
| BonusMoveSpeed | 5 | - | - |
| BuffDuration | 9 | - | - |
| AllyRadius | 4 | - | - |
| AllyHeight | 20 | - | - |
| KnightWhiskerLength | 300 | - | - |
| KnightWhiskerSide | 50 | - | - |
| KnightWhiskerStrength | 0.200 | - | - |
| TossBackSpeed | 100 | - | - |
| KnightPositionStagger | -4 | - | - |
| StunDuration | 1 | - | - |
| HealAmount | 125 | +1.6000 | 167.2 |
| KnightNavSearchDistance | 10 | - | - |
| KnightChargeHeight | 3.500 | - | - |
| GravityAcceleration | -1900 | - | - |
| KnightMaxJumpHeight | 30 | - | - |
| KnightMaxFallHeight | -35 | - | - |
| KnightNavForwardDistance | 8 | - | - |
| KnightJumpSpeed | 900 | - | - |
| AirDrag | 0.800 | - | - |
| FallSpeedMax | 20 | - | - |
| WaveCount | 2 | - | - |
| WavePositionStagger | -15 | - | - |
| KnightBonusPerWave | -99 | - | - |
| KnightCountInFirstWave | 5 | - | - |
| CancelCooldownRefundPercentage | 50 | - | - |
| TargetFindingDelay | 0.040 | - | - |
| MaxAmp | 100 | - | - |
| MaxAmpDistance | 250 | - | - |

**Upgrades**

- **T1** — `HealAmount` +150
- **T2** — `KnightCount` +4, `KnightCountInFirstWave` +4, `AbilityCooldown` -45
- **T3** — `Damage` +160, `StunDuration` +0.500, `MaxAmp` +70

---

## Paradox

*internal id 10 / `hero_chrono` / complexity 3*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 730 | +46 | 1834 | 2340 |
| Health Regen | 1 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.70 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.62 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.43 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_chrono_set`

| stat | value |
|---|---|
| Damage per bullet | 6.80 |
| Bullets per shot | 1 |
| Damage per shot | 6.80 |
| Ammo / clip size | 40 |
| Damage per magazine | 272 |
| Cycle time (nominal) | 0.2940 s |
| Cycle time (effective avg) | 0.1305 s |
| Shots / second | 7.559 |
| Shots / second (with reload) | 4.967 |
| Reload duration | 2.58 s |
| Burst shot count | 5 |
| DPS (sustained, no reload) | 51.40 |
| **DPS (with reload)** | **33.77** |
| Bullet damage per boon | +0.260 |
| Headshot multiplier | x1.65 |
| Bullet speed | 20669.30 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Pulse Grenade

> Throw a grenade that begins pulsing when it lands. Each pulse expands the radius and applies spirit damage, time slow, and stacking increased damage for Paradox against the victim.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 32 | - | - |
| AbilityDuration | 3.200 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 5.500 | - | - |
| RadiusIncreasePerPulse | 1 | - | - |
| PulseInterval | 0.800 | - | - |
| PulseDamage | 35 | +0.3000 | 42.9 |
| DamageAmplificationPerStack | 4 | - | - |
| DebuffDuration | 8 | - | - |
| SlowPercent | 20 | - | - |
| MovementSlowDuration | 0.200 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -12
- **T2** — `PulseDamage` +0.500
- **T3** — `DamageAmplificationPerStack` +4, `AbilityDuration` +1.600

#### Time Wall

> Create a time warping wall that stops time for all enemy projectiles and bullets that touch it and increases the speed and damage of friendly bullets. Enemies that touch the wall will be briefly slowed and silenced .

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 25 | - | - |
| AbilityDuration | 5.500 | - | - |
| AbilityCastRange | 200 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| TimeWallWidth | 8 | - | - |
| TimeWallHeight | 4 | - | - |
| TimeWallDepth | 0.500 | - | - |
| TimeWallDepthVisualScale | 0.160 | - | - |
| TimeWallTimeScale | 0.000 | - | - |
| TimeScaleDuration | 0.500 | - | - |
| TimeWallTimeScaleFriendly | 2 | - | - |
| FriendlyBulletDamageBonus | 30 | - | - |
| MovementSlowPct | 64 | - | - |
| AuraEffectDuration | 2 | - | - |
| TimeWallFormationTime | 0.500 | - | - |

**Upgrades**

- **T1** — `TimeWallWidth` +3, `TimeWallHeight` +1, `AbilityDuration` +3.500
- **T2** — `FriendlyBulletDamageBonus` +35, `DebuffDuration` +2.300
- **T3** — `AbilityCharges` +3, `AbilityCooldownBetweenCharge` +2

#### Kinetic Carbine

> Charge up a powerful shot of time energy, dealing spirit damage and applying a Time-Stop to enemies hit. The damage dealt increases with weapon damage. Move speed is increased while charging. While in the air and charging, to timeslow your movement.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 28 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| SpeedChange | 25 | +0.1300 | 28.4 |
| SpeedBoostDuration | 3.500 | - | - |
| MinBonusBulletDamage | 5 | +10 | 269 |
| MaxBonusBulletDamage | 5 | +125 | 3305 |
| HeadshotBonus | 14 | - | - |
| MaxSlowDuration | 0.400 | - | - |
| BulletTimeScale | 0.010 | - | - |
| ProjectileTimeScale | 0.010 | - | - |
| TimeWarpRadius | 5 | - | - |
| BonusBulletSpeed | 100 | - | - |
| ShotCount | 1 | - | - |
| MaxChargeDuration | 2.500 | - | - |
| BulletRadiusOverride | 16 | - | - |
| MoveSpeedWhileShootingPenaltyReduction | 100 | - | - |
| MinSlowDuration | 0.250 | - | - |
| TimeScaleDebuff | 90 | - | - |
| AirMoveIncreasePercent | 20 | - | - |

**Upgrades**

- **T1** — `MaxSlowDuration` +0.400
- **T2** — `AbilityCooldown` -12, `SpeedChange` +0.060
- **T3** — `SpeedBoostDuration` +2, `MaxBonusBulletDamage` +55

#### Paradoxical Swap (ULTIMATE)

> Fire a projectile that swaps your position with the target enemy hero.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 110 | - | - |
| AbilityCastRange | 25 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| InitialFreezeTime | 0.250 | - | - |
| MinSwapTime | 0.600 | - | - |
| SwapTime | 1 | - | - |
| DistanceToMaxTime | 30 | - | - |
| SwapDamage | 150 | +1.1000 | 179.0 |
| InitialHeight | 350 | - | - |
| TickRate | 0.250 | - | - |

**Upgrades**

- **T1** — `CombatBarrier` +1.500, `BarrierDuration` +8
- **T2** — `AbilityCastRange` +13, `AbilityCooldown` -30
- **T3** — `MultiSwap` +7, `MaxHealthDamage` +10

---

## Pocket

*internal id 50 / `hero_synth` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 780 | +36 | 1644 | 2040 |
| Health Regen | 1 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7.20 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 60 | +1.58 | 115.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_synth_set`

| stat | value |
|---|---|
| Damage per bullet | 4.28 |
| Bullets per shot | 7 |
| Damage per shot | 29.96 |
| Ammo / clip size | 11 |
| Damage per magazine | 329.56 |
| Cycle time (nominal) | 0.5250 s |
| Cycle time (effective avg) | 0.5250 s |
| Shots / second | 1.905 |
| Shots / second (with reload) | 1.244 |
| Reload duration | 2.82 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 57.07 |
| **DPS (with reload)** | **37.26** |
| Bullet damage per boon | +0.140 |
| Headshot multiplier | x1.65 |
| Bullet speed | 22000 |
| Falloff: full damage to | 16.0 m |
| Falloff: decays to | 45.7 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.200 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Barrage

> Channel to start launching projectiles that deal spirit damage and apply slow around their impact point. Projectiles that hit a hero grant Pocket increased damage that stacks.Casting while airborne will cause Pocket to float.Casting AirDash or Flying Cloaking will not cancel Barrage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 32 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.300 | - | - |
| AbilityChannelTime | 2 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| DamagePerProjectile | 32 | +0.4650 | 44.3 |
| ProjectileAmount | 4 | - | - |
| FallSpeedMax | 10 | - | - |
| AirSpeedMax | 100 | - | - |
| AirDrag | 0.300 | - | - |
| Radius | 4.500 | - | - |
| MoveSlowPercent | 24 | - | - |
| SlowDuration | 1.500 | - | - |
| AmpPercentPerStack | 6 | - | - |
| AmpDuration | 15 | - | - |

**Upgrades**

- **T1** — `DamagePerProjectile` +16
- **T2** — `AbilityCooldown` -16
- **T3** — `AmpPercentPerStack` +4, `Radius` +3

#### Flying Cloak

> Launch a sentient cloak that travels forward and damages enemies. You can press Ability 2 to teleport to its location.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 25 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 5 | - | - |
| Damage | 60 | +1.3000 | 94.3 |
| TickRate | 0.100 | - | - |
| MaxLifetime | 3.800 | - | - |

**Upgrades**

- **T1** — `Damage` +70
- **T2** — `WeaponDamageBonus` +5, `WeaponDamageBonusDuration` +6
- **T3** — `MaxLifetime` +1.600, `AbilityCooldown` -10

#### Enchanter's Satchel

> Escape into your suitcase. When the duration ends, deal spirit damage to nearby enemies. Duration can be ended early by performing any action.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 17 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityChannelTime | 1.500 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| Radius | 12 | - | - |
| Damage | 65 | +1.1000 | 94.0 |
| FallSpeedMax | 1 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -5
- **T2** — `Damage` +90
- **T3** — `FireRateSlow` +40, `MoveSlowPercent` +32, `DebuffDuration` +4, `AbilityChannelTime` +1.500, `Radius` +4

#### Affliction (ULTIMATE)

> Applies damage over time to enemies nearby.Affliction's damage is non-lethal and does not apply item procs.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 170 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.600 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| Radius | 9 | - | - |
| DPS | 32 | +0.2100 | 37.5 |
| DamageInterval | 0.500 | - | - |
| DebuffDuration | 10 | - | - |
| CanBePurged | 1 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -35
- **T2** — `DebuffDuration` +3, `Radius` +4
- **T3** — `DPS` +0.100, `DisableHealing` +1

---

## Rem

*internal id 79 / `hero_familiar` / complexity 3*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 680 | +28 | 1352 | 1660 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7.20 m/s |
| Sprint Speed (bonus) | 4 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.72 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.51 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 58 | +1.58 | 113.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`ability_familiar_primary_weapon_bubblegun`

| stat | value |
|---|---|
| Damage per bullet | 16 |
| Bullets per shot | 1 |
| Damage per shot | 16 |
| Ammo / clip size | 13 |
| Damage per magazine | 208 |
| Cycle time (nominal) | 0.2600 s |
| Cycle time (effective avg) | 0.2600 s |
| Shots / second | 3.846 |
| Shots / second (with reload) | 2.309 |
| Reload duration | 2 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 61.54 |
| **DPS (with reload)** | **36.94** |
| Bullet damage per boon | +0.340 |
| Headshot multiplier | x1.65 |
| Bullet speed | 6300 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 76.2 m |
| Move speed while shooting | 85% |
| Spread penalty per shot | 0 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Pillow Toss

> Throw your trusty pillow inflicting spirit damage and heavy knockback.Landing hits reduces the cooldown of your other abilities.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 25 | - | - |
| AbilityCastRange | 40 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.300 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 8 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| OrbsToFire | 1 | - | - |
| Damage | 75 | +1.6000 | 117.2 |
| Radius | 5 | - | - |
| EffectDuration | 3 | - | - |
| FadingSlowPercent | 36 | - | - |
| TossDuration | 0.400 | - | - |
| TossForce | 300 | - | - |
| CDReduceOnPillowHit | 5 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -7
- **T2** — `FireRateSlow` +35, `Radius` +2
- **T3** — `Damage` +100, `AbilityCharges` +1

#### Tag Along

> Jump to an ally and nap alongside them. Both you and the ally receive a burst heal based on missing health followed by lingering regeneration.Hop between allies with Ability 2 to apply the heal, once per ally.You are knocked off if stunned by an ultimate ability.You can use items and all self-casts target your ally instead.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 40 | - | - |
| AbilityDuration | 5.500 | - | - |
| AbilityCastRange | 23 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.500 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 5 | - | - |
| BonusMoveSpeed | 4 | - | - |
| HopOutLockoutDuration | 0.300 | - | - |
| HealthRegenDuration | 2 | - | - |
| HealingPerSecond | 42 | +0.4000 | 52.6 |
| MissingHealthBurstPct | 15 | +0.0300 | 15.8 |

**Upgrades**

- **T1** — `AbilityCooldown` -8
- **T2** — `BonusBarrierAmpPercent` +35, `BonusItemDurationPercent` +35, `BonusItemRangePercent` +35
- **T3** — `TechPowerPercent` +15, `BonusSpiritPower` +35, `HopOffEffecDuration` +10, `MissingHealthBurstPct` +0.016, `HealingPerSecond` +0.340

#### Lil Helpers

> Signal a Helper to lend a hand. They can collect boxes, do Sinner's Sacrifices, or be sent to support allies and troopers.Follow a hero: Provides a short burst of spirit resist and fading move speed.Follow a trooper: Provides healing, damage, resists, and allows tagging along. When no hero is around, souls from trooper kills are split amongst the team.Can be cast during Tag Along. Helpers will take a nap for 15.1s after following someone.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCastRange | 45 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| HelperDowntimeDuration | 15.100 | - | - |
| HelperChoreCooldownDuration | 5 | - | - |
| AuraRadius | 10 | - | - |
| AuraSoftRadius | 10 | - | - |
| AuraAttackHeight | 10 | - | - |
| DPSPerSprite | 1 | - | - |
| TickRate | 0.200 | - | - |
| Damage | 20 | - | - |
| BonusMoveSpeed | 3 | - | - |
| ArmTime | 0.100 | - | - |
| PatrolDamageCooldown | 10 | - | - |
| HelpersPerPatrol | 4 | - | - |
| HelperCount | 1 | - | - |
| InfestHeal | 8 | +0.1400 | 11.7 |
| InfestHealInterval | 2 | - | - |
| InfestDamageTakenPercent | 30 | - | - |
| InfestBurstHealthPercent | 75 | - | - |
| TechArmorGain | 12 | - | - |
| PlayerInfestDuration | 8 | - | - |
| NPCInfestDuration | 50 | - | - |

**Upgrades**

- **T1** — `HelperCount` +1, `BonusMoveSpeed` +1.500
- **T2** — `HelperCount` +1, `InfestDamageTakenPercent` +15
- **T3** — `HelperCount` +1, `TechArmorGain` +15

#### Naptime (ULTIMATE)

> Cast your gaze forward, piercing walls and floors. Enemies in the gaze are slowed, have reduced dash distance, and cannot use movement abilities.When the channel ends they fall asleep before waking up to a splitting headache that deals heavy spirit damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 200 | - | - |
| AbilityCastRange | 24 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.180 | - | - |
| AbilityChannelTime | 1.900 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| SleepDuration | 4 | - | - |
| Radius | 19 | - | - |
| MinSleepTime | 0.500 | - | - |
| SleepDamageThreshold | 100 | +3.1000 | 181.8 |
| SleepMoveSpeed | 1.500 | - | - |
| AwakeDamage | 120 | +1.6000 | 162.2 |
| Height | 20 | - | - |
| MoveSpeedAndDashSlowPct | 20 | - | - |
| DamageResistPctWhileChanneling | 30 | - | - |

**Upgrades**

- **T1** — `ConsumeStaminaOnWake` +1, `NoStaminaRegenDuringSleep` +1
- **T2** — `SleepDuration` +0.750, `Radius` +3
- **T3** — `DamageResistPctWhileChanneling` +50, `UnstoppableWhileChanneling` +1, `AbilityCooldown` -55

---

## Seven

*internal id 2 / `hero_gigawatt` / complexity 1*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 730 | +41 | 1714 | 2165 |
| Health Regen | 1 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.70 m/s |
| Sprint Speed (bonus) | 1.80 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_gigawatt_set`

| stat | value |
|---|---|
| Damage per bullet | 10.80 |
| Bullets per shot | 1 |
| Damage per shot | 10.80 |
| Ammo / clip size | 29 |
| Damage per magazine | 313.20 |
| Cycle time (nominal) | 0.2625 s |
| Cycle time (effective avg) | 0.1626 s |
| Shots / second | 5.831 |
| Shots / second (with reload) | 3.965 |
| Reload duration | 2.35 s |
| Burst shot count | 3 |
| DPS (sustained, no reload) | 62.97 |
| **DPS (with reload)** | **42.82** |
| Bullet damage per boon | +0.240 |
| Headshot multiplier | x1.65 |
| Bullet speed | 25000 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.200 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Lightning Ball

> Shoot a ball of lightning that travels in a straight line. Does damage to all targets in its radius. Slows down when damaging enemies and stops if it hits the world.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 26 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 6 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| ShockRadius | 4.250 | - | - |
| DPS | 75 | +0.5000 | 88.2 |
| TickRate | 0.100 | - | - |
| MinShockDuration | 0.500 | - | - |
| MaxLifetime | 5 | - | - |

**Upgrades**

- **T1** — `AbilityCharges` +1
- **T2** — `SlowPercent` +28, `MaxLifetime` +1
- **T3** — `DPS` +58.500, `ShockRadius` +1.750

#### Static Charge

> Apply a charge to a target enemy hero. After a short duration, the static charge stuns and damages enemies within the radius.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 42 | - | - |
| AbilityCastRange | 15 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| ShockRadius | 5 | - | - |
| Damage | 35 | +0.7921 | 55.9 |
| ShockDelay | 3.500 | - | - |
| StunDuration | 0.900 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -20
- **T2** — `ShockRadius` +7, `AbilityCastRange` +5
- **T3** — `StunDuration` +0.900, `Damage` +160

#### Power Surge

> Power up your weapon with a shock effect, making your bullets proc shock damage on your target. This shock damage bounces to enemies near your target. Occurs once per burst shot.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 50 | - | - |
| AbilityDuration | 10 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DamagePerChain | 10 | +0.1400 | 13.7 |
| BonusPerChain | 10 | +0.3200 | 18.4 |
| ChainCount | 4 | - | - |
| ChainTickRate | 0.200 | - | - |
| ChainRadius | 10 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -18
- **T2** — `BonusMoveSpeed` +3, `BonusPerChain` +0.230, `DamagePerChain` +0.230
- **T3** — `TechResistDebuff` -15, `DebuffDuration` +10, `AbilityDuration` +10

#### Storm Cloud (ULTIMATE)

> Channel an expanding storm cloud around you that damages all enemies within its radius. Enemies do not take damage when they are out of line-of-sight.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 205 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 7 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| Radius | 30 | - | - |
| InitialRadius | 10 | - | - |
| DPS | 95 | +0.6000 | 110.8 |
| DamageInterval | 0.300 | - | - |
| ExpandTime | 3.500 | - | - |
| CloudHeight | 120 | - | - |
| CameraDistance | 600 | - | - |
| EndingSoonTime | 2 | - | - |
| LightningStrikes | 1 | - | - |
| LightningStrikeRadius | 7 | - | - |
| LightningStrikeDelay | 0.250 | - | - |
| LightningStrikeDamage | 75 | +0.5000 | 88.2 |
| LightningStrikeKnockBackForce | 500 | - | - |
| FlightControlEnabled | 1.500 | - | - |

**Upgrades**

- **T1** — `BulletResistOnActive` +55
- **T2** — `Radius` +10, `InitialRadius` +5, `AbilityChannelTime` +7
- **T3** — `DPS` +65, `FlightControlEnabled` +4

---

## Shiv

*internal id 19 / `hero_shiv` / complexity 3*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 830 | +46 | 1934 | 2440 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.50 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.17/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.72 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.51 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_shiv_set`

| stat | value |
|---|---|
| Damage per bullet | 4.80 |
| Bullets per shot | 6 |
| Damage per shot | 28.80 |
| Ammo / clip size | 10 |
| Damage per magazine | 288 |
| Cycle time (nominal) | 0.5513 s |
| Cycle time (effective avg) | 0.5513 s |
| Shots / second | 1.814 |
| Shots / second (with reload) | 1.168 |
| Reload duration | 2.80 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 52.24 |
| **DPS (with reload)** | **33.64** |
| Bullet damage per boon | +0.165 |
| Headshot multiplier | x1.65 |
| Bullet speed | 24000 |
| Falloff: full damage to | 19.8 m |
| Falloff: decays to | 41.1 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.500 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Serrated Knives

> Throw a knife that bleeds an enemy. Each additional hit adds a stack and refreshes the bleed duration, causing the bleed to increase per stack.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 16 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 0.200 | - | - |
| AbilityPostCastDuration | 0.300 | - | - |
| AbilityCharges | 2 | - | - |
| AbilityCooldownBetweenCharge | 2 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| BleedTickRate | 1 | - | - |
| MovementSlow | 28 | - | - |
| BleedDPSPerStack | 10 | +0.1300 | 13.4 |
| BleedDuration | 5 | - | - |
| FullRageCurrentHealthDamagePct | 3.500 | +0.0100 | 3.8 |

**Upgrades**

- **T1** — `BleedDuration` +2
- **T2** — `AbilityCharges` +2
- **T3** — `BleedDPSPerStack` +0.070

#### Slice and Dice

> Perform a dash forward, damaging enemies along the path. Hit Enemies have their spirit resist reduced. This debuff can stack.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 16 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.250 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| TechCleaveExpireTime | 0.350 | - | - |
| DashAngleThreshold | 89 | - | - |
| DashSpeed | 2400 | - | - |
| DashRange | 12 | - | - |
| DashRadius | 2.500 | - | - |
| ImpactDamage | 75 | +1.2000 | 106.7 |
| MoveSpeedPenaltyMaxSpeed | 200 | - | - |
| CameraDistance | 250 | - | - |
| SideMoveSpeedReduction | -100 | - | - |
| TechArmorDamageReduction | -6 | - | - |
| DebuffDuration | 14 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -6
- **T2** — `TechArmorDamageReduction` -4, `DashRange` +2
- **T3** — `ImpactDamage` +50, `CooldownReductionOnHit` +2, `CooldownReductionOnHitNonHero` +1, `MaxCooldownReductionsFromHits` +8

#### Bloodletting

> Take only a portion of incoming damage immediately and defer the rest to be taken over time. Activate to clear a portion of the deferred damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 25 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.250 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DamagePctDeferred | 25 | - | - |
| DeferredDamageDuration | 6 | - | - |
| DeferClearPct | 30 | - | - |
| DamagePctDeferredMaxRage | 15 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -15
- **T2** — `DeferClearPct` +40
- **T3** — `DamagePctDeferred` +15

#### Killing Blow (ULTIMATE)

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 145 | - | - |
| AbilityCastRange | 12 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.050 | - | - |
| AbilityPostCastDuration | 0.150 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| RageDrainRate | 0.250 | - | - |
| RagePerWeaponDamage | 0.016 | - | - |
| RagePerSpiritDamage | 0.015 | - | - |
| RagePerLightMelee | 1.557 | - | - |
| RagePerHeavyMelee | 2.854 | - | - |
| BonusAbilityResource | 10 | - | - |
| BuffDamage | 8 | - | - |
| RageDrainDelayDuration | 12 | - | - |
| Damage | 200 | - | - |
| EnemyHealthPercent | 18 | - | - |
| EnemyHealthPercentBuffer | 3 | - | - |
| CameraDistance | 400 | - | - |
| MoveSpeedToTarget | 30 | - | - |
| MinTimeToTarget | 0.500 | - | - |
| SlashRange | 90 | - | - |
| RecastWindow | 16 | - | - |
| FailedExecuteCooldownPenalty | 30 | - | - |

**Upgrades**

- **T1** — `BonusMoveSpeed` +2, `AbilityCastRange` +6
- **T2** — `BuffDamage` +16, `AbilityCooldown` -25
- **T3** — `EnemyHealthPercent` +10

---

## Silver

*internal id 80 / `hero_werewolf` / complexity 1*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 830 | +31 | 1574 | 1915 |
| Health Regen | 2.50 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.70 m/s |
| Sprint Speed (bonus) | 2.50 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 2 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_werewolf_rifle`

| stat | value |
|---|---|
| Damage per bullet | 5.10 |
| Bullets per shot | 7 |
| Damage per shot | 35.70 |
| Ammo / clip size | 7 |
| Damage per magazine | 249.90 |
| Cycle time (nominal) | 0.8500 s |
| Cycle time (effective avg) | 0.8500 s |
| Shots / second | 1.176 |
| Shots / second (with reload) | 1.077 |
| Reload duration | 0.30 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 42 |
| **DPS (with reload)** | **38.45** |
| Bullet damage per boon | +0.117 |
| Headshot multiplier | x1.65 |
| Bullet speed | 32000 |
| Falloff: full damage to | 17.0 m |
| Falloff: decays to | 42.0 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.600 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Slam Fire

> Instantly reload your gun. You gain bonus fire rate and deal bonus weapon damage based on the target's health for a limited number of shots, but suffer from reduced accuracy.Deals bonus Weapon Damage against troopers and neutrals.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 25 | - | - |
| AbilityDuration | 5 | - | - |
| AbilityCastRange | 1 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.450 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 200 | - | - |
| Damage | 40 | - | - |
| DebuffDuration | 3 | - | - |
| BulletSpread | -1 | - | - |
| BulletEffectiveness | 0.100 | - | - |
| BulletRadiusOverride | 7 | - | - |
| SpreadPenaltyPerShot | 0.500 | - | - |
| RecoilRecoverySpeed | 0.100 | - | - |
| RecoilDelayFactor | 0.050 | - | - |
| RecoilSpeed | 12 | - | - |
| RecoilStrength | 12 | - | - |
| MaxShots | 3 | - | - |
| BonusFireRate | 300 | - | - |
| AccuracyPercentage | -30 | - | - |
| CurrentHealthDamagePercentage | 2.500 | - | - |
| ProcChance | 100 | - | - |
| LingerDuration | 0.100 | - | - |
| NonPlayerBonusWeaponPower | 100 | - | - |

**Upgrades**

- **T1** — `BaseAttackDamagePercent` +15
- **T2** — `AbilityCooldown` -10
- **T3** — `StackDuration` +3, `MaxStacks` +3, `BonusCurrentHealthDamagePercentage` +7

#### Boot Kick

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 21 | - | - |
| AbilityCastRange | 10.600 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.250 | - | - |
| AbilityChannelTime | 0.350 | - | - |
| AbilityPostCastDuration | 0.250 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| LeapRadius | 1.700 | - | - |
| CameraTurnRateMax | 188 | - | - |
| EnemyPushForceAway | 300 | - | - |
| SelfPushForceUp | 200 | - | - |
| SlowDuration | 0.100 | - | - |
| TimeScaleDebuff | 95 | - | - |
| AirDrag | 0.800 | - | - |
| FallSpeedMax | 20 | - | - |
| EnemyPushForceUp | 300 | - | - |
| SelfPushForceCameraAway | 600 | - | - |
| SuccessInputWindow | 0.300 | - | - |
| LeapForwardOffset | 2.500 | - | - |
| BonusDamage | 25 | +2 | 77.8 |
| MarkDuration | 3 | +1 | 29.4 |

**Upgrades**

- **T1** — `AbilityCooldown` -6
- **T2** — `StaminaRestore` +2
- **T3** — `OutgoingDamagePercent` -35, `DebuffDuration` +5, `BonusDamage` +80

#### Entangling Bola

> Throw a bola, dealing spirit damage, applying slow and preventing movement abilities or stamina.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 23 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.240 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 40 | +1.6000 | 82.2 |
| DebuffDuration | 1.500 | - | - |
| SlowPercent | 16 | - | - |
| GravityScale | 100 | - | - |

**Upgrades**

- **T1** — `SlowPercent` +20
- **T2** — `AbilityCooldown` -8
- **T3** — `RicochetCount` +2, `RicochetRange` +15, `DebuffDuration` +0.750

#### Lycan Curse (ULTIMATE)

> Passive: Dealing damage generates bloodlust, increased at low health. At max bloodlust, you automatically cast Lycan Curse.Active: Instantly transform, gaining increased max health, and stacking fire rate on enemy heroes, and replacing your abilities and weapon with their ferocious versions.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 60 | - | - |
| AbilityDuration | 15 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.300 | - | - |
| AbilityPostCastDuration | 0.500 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 100 | - | - |
| BonusHealth | 125 | +15 | 521 |
| CameraTurnRateMax | 188 | - | - |
| BonusMoveSpeed | 1.500 | - | - |
| AutoActivateHealthThreshold | 20 | - | - |
| BonusDurationOnLightMelee | 0.500 | - | - |
| BonusDurationOnHeavyMelee | 1.500 | - | - |
| BonusDurationOnBullet | 0.150 | - | - |
| BonusDurationPerHealthPercentLost | 0.100 | - | - |
| HeadshotResist | -20 | - | - |
| BonusFireRate | 60 | +0.4500 | 71.9 |
| RagePercentagePerSecondOutOfCombat | -3 | - | - |
| MaxRage | 100 | +9.4000 | 348.2 |
| RagePerDamage | 0.255 | - | - |
| ReadyDuration | 3 | - | - |
| LowHealthFraction | 30 | - | - |
| LowHealthRageBonus | 40 | +1.8000 | 87.5 |
| AbilityChargesConditionally | 1 | - | - |
| MaxStacks | 15 | - | - |
| StackDuration | 5 | - | - |
| RagePercentagePerSecondInCombat | 1 | - | - |
| MissingHealthPercentHeal | 30 | - | - |
| EndingWarningSoundDuration | 3 | - | - |

**Upgrades**

- **T1** — `BulletResist` +15, `TechResist` +15
- **T2** — `BonusMoveSpeed` +4, `BonusHealth` +200
- **T3** — `KillDurationBonus` +15, `KillCreditWindow` +1.500

---

## Sinclair

*internal id 60 / `hero_magician` / complexity 4*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 730 | +38 | 1642 | 2060 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7.20 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_magician_set`

| stat | value |
|---|---|
| Damage per bullet | 17.76 |
| Bullets per shot | 1 |
| Damage per shot | 17.76 |
| Ammo / clip size | 16 |
| Damage per magazine | 284.16 |
| Cycle time (nominal) | 0.5250 s |
| Cycle time (effective avg) | 0.3609 s |
| Shots / second | 2.721 |
| Shots / second (with reload) | 1.877 |
| Reload duration | 2.50 s |
| Burst shot count | 2 |
| DPS (sustained, no reload) | 48.33 |
| **DPS (with reload)** | **33.33** |
| Bullet damage per boon | +0.550 |
| Headshot multiplier | x1.65 |
| Bullet speed | 11811 |
| Falloff: full damage to | 25.4 m |
| Falloff: decays to | 61.0 m |
| Falloff: damage retained | 30% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 1 |

### Spirit scaling

- Spirit Power per boon: **+1.30**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **31.2**
- Spirit Power at 50k net worth (no items): **45.5**

### Abilities


#### Vexing Bolt

> Fire a bolt of magic that deals Damage, increasing as it travels. If you have an Assistant, they also cast Vexing Bolt at reduced damage. Press Ability 1 to redirect the bolt towards your crosshairs.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 24 | - | - |
| AbilityCastRange | 500 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityPostCastDuration | 0.300 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 3 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| MaxDamage | 120 | +1.8600 | 178.0 |
| Radius | 3.250 | - | - |
| RedirectVelocity | 1500 | - | - |
| ProjectileLifetime | 4 | - | - |
| InitialProjectileVelocity | 800 | - | - |
| ProjectileRedirectCount | 1 | - | - |
| CloneDamagePercentage | 50 | - | - |
| MinDamage | 60 | +0.9300 | 89.0 |
| MaxDamageTime | 2 | - | - |
| CloneBoltDelay | 0.100 | - | - |

**Upgrades**

- **T1** — `FireRateSlow` +25, `DebuffDuration` +5
- **T2** — `AbilityCooldown` -13
- **T3** — `MaxDamage` +126, `CloneDamagePercentage` +50

#### Spectral Assistant

> Summon an Assistant at the targeted location. The Assistant attacks whenever you fire your weapon, dealing Damage. While the Assistant is out, you can press Ability 2 to swap positions with your Assistant. Casting Spectral Assistant also reloads your weapon.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 40 | - | - |
| AbilityDuration | 6 | - | - |
| AbilityCastRange | 15 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 15 | +0.3600 | 26.2 |
| TurretBulletVerticalOffset | 2 | - | - |
| TurretBulletTargetAngle | 20 | - | - |
| TurretBulletTargetRadius | 500 | - | - |
| TotalSwaps | 2 | - | - |
| LeashRadius | 20 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -10
- **T2** — `AbilityDuration` +7, `AbilityCastRange` +5, `LeashRadius` +5
- **T3** — `BonusFireRate` +60, `Damage` +12.600

#### Rabbit Hex

> Hex a target area and transforming all enemies into a Rabbit for a limited duration. Rabbits are small and move faster, but take increased Damage and are unable to perform most actions.Hex does not interrupt abilities.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 26 | - | - |
| AbilityCastRange | 24 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DamageAmpPercentage | 15 | +0.0558 | 16.7 |
| Radius | 6.500 | - | - |
| SelfBumpImpulse | 500 | - | - |
| AirDampingDuration | 1 | - | - |
| HexMoveSpeedLimit | 6 | - | - |
| MoveSpeedBonusPct | 36 | - | - |
| HexDuration | 2 | - | - |
| DetonationDelay | 0.900 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -10
- **T2** — `HexDuration` +1
- **T3** — `Radius` +3, `DamageAmpPercentage` +7

#### Audience Participation (ULTIMATE)

> Copy the Ultimate of an enemy hero for a limited time. Reactivating the ability will use the Copied Ultimate instead.Copies will inherit this ability's upgrade points.Audience Participation will also copy the cooldown.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 85 | - | - |
| AbilityCastRange | 20 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| CopiedUltWindow | 12 | - | - |
| CopyInternalCooldown | 0.500 | - | - |
| CopyCooldownPercentage | 40 | - | - |

**Upgrades**

- **T1** — (see description)
- **T2** — (see description)
- **T3** — (see description)

---

## The Doorman

*internal id 69 / `hero_doorman` / complexity 1*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 755 | +42 | 1763 | 2225 |
| Health Regen | 1 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7.90 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.62 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.43 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_doorman_set`

| stat | value |
|---|---|
| Damage per bullet | 24 |
| Bullets per shot | 1 |
| Damage per shot | 24 |
| Ammo / clip size | 8 |
| Damage per magazine | 192 |
| Cycle time (nominal) | 0.6300 s |
| Cycle time (effective avg) | 0.6738 s |
| Shots / second | 1.471 |
| Shots / second (with reload) | 0.995 |
| Reload duration | 2.40 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 35.29 |
| **DPS (with reload)** | **23.88** |
| Bullet damage per boon | +1.250 |
| Headshot multiplier | x1.65 |
| Bullet speed | 8000 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.500 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Call Bell

> Throw out a call bell that deals spirit damage on impact. After a short delay it explodes, dealing additional spirit damage and causing affected enemies to suffer reduced weapon accuracy and movement slow.Can be shot to detonate early.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 18 | - | - |
| AbilityDuration | 4 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityPostCastDuration | 0.500 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 7 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 5.500 | - | - |
| ExplosionDamage | 55 | +1.2000 | 86.7 |
| ProjectileFuse | 3 | - | - |
| ProjectileDrag | 0.975 | - | - |
| DebuffAccuracy | -40 | - | - |
| ImpactDamage | 40 | +0.7000 | 58.5 |
| AccuracyDebuffFalloffBias | 0.300 | - | - |
| SlowPercent | 28 | - | - |
| EnableAura | 1 | - | - |

**Upgrades**

- **T1** — `AbilityCharges` +1
- **T2** — `ImpactDamage` +30, `ExplosionDamage` +40
- **T3** — `ProjectileFuse` +26, `Radius` +4.500, `ImpactDamage` +0.350, `ExplosionDamage` +0.350

#### Doorway

> Place two connected doors in the world. Players and most projectiles entering one door will exit out through the other. The doors will close at the end of the duration.The two doors must be placed within the doorway distance of each other.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 45 | - | - |
| AbilityDuration | 15 | - | - |
| AbilityCastRange | 50 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DoorwayCloseCooldown | 8 | - | - |
| DoorwayDistance | 65 | - | - |

**Upgrades**

- **T1** — `AbilityDuration` +20
- **T2** — `CombatBarrier` +1.500, `BarrierDuration` +12
- **T3** — `DoorwayDistance` +0.150, `AbilityCastRange` +30

#### Luggage Cart

> Send out a luggage Cart that deals spirit damage and pulls enemy heroes along its path. Can be alt cast with to target friendly heroes instead.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 30 | - | - |
| AbilityDuration | 6 | - | - |
| AbilityCastRange | 20 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.250 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| CartDamage | 60 | +0.7500 | 79.8 |

**Upgrades**

- **T1** — `CartDamage` +80
- **T2** — `AbilityCastRange` +25, `WallImpactDamage` +0.600
- **T3** — `StunDuration` +1.250, `AbilityCooldown` -15

#### Hotel Guest (ULTIMATE)

> Send the target's physical body to be a guest at the Baroness Hotel. The guest is to promptly make their way to the exit elevator, where they'll be sent back to their original position. A stay at the Baroness Hotel is paid for in spirit damage. Failure to check-out on time costs additional spirit damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 140 | - | - |
| AbilityDuration | 6.500 | - | - |
| AbilityCastRange | 7 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 1 | - | - |
| AbilityPostCastDuration | 0.700 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 75 | +1 | 101.4 |
| LateCheckoutDamage | 125 | +1.5000 | 164.6 |
| TimeSlowDuration | 1 | - | - |
| TimeSlowPercentage | 100 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -20, `StaminaDrain` +1
- **T2** — `Damage` +150, `LateCheckoutDamage` +150, `LateCheckoutStun` +1.500
- **T3** — `UnstoppableWhileHotelOccupied` +1, `LateCheckoutCooldown` +15

---

## Venator

*internal id 65 / `hero_priest` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 820 | +43 | 1852 | 2325 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.40 m/s |
| Sprint Speed (bonus) | 1 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.72 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.51 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.70 | 109.50 |
| Heavy Melee | 125 | - | - |

### Weapon

`citadel_weapon_priest_set`

| stat | value |
|---|---|
| Damage per bullet | 8 |
| Bullets per shot | 1 |
| Damage per shot | 8 |
| Ammo / clip size | 33 |
| Damage per magazine | 264 |
| Cycle time (nominal) | 0.1260 s |
| Cycle time (effective avg) | 0.1260 s |
| Shots / second | 7.937 |
| Shots / second (with reload) | 4.578 |
| Reload duration | 2.80 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 63.49 |
| **DPS (with reload)** | **36.63** |
| Bullet damage per boon | +0.270 |
| Headshot multiplier | x1.65 |
| Bullet speed | 62500 |
| Falloff: full damage to | 18.0 m |
| Falloff: decays to | 47.0 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.200 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Consecrating Grenade

> Fire a grenade that bounces before exploding, dealing weapon damage and setting enemies on fire. Burning targets deal pure damage to enemies in the area and suffer from reduced healing.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 25 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.030 | - | - |
| AbilityPostCastDuration | 0.150 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 4.500 | - | - |
| Damage | 35 | +1 | 61.4 |
| CameraTurnRateMax | 15 | - | - |
| BurnDuration | 3.500 | - | - |
| DPS | 10 | +1.6000 | 52.2 |
| HealAmpRegenPenaltyPercent | -30 | - | - |
| TickRate | 0.200 | - | - |
| BounceGrenadeSpeed | 1100 | - | - |
| BurnRadius | 4.500 | - | - |
| BurnLingerDuration | 0.150 | - | - |
| HealAmpReceivePenaltyPercent | -30 | - | - |
| PreBounceLifetime | 15 | - | - |
| BounceLifetime | 0.500 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -5
- **T2** — `Radius` +1.500, `BurnRadius` +1.500, `BurnDuration` +1
- **T3** — `HealAmpReceivePenaltyPercent` -20, `HealAmpRegenPenaltyPercent` -20, `AbilityCharges` +1, `AbilityCooldownBetweenCharge` +3

#### Gutshot

> Fire a blast with your shotgun, dealing weapon damage and pushing enemies back. Enemies near a wall receive stun and take bonus weapon damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 23 | - | - |
| AbilityCastRange | 10 | - | - |
| AbilityUnitTargetLimit | 99 | - | - |
| AbilityCastDelay | 0.250 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 60 | +0.7000 | 78.5 |
| BonusDamage | 30 | +0.8000 | 51.1 |
| StunDuration | 0.600 | - | - |
| KnockbackSpeed | 1200 | - | - |
| BonusKnockbackDistance | 3.500 | - | - |
| TargetingConeAngle | 60 | - | - |
| PushForce | 6 | - | - |
| SelfPushForce | 500 | - | - |
| MaxPushForceHorizontal | 1400 | - | - |
| MaxPushForceVertical | 500 | - | - |
| WallStunDistance | 7 | - | - |

**Upgrades**

- **T1** — `Damage` +25
- **T2** — `AbilityCooldown` -10, `StunDuration` +0.400
- **T3** — `BuffDuration` +5

#### Hex-Lined Snap Trap

> Kick a trap that arms after a brief delay. The trap springs on the first enemy it touches, dealing spirit damage, applying immobilize, and revealing enemies for a duration afterwards.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 28 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCharges | 2 | - | - |
| AbilityCooldownBetweenCharge | 8 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 2 | - | - |
| TrapHeight | 2 | - | - |
| Lifetime | 30 | - | - |
| Damage | 80 | +2.2000 | 138.1 |
| ImmobilizeDuration | 1.250 | - | - |
| ArmTime | 0.500 | - | - |
| TripUpSpeed | 250 | - | - |
| RevealDuration | 6 | - | - |
| TickRate | 0.100 | - | - |
| TetherRadius | 0.300 | - | - |
| TetherDuration | 0.600 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -11
- **T2** — `ImmobilizeDuration` +1
- **T3** — `IncomingDamagePercentFromCaster` +30, `AbilityCharges` +1

#### Ira Domini (ULTIMATE)

> Load your crossbow with 3 stakes, dealing massively increased weapon damage.The final stake is blessed, dealing bonus pure damage and executing low-health enemies.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 160 | - | - |
| AbilityDuration | 15 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.300 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 120 | +1.5000 | 159.6 |
| ExecuteThreshold | 8 | - | - |
| PushForce | 500 | - | - |
| ExplodeRadius | 0.200 | - | - |
| SwapEndDelay | 0.600 | - | - |
| StakeCount | 3 | - | - |
| BonusDamage | 115 | +3 | 194.2 |
| BonusAmpToVampire | 5 | - | - |

**Upgrades**

- **T1** — `BonusMoveSpeed` +1.200
- **T2** — `BonusDamage` +65, `AbilityCooldown` -15
- **T3** — `AllStakesBlessed` +1

---

## Victor

*internal id 66 / `hero_frank` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 800 | +34 | 1616 | 1990 |
| Health Regen | 1.50 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.30 m/s |
| Sprint Speed (bonus) | 1.10 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.72 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.51 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_frank_set2`

| stat | value |
|---|---|
| Damage per bullet | 12 |
| Bullets per shot | 1 |
| Damage per shot | 12 |
| Ammo / clip size | 24 |
| Damage per magazine | 288 |
| Cycle time (nominal) | 0.1980 s |
| Cycle time (effective avg) | 0.1980 s |
| Shots / second | 5.051 |
| Shots / second (with reload) | 3.242 |
| Reload duration | 2.40 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 60.61 |
| **DPS (with reload)** | **38.91** |
| Bullet damage per boon | +0.260 |
| Headshot multiplier | x1.65 |
| Bullet speed | 8000 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 1 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Pain Battery

> Taking any damage passively charges up your Pain Battery. Once full, activating the ability fires multiple shocking bolts, dealing spirit damage once per target.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 2 | - | - |
| AbilityCastRange | 28 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.350 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 100 | +1.6000 | 142.2 |
| AbilityChargesConditionally | 1 | - | - |
| BonusShocksDelay | 0.200 | - | - |
| SpreadAngle | 40 | - | - |
| BoltCount | 7 | - | - |
| StoredDamageHealthPercentRequired | 40 | - | - |
| SpreadRandomness | 0.005 | - | - |
| BatteryGenerationPercent | 100 | +-1 | 73.6 |

**Upgrades**

- **T1** — `SlowPercent` +32, `SlowDuration` +2
- **T2** — `Damage` +50
- **T3** — `MissingHealthPercentHeal` +15, `Damage` +0.600

#### Jumpstart

> Deal spirit damage to yourself. Then, gain bonus regeneration and bonus move speed, decaying over time.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 30 | - | - |
| AbilityDuration | 4.500 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 0.350 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 8 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| BonusMoveSpeed | 3 | - | - |
| CurrentHealthPercentDamage | 15 | - | - |
| TotalHealthRegen | 100 | +1.2000 | 131.7 |

**Upgrades**

- **T1** — `BonusMoveSpeed` +3
- **T2** — `TotalHealthRegen` +70, `AbilityCooldown` -8
- **T3** — `AbilityCharges` +1, `TotalHealthRegen` +0.900, `StatusResistancePercent` +50

#### Aura of Suffering

> Unleash pain, dealing spirit damage over time to both enemies and yourself. The damage continues to increase the longer the ability is channeled, up to a maximum amount.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 2 | - | - |
| AbilityDuration | 8 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 8 | - | - |
| MinDPS | 13 | +0.1500 | 17.0 |
| SelfDPS | 15 | - | - |
| TickRate | 0.250 | - | - |
| DebuffDuration | 0.500 | - | - |
| ToggleOffDelay | 0.500 | - | - |
| MaxDPS | 58 | +0.7200 | 77.0 |
| SelfDamagePercentage | 70 | - | - |

**Upgrades**

- **T1** — `SlowPercent` +20, `EnemyDashSlowPercent` -22, `DebuffDuration` +0.500
- **T2** — `MinDps` +6, `MaxDPS` +34
- **T3** — `IncomingDamagePercent` +15, `Radius` +1

#### Shocking Reanimation (ULTIMATE)

> Release a wave after taking lethal damage, applying a diminishing slow. After a brief channel you reanimate, dealing spirit damage and applying stun to nearby enemies.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 240 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 3 | - | - |
| AbilityPostCastDuration | 0.660 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 200 | +2 | 252.8 |
| Radius | 18 | - | - |
| HalfHeight | 15 | - | - |
| InitialDelay | 0.500 | - | - |
| RespawnDelay | 3 | - | - |
| RespawnHealthPercent | 50 | - | - |
| SlowPercent | 120 | - | - |
| EnemyDashSlowPercent | -26 | - | - |
| SlowDuration | 3 | - | - |
| ZombieTickRate | 0.020 | - | - |
| StunDuration | 1.500 | - | - |

**Upgrades**

- **T1** — `BonusDamagePerBullet` +0.060, `BonusFireRate` +15
- **T2** — `RespawnHealthPercent` +50
- **T3** — `Damage` +175, `StunDuration` +1.500, `AbilityCooldown` -95

---

## Vindicta

*internal id 3 / `hero_hornet` / complexity 1*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 755 | +28 | 1427 | 1735 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7.90 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 2 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_hornet_set`

| stat | value |
|---|---|
| Damage per bullet | 12.33 |
| Bullets per shot | 1 |
| Damage per shot | 12.33 |
| Ammo / clip size | 19 |
| Damage per magazine | 234.27 |
| Cycle time (nominal) | 0.2310 s |
| Cycle time (effective avg) | 0.2310 s |
| Shots / second | 4.329 |
| Shots / second (with reload) | 2.516 |
| Reload duration | 2.91 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 53.38 |
| **DPS (with reload)** | **31.02** |
| Bullet damage per boon | +0.495 |
| Headshot multiplier | x1.65 |
| Bullet speed | 25984.30 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 64.0 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 2 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Stake

> Throw a stake that tethers enemies to the location where the stake lands. Enemy movement is restricted to the length of the tether.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 40 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 40 | +0.5000 | 53.2 |
| SlowPercent | 40 | - | - |
| ChainLength | 9 | - | - |
| CaptureRadius | 9 | - | - |
| ChainDuration | 1.750 | - | - |
| EnemyDragSpeed | 1000 | - | - |

**Upgrades**

- **T1** — `Damage` +45
- **T2** — `AbilityCooldown` -22
- **T3** — `ChainDuration` +0.750, `CaptureRadius` +2

#### Flight

> Leap into the air and fly. While in flight your weapon deals bonus spirit damage and your items have increased range.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 42 | - | - |
| AbilityDuration | 13 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| FlyingItemCastRange | 50 | - | - |
| MaxFlyHeight | 1720 | - | - |
| JumpVelocity | 1000 | - | - |
| AirSideMoveSpeedPercentage | -35 | - | - |
| MinVelocityZ | -20 | - | - |
| WeaponRecoilReduction | 40 | - | - |
| MagicDamagePerBullet | 10 | +0.1800 | 14.8 |

**Upgrades**

- **T1** — `BonusClipSizePercent` +50
- **T2** — `AbilityDuration` +10
- **T3** — `MagicDamagePerBullet` +0.100, `RefreshOnKill` +1

#### Crow Familiar

> Your crow familiar deals impact damage, reduces their bullet resist and applies a bleed that deals damage based on the target's current health.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 32 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DotHealthPercent | 2.200 | - | - |
| TickRate | 1 | - | - |
| ImpactDamage | 40 | +0.7440 | 59.6 |
| DebuffDuration | 5 | - | - |
| VisualSplashRadius | 4 | - | - |
| BulletResistReduction | -6 | - | - |
| TechArmorDamageReduction | -6 | - | - |

**Upgrades**

- **T1** — `HealAmpReceivePenaltyPercent` -35, `HealAmpRegenPenaltyPercent` -35
- **T2** — `AbilityCooldown` -16, `DotHealthPercent` +0.500
- **T3** — `BulletResistReduction` -8, `TechArmorDamageReduction` -8, `DebuffDuration` +2

#### Assassinate (ULTIMATE)

> Use your scoped rifle to fire a powerful shot over long distances. Deal only partial damage until fully charged after 1.0s of being scoped. Does bonus damage to enemies with less than 50% health remaining. Landing a killing blow on a player with Assassinate grants you bonus weapon damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 55 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCharges | 2 | - | - |
| AbilityCooldownBetweenCharge | 2.500 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Range | 1000 | - | - |
| Damage | 90 | +0.9300 | 114.6 |
| ShotRadius | 4 | - | - |
| LowHealthEnemyDamageBonus | 90 | +2.3000 | 150.7 |
| LowHealthEnemyThresholdPct | 50 | - | - |
| ViewPunch | 2.500 | - | - |
| MoveSpeed | 4 | - | - |
| MaxSoundDistance | 2000 | - | - |
| WeaponDamageBonusPerKill | 6 | - | - |
| BonusGoldOnKill | 250 | - | - |
| HeadshotBonus | 20 | - | - |
| MinChargeDamagePercent | 50 | - | - |
| TimeToFullCharge | 1 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -15
- **T2** — `LowHealthEnemyDamageBonus` +80
- **T3** — `WeaponDamageBonusPerKill` +4

---

## Viscous

*internal id 35 / `hero_viscous` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 780 | +45 | 1860 | 2355 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7.20 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 63 | +1.58 | 118.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_viscous_set`

| stat | value |
|---|---|
| Damage per bullet | 10.34 |
| Bullets per shot | 1 |
| Damage per shot | 10.34 |
| Ammo / clip size | 20 |
| Damage per magazine | 206.80 |
| Cycle time (nominal) | 0.2100 s |
| Cycle time (effective avg) | 0.2100 s |
| Shots / second | 4.762 |
| Shots / second (with reload) | 2.878 |
| Reload duration | 2.50 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 49.24 |
| **DPS (with reload)** | **29.76** |
| Bullet damage per boon | +0.360 |
| Headshot multiplier | x1.65 |
| Bullet speed | 10000 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 57.5 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.500 |

### Spirit scaling

- Spirit Power per boon: **+1.30**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **31.2**
- Spirit Power at 50k net worth (no items): **45.5**

### Abilities


#### Splatter

> Throw a ball of goo that deals damage and leaves puddles of goo behind that apply movement slow to enemies in the radius.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 26 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.001 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| SlowPercent | 28 | - | - |
| MaxBounces | 2 | - | - |
| Damage | 55 | +0.7000 | 76.8 |
| Radius | 5 | - | - |
| PuddleDuration | 10 | +1.1000 | 44.3 |
| DetonateCooldown | 0.120 | - | - |
| SecondHitDamagePercentage | 0.500 | - | - |
| ThirdHitDamagePercentage | 0.380 | - | - |
| FourthHitDamagePercentage | 0.260 | - | - |
| PuddleSlideBuff | 60 | - | - |

**Upgrades**

- **T1** — `Damage` +36, `Radius` +1.500
- **T2** — `AbilityCooldown` -14
- **T3** — `MaxBounces` +1, `Damage` +0.900

#### The Cube

> Encase the target in a cube of restorative goo that protects from damage, and increases health regen. Target is unable to take any new actions while cubed. Can be used on self. Press Jump / mantle to escape early.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 42 | - | - |
| AbilityDuration | 3 | - | - |
| AbilityCastRange | 20 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| CubeScale | 1.500 | - | - |
| Friction | -80 | - | - |
| BonusHealthRegen | 40 | +0.3000 | 49.4 |
| PushBackRadius | 50 | - | - |
| PushBackForce | 250 | - | - |
| LightMeleeForce | 300 | - | - |
| HeavyMeleeForce | 700 | - | - |
| BulletForce | 600 | - | - |
| SlideForce | 70 | - | - |
| BreakoutTime | 1 | - | - |
| PostCubeBuffDuration | 8 | - | - |

**Upgrades**

- **T1** — `BonusMoveSpeed` +2.500, `StaminaCooldownReduction` +30, `PostCubeBuff` +1
- **T2** — `BonusHealthRegen` +25, `AbilityDuration` +1
- **T3** — `AbilityCooldown` -20, `PurgeDebuffs` +1

#### Puddle Punch

> Materialize a fist in the world that punches everyone in the area, applying knockup. Punching an enemy deals melee damage and applies slow.You and your allies have increased Air Control.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 24 | - | - |
| AbilityCastRange | 40 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCharges | 1 | - | - |
| AbilityCooldownBetweenCharge | 1.700 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 20 | +0.6000 | 38.7 |
| Radius | 4 | - | - |
| PunchHalfHeight | 5.500 | - | - |
| TossSpeed | 625 | - | - |
| TossSpeedWall | 750 | - | - |
| TossSpeedUpWall | 500 | - | - |
| TossGroundSideRatio | 0.700 | - | - |
| PunchRollSlow | -36 | - | - |
| PunchRollSlowDuration | 1 | - | - |
| SlowPercent | 24 | - | - |
| ImpactDuration | 3 | - | - |
| FriendlyImpactDuration | 2 | - | - |
| TossDuration | 0.600 | - | - |
| PunchFriendlyAirControl | 30 | - | - |

**Upgrades**

- **T1** — `AbilityCharges` +1, `Damage` +20
- **T2** — `Radius` +1.500, `LifeStealPercentOnHit` +60
- **T3** — `AbilityCooldown` -14, `UseHeavyMelee` +1, `DamageHeavyMelee` +40, `Damage` -40

#### Goo Ball (ULTIMATE)

> Morph into a large goo ball that deals damage and stuns enemies on impact. The ball grants large amounts of Bullet and Spirit resist, bounces off walls and can double jump.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 150 | - | - |
| AbilityDuration | 11 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.550 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 7 | - | - |
| BallRadius | 1.400 | - | - |
| BallHitRadius | 1.800 | - | - |
| Damage | 110 | +1 | 141.2 |
| BallOffset | 50 | - | - |
| FrictionPercentage | -85 | - | - |
| AccelerationPercentage | -60 | - | - |
| MoveSpeedMax | 7 | - | - |
| BreakablePropDamageRadius | 75 | - | - |
| JumpForce | 500 | - | - |
| ParticleRadiusMultiplier | 1.200 | - | - |
| TickRate | 0.250 | - | - |
| StunDuration | 0.500 | - | - |
| KnockForce | 400 | - | - |
| TechResist | 35 | - | - |
| BulletResist | 35 | - | - |
| AirJumpForce | 500 | - | - |
| CastWhileRolling | 1 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -25
- **T2** — `Damage` +70, `BulletResist` +20, `TechResist` +20
- **T3** — `AbilityDuration` +7, `StunDuration` +0.300, `Damage` +0.200

---

## Vyper

*internal id 58 / `hero_viper` / complexity 1*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 780 | +35 | 1620 | 2005 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.90 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 4 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_viper_set`

| stat | value |
|---|---|
| Damage per bullet | 6.58 |
| Bullets per shot | 1 |
| Damage per shot | 6.58 |
| Ammo / clip size | 24 |
| Damage per magazine | 157.92 |
| Cycle time (nominal) | 0.0700 s |
| Cycle time (effective avg) | 0.0700 s |
| Shots / second | 14.286 |
| Shots / second (with reload) | 6.799 |
| Reload duration | 1.60 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 94 |
| **DPS (with reload)** | **44.74** |
| Bullet damage per boon | +0.178 |
| Headshot multiplier | x1.65 |
| Bullet speed | 16200 |
| Falloff: full damage to | 15.0 m |
| Falloff: decays to | 33.0 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.020 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Screwjab Dagger

> Throw a dagger, dealing spirit damage and applying slow. Every subsequent dagger against the same target stacks in spirit damage and slow.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 10 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.200 | - | - |
| AbilityCharges | 2 | - | - |
| AbilityCooldownBetweenCharge | 4 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 50 | +0.8000 | 71.1 |
| SlowDuration | 2 | - | - |
| SlowPercent | 28 | - | - |
| DamagePerStack | 25 | +0.4000 | 35.6 |
| SlowPercentPerStack | 12 | - | - |
| StackDuration | 10 | - | - |
| MaxStacks | 3 | - | - |

**Upgrades**

- **T1** — `AbilityCharges` +1
- **T2** — `BulletResistReduction` -8, `BulletResistReductionPerStack` -6
- **T3** — `CooldownRefundPercent` +55, `MaxStacks` +2, `AbilityCooldownBetweenCharge` -2

#### Lethal Venom

> Inject a target with lethal venom. After a delay the venom triggers, dealing Spirit Damage. The damage is increased by the target's missing health.Lethal Venom will ignore Petrify's damage block.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 28 | - | - |
| AbilityCastRange | 10 | +0.2000 | 15.3 |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| VenomDuration | 3 | - | - |
| VenomMinDamage | 20 | +0.6510 | 37.2 |
| VenomMaxDamage | 140 | +2.7900 | 213.7 |
| VenomMinDamageHealthPercentage | 100 | - | - |
| VenomMaxDamageHealthPercentage | 30 | - | - |
| VenomBuildupPerShot | 1 | - | - |
| BuildUpDuration | 5 | - | - |

**Upgrades**

- **T1** — `VenomMaxDamage` +31.500
- **T2** — `HealAmpRegenPenaltyPercent` -40, `HealAmpReceivePenaltyPercent` -40, `AbilityCooldown` -12
- **T3** — `BuildUpPerShot` +4.500

#### Slither

> You have increased Slide Distance, can Slide up hills, and can turn faster while Sliding.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| SlideScale | 15 | - | - |

**Upgrades**

- **T1** — `SlideScale` +20
- **T2** — `Stamina` +2
- **T3** — `BuffDuration` +4, `CombatBarrier` +0.800, `AbilityCooldown` +8

#### Petrifying Bola (ULTIMATE)

> Throw an explosive bola. On exploding, the bola Slows and Damages all enemies in the area. Direct hits deal Additional Damage and Petrify instead. Petrified units block all damage, but cannot take actions.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 115 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 50 | +0.7440 | 69.6 |
| PetrifyDamage | 180 | +2.0460 | 234.0 |
| Radius | 12 | - | - |
| PetrifyDuration | 2.200 | - | - |
| SlowDuration | 1.500 | - | - |
| PetrifyDamageBreakThreshold | 200 | - | - |
| SlowPercent | 40 | - | - |

**Upgrades**

- **T1** — `PetrifyDamage` +49.500
- **T2** — `AbilityCooldown` -20
- **T3** — `PetrifyDuration` +1

---

## Warden

*internal id 25 / `hero_warden` / complexity 2*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 805 | +60 | 2245 | 2905 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 6.30 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_warden_set`

| stat | value |
|---|---|
| Damage per bullet | 17.34 |
| Bullets per shot | 1 |
| Damage per shot | 17.34 |
| Ammo / clip size | 17 |
| Damage per magazine | 294.78 |
| Cycle time (nominal) | 0.2625 s |
| Cycle time (effective avg) | 0.2625 s |
| Shots / second | 3.810 |
| Shots / second (with reload) | 2.229 |
| Reload duration | 2.91 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 66.06 |
| **DPS (with reload)** | **38.65** |
| Bullet damage per boon | +0.250 |
| Headshot multiplier | x1.65 |
| Bullet speed | 11417.30 |
| Falloff: full damage to | 18.0 m |
| Falloff: decays to | 47 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Alchemical Flask

> Throw a flask that damages and reduces the weapon damage and move speed of enemies it hits.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 12 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.100 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Radius | 5.500 | - | - |
| Damage | 60 | +0.6300 | 76.6 |
| WeaponPowerDebuff | -25 | - | - |
| SlowDuration | 3 | - | - |
| DebuffDuration | 7 | - | - |
| MoveSpeedSlowPct | 16 | - | - |
| ForwardVelocity | 800 | - | - |
| ProjectileLifetime | 60 | - | - |

**Upgrades**

- **T1** — `StaminaReduction` +1
- **T2** — `Damage` +35, `WeaponPowerDebuff` -25
- **T3** — `FireRateSlow` +30, `AbilityCooldown` -7, `Radius` +2

#### Willpower

> Gain a Barrier and bonus move speed.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 40 | - | - |
| AbilityDuration | 5 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| MoveSpeedBonusPct | 15 | - | - |
| CombatBarrier | 125 | +0.8000 | 146.1 |

**Upgrades**

- **T1** — `MoveSpeedBonusPct` +20
- **T2** — `AbilityCooldown` -24, `AbilityDuration` +2
- **T3** — `StatusResistancePercent` +30, `CombatBarrier` +2.100

#### Binding Word

> Curse an enemy hero. If they don't move away from their initial position within the escape time, they will be damaged and immobilized.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 34 | - | - |
| AbilityCastRange | 15 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.150 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| ImmobilizeDuration | 1.750 | - | - |
| Damage | 110 | +2.4373 | 174.3 |
| EscapeRange | 20 | - | - |
| EscapeTime | 2.800 | - | - |
| AdditionalTargetRadius | 20 | - | - |

**Upgrades**

- **T1** — `BulletArmorReduction` +20, `BulletArmorReductionDuration` +5
- **T2** — `ImmobilizeDuration` +0.750
- **T3** — `AbilityCooldown` -14, `SilenceDebuff` +1

#### Last Stand (ULTIMATE)

> After charging for 2s, release pulses that damage enemies and heal you based on the damage done. While channeling Last Stand you have greatly increased bullet and spirit resist.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 180 | - | - |
| AbilityDuration | 6 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 2 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| PulseInterval | 0.500 | - | - |
| PulseDPS | 70 | +1.3000 | 104.3 |
| Radius | 12 | - | - |
| HealthStealPctHero | 75 | - | - |
| HealthStealPct | 10 | - | - |
| ConeAngle | 115 | - | - |
| BulletResist | 50 | - | - |
| TechResist | 50 | - | - |

**Upgrades**

- **T1** — `Radius` +4
- **T2** — `PulseDPS` +40.500, `AbilityCooldown` -30
- **T3** — `AbilityDuration` +4, `UnstoppableCastDelay` +1, `BulletResist` +30, `TechResist` +30

---

## Wraith

*internal id 7 / `hero_wraith` / complexity 1*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 730 | +35 | 1570 | 1955 |
| Health Regen | 2 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 7.20 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 50 | +1.58 | 105.30 |
| Heavy Melee | 116 | - | - |

### Weapon

`citadel_weapon_wraith_set`

| stat | value |
|---|---|
| Damage per bullet | 5.64 |
| Bullets per shot | 1 |
| Damage per shot | 5.64 |
| Ammo / clip size | 52 |
| Damage per magazine | 293.28 |
| Cycle time (nominal) | 0.0945 s |
| Cycle time (effective avg) | 0.0945 s |
| Shots / second | 10.582 |
| Shots / second (with reload) | 6.513 |
| Reload duration | 2.82 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 59.68 |
| **DPS (with reload)** | **36.73** |
| Bullet damage per boon | +0.140 |
| Headshot multiplier | x1.65 |
| Bullet speed | 22500 |
| Falloff: full damage to | 18.0 m |
| Falloff: decays to | 52 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 1 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Card Trick

> Deal weapon damage to summon cards of a random suit. Each card can be thrown, dealing damage and applying a different effect depending of its suit. Cards thrown fly towards the enemy or point under your crosshair. Alt-cast to throw first card

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 0.600 | - | - |
| AbilityCastRange | 500 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityPostCastDuration | 0.100 | - | - |
| AbilityCharges | 2 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| Damage | 45 | +0.5500 | 59.5 |
| Radius | 4 | - | - |
| AbilityChargesConditionally | 1 | - | - |
| ResourcePerCard | 100 | - | - |
| BonusAbilityResource | 100 | - | - |
| NonPlayerCardResourceScale | 0.350 | - | - |
| CardResourcePerBulletHit | 4 | - | - |
| CardResourcePerBulletCrit | 6 | - | - |
| CardResourcePerLightMelee | 10 | - | - |
| CardResourcePerHeavyMelee | 25 | - | - |
| CardResourceGenPctScale | 85 | +-1 | 58.6 |
| ProjectileOriginHeightOffset | 50 | - | - |
| ClubSlowPercent | 24 | - | - |
| ClubSlowDuration | 3 | - | - |
| DiamondResistShredDuration | 5 | - | - |
| DiamondResistShred | -7 | - | - |
| JokerExtraCardSearchRadius | 20 | - | - |
| CooldownBetweenCards | 0.500 | - | - |
| HeartHeal | 60 | +0.5000 | 73.2 |
| HeartHealNonHeroRatio | 0.500 | - | - |
| SpadeDamageBonus | 60 | - | - |

**Upgrades**

- **T1** — `AbilityCharges` +2
- **T2** — `Damage` +0.400
- **T3** — `ImprovedJokerChance` +1, `SpadeDamageBonus` +40, `DiamondResistShred` -4, `HeartHeal` +0.500, `ClubSlowPercent` +12

#### Project Mind

> Teleport to the targeted location.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 46 | - | - |
| AbilityCastRange | 25 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.750 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 5.100 | - | - |
| CameraDistance | 250 | - | - |
| TrailInterval | 0.100 | - | - |

**Upgrades**

- **T1** — `AbilityCastRange` +15
- **T2** — `CombatBarrier` +1.700, `BarrierDuration` +5
- **T3** — `AbilityCooldown` -32

#### Full Auto

> Temporarily boosts your fire rate and deal bonus spirit damage

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 45 | - | - |
| AbilityDuration | 5 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| BonusFireRate | 20 | - | - |
| MagicDamagePerBullet | 2 | +0.0450 | 3.2 |

**Upgrades**

- **T1** — `AbilityCooldown` -20
- **T2** — `BonusFireRate` +10, `AbilityDuration` +3
- **T3** — `MagicDamagePerBullet` +0.045, `UnlimitedAmmo` +1

#### Telekinesis (ULTIMATE)

> Lift an enemy hero into the air and then slam them towards the target location.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 150 | - | - |
| AbilityDuration | 2.250 | - | - |
| AbilityCastRange | 10 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.450 | - | - |
| AbilityChannelTime | 0.650 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| DampingFactor | 0.300 | - | - |
| LiftHeight | 80 | - | - |
| Damage | 100 | +1 | 126.4 |
| LiftChainRadius | 20 | - | - |
| LiftDuration | 2 | - | - |
| TossDistance | 13 | - | - |
| SlowPercent | 32 | - | - |
| TossUpStrength | 220 | - | - |

**Upgrades**

- **T1** — `Damage` +100
- **T2** — `AbilityCooldown` -45
- **T3** — `AbilityDuration` +1.500, `TossDistance` +6, `AbilityCastRange` +6

---

## Yamato

*internal id 27 / `hero_yamato` / complexity 3*


### Vitality

| stat | base | per boon | at 20k NW | at 50k NW (35 boons) |
|---|---|---|---|---|
| Max Health | 730 | +45 | 1810 | 2305 |
| Health Regen | 1 | - | - | - |

### Movement

| stat | value |
|---|---|
| Max Move Speed | 8.20 m/s |
| Sprint Speed (bonus) | 1.60 m/s |
| Crouch Speed | 4.75 m/s |
| Move Acceleration | 4 |
| Stamina | 3 |
| Stamina Regen | 0.22/s |
| Ground Dash Distance | 10 m |
| Ground Dash Duration | 0.68 s |
| Air Dash Distance | 8 m |
| Air Dash Duration | 0.47 s |

### Melee

| stat | base | per boon | at 50k NW |
|---|---|---|---|
| Light Melee | 55 | +1.58 | 110.30 |
| Heavy Melee | 128 | - | - |

### Weapon

`citadel_weapon_yamato_set`

| stat | value |
|---|---|
| Damage per bullet | 5.31 |
| Bullets per shot | 5 |
| Damage per shot | 26.55 |
| Ammo / clip size | 12 |
| Damage per magazine | 318.60 |
| Cycle time (nominal) | 0.4200 s |
| Cycle time (effective avg) | 0.4200 s |
| Shots / second | 2.381 |
| Shots / second (with reload) | 1.552 |
| Reload duration | 2.44 s |
| Burst shot count | 1 |
| DPS (sustained, no reload) | 63.21 |
| **DPS (with reload)** | **41.19** |
| Bullet damage per boon | +0.154 |
| Headshot multiplier | x1.65 |
| Bullet speed | 10000 |
| Falloff: full damage to | 20.0 m |
| Falloff: decays to | 45.7 m |
| Falloff: damage retained | 10% |
| Max range | 177.8 m |
| Move speed while shooting | 75% |
| Spread penalty per shot | 0.250 |

### Spirit scaling

- Spirit Power per boon: **+1.10**  (field is 1.1 for most heroes; Grey Talon 1.6, Haze 0.5)
- Spirit Power at 20k net worth (no items): **26.4**
- Spirit Power at 50k net worth (no items): **38.5**

### Abilities


#### Power Slash

> Channel to increase damage over 1.4 seconds, then release a fully-charged sword strike.Press Ability 1 or to trigger the strike early, dealing partial damage.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 12 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 1.400 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| ChannelMoveSpeed | 1.300 | - | - |
| SlashLength | 22 | - | - |
| ShortChargeDamagePct | 30 | - | - |
| MediumChargeDamagePct | 50 | - | - |
| FullChargeDamage | 145 | +1.8500 | 193.8 |
| SlashRadius | 41 | - | - |
| FallSpeedMax | 5 | - | - |
| PowerUpStages | 3 | - | - |
| SlashCollisionRadius | 4 | - | - |
| BulletResist | 60 | - | - |

**Upgrades**

- **T1** — `SlowDuration` +3, `SlowPercent` +32
- **T2** — `AbilityCooldown` -4
- **T3** — `FullChargeDamage` +0.500, `SlashLength` +8

#### Flying Slash

> Throw a grappling hook to reel yourself towards an enemy, dealing Light melee damage and slowing the target when you arrive.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 36 | - | - |
| AbilityCastRange | 26 | - | - |
| AbilityUnitTargetLimit | 10 | - | - |
| AbilityPostCastDuration | 0.200 | - | - |
| ChannelMoveSpeed | -1 | - | - |
| SlowDuration | 2.500 | - | - |
| SlowPercent | 40 | - | - |

**Upgrades**

- **T1** — `AbilityCooldown` -18
- **T2** — `SpiritBonus` +35, `BuffDuration` +6
- **T3** — `AbilityCastRange` +15, `CanGrappleAllyHeroes` +1, `AbilityCharges` +2, `AbilityCooldownBetweenCharge` +5

#### Crimson Slash

> Slash enemies in front of you, damaging them and slowing their fire rate. If any enemy heroes are hit, you heal.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 16 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityCastDelay | 0.300 | - | - |
| AbilityPostCastDuration | 0.400 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| Damage | 55 | +0.3700 | 64.8 |
| Radius | 13 | - | - |
| HealFixedHealth | 55 | +1.0359 | 82.3 |
| DebuffDuration | 4 | - | - |
| FireRateSlow | 30 | - | - |

**Upgrades**

- **T1** — `BuffDuration` +4, `BuffMeleeDamage` +30
- **T2** — `HealMaxHealth` +6
- **T3** — `AbilityCooldown` -10, `Damage` +0.600, `HealFixedHealth` +0.400

#### Shadow Transformation (ULTIMATE)

> Become infused with Yamato's shadow soul. After an initial invincible transformation your abilities are refreshed and are 60% faster. You gain immunity to negative status effects and have greatly increased bullet and spirit resist.When you get a hero kill, you heal and the duration is extended.

| property | value | spirit coef | at 20k SP |
|---|---|---|---|
| AbilityCooldown | 150 | - | - |
| AbilityDuration | 5 | - | - |
| AbilityUnitTargetLimit | 1 | - | - |
| AbilityChannelTime | 1.500 | - | - |
| AbilityCooldownBetweenCharge | -1 | - | - |
| AbilitySpeedPct | 60 | - | - |
| BulletResist | 30 | - | - |
| TechResist | 30 | - | - |
| MaxHealthRegen | 15 | - | - |
| ShadowFormDurationOnKill | 2 | - | - |

**Upgrades**

- **T1** — `WeaponDamageBonus` +7
- **T2** — `BonusMoveSpeed` +4, `AbilityCooldown` -20
- **T3** — `AbilityDuration` +3, `BulletResist` +30, `TechResist` +30

---
