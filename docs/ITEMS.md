# Deadlock — Complete Item Reference

*Patch: Minor Update 09-16-2026 · extracted 2026-09-18*

173 purchasable items. Tier 5 entries exist in the files but are **Street Brawl only** and are excluded from standard-mode builds.


## WEAPON items


### Tier 1 — 800 souls


**Close Quarters** (passive)
  
> Deal additional Weapon Damage when in close range to your target.

| property | value |
|---|---|
| CloseRangeBonusWeaponPower | 20 |
| CloseRangeBonusDamageRange | 15 |
| MeleeResistPercent | 20 |
- upgrade 1: `CloseRangeBonusWeaponPower` 15, `MeleeResistPercent` 10

**Extended Magazine** (passive)

| property | value |
|---|---|
| BonusClipSizePercent | 30 |
| BaseAttackDamagePercent | 8 |
- upgrade 1: `BonusClipSizePercent` 30

**Headshot Booster** (passive)
  
> Your next headshot against an enemy Hero deals bonus weapon damage.

| property | value |
|---|---|
| AbilityCooldown | 9 |
| HeadShotBonusDamage | 45 |
| BonusHealth | 30 |
| ProcChance | 100 |
- upgrade 1: `HeadShotBonusDamage` 55

**High-Velocity Rounds** (passive)

| property | value |
|---|---|
| BonusBulletSpeedPercent | 60 |
| BaseAttackDamagePercent | 8 |
- upgrade 1: `BonusBulletSpeedPercent` 45, `BaseAttackDamagePercent` 15

**Monster Rounds** (passive)

| property | value |
|---|---|
| NonPlayerBonusWeaponPower | 25 |
| OutOfCombatHealthRegen | 1 |
| NonPlayerBulletResist | 25 |
- upgrade 1: `NonPlayerBonusWeaponPower` 35, `NonPlayerBulletResist` 35, `OutOfCombatHealthRegen` 1

**Rapid Rounds** (passive)

| property | value |
|---|---|
| BonusFireRate | 9 |
- upgrade 1: `BonusFireRate` 15

**Restorative Shot** (passive)
  
> Your next bullet will heal you based on what target you hit.

| property | value |
|---|---|
| AbilityCooldown | 6 |
| Radius | 1 |
| ProcChance | 100 |
| HealFromHero | 50 |
| HealFromNPC | 20 |
| BaseAttackDamagePercent | 6 |
- upgrade 1: `HealFromHero` 100, `HealFromNPC` 40

### Tier 2 — 1600 souls


**Active Reload** (passive)
  
> While reloading, pressing Reload during the highlighted portion will instantly finish your reload and grant you Fire Rate, Bullet Lifesteal and Move Speed.

| property | value |
|---|---|
| AbilityCooldown | 12 |
| AbilityDuration | 7 |
| BulletLifestealPercent | 16 |
| BonusFireRate | 25 |
| BonusClipSizePercent | 20 |
| BonusMoveSpeed | 0.750 |
- upgrade 1: `BonusFireRate` 15, `BonusMoveSpeed` 3, `BulletLifestealPercent` 12, `BonusClipSizePercent` 10

**Fleetfoot** (ACTIVE)
  
> Removes the Move Speed penalty while shooting.

| property | value |
|---|---|
| AbilityCooldown | 16 |
| AbilityDuration | 5 |
| MoveWhileShootingSpeedPenaltyReductionPercent | 100 |
| MoveWhileZoomedSpeedPenaltyReductionPercent | 100 |
| ActiveBonusMoveSpeed | 3 |
| SlideScale | 35 |
| BulletResist | 6 |
| SlowResistancePercent | 40 |
| BaseAttackDamagePercent | 6 |
- upgrade 1: `SlowResistancePercent` 30, `BulletResist` 12, `ActiveBonusMoveSpeed` 3

**Intensifying Magazine** (passive)
  
> Increases Weapon Damage as you continuously fire your weapon.

| property | value |
|---|---|
| BonusClipSizePercent | 20 |
| ShootDurationForMax | 2.500 |
| BaseAttackDamagePercentAtMaxDuration | 45 |
- upgrade 1: `BonusClipSizePercent` 40, `BaseAttackDamagePercentAtMaxDuration` 55

**Kinetic Dash** (passive)
  
*builds from: upgrade_improved_stamina*
  
> When you Dash-Jump you gain Fire Rate and bonus Ammo until your next reload. Lasts up to 7s.

| property | value |
|---|---|
| AbilityDuration | 7 |
| BonusFireRate | 25 |
| BonusClipSize | 6 |
| Stamina | 1 |
| StaminaCooldownReduction | 12 |
- upgrade 1: `BonusFireRate` 20, `Stamina` 1, `BonusClipSize` 6, `StaminaCooldownReduction` 14

**Long Range** (passive)
  
> Deal additional Weapon Damage when beyond a minimum distance from your target.

| property | value |
|---|---|
| LongRangeBonusWeaponPower | 40 |
| LongRangeBonusWeaponPowerMinRange | 15 |
| BonusSprintSpeed | 0.750 |
| BonusAttackRangePercent | 8 |
- upgrade 1: `BonusAttackRangePercent` 8, `LongRangeBonusWeaponPower` 30

**Melee Charge** (passive)
  
> Your next Heavy Melee attack against an enemy deals increased damage.

| property | value |
|---|---|
| AbilityCooldown | 5 |
| BulletResist | 6 |
| BonusMeleeDamagePercent | 10 |
| MeleeDistanceScale | 50 |
| BonusHeavyMeleeDamage | 25 |
- upgrade 1: `MeleeDistanceScale` 30, `BulletResist` 12, `BonusHeavyMeleeDamage` 15

**Mystic Shot** (passive)
  
> Your next bullet deals bonus spirit damage.

| property | value |
|---|---|
| AbilityCooldown | 8 |
| Radius | 1 |
| ProcChance | 100 |
| ProcCooldown | 1 |
| ProcBonusMagicDamage | 40 |
| SpiritPower | 7 |
- upgrade 1: `ProcBonusMagicDamage` 109, `SpiritPower` 14

**Opening Rounds** (passive)
  
*builds from: upgrade_high_velocity_mag*
  
> Your attacks have additional Weapon Damage against enemies above 50% health.

| property | value |
|---|---|
| TechPower | 7 |
| EnemyLifeThreshold | 50 |
| BonusBulletSpeedPercent | 60 |
| BaseAttackDamagePercent | 8 |
| BaseAttackDamagePercentBonus | 25 |
- upgrade 1: `BaseAttackDamagePercentBonus` 25, `TechPower` 18, `BonusBulletSpeedPercent` 45, `BaseAttackDamagePercent` 15

**Recharging Rush** (passive)
  
> Dealing significant weapon damage replenishes a charge for each of your charged abilities.

| property | value |
|---|---|
| AbilityCooldown | 25 |
| BonusClipSizePercent | 20 |
| BaseAttackDamagePercent | 10 |
| DamageThreshold | 200 |
| DamageWindow | 3.500 |
- upgrade 1: `AbilityCooldown` -12, `BonusClipSizePercent` 30, `BaseAttackDamagePercent` 30

**Slowing Bullets** (passive)
  
> Your bullets build up a Movement Slow on enemies.

| property | value |
|---|---|
| SlowPercent | 24 |
| GroundDashReductionPercent | -20 |
| SlowDuration | 3.500 |
| BuildUpDuration | 5 |
| BuildUpPerShot | 0.700 |
- upgrade 1: `SlowPercent` 16, `GroundDashReductionPercent` -8

**Spirit Shredder Bullets** (passive)
  
> Your bullets apply a debuff that reduces the Spirit Resist of the target and grants you and your allies Spirit Lifesteal against them.

| property | value |
|---|---|
| TechArmorDamageReduction | -8 |
| DebuffDuration | 8 |
| AbilityLifestealPercentHero | 10 |
- upgrade 1: `TechArmorDamageReduction` -10, `AbilityLifestealPercentHero` 10

**Split Shot** (ACTIVE)
  
> Make your weapon fire multishot. Hitting more than one Hero per attack will grant a stacking weapon damage bonus. Targets can only be hit once per multishot.

| property | value |
|---|---|
| AbilityCooldown | 27 |
| BonusShotsDuration | 5 |
| BulletSplitShot | 5 |
| SpreadAngleDegrees | 45 |
| WeaponDamageBonusDuration | 12 |
| WeaponDamagePerStack | 8 |
| MaxStacks | 5 |
- upgrade 1: `BulletSplitShot` 4, `WeaponDamagePerStack` 8, `AbilityCooldown` -8

**Stalker** (passive)
  
> Dealing weapon damage at close range opens a wound and grants you bonus move speed. Wounded enemies take spirit damage over time, have reduced bullet resist, and are revealed through walls.

| property | value |
|---|---|
| AbilityCooldown | 6 |
| AbilityDuration | 5 |
| BonusHealth | 50 |
| DPS | 17 |
| TickRate | 0.500 |
| ProcRadius | 8 |
| DebuffRadius | 25 |
| BulletResistReduction | -6 |
| DebuffDuration | 5 |
| BonusMoveSpeed | 1.500 |
| ReduceFootstepSound | -50 |
- upgrade 1: `BulletResistReduction` -10, `BonusMoveSpeed` 2, `DPS` 20, `ReduceFootstepSound` -50

**Swift Striker** (passive)
  
*builds from: upgrade_rapid_rounds*

| property | value |
|---|---|
| BonusFireRate | 20 |
| BonusSprintSpeed | 0.750 |
- upgrade 1: `BonusFireRate` 15, `BonusSprintSpeed` 4

**Titanic Magazine** (passive)
  
*builds from: upgrade_clip_size*

| property | value |
|---|---|
| BonusClipSizePercent | 100 |
| BaseAttackDamagePercent | 14 |
- upgrade 1: `BaseAttackDamagePercent` 18, `BonusClipSizePercent` 70

**Weakening Headshot** (passive)
  
> Landing a Headshot reduces their Bullet Resist.

| property | value |
|---|---|
| BulletResistReduction | -12 |
| DebuffDuration | 12 |
| DiminishingMultiplier | 0.500 |
| BonusHealth | 60 |
- upgrade 1: `BulletResistReduction` -7, `BonusHealth` 125

### Tier 3 — 3200 souls


**Alchemical Fire** (ACTIVE)
  
> Throw a flask that explodes on contact, creating an area that does increasing spirit damage per second and reduces enemy Bullet Resist.50% less effective vs non-heroes.

| property | value |
|---|---|
| AbilityCooldown | 30 |
| AbilityDuration | 5 |
| AbilityCastDelay | 0.200 |
| DPS | 45 |
| DPSIncrease | 7 |
| DPSMax | 95 |
| NonHeroReductionPercent | 50 |
| Radius | 10 |
| HeightOffGround | 50 |
| TickRate | 0.500 |
| BulletArmorReduction | -7 |
| SpiritPower | 10 |
- upgrade 1: `DPS` 30, `DPSMax` 30, `BulletArmorReduction` -8, `SpiritPower` 15

