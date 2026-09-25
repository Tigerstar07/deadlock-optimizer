# Deadlock — Verified Mechanics and Formulas

*Patch: Minor Update 09-16-2026*

Every formula here was checked against the shipped game files AND a second source, and the check is recorded next to it.


## Boons (levels)

Boons come from **net worth thresholds**, not from spending. Buying an item never changes your boon count. Max boon is 35, reached at 48,600 net worth.

Per-boon gains are per hero (health, bullet damage, melee), except Spirit Power which is +1.1 for 32 of 38 heroes. Exceptions: **Grey Talon +1.6**, **Haze +0.5**, three heroes at +1.3, one at +1.2. Only **Bebop (+0.3%)** and **Dynamo (+0.625%)** gain Bullet Resist per boon.

> Verified: the shipped per-boon health values match the 09-16-2026 patch notes exactly — Graves 33→35, Holliday 41→43, Silver 28→31.

Ability points also come from the shipped level table. The five optimizer checkpoints provide **8 / 15 / 21 / 26 / 32** points at 6k / 12k / 20k / 32k / 50k net worth. Ability tiers cost 1, 2 and 5 additional points.


## Investments (the biggest build lever in the game)

Bonuses scale off **cumulative souls spent per category**, not per item.

| souls in category | weapon dmg | health | spirit power |
|---|---|---|---|
| 800 | +9% | +9% | +7 |
| 1,600 | +12% | +12% | +11 |
| 2,400 | +15% | +15% | +15 |
| 3,200 | +18% | +20% | +19 |
| 4,800 | +46% | +38% | +38 |
| 6,400 | +54% | +42% | +45 |
| 8,000 | +62% | +46% | +52 |
| 11,200 | +74% | +50% | +59 |
| 16,000 | +86% | +54% | +66 |
| 22,400 | +100% | +60% | +75 |
| 28,800 | +115% | +66% | +100 |

Note the discontinuity at **4,800 souls**: weapon damage jumps +18% → +46% for one more 1,600-soul item. This is the single largest power spike available and it is why build ORDER matters more than build CONTENTS in the mid game.


## Damage formulas

```
Spirit damage   = base + SpiritPower * coefficient      (linear)
Bullet damage   = (base + boons * per_boon) * (1 + weapon%)
Sustained DPS   = clip*bullets*dmg / (clip*cycle + reload + 0.25)
```

The **+0.25s** reload-initiation constant was derived by inverting the game's own `damage_per_second_with_reload` and comes out to exactly 0.2500 for 32 of 38 heroes. The six burst/charge weapons use an effective cycle derived from the shipped DPS value.

Weapon damage is averaged over each scenario's **spread of engagement distances** (e.g. teamfight 10/20/30 m at 25/50/25%). Falloff is linear between the shipped start/end ranges, after falloff-range item bonuses; close-range items (Point Blank, Stalker, Hunter's Aura, Torment Pulse) count only inside their radius.


## Engagement window

Each scenario is **one 20-second engagement entered with every cooldown ready**. Uptime, cast rate and healing of anything on a longer cooldown are amortised over 20 s instead of the full cooldown (actives, ultimates, barriers, shielding procs). Barriers count once per fight.


## Resistances

```
Total resist    = 1 - product(1 - Ri)        (multiplicative)
Total shred     = 1 - product(1 - Si)        (pooled the same way)
Final resist    = Total resist - Total shred (subtracted, not pooled)
```

Because shred subtracts from a multiplicatively-pooled total, it gets *more* effective the more the target has stacked resist.

Lifesteal and cooldown reduction also pool multiplicatively. Item cooldown reduction is separate from ability cooldown reduction.

Explicit hero ability resistance buffs are applied after tier upgrades and pooled with item/boon resistance at duration-to-cooldown uptime. A summon resistance with no hero-buff duration is skipped.

Ability-applied bullet/spirit shred is also tier-upgraded and uptime weighted when an explicit debuff duration is present. Resource-gated and unknown-duration shred is skipped rather than guessed.


## Healing order

```
gross healing = lifesteal + regen*(1+regen amp) + cast heals*(1+cast amp)
net healing   = gross healing*(1-enemy anti-heal) + Siphon Bullets - self health drain
net incoming  = max(25% of incoming, incoming - net healing)
```

Siphon Bullets steals 2.5% of the target's current max HP per 1.2 s as damage and as healing that ignores healing reduction, decaying as the target's max HP shrinks. Healing can offset at most 75% of incoming damage.

Healing Tempo does not amplify passive lifesteal and its fire-rate buff requires an applied-heal trigger. Enemy anti-heal does not reduce Blood Tribute's self-inflicted health drain.


## Duel score

Target bullet and spirit resistance reduce the matching damage channel first. Time-to-kill then divides the target's **raw health and barrier pool** by that resistance-adjusted DPS. The displayed mixed-damage EHP is diagnostic only; using it in the time-to-kill denominator would count target resistance twice. Incoming reference DPS is recorded before mitigation because the defender's mixed EHP applies its own resistances. For the 60/40 bullet/spirit mix, EHP is raw health divided by the weighted damage multiplier. Healing is subtracted after mitigation.


## Slots and limits

- **12 item slots** max: 9 base + 3 unlocked by destroying Walkers
- Slots are **universal** — any category in any slot
- **Max 4 active items** (keybind limit)
- Tier costs: 800 / 1,600 / 3,200 / 6,400
- Owning a component discounts the upgrade by the component's cost
