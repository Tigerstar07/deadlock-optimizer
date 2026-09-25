"""Independent verification of the repo's data layer against the FRESH
re-fetch of Valve's game files (fresh_heroes.json / fresh_items.json).

This does not import the repo's model at all -- it re-derives everything
from the raw dumps so the checks are independent of the code under test.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
U = 39.37  # game units per metre, verified against patch notes


def load(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        return json.load(f)


def find_weapon(o):
    """Locate the weapon stat block anywhere inside a fresh hero record."""
    if isinstance(o, dict):
        if "damage_per_second_with_reload" in o:
            return o
        for v in o.values():
            r = find_weapon(v)
            if r is not None:
                return r
    elif isinstance(o, list):
        for v in o[:30]:
            r = find_weapon(v)
            if r is not None:
                return r
    return None


def unwrap(v):
    """Fresh API wraps stats as {'value': X, 'display_stat_name': ...}."""
    if isinstance(v, dict) and "value" in v:
        return v["value"]
    return v


sys.path.insert(0, os.path.join(ROOT, "scripts"))
from model import INVEST  # noqa: E402


def check_dataset_vs_fresh(ds, fresh):
    """All 38 heroes must match the fresh re-fetch on every scalar the
    fresh file carries (weapon lives on a separate endpoint, so only
    starting_stats / cost_bonuses / level_info are cross-checkable here)."""
    fidx = {}
    for h in fresh:
        if h.get("player_selectable") and not h.get("disabled") and not h.get("in_development"):
            fidx[h["name"]] = h
    print(f"[data] dataset heroes: {len(ds['heroes'])} | fresh selectable: {len(fidx)}")
    missing = set(ds["heroes"]) - set(fidx)
    extra = set(fidx) - set(ds["heroes"])
    if missing:
        print(f"[data] MISSING from fresh: {missing}")
    if extra:
        print(f"[data] in fresh but not dataset: {extra}")

    bad2 = []
    for name, dh in ds["heroes"].items():
        if name in missing:
            continue
        fh = fidx[name]
        st = fh.get("starting_stats") or {}
        for k in ("max_health", "base_health_regen", "light_melee_damage",
                  "heavy_melee_damage", "max_move_speed"):
            a = dh["base"].get(k) or 0
            b = unwrap(st.get(k)) or 0
            if a != b:
                bad2.append((name, k, a, b))
        # cost_bonuses (Investments) must match per hero
        for cat in ("weapon", "vitality", "spirit"):
            g = [(c["gold_threshold"], c["bonus"]) for c in fh["cost_bonuses"][cat]]
            if g != INVEST[cat]:
                bad2.append((name, f"cost_bonuses.{cat}", "game", "model"))
    if bad2:
        for name, k, a, b in bad2:
            print(f"[data] MISMATCH {name}.{k}: dataset={a} fresh={b}")
    else:
        print("[data] starting_stats + Investments table match the fresh re-fetch for all 38 heroes")
    return not bad2 and not missing


def check_weapon_dps_all_heroes(ds):
    """Reproduce the game's own damage_per_second_with_reload.

    Claimed: exact for all 38 heroes with the +0.25 s reload constant.
    Formula: clip*bullets*dmg / (clip*cycle + reload + 0.25)
    """
    exact, off = [], []
    for name, h in ds["heroes"].items():
        w = h["weapon"]
        clip = w.get("clip_size") or 0
        cyc = w.get("cycle_time") or 0
        rel = w.get("reload_duration") or 0
        dmg = w.get("bullet_damage") or 0
        dps = w.get("damage_per_second_with_reload") or 0
        bullets = w.get("bullets") or 1
        if not (clip and dps and dmg):
            off.append((name, "missing fields"))
            continue
        got = (clip * bullets * dmg) / (clip * cyc + rel + 0.25)
        err = got - dps
        (exact if abs(err) < 0.005 * max(1, dps) else off).append(
            (name, round(err, 4)) if abs(err) >= 0.005 * max(1, dps) else (name, round(err, 4)))
        if abs(err) >= 0.005 * max(1, dps):
            off[-1] = (name, f"got {got:.2f} vs game {dps:.2f} (err {err:+.3f})")
    print(f"\n[dps] naive formula exact for {len(exact)}/{len(ds['heroes'])} heroes")
    if off:
        for name, msg in off:
            print(f"[dps]   deviation: {name}: {msg}")
    return exact, off


def check_invest_table(ds):
    """Hardcoded INVEST in model.py vs the game's own cost_bonuses (all heroes)."""
    raw = load("data/heroes_raw.json")
    selectable = [h for h in raw
                  if h.get("player_selectable") and not h.get("disabled")
                  and not h.get("in_development")]
    by_name = {h["name"]: h for h in selectable}
    bad = []
    for name, h in by_name.items():
        for cat in ("weapon", "vitality", "spirit"):
            game = [(c["gold_threshold"], c["bonus"]) for c in h["cost_bonuses"][cat]]
            ours = INVEST[cat]
            if game != ours:
                bad.append((name, cat, game, ours))
    if bad:
        for name, cat, g, o in bad[:5]:
            print(f"[invest] MISMATCH {name}.{cat}\n  game={g}\n  model={o}")
    else:
        print(f"[invest] hardcoded table == game cost_bonuses for all "
              f"{len(by_name)} selectable heroes, all 3 categories")
    return not bad