**Ballistic Enchantment** (passive)
  
*builds from: upgrade_magic_reach*
  
> Imbue an ability with increased range. Dealing damage with that ability grants you increased weapon damage per unique hero hit. Has reduced effect on non-heroes.

| property | value |
|---|---|
| AbilityDuration | 20 |
| TechRangeMultiplier | 22 |
| TechRadiusMultiplier | 22 |
| WeaponPowerPerStack | 20 |
| WeaponPowerPerStackNonHero | 5 |
| NonHeroStackLimit | 8 |
- upgrade 1: `WeaponPowerPerStack` 15, `TechRangeMultiplier` 15, `TechRadiusMultiplier` 15

**Berserker** (passive)
  
> Your Weapon Damage increases as you take sustained damage.

| property | value |
|---|---|
| DamageDuration | 10 |
| DamageToStack | 120 |
| WeaponPowerPerStack | 7 |
| MaxStacks | 10 |
| BulletResist | 8 |
- upgrade 1: `WeaponPowerPerStack` 3, `BulletResist` 8, `MaxStacks` 8

**Blood Tribute** (ACTIVE)
  
> Toggle: Continually sacrifice Health to improve fire rate, Debuff Resistance and Move Speed.

| property | value |
|---|---|
| TechResist | 8 |
| HealthDrainedPerSecond | 50 |
| TickRate | 0.100 |
| BonusFireRate | 35 |
| StatusResistancePercent | 35 |
| InnateStatusResistancePercent | 8 |
| BonusMoveSpeed | 2 |
| OutOfCombatHealthRegen | 4 |
- upgrade 1: `HealthDrainedPerSecond` -20, `BonusFireRate` 30, `TechResist` 14, `OutOfCombatHealthRegen` 8

**Burst Fire** (passive)
  
*builds from: upgrade_rapid_rounds*
  
> Briefly gain Fire Rate and Move Speed when one of your bullets hits an enemy hero.

| property | value |
|---|---|
| AbilityCooldown | 9 |
| AbilityDuration | 4.500 |
| BonusFireRate | 10 |
| ActivatedFireRate | 32 |
| SlideScale | 50 |
| BonusMoveSpeed | 1.250 |
- upgrade 1: `SlideScale` 50, `ActivatedFireRate` 15, `BonusMoveSpeed` 1.500, `BonusFireRate` 14, `AbilityCooldown` -1

**Cultist Sacrifice** (ACTIVE)
  
*builds from: upgrade_non_player_bonus*
  
> Target an enemy NPC and consume it for 170% Bonus Souls and grants a powerful long lasting buff.

| property | value |
|---|---|
| AbilityCooldown | 270 |
| AbilityDuration | 160 |
| AbilityCastRange | 7 |
| NonPlayerBonusWeaponPower | 30 |
| OutOfCombatHealthRegen | 2 |
| NonPlayerBulletResist | 30 |
| BonusSoulsPct | 170 |
| BonusHealth | 50 |
| BaseAttackDamagePercent | 10 |
| BonusAbilityCharges | 1 |
| TechRangeMultiplier | 12 |
| TechRadiusMultiplier | 12 |
- upgrade 1: `TechRadiusMultiplier` 40, `TechRangeMultiplier` 40, `BaseAttackDamagePercent` 47, `BonusHealth` 300, `NonPlayerBonusWeaponPower` 30, `NonPlayerBulletResist` 30

**Escalating Resilience** (passive)
  
*builds from: upgrade_clip_size*
  
> Grants Bullet Resist when your bullets hit an enemy hero. Each shot can only grant one stack.

| property | value |
|---|---|
| MaxArmorStacks | 30 |
| BulletResistPerStack | 2 |
| BulletResistDuration | 24 |
| BaseAttackDamagePercent | 18 |
| BonusHealth | 75 |
| BonusClipSizePercent | 35 |
- upgrade 1: `BulletResistPerStack` 2, `MaxArmorStacks` 20, `BonusClipSizePercent` 30, `BonusHealth` 125, `WeaponPower` 10

**Express Shot** (passive)
  
*builds from: upgrade_high_velocity_mag*
  
> Your next attack will fire twice in quick succession with increased damage and velocity. This attack consumes extra ammo.

| property | value |
|---|---|
| AbilityCooldown | 8 |
| BonusBulletSpeedPercent | 60 |
| BaseAttackDamagePercent | 8 |
| ProcAmmoConsumed | 2 |
| ProcBulletVelocity | 100 |
| ProcBaseAttackDamagePercent | 125 |
| ProcBaseAttackDamagePercentAltFire | 40 |
- upgrade 1: `ProcBaseAttackDamagePercent` 75, `ProcBaseAttackDamagePercentAltFire` 25, `BonusBulletSpeedPercent` 45, `BaseAttackDamagePercent` 15

**Headhunter** (passive)
  
*builds from: upgrade_headshot_booster*
  
> Your next headshot against an enemy Hero deals bonus weapon damage, heal you, and briefly grants bonus move speed.

| property | value |
|---|---|
| AbilityCooldown | 8 |
| HeadShotBonusDamage | 75 |
| BaseAttackDamagePercent | 5 |
| BonusHealth | 50 |
| HealPercentPerHeadshot | 4 |
| BonusMoveSpeed | 1.750 |
| MovementSpeedBonusDuration | 3 |
| ProcChance | 100 |
- upgrade 1: `HeadShotBonusDamage` 75, `HealPercentPerHeadshot` 4, `AbilityCooldown` -3

**Heroic Aura** (ACTIVE)
  
> Provides Bullet Resist to nearby friendly units.

| property | value |
|---|---|
| AbilityCooldown | 22 |
| AbilityDuration | 7 |
| BonusFireRate | 26 |
| Radius | 35 |
| ActiveRadius | 35 |
| ActiveBonusMoveSpeed | 2.250 |
| BulletResist | 17 |
| NonHeroMult | 2 |
| BonusSprintSpeed | 1.500 |
- upgrade 1: `ActiveBonusMoveSpeed` 3, `BonusFireRate` 34, `BulletResist` 10, `ActiveRadius` 15

**Hollow Point** (passive)
  
> When you are above 65% health, deal additional Weapon Damage and your bullets reduce enemy Bullet Resist.

| property | value |
|---|---|
| LifeThreshold | 65 |
| BaseAttackDamagePercent | 35 |
| OutOfCombatHealthRegen | 4.500 |
| BonusHealth | 125 |
| BulletArmorReduction | -10 |
| DebuffDuration | 8 |
- upgrade 1: `BulletArmorReduction` -12, `BonusHealth` 150, `BaseAttackDamagePercent` 25

**Hunter's Aura** (passive)
  
> Reduces nearby enemies' Bullet Resist and Fire Rate. If there is only one enemy hero nearby, this effect is doubled.

| property | value |
|---|---|
| BonusHealth | 100 |
| Radius | 15 |
| BulletArmorReduction | -10 |
| FireRateSlow | 15 |
| SingleTargetPlayerMultiplier | 2 |
| BonusSprintSpeed | 0.750 |
- upgrade 1: `FireRateSlow` 5, `BulletArmorReduction` -6, `BonusHealth` 125, `BonusSprintSpeed` 3

**Point Blank** (passive)
  
*builds from: upgrade_close_range*
  
> When in close range to your target, gain Weapon Damage and your bullets apply a Movement Slow.

| property | value |
|---|---|
| CloseRangeBonusWeaponPower | 50 |
| SlowPercent | 20 |
| SlowDuration | 2 |
| CloseRangeBonusDamageRange | 15 |
| MeleeResistPercent | 30 |
| BonusHealth | 75 |
- upgrade 1: `CloseRangeBonusWeaponPower` 30, `MeleeResistPercent` 30, `BonusHealth` 150, `SlowPercent` 4

**Shadow Weave** (ACTIVE)
  
*builds from: upgrade_sprint_booster*
  
> Become Stealthed. Whenever you take damage while Stealthed you get briefly revealed.

| property | value |
|---|---|
| AbilityCooldown | 37 |
| AbilityDuration | 13 |
| InvisAlertWhenFading | 1 |
| InvisCancelOnDamage | 1 |
| InvisFadeToDuration | 0.600 |
| InvisMoveSpeedMod | 5 |
| SpottedRadius | 20 |
| RevealOnDamageDuration | 1.500 |
| RevealOnSpottedDuration | 1.500 |
| FullInvisDistance | 30 |
| AmbushDuration | 5 |
| AmbushBonusFireRate | 25 |
| AmbushBonusTechPower | 25 |
| AmbushBonusMeleeDamage | 25 |
| OutOfCombatHealthRegen | 5 |
| BonusSprintSpeed | 2 |
- upgrade 1: `OutOfCombatHealthRegen` 20, `AmbushBonusFireRate` 35, `AmbushBonusMeleeDamage` 30, `AmbushBonusTechPower` 35, `AbilityCooldown` -17

**Sharpshooter** (passive)
  
*builds from: upgrade_long_range, upgrade_high_velocity_mag*
  
> Deal additional Weapon Damage when beyond a minimum distance from your target.

| property | value |
|---|---|
| BaseAttackDamagePercent | 10 |
| LongRangeBonusWeaponPower | 60 |
| LongRangeBonusWeaponPowerMinRange | 15 |
| BonusAttackRangePercent | 20 |
| BonusZoomPercent | 25 |
| BonusMoveSpeed | -0.700 |
| BonusSprintSpeed | 1 |
| BonusBulletSpeedPercent | 60 |
- upgrade 1: `LongRangeBonusWeaponPower` 40, `BonusAttackRangePercent` 10, `BonusBulletSpeedPercent` 45, `BaseAttackDamagePercent` 15

**Spirit Rend** (passive)
  
*builds from: upgrade_tech_defense_shredders*

| property | value |
|---|---|
| ProcCooldown | 2 |
| BonusHealth | 75 |
| MaxStacks | 4 |
| AbilityLifestealPercentHero | 10 |
| MagicResistReduction | -7 |
| TechArmorDamageReduction | -8 |
| DebuffDuration | 8 |
- upgrade 1: `MagicResistReduction` -5, `AbilityLifestealPercentHero` 10, `TechArmorDamageReduction` -10

**Tesla Bullets** (passive)
  
> Your bullets have a chance to shock your target. The shock will jump to a nearby enemy.

| property | value |
|---|---|
| ProcCooldown | 0.200 |
| DamagePerChain | 33 |
| BonusPerChain | 33 |
| ChainRadius | 8 |
| ProcChance | 15 |
| ChainCount | 4 |
| ChainTickRate | 0.400 |
- upgrade 1: `DamagePerChain` 25, `BonusPerChain` 25

**Toxic Bullets** (passive)
  
> Your bullets build up a Bleed on enemies, causing them to lose a percentage of their Max Health over time. Also applies Healing Reduction on the bleeding target.

