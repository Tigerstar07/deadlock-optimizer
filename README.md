# Deadlock Build Optimizer

Hero and item data extracted from Deadlock's shipped game files, a combat
model checked against the game's own numbers and deadlock.wiki mechanics, a
parallel build optimiser, and a local web app backed by the same model.

**Patch baseline: Minor Update 09-16-2026** (still the live patch on 2026-09-25).

## The answer

[docs/FINDINGS.md](docs/FINDINGS.md) — generated from the solver output, never
hand-edited: the best teamfight sustain + damage hero and build, the purchase
order, stage-by-stage ranks, the top 10 for both objectives, and a benchmark
against a real high-performing match build.

## Quick start

```bash
python scripts/serve.py                 # web app + model API on http://localhost:8777
python scripts/pipeline.py              # recompute everything (~12 min on 28 cores)
python scripts/pipeline.py --skip-solve # rebuild orders/docs/site from existing results
```

## Layout

```
data/     raw game-file dumps, dataset.json, solver output (optimization.json,
          orders.json, routes.json, niches.json, benchmarks.json), Ascendant+
          item and pro-evidence snapshots
docs/     FINDINGS.md (generated), HEROES.md, ITEMS.md, MECHANICS.md
scripts/  extract.py     game files -> dataset.json
          model.py       the combat model (single source of truth)
          optimize.py    parallel per-hero solver, both objectives, reference fixed point
          order_all.py   component-aware purchase orders for each stage build
          route.py       full-game routes: buy, upgrade, SELL and ability order from
                         0 souls to the final build, all abilities maxed
          item_meta.py   Ascendant+ item usage snapshot (--refresh to refetch)
          niches.py      counter builds, signature items, model vs real players
          benchmarks.py  real match builds vs the solver at equal souls
          pro_rank.py    pro-leaning evidence index (--refresh to refetch)
          findings.py    writes docs/FINDINGS.md from the results
          docs_gen.py    writes HEROES/ITEMS/MECHANICS.md
          export_web.py  builds web/data.json
          serve.py       static site + /api/evaluate + /api/optimize
          pipeline.py    runs all of the above in order
verify/   test_model.py (mechanics regression tests), check_outputs.py
          (recomputes every published number; --deep proves local optimality)
web/      the site: answer, rankings, all builds, hero routes, niches, build lab,
          heroes, items, dark mode
archive/  the pre-2026-09-25 state and the one-off scripts that hand-patched it
```

## What you get per hero

- **Full-game route** — what to buy, upgrade and sell, in order, with the net worth of every step:
  early items are sold when a better one needs the slot or the souls (50% refund), the final
  build is complete by 56k at the latest, and every ability ends at tier 3.
- **Counter builds** vs gun-heavy and spirit-heavy teams and for isolated picks (32k and 50k).
- **Signature items** (unusually strong on this hero) and **hidden gems / traps** versus what
  Ascendant+ players actually buy this patch, with their average buy minute.
- Stage builds for two objectives (teamfight, all-round) and a Build Lab that scores any build
  with the same model.

## Model in one paragraph

Each build is scored in five combat scenarios (pick, skirmish, teamfight,
bullet-heavy teamfight, spirit-heavy teamfight) against a reference opponent:
the median hero running its own solved build, iterated to a fixed point.
Scenario score is time-to-die ÷ time-to-kill; the objective is a weighted
geometric mean. **All-round** weights 15/30/35/10/10; **Teamfight** uses only
the three teamfight scenarios. Shop rules: slots take any category, 9 at the
start plus one per enemy Walker destroyed (assumed at 16k / 26k / 36k net
worth), up to 12; 4 actives; spend ≤ net worth; stage-legal ability points
with every maximum-spend tier allocation tried. Each scenario is one
20-second engagement entered with every cooldown ready. See the Method tab or
`scripts/model.py` for every formula and assumption.

## What is verified

- 35 regression tests (`verify/test_model.py`) pin every corrected mechanic and the route rules.
- `verify/check_outputs.py` also replays all 76 full-game routes: souls never go negative, slots
  never exceed what is unlocked, sells refund 50%, components exist before upgrades, and every
  route ends on the solved full build with all abilities maxed.
- Weapon DPS reproduces the shipped `damage_per_second_with_reload` for all 38 heroes.
- Investments, multiplicative resist / lifesteal / cooldown pooling, falloff, stage ability points.
- Item mechanics re-checked against deadlock.wiki on 2026-09-25: slot rules, Siphon Bullets,
  Lucky Shot, Inhibitor, Ricochet, Escalating Resilience, Burst Fire, Toxic Bullets,
  Juggernaut, Hunter's Aura, Mercurial Magnum, lifesteal stacking, Drifter's kit.
- `verify/check_outputs.py --deep` recomputes every published row and order and proves each
  build is a one-item-exchange local optimum (not a proof of the global optimum).

## What is not modelled

Crowd control, mobility, objectives, farming speed, vision, team composition,
player skill, melee routing and resource-gated abilities (Victor's Pain
Battery, Wraith's Card Trick, Graves' Jar of Dead). The cross-hero order is a
combat ranking, not a universal tier list.