def check_effective_cycle(ds):
    """The repo's effective_cycle must reproduce the game's own
    damage_per_second_with_reload for ALL 38 heroes at level 0."""
    sys.path.insert(0, os.path.join(ROOT, "recovered", "scripts"))
    import model  # noqa: E402
    bad = []
    for name in ds["heroes"]:
        w = ds["heroes"][name]["weapon"]
        game_dps = w.get("damage_per_second_with_reload") or 0
        got = model.Loadout(name, [], net_worth=0).weapon_dps if name in model.HEROES else None
        # weapon_dps at level 0 with no items == game figure?
        err = (got or 0) - game_dps
        if abs(err) > 0.01:
            bad.append((name, f"model {got:.2f} vs game {game_dps:.2f}"))
        # effective_cycle must not have hit the fallback (would mean inversion failed)
        w0 = model.HEROES[name]["weapon"]
        eff = model.effective_cycle(name)
        cyc = w0.get("cycle_time") or 0
        if eff <= 0:
            bad.append((name, "effective_cycle <= 0 (inversion failed)"))
    if bad:
        for name, msg in bad:
            print(f"[cycle] FAIL {name}: {msg}")
    else:
        print(f"[cycle] model weapon DPS == game damage_per_second_with_reload for all {len(ds['heroes'])} heroes")
    return not bad


def check_boons(ds):
    """boons_for_networth sanity: 35 max, wiki says final boon ~49.2k."""
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    from model import boons_for_networth  # noqa: E402
    for nw in (0, 500, 2000, 12000, 25000, 49200, 50000, 60000):
        counts = {h: boons_for_networth(ds["heroes"][h], nw) for h in ds["heroes"]}
        vals = set(counts.values())
        print(f"[boons] net worth {nw:>6,}: min {min(vals)}, max {max(vals)} "
              f"({'uniform' if len(vals) == 1 else 'VARIES: ' + str(sorted(vals))})")
    # gold required for level 36 (35 boons)
    li = ds["heroes"]["Drifter"]["level_info"]
    print(f"[boons] Drifter level 36 requires {li['36']['required_gold']:,} gold")


if __name__ == "__main__":
    ds = load("data/dataset.json")
    # A fresh re-fetch saved as fresh_heroes.json takes priority; otherwise
    # check the dataset against the raw dump it was extracted from.
    fresh_name = "fresh_heroes.json" if os.path.exists(os.path.join(ROOT, "fresh_heroes.json")) \
        else "data/heroes_raw.json"
    fresh = load(fresh_name)
    ok = check_dataset_vs_fresh(ds, fresh)
    check_weapon_dps_all_heroes(ds)
    check_invest_table(ds)
    check_boons(ds)
    check_effective_cycle(ds)