| property | value |
|---|---|
| DotHealthPercent | 1.900 |
| DotDuration | 4 |
| BuildUpPerShot | 1.280 |
| BuildUpDuration | 5 |
| TickRate | 0.500 |
| HealAmpReceivePenaltyPercent | -35 |
| HealAmpRegenPenaltyPercent | -35 |
| DotMultiplerTroopers | 0.500 |
- upgrade 1: `HealAmpReceivePenaltyPercent` -30, `HealAmpRegenPenaltyPercent` -30, `DotHealthPercent` 0.700

**Weighted Shots** (passive)
  
*builds from: upgrade_slowing_bullets*
  
> Your bullets build up a Movement Slow on enemies.

| property | value |
|---|---|
| BaseAttackDamagePercent | 30 |
| StatusResistancePercent | 22 |
| StaminaCooldownReduction | -14 |
| SlowPercent | 24 |
| GroundDashReductionPercent | -20 |
| SlowDuration | 3.500 |
| BonusMoveSpeed | -0.500 |
| BuildUpDuration | 5 |
| BuildUpPerShot | 0.700 |
- upgrade 1: `StatusResistancePercent` 10, `BaseAttackDamagePercent` 35, `SlowPercent` 16, `GroundDashReductionPercent` -8

### Tier 4 — 6400 souls


**Armor Piercing Rounds** (passive)
  
*builds from: upgrade_high_velocity_mag*
  
> Your Bullets have a chance to become unavoidable, piercing through enemies and ignoring their Bullet Resistance.

| property | value |
|---|---|
| BonusBulletSpeedPercent | 60 |
| ProcChance | 55 |
| BaseAttackDamagePercent | 8 |
- upgrade 1: `BonusBulletSpeedPercent` 55, `ProcChance` 20, `BaseAttackDamagePercent` 30

**Capacitor** (ACTIVE)
  
*builds from: upgrade_chain_lightning*
  
> Launch a projectile that deals damage, applies a strong slow that recovers over time, prevents Stamina usage and Silences their movement-based items and abilities.

| property | value |
|---|---|
| AbilityCooldown | 40 |
| AbilityCastDelay | 0.200 |
| ProcCooldown | 0.200 |
| DamagePerChain | 43 |
| BonusPerChain | 43 |
| ChainRadius | 10 |
| ProcChance | 20 |
| ChainCount | 6 |
| ChainTickRate | 0.400 |
| Damage | 100 |
| MaxSlowPercent | 60 |
| SlowDuration | 3 |
| BonusFireRate | 5 |
- upgrade 1: `ProcChance` 5, `BonusFireRate` 15, `DamagePerChain` 25, `AbilityCooldown` -32, `Damage` 25

**Crippling Headshot** (passive)
  
*builds from: upgrade_headshot_booster2*
  
> Landing a Headshot will reduce their Bullet and Spirit Resist and applies Healing Reduction.

| property | value |
|---|---|
| BonusHealth | 125 |
| BulletResistReduction | -16 |
| MagicResistReduction | -16 |
| HealAmpReceivePenaltyPercent | -35 |
| HealAmpRegenPenaltyPercent | -35 |
| DebuffDuration | 12 |
| DiminishingMultiplier | 0.500 |
- upgrade 1: `MagicResistReduction` -12, `BulletResistReduction` -12, `HealAmpReceivePenaltyPercent` -25, `HealAmpRegenPenaltyPercent` -25, `BonusHealth` 150

**Crushing Fists** (passive)
  
*builds from: upgrade_melee_charge*
  
> Your melee damage will restore ammo and apply a stacking bullet resist debuff on enemies. Heavy melee applies 2 stacks. If the target reaches max stacks, they will be stunned.

| property | value |
|---|---|
| AbilityCooldown | 5 |
| BulletResist | 12 |
| BonusMeleeDamagePercent | 22 |
| MeleeDistanceScale | 60 |
| BonusHeavyMeleeDamage | 25 |
| MaxStacks | 6 |
| DebuffDuration | 8 |
| StunDuration | 0.750 |
| LightMeleeStacks | 1 |
| LightMeleeAmmo | 15 |
| HeavyMeleeMultiplier | 2 |
| BulletResistReduction | -5 |
- upgrade 1: `MeleeDistanceScale` 40, `BulletResist` 12, `BonusMeleeDamagePercent` 15, `BulletResistReduction` -4, `BonusHeavyMeleeDamage` 15

**Frenzy** (passive)
  
> While you are below 50% health, you gain stat bonuses for a duration and existing debuffs on you are reduced.

| property | value |
|---|---|
| AbilityCooldown | 16 |
| AbilityDuration | 10 |
| LowHealthThreshold | 50 |
| BonusHealth | 160 |
| BonusFireRate | 15 |
| BulletLifestealPercent | 10 |
| FervorMovespeed | 4 |
| FervorFireRate | 40 |
| FervorStatusResistancePercent | 40 |
- upgrade 1: `BonusHealth` 125, `FervorFireRate` 20, `FervorMovespeed` 3, `FervorStatusResistancePercent` 15

**Glass Cannon** (passive)
  
> Each hero kill grants permanent Fire Rate (up to a max of 8 times). Death results in the loss of 1 stack.

| property | value |
|---|---|
| BaseAttackDamagePercent | 80 |
| MaxHealthLossPercent | -13 |
| BonusClipPerKill | 2 |
| FireRatePerKill | 7 |
| MaxStacks | 8 |
| SlowPercent | 30 |
| SlowDuration | 3 |
| BuildUpDuration | 2 |
| BuildUpPerShot | 1.200 |
- upgrade 1: `FireRatePerKill` 8, `BaseAttackDamagePercent` 60

**Lucky Shot** (passive)
  
> Your bullets have a chance to be empowered, causing them to deal bonus weapon damage on hit.Bonus damage cannot Crit.

| property | value |
|---|---|
| Radius | 1 |
| ProcChance | 25 |
| CritDamagePercent | 100 |
| BonusClipSizePercent | 30 |
- upgrade 1: `CritDamagePercent` 30, `BonusClipSizePercent` 40, `ProcChance` 5

**Ricochet** (passive)
  
> Your bullets will ricochet on enemies near your target, applying any bullet procs and dealing a percentage of the original damage.

| property | value |
|---|---|
| RicochetDamagePercent | 65 |
| RicochetRadius | 13 |
| RicochetTargetsTooltipOnly | 2 |
| BonusFireRate | 18 |
- upgrade 1: `RicochetDamagePercent` 15, `BonusFireRate` 25

**Silencer** (passive)
  
> Your bullets build up to a Silence. Victims are immune to the build up for 10s after silence expires.

| property | value |
|---|---|
| TechResist | 12 |
| TechDamageReduction | -25 |
| SilenceDuration | 2.500 |
| DebuffDuration | 6 |
| ImmunityDuration | 10 |
| BuildUpPerShot | 1.040 |
| BuildUpDuration | 5 |
- upgrade 1: `TechDamageReduction` -15, `SilenceDuration` 1.250, `TechResist` 15

**Spellslinger** (passive)
  
> While in-combat whenever you cast an ability or item, gain a stacking buff that improves fire rate and reload speed. Each stack refreshes the duration.

| property | value |
|---|---|
| CooldownReduction | 5 |
| BonusFireRate | 11 |
| ReloadSpeedMultipler | -10 |
| BuffDuration | 18 |
| MaxStacks | 6 |
- upgrade 1: `ReloadSpeedMultipler` -3, `BonusFireRate` 6, `CooldownReduction` 8

**Spiritual Overflow** (passive)
  
*builds from: upgrade_health_stealing_magic*
  
> Gain bonus Fire Rate, Spirit Power and Spirit Lifesteal by charging up when shooting enemy heroes.

| property | value |
|---|---|
| AbilityDuration | 15 |
| TechPower | 6 |
| AbilityLifestealPercentHero | 13 |
| NonHeroAbilityLifestealTooltipOnly | 3 |
| BonusHealth | 90 |
| BonusFireRate | 25 |
| BonusSpirit | 30 |
| BonusSpiritLifesteal | 10 |
| BonusAbilityDurationPercent | 13 |
| BuildUpPerShot | 1.080 |
| BuildUpDuration | 5 |
- upgrade 1: `BonusAbilityDurationPercent` 15, `BonusSpirit` 30, `BonusFireRate` 20, `AbilityLifestealPercentHero` 15, `BonusHealth` 80, `TechPower` 9

## VITALITY items


### Tier 1 — 800 souls


**Extra Health** (passive)

| property | value |
|---|---|
| BonusHealth | 210 |
- upgrade 1: `BonusHealth` 115

**Extra Regen** (passive)

| property | value |
|---|---|
| BonusHealthRegen | 2.500 |
| OutOfCombatHealthRegen | 1.500 |
- upgrade 1: `BonusHealthRegen` 9

**Extra Stamina** (passive)

| property | value |
|---|---|
| Stamina | 1 |
| StaminaCooldownReduction | 12 |
- upgrade 1: `Stamina` 1, `StaminaCooldownReduction` 14

**Grit** (ACTIVE)
  
> Gain a Barrier for a short duration.

| property | value |
|---|---|
| AbilityCooldown | 60 |
| CombatBarrier | 200 |
| OutOfCombatHealthRegen | 1 |
| BarrierDuration | 4 |
- upgrade 1: `CombatBarrier` 250, `OutOfCombatHealthRegen` 10, `AbilityCooldown` -25

**Healing Rite** (ACTIVE)
  
> Grant Regen and Sprint Speed to the target. Gets dispelled if you take damage from enemy players or objectives. Can be self-cast.

| property | value |
|---|---|
| AbilityCooldown | 70 |
| AbilityCastRange | 30 |
| AbilityCastDelay | 0.200 |
| TotalHealthRegen | 300 |
| RegenDuration | 20 |
| BonusSprintSpeed | 2 |
- upgrade 1: `TotalHealthRegen` 600, `BonusSprintSpeed` 6, `AbilityCooldown` -60

**Melee Lifesteal** (passive)
  
> Your next Melee attack heals you. This heal is 30% effective vs non-heroes. Cooldown is 1.5x as long for Light Melee hits.

| property | value |
|---|---|
| AbilityCooldown | 8 |
| LightMeleeCooldownMult | 1.500 |
| BonusMeleeDamagePercent | 12 |
| LifestrikeHeal | 100 |
| NonHeroHealPct | 30 |
- upgrade 1: `BonusMeleeDamagePercent` 12, `AbilityCooldown` -6

**Rebuttal** (passive)
  
> On a successful Parry against an enemy Hero, Heal yourself for the damage parried and returns that damage to the target, and temporarily gain increased damage.

| property | value |
|---|---|
| BonusHealth | 75 |
| ParryCooldownReduction | 1.750 |
| BuffDuration | 6 |
| BonusDamagePercent | 30 |
| ParrySuccessHealPercentage | 100 |
| MeleeResistPercent | 18 |
- upgrade 1: `ParryCooldownReduction` 0.500, `MeleeResistPercent` 22, `BonusDamagePercent` 20, `BonusHealth` 150

**Sprint Boots** (passive)

| property | value |
|---|---|
| BonusSprintSpeed | 2 |
| OutOfCombatHealthRegen | 2 |
- upgrade 1: `OutOfCombatHealthRegen` 8, `BonusSprintSpeed` 12

### Tier 2 — 1600 souls


**Battle Vest** (passive)
  
> While you are above 65% health, gain weapon damage and bonus fire rate.

| property | value |
|---|---|
| BulletResist | 18 |
| OutOfCombatHealthRegen | 3 |
| LifeThreshold | 65 |
| BaseAttackDamagePercent | 18 |
| BonusFireRate | 7 |
- upgrade 1: `OutOfCombatHealthRegen` 3, `BulletResist` 12, `BaseAttackDamagePercent` 15, `BonusFireRate` 8

**Bullet Lifesteal** (passive)

| property | value |
|---|---|
| BulletLifestealPercent | 13 |
| BonusHealth | 90 |
| BaseAttackDamagePercent | 6 |
- upgrade 1: `BulletLifestealPercent` 16, `BonusHealth` 120

**Debuff Reducer** (passive)
  
> Reduces the duration of all negative effects applied to you.

| property | value |
|---|---|
| StatusResistancePercent | 25 |
| BonusHealth | 90 |
- upgrade 1: `StatusResistancePercent` 15

**Enchanter's Emblem** (passive)
  
> While you are above 65% health, gain bonus Spirit and Cooldown Reduction.

| property | value |
|---|---|
| TechPower | 15 |
| TechResist | 18 |
| OutOfCombatHealthRegen | 2 |
| LifeThreshold | 65 |
| CooldownReduction | 5 |
- upgrade 1: `TechResist` 13, `OutOfCombatHealthRegen` 3, `TechPower` 15, `CooldownReduction` 7

**Enduring Speed** (passive)
  
*builds from: upgrade_sprint_booster*
  
> Reduces the effect of enemy Move Speed penalties.

| property | value |
|---|---|
| BonusMoveSpeed | 2 |
| SlowResistancePercent | 25 |
| OutOfCombatHealthRegen | 2 |
- upgrade 1: `SlowResistancePercent` 30, `BonusMoveSpeed` 2, `OutOfCombatHealthRegen` 8

**Guardian Ward** (ACTIVE)
  
*builds from: upgrade_grit*
  
> Provide the target with a Barrier and temporary Move Speed. Can be self-cast.Cooldown is reduced by half when cast on someone else.

| property | value |
|---|---|
| AbilityCooldown | 60 |
| AbilityCastRange | 40 |
| AbilityCastDelay | 0.200 |
| CooldownReductionPctOnOthers | 50 |
| OutOfCombatHealthRegen | 1.500 |
| BuffDuration | 6 |
| GuardianWardCombatBarrier | 250 |
| BonusMoveSpeed | 2.750 |
| TechRangeMultiplier | 8 |
| TechRadiusMultiplier | 8 |
- upgrade 1: `TechRangeMultiplier` 12, `TechRadiusMultiplier` 12, `GuardianWardCombatBarrier` 250, `ChannelMoveSpeed` 2, `AbilityCooldown` -12

**Healbane** (passive)
  
> Your spirit damage applies Healing Reduction. If an enemy hero dies under this effect, you receive a large heal.

| property | value |
|---|---|
| AbilityDuration | 8 |
| TechPower | 7 |
| HealAmpReceivePenaltyPercent | -35 |
| HealAmpRegenPenaltyPercent | -35 |
| HealOnKill | 275 |
- upgrade 1: `HealAmpRegenPenaltyPercent` -20, `HealAmpReceivePenaltyPercent` -20, `TechPower` 11, `HealOnKill` 125

**Healing Booster** (passive)
  
*builds from: upgrade_endurance*
  
> Increases the effectiveness of your healing.

| property | value |
|---|---|
| HealAmpCastPercent | 20 |
| HealAmpRegenPercent | 20 |
| BonusHealthRegen | 3 |
| OutOfCombatHealthRegen | 1 |
- upgrade 1: `HealAmpRegenPercent` 15, `HealAmpCastPercent` 15, `BonusHealthRegen` 9

**Reactive Barrier** (passive)
  
*builds from: upgrade_grit*
  
> Gain a Barrier when you are Stunned, Chained, Immobilized, Slept or Silenced.

| property | value |
|---|---|
| AbilityCooldown | 55 |
| AbilityDuration | 10 |
| VexBarrierCombatBarrier | 325 |
| OutOfCombatHealthRegen | 1 |
- upgrade 1: `VexBarrierCombatBarrier` 375, `AbilityCooldown` -15

**Restorative Locket** (ACTIVE)
  
> When an enemy uses an ability within 32mm range from you, store one Restoration Stack. Consume all stacks to heal yourself and replenish up to 3 stamina based on how many stacks you have.

| property | value |
|---|---|
| AbilityCooldown | 20 |
| AbilityCastRange | 32 |
| AbilityCastDelay | 0.100 |
| Radius | 32 |
| TechResist | 8 |
| HealPerStack | 16 |
| MaxStacks | 25 |
| MaxStaminaRestore | 3 |
- upgrade 1: `TechResist` 10, `HealPerStack` 30, `AbilityCooldown` -8, `MaxStaminaRestore` 2, `MinStaminaRestore` 2

**Return Fire** (ACTIVE)
  
> Automatically fire a bullet towards any attacker who damages you with their abilities or weapon.

| property | value |
|---|---|
| AbilityCooldown | 23 |
| AbilityDuration | 6.500 |
| BulletDamageReflectedPct | 65 |
| SpiritDamageReflectedPct | 25 |
| BulletResist | 10 |
- upgrade 1: `BulletResist` 16, `SpiritDamageReflectedPct` 15, `BulletDamageReflectedPct` 25, `AbilityCooldown` -10

**Spirit Lifesteal** (passive)

| property | value |
|---|---|
| TechPower | 6 |
| AbilityLifestealPercentHero | 13 |
| NonHeroAbilityLifestealTooltipOnly | 3 |
| BonusHealth | 90 |
- upgrade 1: `AbilityLifestealPercentHero` 14, `BonusHealth` 80, `TechPower` 9

**Spirit Shielding** (passive)
  
*builds from: upgrade_grit*
  
> Gain a Barrier whenever you take significant spirit damage from enemy Heroes in a small time frame.

| property | value |
|---|---|
| AbilityCooldown | 45 |
| DamageWindow | 3.500 |
| DamageThreshold | 225 |
| CombatBarrier | 300 |
| OutOfCombatHealthRegen | 2.500 |
| BarrierDuration | 8 |
| TechResist | 18 |
- upgrade 1: `OutOfCombatHealthRegen` 3, `CombatBarrier` 175, `TechResist` 20, `AbilityCooldown` -20

**Trophy Collector** (passive)
  
*builds from: upgrade_sprint_booster*
  
> Whenever you score an assist or kill, gain extra sprint, ability range and passive soul generation. This effect stacks and persists through death.

| property | value |
|---|---|
| BonusSprintSpeed | 2 |
| OutOfCombatHealthRegen | 2 |
| StackingBonusSprintSpeed | 0.150 |
| StackingTechRangeMultiplier | 0.750 |
| StackingTechRadiusMultiplier | 0.750 |
| StackingGoldPerMinute | 16 |
| ThinkRate | 3 |
| MaxStacks | 16 |
| NonPlayerBonusWeaponPower | -15 |
- upgrade 1: `StackingTechRadiusMultiplier` 3, `StackingTechRangeMultiplier` 3, `OutOfCombatHealthRegen` 6, `BonusSprintSpeed` 12, `MaxStacks` 83

**Weapon Shielding** (passive)
  
*builds from: upgrade_grit*
  
> Gain a Barrier whenever you take significant weapon damage from enemy Heroes in a small time frame.

| property | value |
|---|---|
| AbilityCooldown | 35 |
| DamageWindow | 4 |
| DamageThreshold | 250 |
| CombatBarrier | 300 |
| OutOfCombatHealthRegen | 2.500 |
| BarrierDuration | 8 |
| BulletResist | 18 |
- upgrade 1: `OutOfCombatHealthRegen` 3, `CombatBarrier` 225, `BulletResist` 15, `AbilityCooldown` -20

### Tier 3 — 3200 souls


**Bullet Resilience** (passive)
  
> When below 50% health, gain additional Bullet Resist.

| property | value |
|---|---|
| BulletResist | 30 |
| HealthThreshold | 50 |
| BulletResistBelowThreshold | 15 |
| OutOfCombatHealthRegen | 3 |
- upgrade 1: `BulletResist` 10, `BulletResistBelowThreshold` 10

**Counterspell** (passive)
  
> Your next parry protects you from the damage and effects of enemy abilities and items. On a successful spell parry heal and gain move speed and Spirit.

| property | value |
|---|---|
| AbilityCooldown | 23 |
| SpiritPower | 20 |
| BonusMoveSpeed | 1.750 |
| BuffDuration | 6 |
| SpellParryDuration | 0.800 |
| BonusHealth | 50 |
| SpiritPowerInnate | 5 |
| HealOnSuccess | 150 |
- upgrade 1: `SpiritPower` 20, `BonusHealth` 150, `HealOnSuccess` 250, `BonusMoveSpeed` 2, `AbilityCooldown` -8

**Dispel Magic** (ACTIVE)
  
> Purge all non-ultimate negative effects currently applied to you. If any effects were removed, heal yourself and gain a move speed bonus. Cannot be used while Stunned or Slept.

| property | value |
|---|---|
| AbilityCooldown | 45 |
| TechResist | 10 |
| ActiveBonusMoveSpeed | 2 |
| BuffDuration | 3 |
| HealOnActivate | 250 |
- upgrade 1: `HealOnActivate` 150, `TechResist` 20, `AbilityCooldown` -25

**Fortitude** (passive)
  
*builds from: upgrade_health*
  
> After not taking damage for a period, gain health regen.

| property | value |
|---|---|
| RestoreDelay | 10 |
| HealLifePercentOutOfCombat | 2.250 |
| HealthThreshold | 75 |
| BonusMoveSpeed | 1.500 |
| BonusHealth | 375 |
- upgrade 1: `RestoreDelay` -6, `BonusHealth` 375, `BonusMoveSpeed` 1, `HealLifePercentOutOfCombat` 1

**Fury Trance** (ACTIVE)
  
*builds from: upgrade_vampire*
  
> Grants Fire Rate, Spirit Resistance and Move Speed, and removes the Move Speed penalty while shooting, but Silences you and disables stamina usage and regeneration.

| property | value |
|---|---|
| AbilityCooldown | 18 |
| AbilityDuration | 6.500 |
| BulletLifestealPercent | 14 |
| ActiveBonusFireRate | 32 |
| TechResist | 40 |
| BonusHealth | 100 |
| BaseAttackDamagePercent | 6 |
| ActiveBonusMoveSpeed | 1 |
| MoveWhileShootingSpeedPenaltyReductionPercent | 100 |
- upgrade 1: `BulletLifestealPercent` 28, `ActiveBonusFireRate` 25, `TechResist` 20, `BonusHealth` 110

**Healing Nova** (ACTIVE)
  
*builds from: upgrade_health_stimpak*
  
> Heal yourself and nearby allies.

| property | value |
|---|---|
| AbilityCooldown | 60 |
| AbilityCastDelay | 0.250 |
| TotalHealthRegen | 325 |
| RegenDuration | 2 |
| AuraRadius | 18 |
| SpiritPower | 8 |
| TechRangeMultiplier | 5 |
| TechRadiusMultiplier | 5 |
- upgrade 1: `TechRadiusMultiplier` 12, `TechRangeMultiplier` 12, `TechPower` 12, `TotalHealthRegen` 425

**Lifestrike** (passive)
  
*builds from: upgrade_lifestrike_gauntlets*
  
> Your Melee Attack applies Movement Slow and heals you for a percentage of the Melee Damage dealt plus a fixed amount. This heal is 40% effective vs non-heroes. Cooldown is 1.5x as long for Light Melee hits.

| property | value |
|---|---|
| AbilityCooldown | 4 |
| LightMeleeCooldownMult | 1.500 |
| SlowPercent | 48 |
| SlowDuration | 2.500 |
| BonusMeleeDamagePercent | 16 |
| LifestealHeal | 120 |
| LifestealHealPercent | 35 |
| BonusHealth | 125 |
| NonHeroHealPct | 40 |
- upgrade 1: `BonusMeleeDamagePercent` 10, `BonusHealth` 125, `AbilityCooldown` -3

**Majestic Leap** (ACTIVE)
  
> Launch yourself high into the air and grant yourself a Barrier. While in the air, you can use the active again to drop down faster.Cannot be used for 5s if attacked by enemy Hero.

| property | value |
|---|---|
| AbilityCooldown | 45 |
| JumpVelocityHidden | 27 |
| InterruptCooldown | 5 |
| AirControlPercent | 100 |
| AirControlPercentBarrier | 50 |
| SlamDownRadius | 10 |
| VerticalDifferenceTolerance | 2 |
| TossSpeed | 500 |
| SlowPercent | 32 |
| SlowDuration | 2.500 |
| DropDownSpeed | 35 |
| MaxLandingSpeed | 20 |
| ImpactHeight | 2 |
| MinAimAngle | 30 |
| CombatBarrier | 200 |
| BarrierDuration | 8 |
- upgrade 1: `AbilityCooldown` -35, `CombatBarrier` 275, `InterruptCooldown` -3

**Metal Skin** (ACTIVE)
  
> Become immune to bullets.

| property | value |
|---|---|
| AbilityCooldown | 24 |
| AbilityDuration | 5 |
| BulletResist | 12 |
| ActiveMoveSpeedPenalty | -1.500 |
| GroundDashReductionPercent | -20 |
- upgrade 1: `ActiveMoveSpeedPenalty` 6.500, `GroundDashReductionPercent` 60, `AbilityCooldown` -2, `BulletResist` 5

**Rescue Beam** (ACTIVE)
  
*builds from: upgrade_health_stimpak*
  
> Heals a target allied hero and yourself for a percentage of Max Health. Once while healing, you can Pull the target towards you. Can be self-cast.

| property | value |
|---|---|
| AbilityCooldown | 60 |
| AbilityCastRange | 35 |
| AbilityChannelTime | 2.500 |
| HealPercentAmount | 20 |
| HealInterval | 0.200 |
| BonusSprintSpeed | 0.750 |
| SelfModifier | 100 |
| TechRangeMultiplier | 6 |
| TechRadiusMultiplier | 6 |
- upgrade 1: `TechRadiusMultiplier` 20, `TechRangeMultiplier` 20, `HealPercentAmount` 15, `AbilityCooldown` -45

**Spirit Resilience** (passive)
  
> When below 50% health, gain additional Spirit Resist.

| property | value |
|---|---|
| TechResist | 30 |
| HealthThreshold | 50 |
| TechResistBelowThreshold | 15 |
| OutOfCombatHealthRegen | 3 |
- upgrade 1: `TechResist` 10, `TechResistBelowThreshold` 10

**Stamina Mastery** (passive)
  
*builds from: upgrade_improved_stamina*
  
> Allows an additional use of Air Jump or Air Dash before landing.

| property | value |
|---|---|
| Stamina | 2 |
| StaminaCooldownReduction | 18 |
| AirMoveIncreasePercent | 23 |
- upgrade 1: `Stamina` 2, `AirMoveIncreasePercent` 40, `StaminaCooldownReduction` 15

**Veil Walker** (passive)
  
> Walking through a cosmic veil grants you Stealth, Heal and increased Move Speed.

| property | value |
|---|---|
| AbilityCooldown | 15 |
| AbilityDuration | 16 |
| InvisAlertWhenFading | 1 |
| InvisFadeToDuration | 0.250 |
| SpottedRadius | 20 |
| RevealOnDamageDuration | 0.500 |
| RevealOnSpottedDuration | 1.250 |
| BonusHealth | 125 |
| SpiritPower | 6 |
| InvisDuration | 8 |
| BonusMoveSpeed | 3.500 |
| HealOnVeil | 85 |
- upgrade 1: `SpiritPower` 25, `InvisMoveSpeedMod` 6, `HealOnVeil` 300, `AbilityCooldown` -9, `InvisDuration` 4, `BonusMoveSpeed` 4, `OutOfCombatHealthRegen` 8, `BonusSprintSpeed` 12

**Warp Stone** (ACTIVE)
  
> Teleport straight ahead, gaining Bullet Resist.

| property | value |
|---|---|
| AbilityCooldown | 16 |
| AbilityCastRange | 11 |
| BulletResist | 30 |
| CasterBuffDuration | 6 |
- upgrade 1: `BulletResist` 20, `AbilityCastRange` 9, `AbilityCooldown` -3

### Tier 4 — 6400 souls


**Cheat Death** (passive)

| property | value |
|---|---|
| AbilityCooldown | 90 |
| DeathImmunityDuration | 4.500 |
| BonusHealth | 200 |
| BulletResist | 15 |
| DeathImmunityDamageReduction | -60 |
| HealAmpReceivePenaltyPercent | -60 |
| HealAmpRegenPenaltyPercent | -60 |
- upgrade 1: `DeathImmunityDamageReduction` 90, `HealAmpReceivePenaltyPercent` 90, `HealAmpRegenPenaltyPercent` 90, `DeathImmunityDuration` 0.500, `AbilityCooldown` -20

**Colossus** (ACTIVE)
  
*builds from: upgrade_health*
  
> Grow larger in size, gaining bullet resist, spirit resist, and melee damage. Nearby enemies suffer from slow and have reduced dash speed.

| property | value |
|---|---|
| AbilityCooldown | 37 |
| AbilityDuration | 7 |
| BonusBaseHealth | 25 |
| BaseAttackDamagePercent | 15 |
| BuffBulletResist | 35 |
| BuffTechResist | 35 |
| SlowPercent | 24 |
| GroundDashReductionPercent | -22 |
| Radius | 14 |
| ModelScaleGrowth | 1.200 |
| ModelScaleGrowthTooltip | 20 |
| BonusMeleeDamagePercent | 30 |
- upgrade 1: `BonusBaseHealth` 15, `ModelScaleGrowth` 0.200, `ModelScaleGrowthTooltip` 20, `BuffBulletResist` 10, `BuffTechResist` 10, `AbilityCooldown` -7

**Divine Barrier** (ACTIVE)
  
*builds from: upgrade_guardian_ward*
  
> Remove all non-stun debuffs from the target and provide them with a Barrier and Move Speed. Can be self-cast. Cooldown is reduced by half when cast on someone else.

| property | value |
|---|---|
| AbilityCooldown | 45 |
| AbilityCastRange | 40 |
| AbilityCastDelay | 0.200 |
| OutOfCombatHealthRegen | 1.500 |
| CooldownReductionPctOnOthers | 50 |
| BuffDuration | 6 |
| CombatBarrier | 600 |
| BonusMoveSpeed | 2.750 |
| TechRangeMultiplier | 10 |
| TechRadiusMultiplier | 10 |
- upgrade 1: `AbilityCooldown` -27, `TechRadiusMultiplier` 10, `TechRangeMultiplier` 10

**Diviner's Kevlar** (passive)
  
> Upon casting an ultimate ability gain a Barrier and temporary Spirit Power.

| property | value |
|---|---|
| AbilityCooldown | 40 |
| TechPower | 40 |
| CombatBarrier | 1000 |
| BuffDuration | 20 |
| BonusAbilityDurationPercent | 15 |
| UltimateCooldownReduction | 10 |
- upgrade 1: `BonusAbilityDurationPercent` 15, `TechPower` 55, `CombatBarrier` 500, `AbilityCooldown` -14

**Healing Tempo** (passive)
  
*builds from: upgrade_healing_booster*
  
> Applying heal to yourself or an ally grants the target bonus fire rate and bonus move speed.Does not apply on innate Regen or passive Bullet/Spirit Lifesteals.

| property | value |
|---|---|
| AbilityCooldown | 1 |
| BonusFireRate | 35 |
| BuffDuration | 7 |
| BonusMoveSpeed | 1.250 |
| MinimumHealAmount | 1 |
| TechResist | 10 |
| BonusHealthRegen | 6 |
| HealAmpCastPercent | 25 |
| HealAmpRegenPercent | 25 |
| OutOfCombatHealthRegen | 4 |
- upgrade 1: `HealAmpRegenPercent` 10, `HealAmpCastPercent` 10, `TechResist` 10, `BonusMoveSpeed` 2, `BonusFireRate` 20, `BonusHealthRegen` 6

**Indomitable** (passive)
  
*builds from: upgrade_vex_barrier*

| property | value |
|---|---|
| AbilityCooldown | 55 |
| AbilityDuration | 10 |
| BulletResist | 10 |
| TechResist | 10 |
| CooldownReductionOnProc | 20 |
| VexBarrierCombatBarrier | 325 |
| OutOfCombatHealthRegen | 2 |
- upgrade 1: `BulletResist` 14, `TechResist` 14, `AbilityCooldown` -35, `VexBarrierCombatBarrier` 450

**Infuser** (ACTIVE)
  
*builds from: upgrade_health_stealing_magic*
  
> Gain Spirit Lifesteal and Spirit Power.

| property | value |
|---|---|
| AbilityCooldown | 30 |
| AbilityDuration | 7 |
| TechPower | 6 |
| BonusHealth | 100 |
| BonusSpirit | 30 |
| AbilityLifestealPercentHero | 70 |
| TechResist | 10 |
| AbilityLifestealPercentHeroPassive | 13 |
| NonHeroAbilityLifestealTooltipOnly | 3 |
- upgrade 1: `AbilityCooldown` -10, `TechResist` 10, `BonusSpirit` 30, `BonusHealth` 50, `AbilityLifestealPercentHeroPassive` 16

**Inhibitor** (passive)
  
> Your bullets build up to reduce the target's outgoing damage and apply healing reduction.

| property | value |
|---|---|
| BonusHealth | 150 |
| DebuffDuration | 5 |
| BuildUpPerShot | 0.770 |
| BuildUpDuration | 5 |
| OutgoingDamagePenaltyPercent | -30 |
| BaseAttackDamagePercent | 10 |
| HealAmpReceivePenaltyPercent | -40 |
| HealAmpRegenPenaltyPercent | -40 |
- upgrade 1: `OutgoingDamagePenaltyPercent` -20, `HealAmpReceivePenaltyPercent` -20, `HealAmpRegenPenaltyPercent` -20, `BonusHealth` 125, `BaseAttackDamagePercent` 20

**Juggernaut** (passive)
  
*builds from: upgrade_cardio_calibrator*

| property | value |
|---|---|
| MeleeResistPercent | 25 |
| SlowResistancePercent | 50 |
| FireRateSlow | 40 |
| BonusHealthRegen | 8 |
| BonusMoveSpeed | 2.500 |
| FireRateSlowDuration | 4 |
- upgrade 1: `BonusMoveSpeed` 3.500, `MeleeResistPercent` 15, `FireRateSlow` 20, `SlowResistancePercent` 15, `BonusHealthRegen` 8

**Leech** (passive)
  
*builds from: upgrade_vampire, upgrade_health_stealing_magic*
  
> Reduces the effect of enemy applied healing reduction.

| property | value |
|---|---|
| TechPower | 12 |
| AbilityLifestealPercentHero | 28 |
| BulletLifestealPercent | 28 |
| BaseAttackDamagePercent | 12 |
| BonusHealth | 180 |
- upgrade 1: `BulletLifestealPercent` 15, `AbilityLifestealPercentHero` 15, `BonusHealth` 200, `TechPower` 15, `BaseAttackDamagePercent` 15

**Phantom Strike** (ACTIVE)
  
> Teleport to an enemy target and pull them to the ground. Dealing damage, Move speed reduction and Disarm.

| property | value |
|---|---|
| AbilityCooldown | 35 |
| AbilityCastRange | 25 |
| AbilityCastDelay | 0.350 |
| TechPower | 8 |
| BaseAttackDamagePercent | 15 |
| SlowPercent | 40 |
| SlowDuration | 3 |
| ImpactDamage | 75 |
- upgrade 1: `TechPower` 12, `BaseAttackDamagePercent` 20, `AbilityCooldown` -20, `ImpactDamage` 100

**Plated Armor** (passive)
  
> Gain a chance to either deflect incoming bullets, preventing all weapon damage or prevent all on-hit effects from bullets.

| property | value |
|---|---|
| AbilityCooldown | 1 |
| DeflectionPercent | 30 |
| BulletProcDeflectionPercent | 50 |
| DeflectionRandomness | 1 |
| BonusHealth | 130 |
- upgrade 1: `DeflectionPercent` 15, `BulletProcDeflectionPercent` 15

**Siphon Bullets** (passive)
  
> Your bullets temporarily steal Max HP from enemies. Enemies regain their stolen health when the debuff expires.

| property | value |
|---|---|
| BaseAttackDamagePercent | 15 |
| BulletResist | 10 |
| StealPerHit | 1 |
| StealPerKill | 1 |
| StackLostPerDeath | 2 |
| MaxStacks | 9999 |
| StealDuration | 17 |
| ProcCooldown | 1.200 |
| HealthStealPctHero | 2.500 |
| ParticleRadius | 1 |
- upgrade 1: `HealthStealPctHero` 1.500, `BulletResist` 10

**Spellbreaker** (passive)
  
*builds from: upgrade_debuff_reducer*
  
> The next instance of high spirit damage you take is significantly reduced.

| property | value |
|---|---|
| AbilityCooldown | 9 |
| TechResist | 18 |
| StatusResistancePercent | 25 |
| DamageThreshold | 175 |
| SpiritDamageReductionProc | 65 |
| BonusHealth | 90 |
- upgrade 1: `TechResist` 15, `StatusResistancePercent` 15, `AbilityCooldown` -3

**Unstoppable** (ACTIVE)
  
*builds from: upgrade_debuff_reducer*
  
> Temporarily suppress negative status effects and become immune to Stun, Silence, Sleep, Root, and Disarm. Cannot be used while Stunned or Slept.

| property | value |
|---|---|
| AbilityCooldown | 60 |
| AbilityDuration | 5.500 |
| BonusHealth | 125 |
| StatusResistancePercent | 25 |
- upgrade 1: `AbilityDuration` 1.250, `BonusHealth` 75, `AbilityCooldown` -35, `StatusResistancePercent` 15

**Vampiric Burst** (ACTIVE)
  
*builds from: upgrade_vampire*
  
> Grants Lifesteal, Fire Rate, and Ammo. This added Ammo is not limited by your max magazine size.

| property | value |
|---|---|
| AbilityCooldown | 30 |
| AbilityDuration | 5 |
| ActiveBonusFireRate | 34 |
| ActiveBonusLifesteal | 70 |
| BonusHealth | 100 |
| ActiveReloadPercent | 75 |
| BulletResist | 10 |
| BulletLifestealPercent | 13 |
| BaseAttackDamagePercent | 6 |
- upgrade 1: `ActiveBonusFireRate` 25, `AbilityCooldown` -10, `BulletResist` 10, `BulletLifestealPercent` 16, `BonusHealth` 110

**Witchmail** (passive)
  
> Taking heavy hits of spirit damage from an enemy reduces a random ability cooldown.

| property | value |
|---|---|
| AbilityCooldown | 1 |
| TechPower | 14 |
| TechResist | 22 |
| CooldownReductionPerHit | 4 |
| CooldownReduction | 7 |
| DamageThreshold | 75 |
- upgrade 1: `TechPower` 26, `CooldownReductionPerHit` 2, `TechResist` 5

## SPIRIT items


### Tier 1 — 800 souls


**Extra Charge** (passive)

| property | value |
|---|---|
| BonusAbilityCharges | 1 |
| BonusSpiritForChargedAbilities | 7 |
- upgrade 1: `BonusAbilityCharges` 1, `BonusSpiritForChargedAbilities` 7

**Extra Spirit** (passive)

| property | value |
|---|---|
| TechPower | 10 |
- upgrade 1: `TechPower` 10

**Golden Goose Egg** (ACTIVE)
  
> Gain souls over time, as long as you are alive.

| property | value |
|---|---|
| AbilityChannelTime | 2 |
| BonusGoldPerMinute | 80 |
| OutgoingDamagePenaltyPercent | -15 |
| ThinkRate | 3 |
| BonusSprintSpeed | 1 |
| OutOfCombatHealthRegen | 1 |
| StartingGold | 400 |
| BonusBuffsPerGold | 80 |
- upgrade 1: `BonusSprintSpeed` 5, `OutOfCombatHealthRegen` 10, `BonusBuffsPerGold` -50, `OutgoingDamagePenaltyPercent` 20

**Mystic Burst** (passive)
  
> Charges up over time with bonus spirit damage, causing abilities dealing more than 80 damage to deal additional damage.

| property | value |
|---|---|
| AbilityCooldown | 14 |
| Damage | 40 |
| MinimumDamage | 80 |
| AbilityChargeUpTime | 14 |
- upgrade 1: `Damage` 60

**Mystic Expansion** (passive)
  
> Imbue an ability to increase its range and effect radius.

| property | value |
|---|---|
| TechRangeMultiplier | 20 |
| TechRadiusMultiplier | 20 |
- upgrade 1: `TechRadiusMultiplier` 15, `TechRangeMultiplier` 15

**Mystic Regeneration** (passive)
  
> Dealing spirit damage to enemy Heroes grants you Bonus regeneration. Stacks when dealing damage to different heroes.

| property | value |
|---|---|
| Regeneration | 4 |
| RegenerationDuration | 7 |
| BonusHealth | 50 |
- upgrade 1: `Regeneration` 8, `BonusHealth` 150

**Rusted Barrel** (ACTIVE)
  
> Target an enemy to reduce their Fire Rate and Bullet Resistance.

| property | value |
|---|---|
| AbilityCooldown | 16 |
| AbilityDuration | 5 |
| AbilityCastRange | 32 |
| AbilityCastDelay | 0.100 |
| FireRateSlow | 32 |
| BonusHealth | 60 |
| BonusSprintSpeed | 0.500 |
| BulletArmorReduction | -8 |
- upgrade 1: `BonusHealth` 130, `BulletArmorReduction` -4, `FireRateSlow` 20, `AbilityCooldown` -8

**Spirit Strike** (passive)
  
> When you perform a Light or Heavy Melee attack against a hero, deal extra spirit damage with the attack and reduce the target's Spirit Resist.Cooldown is 2x longer for Light Melee hits.

| property | value |
|---|---|
| AbilityCooldown | 8 |
| AbilityDuration | 6 |
| LightMeleeCooldownMult | 2 |
| SpiritDamage | 40 |
| TechArmorDamageReduction | -6 |
- upgrade 1: `SpiritDamage` 80, `TechArmorDamageReduction` -5

### Tier 2 — 1600 souls


**Arcane Surge** (passive)
  
*builds from: upgrade_improved_stamina*
  
> After you Dash-Jump, the next ability you use within 7s will have bonus Range, Duration, and Spirit Power.

| property | value |
|---|---|
| AbilityDuration | 7 |
| BonusAbilityDurationPercent | 15 |
| SpiritPower | 20 |
| TechRadiusMultiplierBuff | 12 |
| TechRangeMultiplierBuff | 12 |
| Stamina | 1 |
| StaminaCooldownReduction | 12 |
- upgrade 1: `Stamina` 1, `SpiritPower` 25, `TechRadiusMultiplierBuff` 15, `TechRangeMultiplierBuff` 15, `BonusAbilityDurationPercent` 15, `StaminaCooldownReduction` 14

**Bullet Resist Shredder** (passive)
  
> Reduces Bullet Resist on enemies when you deal spirit damage.

| property | value |
|---|---|
| AbilityDuration | 8 |
| BulletArmorReduction | -10 |
| BaseAttackDamagePercent | 9 |
| BulletResist | 9 |
- upgrade 1: `BulletResist` 7, `BulletArmorReduction` -11, `BaseAttackDamagePercent` 15

**Cold Front** (ACTIVE)
  
> Release an expanding ice blast that deals spirit damage and Slows targets it hits.

| property | value |
|---|---|
| AbilityCooldown | 25 |
| AbilityDuration | 4 |
| SpreadDuration | 0.600 |
| StartRadius | 2 |
| EndRadius | 10 |
| MovementSpeedSlow | 48 |
| Damage | 95 |
| DamageHeight | 7 |
| NPCDamageMult | 1 |
| TechResist | 6 |
- upgrade 1: `TechResist` 8, `AbilityCooldown` -13, `Damage` 60

**Compress Cooldown** (passive)
  
> Imbue an ability to reduce its Cooldown.

| property | value |
|---|---|
| CooldownReduction | 18 |
- upgrade 1: `CooldownReduction` 10

**Duration Extender** (passive)
  
> Imbue an ability to increase its Duration.

| property | value |
|---|---|
| BonusAbilityDurationPercent | 22 |
- upgrade 1: `BonusAbilityDurationPercent` 12

**Improved Spirit** (passive)
  
*builds from: upgrade_improved_spirit*

| property | value |
|---|---|
| TechPower | 18 |
| BonusSprintSpeed | 1 |
| BonusHealth | 75 |
| OutOfCombatHealthRegen | 1.500 |
- upgrade 1: `TechPower` 22, `OutOfCombatHealthRegen` 3

**Mystic Slow** (passive)
  
> When the target takes spirit damage, they have their Move Speed reduced.

| property | value |
|---|---|
| AbilityDuration | 2 |
| MovementSpeedSlow | 24 |
| GroundDashReductionPercent | -10 |
| BonusSprintSpeed | 0.750 |
| BonusHealth | 50 |
- upgrade 1: `MovementSpeedSlow` 12, `GroundDashReductionPercent` -10, `BonusHealth` 100, `BonusSprintSpeed` 1

**Mystic Vulnerability** (passive)
  
> When an enemy takes spirit damage, they have their spirit resist reduced.

| property | value |
|---|---|
| AbilityDuration | 7 |
| TechArmorDamageReduction | -8 |
| TechResist | 8 |
- upgrade 1: `TechResist` 8, `TechArmorDamageReduction` -10

**Quicksilver Reload** (passive)
  
> Your imbued ability charges up over time with bonus spirit damage, bonus fire rate, and reloads bullets on use.

| property | value |
|---|---|
| AbilityCooldown | 18 |
| BonusFireRate | 10 |
| BuffDuration | 12 |
| Damage | 44 |
| AmmoReloadPercent | 100 |
| AbilityChargeUpTime | 18 |
- upgrade 1: `BonusFireRate` 20, `Damage` 56, `AbilityChargeUpTime` -4, `AbilityCooldown` -4

**Slowing Hex** (ACTIVE)
  
> Slows movement of enemy target. Also Silences their movement-based items and abilities.Increases the target's gravity.Does not affect target's stamina usage.

| property | value |
|---|---|
| AbilityCooldown | 29 |
| AbilityDuration | 3.500 |
| AbilityCastRange | 25 |
| AbilityCastDelay | 0.100 |
| SlowPercent | 16 |
| GroundDashReductionPercent | -26 |
| BonusSprintSpeed | 0.500 |
- upgrade 1: `SlowPercent` 8, `AbilityCooldown` -18, `GroundDashReductionPercent` -6

**Spirit Sap** (ACTIVE)
  
> Target an enemy to reduce their Spirit Resist and Spirit Power.

| property | value |
|---|---|
| AbilityCooldown | 18 |
| AbilityDuration | 12 |
| AbilityCastRange | 40 |
| AbilityCastDelay | 0.100 |
| MagicResistReduction | -9 |
| BonusHealth | 50 |
| TechPowerReduction | -30 |
- upgrade 1: `BonusHealth` 150, `MagicResistReduction` -12, `AbilityCooldown` -12, `TechPowerReduction` -26

**Suppressor** (passive)
  
> When you deal spirit damage to enemies, you also reduce their Fire Rate.

| property | value |
|---|---|
| AbilityDuration | 4.500 |
| TechPower | 6 |
| FireRateSlow | 28 |
| BulletResist | 8 |
- upgrade 1: `TechPower` 12, `BulletResist` 16, `FireRateSlow` 20

### Tier 3 — 3200 souls


**Decay** (ACTIVE)
  
> Inflict damage over time to a target, dealing damage based on their current health.Decay's damage is non-lethal and does not apply item procs.

| property | value |
|---|---|
| AbilityCooldown | 30 |
| AbilityDuration | 12 |
| AbilityCastRange | 20 |
| AbilityCastDelay | 0.100 |
| TechPower | 8 |
| HealAmpReceivePenaltyPercent | -50 |
| HealAmpRegenPenaltyPercent | -50 |
| TickRate | 1 |
| DotHealthPercent | 1.950 |
| BonusHealth | 65 |
- upgrade 1: `TechPower` 12, `BonusHealth` 90, `HealAmpReceivePenaltyPercent` -20, `HealAmpRegenPenaltyPercent` -20, `DotHealthPercent` 0.375, `AbilityCooldown` -10

**Disarming Hex** (ACTIVE)
  
*builds from: upgrade_withering_whip*
  
> Disarms enemy target and reduces their Bullet Resist.

| property | value |
|---|---|
| AbilityCooldown | 16 |
| AbilityDuration | 4.250 |
| AbilityCastRange | 32 |
| AbilityCastDelay | 0.100 |
| BonusSprintSpeed | 0.750 |
| BonusHealth | 75 |
| BulletArmorReduction | -13 |
- upgrade 1: `BonusHealth` 175, `BulletArmorReduction` -7, `AbilityCooldown` -8

**Greater Expansion** (passive)
  
*builds from: upgrade_magic_reach*
  
> Increases the range and effect radius of your abilities and items.

| property | value |
|---|---|
| TechRangeMultiplier | 30 |
| TechRadiusMultiplier | 30 |
| TechResist | 10 |
- upgrade 1: `TechResist` 10, `TechRadiusMultiplier` 20, `TechRangeMultiplier` 20

**Knockdown** (ACTIVE)
  
> Apply a Stun after 2s. Stun duration is increased against airborne targets.Increases the target's gravity for the duration of the stun.

| property | value |
|---|---|
| AbilityCooldown | 35 |
| AbilityCastRange | 45 |
| AbilityCastDelay | 0.100 |
| StunDelay | 2 |
| StunDuration | 0.500 |
| VisualContractRadius | 3 |
| BonusHealth | 75 |
| MaxBonusDuration | 1.500 |
| MaxHeightForBonus | 30 |
| TechRangeMultiplier | 5 |
| TechRadiusMultiplier | 5 |
- upgrade 1: `TechRadiusMultiplier` 6, `TechRangeMultiplier` 6, `StunDuration` 0.750, `BonusHealth` 75

**Radiant Regeneration** (passive)
  
*builds from: upgrade_mystic_regeneration*
  
> Heal and gain bonus Movement Speed for a short duration when you cast an ability.

| property | value |
|---|---|
| AbilityCooldown | 6 |
| AbilityDuration | 3 |
| HealingPerCast | 65 |
| BonusMoveSpeed | 1.750 |
| Regeneration | 4 |
| RegenerationDuration | 7 |
| BonusHealth | 90 |
- upgrade 1: `Regeneration` 9, `HealingPerCast` 60, `BonusHealth` 110, `BonusMoveSpeed` 1

**Rapid Recharge** (passive)
  
*builds from: upgrade_extra_charge*

| property | value |
|---|---|
| CooldownBetweenChargeReduction | 30 |
| BonusAbilityCharges | 2 |
| CooldownReductionOnChargedAbilities | 14 |
| BonusSpiritForChargedAbilities | 14 |
- upgrade 1: `BonusAbilityCharges` 2, `CooldownReductionOnChargedAbilities` 15, `BonusSpiritForChargedAbilities` 20, `CooldownBetweenChargeReduction` 5

**Silence Wave** (ACTIVE)
  
> Launch an expanding projectile which Silences enemies for a short duration and deals impact damage. Silence does not interrupt channeling abilities.

| property | value |
|---|---|
| AbilityCooldown | 42 |
| AbilityDuration | 3 |
| AbilityCastRange | 40 |
| AbilityCastDelay | 0.100 |
| BonusHealth | 50 |
| CooldownOnMiss | 30 |
| HeightOffGround | 1 |
| GrowthPerMeter | 0.150 |
| InitialWidth | 5 |
| Damage | 75 |
- upgrade 1: `AbilityCooldown` -10, `Damage` 125, `BonusHealth` 75

**Spirit Snatch** (passive)
  
*builds from: upgrade_acolytes_glove*
  
> When you perform a Light or Heavy Melee attack against a hero, the attack deals extra spirit damage and steals Spirit Resist and Spirit Power.Effects are reduced by 30% for Light Melee hits.

| property | value |
|---|---|
| AbilityCooldown | 6 |
| AbilityDuration | 10 |
| LightMeleeReduction | 30 |
| SpiritDamage | 50 |
| TechArmorDamageReduction | -12 |
| TechArmorGain | 12 |
| TechPowerReduction | -25 |
| TechPowerGain | 25 |
| BonusMeleeDamagePercent | 7 |
| BonusHealth | 75 |
- upgrade 1: `SpiritDamage` 50, `TechArmorGain` 5, `TechArmorDamageReduction` -5, `TechPowerGain` 35, `TechPowerReduction` -35

**Superior Cooldown** (passive)
  
*builds from: upgrade_magic_tempo*
  
> Reduces the Cooldown of your abilities.

| property | value |
|---|---|
| CooldownReduction | 20 |
| OutOfCombatHealthRegen | 4 |
- upgrade 1: `CooldownReduction` 10, `OutOfCombatHealthRegen` 6

**Superior Duration** (passive)
  
*builds from: upgrade_arcane_extension*
  
> Increases the duration of your abilities and items.

| property | value |
|---|---|
| BonusAbilityDurationPercent | 28 |
| BulletResist | 8 |
- upgrade 1: `BonusAbilityDurationPercent` 12, `BulletResist` 8

**Surge of Power** (passive)
  
*builds from: upgrade_improved_spirit*
  
> Imbue an ability with permanent Spirit Power. When that ability is used, gain bonus Move Speed and maintain full speed while attacking.

| property | value |
|---|---|
| AbilityCooldown | 14 |
| ImbuedTechPower | 28 |
| FireRateBonus | 20 |
| BonusMoveSpeed | 1.750 |
| MovementSpeedBonusDuration | 8 |
| MoveWhileShootingSpeedPenaltyReductionPercent | 100 |
| MoveWhileZoomedSpeedPenaltyReductionPercent | 100 |
- upgrade 1: `ImbuedTechPower` 32, `FireRateBonus` 18, `BonusMoveSpeed` 2

**Tankbuster** (passive)
  
*builds from: upgrade_magic_burst*
  
> Charges up over time with bonus spirit damage, causing abilities dealing more than 165 damage to deal additional damage. Ignores Spirit Resistance.

| property | value |
|---|---|
| AbilityCooldown | 14 |
| MinimumDamage | 165 |
| ReProcLockoutTime | 5 |
| WatcherMaxDuration | 30 |
| CurrentHealthDamage | 7.500 |
| Damage | 40 |
| AbilityChargeUpTime | 14 |
| BonusHealth | 50 |
- upgrade 1: `CurrentHealthDamage` 5, `BonusHealth` 100, `Damage` 60

**Torment Pulse** (passive)
  
> Periodically deals spirit damage to the closest two enemies nearby.

| property | value |
|---|---|
| AbilityCooldown | 1.400 |
| BonusHealth | 100 |
| DamagePulseAmount | 25 |
| DamagePulseRadius | 9 |
| MeleeResistPercent | 18 |
- upgrade 1: `BonusHealth` 75, `DamagePulseAmount` 30

### Tier 4 — 6400 souls


**Arctic Blast** (ACTIVE)
  
*builds from: upgrade_cold_front*
  
> Release an expanding ice blast that deals spirit damage, Freezing and then Slowing targets it hits.Slowed targets have their stamina regen frozen

| property | value |
|---|---|
| AbilityCooldown | 24 |
| SpreadDuration | 0.600 |
| StartRadius | 2 |
| EndRadius | 16 |
| SlowPercent | 48 |
| SlowDuration | 4 |
| Damage | 175 |
| DamageHeight | 7 |
| NPCDamageMult | 1 |
| TechResist | 10 |
| FreezeDuration | 1 |
- upgrade 1: `Damage` 150, `AbilityCooldown` -12, `TechResist` 15, `FreezeDuration` 0.250

**Boundless Spirit** (passive)
  
*builds from: upgrade_soaring_spirit*

| property | value |
|---|---|
| TechPower | 30 |
| BonusHealth | 75 |
| OutOfCombatHealthRegen | 4 |
| TechPowerPercent | 15 |
- upgrade 1: `TechPower` 25, `TechPowerPercent` 10, `OutOfCombatHealthRegen` 4, `BonusHealth` 100

**Cursed Relic** (ACTIVE)
  
> Curses an enemy - interrupting, Silencing, Disarming, and preventing item usage. Removes all non-ultimate buffs.Your own Damage Output is reduced for the duration.

| property | value |
|---|---|
| AbilityCooldown | 55 |
| AbilityDuration | 3.250 |
| AbilityCastRange | 20 |
| AbilityCastDelay | 0.100 |
| SkipFrames | 6 |
| OutgoingDamagePenaltyPercent | -25 |
- upgrade 1: `AbilityCooldown` -40, `AbilityDuration` 0.250

**Echo Shard** (ACTIVE)
  
> Reset the cooldown of the imbued non-ultimate ability.This item's cooldown is increased by the cooldown of the imbued ability.

| property | value |
|---|---|
| AbilityCooldown | 30 |
| AbilityPostCastDuration | 0.500 |
| TechResist | 5 |
| BulletResist | 5 |
| ImbuedCooldownMultiplier | 1 |
- upgrade 1: `BulletResist` 5, `TechResist` 5, `AbilityCooldown` -10

**Escalating Exposure** (passive)
  
*builds from: upgrade_magic_vulnerability*
  
> Dealing spirit damage applies a stacking Spirit Amp that increases your spirit damage to the target.

| property | value |
|---|---|
| AbilityDuration | 12 |
| ProcCooldown | 0.700 |
| MagicIncreasePerStack | 4.500 |
| TechResist | 17 |
| MaxStacks | 12 |
| TechArmorDamageReduction | -8 |
- upgrade 1: `MagicIncreasePerStack` 1.500, `TechResist` 8, `TechArmorDamageReduction` -10, `MaxStacks` 6

**Ethereal Shift** (ACTIVE)
  
> You enter a void state and become untargetable and invincible for a short duration, during which you float slowly and cannot perform actions. Afterwards you gain Spirit Power, Move Speed, and Spirit Resist.Can be canceled early.Activation cancels any active ability.

| property | value |
|---|---|
| AbilityCooldown | 37 |
| AbilityDuration | 4 |
| BuffDuration | 5 |
| TechResist | 30 |
| DampingFactor | 3 |
| LiftHeight | 200 |
| BonusSpirit | 20 |
| FloatMoveSpeed | 2.500 |
| BonusMoveSpeed | 3 |
- upgrade 1: `AbilityDuration` 2, `BonusSpirit` 30, `BonusMoveSpeed` 2, `TechResist` 10, `AbilityCooldown` -10, `FloatMoveSpeed` 3.500

**Focus Lens** (ACTIVE)
  
*builds from: upgrade_spirit_sap*
  
> Target an enemy to Silence them. A portion of all damage dealt during the silence gets applied to the target when the silence wears off.

| property | value |
|---|---|
| AbilityCooldown | 45 |
| AbilityDuration | 4.500 |
| AbilityCastRange | 25 |
| AbilityCastDelay | 0.100 |
| PercentDamage | 35 |
| BonusFireRate | 10 |
| MagicResistReduction | -9 |
| TechPowerReduction | -30 |
| ResistReductionDuration | 12 |
- upgrade 1: `PercentDamage` 20, `BonusFireRate` 20, `TechPowerReduction` -26, `MagicResistReduction` -12, `AbilityDuration` 0.250, `AbilityCooldown` -12

**Lightning Scroll** (passive)
  
*builds from: upgrade_magic_slow*
  
> Damage from your ultimate applies a stun and deals bonus spirit damage after a short delay.

| property | value |
|---|---|
| AbilityDuration | 2 |
| Damage | 150 |
| SlowPercent | 64 |
| BonusHealth | 50 |
| StunDuration | 0.750 |
| DelayBeforeStun | 3 |
| BonusSprintSpeed | 0.750 |
| MovementSpeedSlow | 24 |
| GroundDashReductionPercent | -10 |
- upgrade 1: `BonusHealth` 100, `Damage` 100, `BonusSprintSpeed` 5, `StunDuration` 0.750

**Magic Carpet** (ACTIVE)
  
> Summon a Magic Carpet that will fly you away. While flying you are immune to slows and doing any action will dismiss the carpet. Cannot use abilities while the carpet is being summoned.

| property | value |
|---|---|
| AbilityCooldown | 32 |
| AbilityDuration | 12 |
| AbilityCastDelay | 0.200 |
| TechPower | 14 |
| SummonDuration | 1.300 |
| FlyMoveSpeed | 7 |
| BonusAbilityDurationPercent | 15 |
| AirControlPercent | 25 |
| GravityScale | -15 |
| BonusHealth | 125 |
- upgrade 1: `TechPower` 46, `AbilityDuration` 8, `BonusAbilityDurationPercent` 15, `FlyMoveSpeed` 6, `SummonDuration` -0.300

**Mercurial Magnum** (passive)
  
*builds from: upgrade_quick_silver*
  
> Your imbued ability charges up over time with bonus spirit damage, bonus fire rate, and reloads bullets on use. Until your next reload, your bullets deal bonus spirit damage based on your Spirit Power.

| property | value |
|---|---|
| AbilityCooldown | 15 |
| TechPower | 7 |
| BonusFireRate | 22 |
| BuffDuration | 12 |
| Damage | 60 |
| AmmoReloadPercent | 100 |
| AbilityChargeUpTime | 14 |
| BulletsBonusMagicDamage | 20 |
| BonusClipSizePercent | 20 |
- upgrade 1: `BonusFireRate` 20, `BonusClipSizePercent` 60, `Damage` 120, `BulletsBonusMagicDamage` 20, `TechPower` 15

**Mystic Reverb** (passive)

| property | value |
|---|---|
| AbilityCooldown | 6.250 |
| TechDamagePercent | 50 |
| DelayDuration | 3 |
| MinimumDamage | 100 |
| Radius | 16 |
| AbilityLifestealPercentHero | 8 |
| ImbueAbilityLifesteal | 22 |
| MovementSpeedSlow | 32 |
| MaxHealthDamage | 10 |
- upgrade 1: `AbilityLifestealPercentHero` 25, `TechDamagePercent` 20

**Refresher** (ACTIVE)
  
> Reset the cooldown of all your abilities and restore all your charges.

| property | value |
|---|---|
| AbilityCooldown | 300 |
| AbilityCastDelay | 0.600 |
| TechResist | 14 |
| BulletResist | 15 |
- upgrade 1: `AbilityCooldown` -210

**Scourge** (ACTIVE)
  
> Apply Spirit Resist, Debuff Resist and an aura on a friendly target that deals damage to enemies proportional to their max health. Existing debuffs on the target are reduced.Can be self cast.

| property | value |
|---|---|
| AbilityCooldown | 35 |
| AbilityDuration | 10 |
| AbilityCastRange | 35 |
| AbilityCastDelay | 0.250 |
| TickRate | 0.250 |
| MaxHealthPercentAsDPS | 2.300 |
| AuraRadius | 10 |
| TechResist | 40 |
| BonusHealth | 100 |
| StatusResistancePercent | 20 |
- upgrade 1: `MaxHealthPercentAsDPS` 2, `CombatBarrier` 300, `StatusResistancePercent` 20, `BonusHealth` 125, `AbilityDuration` 3

**Spirit Burn** (passive)
  
> Dealing significant spirit damage to an enemy within 5s causes an explosion dealing damage and a burn to that enemy. While burning, enemies take damage over time and receive reduced healing.The cooldown is per enemy, so each target can only be burned once per cooldown. Deals half-damage on non-heroes.

| property | value |
|---|---|
| TechRangeMultiplier | 6 |
| TechRadiusMultiplier | 6 |
| DamageThreshold | 500 |
| DamageThresholdDuration | 5 |
| ExplosionDamage | 50 |
| ExplosionRadius | 3 |
| DPS | 24 |
| DebuffDuration | 8 |
| HealAmpReceivePenaltyPercent | -70 |
| HealAmpRegenPenaltyPercent | -70 |
| TickRate | 0.500 |
| ImmunityDuration | 20 |
| DamagePctVsNonHeroes | 50 |
- upgrade 1: `ExplosionDamage` 160, `TechRadiusMultiplier` 12, `TechRangeMultiplier` 12, `DPS` 20, `ImmunityDuration` -6

**Transcendent Cooldown** (passive)
  
*builds from: upgrade_cooldown_reduction*
  
> Reduces the Cooldown of your abilities and items.

| property | value |
|---|---|
| CooldownReduction | 25 |
| ItemCooldownReduction | 25 |
| OutOfCombatHealthRegen | 4 |
- upgrade 1: `ItemCooldownReduction` 10, `OutOfCombatHealthRegen` 10, `CooldownReduction` 15

**Vortex Web** (ACTIVE)
  
*builds from: upgrade_containment*
  
> Throw a vacuum grenade, pulling all enemies into a small area and applying Slowing Hex. Alt Cast to Target Unit Directly.

| property | value |
|---|---|
| AbilityCooldown | 42 |
| AbilityDuration | 4 |
| AbilityCastRange | 30 |
| AbilityCastDelay | 0.200 |
| CaptureRadius | 12 |
| TetherDuration | 0.500 |
| TetherRadius | 1 |
| SlowPercent | 28 |
| GroundDashReductionPercent | -36 |
| TechRangeMultiplier | 8 |
| TechRadiusMultiplier | 8 |
| BonusSprintSpeed | 0.750 |
- upgrade 1: `BonusSprintSpeed` 9, `AbilityCooldown` -22, `TechRadiusMultiplier` 10, `TechRangeMultiplier` 10, `SlowPercent` 12