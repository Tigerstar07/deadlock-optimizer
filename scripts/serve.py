"""
Local web server: serves web/ and exposes the Python model as a JSON API.

The Build Lab used to carry its own JavaScript copy of the model, which
drifted from model.py (16 slots, a hard-coded Drifter range, stale item
rules). Now there is one model: the browser asks this server.

    python scripts/serve.py            # http://localhost:8777

Endpoints
  POST /api/evaluate  {hero, items, net_worth, objective?}
       -> stats + per-scenario results from model.Loadout.evaluate
  POST /api/optimize  {hero, net_worth, objective?, items?, iterations?}
       -> best build found from the given/nearest solved build
"""

import argparse
import json
import os
import random
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from model import (HEROES, ITEMS, MAX_ACTIVES, OBJECTIVES,  # noqa: E402
                   SCENARIO_BY_NAME, Loadout, slots_at, valid_build)
from optimize import STAGES, Search, ref_at, search_pool  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, "web")
DATA = os.path.join(ROOT, "data")
_OPT_LOCK = threading.Lock()


def _refs():
    with open(os.path.join(DATA, "optimization.json"), encoding="utf-8") as f:
        data = json.load(f)
    return data


def evaluate(body):
    hero = body["hero"]
    items = [i for i in body.get("items", []) if i in ITEMS]
    nw = float(body.get("net_worth", 20000))
    objective = body.get("objective", "allround")
    data = _refs()
    ref = ref_at(data["refs"], nw)
    lo = Loadout(hero, items, net_worth=nw)
    score, levels, results = lo.evaluate(ref, objective)
    other = "teamfight" if objective == "allround" else "allround"
    other_score = Loadout(hero, items, net_worth=nw).evaluate(ref, other)[0]
    br, sr = lo.total_resists(levels)
    burst, _ = lo.ability_burst(levels)
    return {
        "hero": hero, "items": items, "net_worth": nw, "objective": objective,
        "score": score, "scores": {objective: score, other: other_score},
        "ability_levels": list(levels), "ability_points": lo.ability_points,
        "legal": valid_build(items, nw), "slots": len(items), "max_slots": slots_at(nw),
        "actives": lo.n_actives, "max_actives": MAX_ACTIVES, "spend": lo.spend,
        "ref": ref,
        "stats": {
            "boons": lo.boons, "spirit_power": lo.spirit_power,
            "weapon_pct": lo.weapon_pct, "bullet_damage": lo.bullet_damage,
            "fire_rate_pct": lo.firerate_pct, "clip": lo.clip_size,
            "weapon_dps": lo.weapon_dps, "ability_dps": lo.ability_sustained_dps(levels),
            "ability_burst": burst,
            "health": lo.health + lo.ability_bonus_health(levels),
            "barrier": lo.barrier_pool(levels),
            "ehp": lo.ehp(0.6, levels), "bullet_resist": br, "spirit_resist": sr,
            "bullet_lifesteal": lo.bullet_lifesteal,
            "spirit_lifesteal": lo.ability_lifesteal_total(levels),
            "cdr": lo.cdr, "self_drain": lo.self_drain,
            "heal_amp_cast": lo.heal_amp_cast, "heal_amp_regen": lo.heal_amp_regen,
            "invest": {"weapon": [lo.spend_by_cat["weapon"], lo.inv_weapon],
                       "vitality": [lo.spend_by_cat["vitality"], lo.inv_vit],
                       "spirit": [lo.spend_by_cat["spirit"], lo.inv_spirit]},
        },
        "scenarios": {name: {k: v for k, v in r.items() if not isinstance(v, (list, dict))}
                      for name, r in results.items()},
        "weights": OBJECTIVES[objective],
        "scenario_params": {name: SCENARIO_BY_NAME[name]._asdict() for name in results},
    }


def optimize(body):
    hero = body["hero"]
    nw = float(body.get("net_worth", 20000))
    objective = body.get("objective", "allround")
    iterations = max(0, min(int(body.get("iterations", 4)), 12))
    data = _refs()
    ref = ref_at(data["refs"], nw)
    seeds = []
    if body.get("items"):
        seeds.append([i for i in body["items"] if i in ITEMS])
    table = data["stages"] if objective == "allround" else data["teamfight"]["stages"]
    for stage, budget in STAGES:
        row = next((r for r in table[stage] if r["hero"] == hero), None)
        if row and budget <= nw * 1.35:
            seeds.append(row["items"])
    search = Search(hero, nw, ref, objective, search_pool(hero), random.Random(7))
    starts = []
    for seed in seeds[-3:]:
        trimmed = sorted(seed, key=lambda n: -ITEMS[n]["cost"])
        while trimmed and not valid_build(trimmed, nw):
            trimmed.pop()
        starts.append(search.greedy(trimmed)[0])
    if not starts:
        starts.append(search.greedy()[0])
    best = max((search.climb(s) for s in starts), key=lambda p: p[1])[0]
    if iterations:
        best, _ = search.ils(best, iterations)
    result = evaluate({"hero": hero, "items": sorted(best), "net_worth": nw, "objective": objective})
    result["evaluations"] = search.evals
    return result


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB, **kwargs)

    def log_message(self, fmt, *args):
        if "/api/" in (self.path or ""):
            sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def end_headers(self):
        if self.path.endswith(".json") or "/api/" in self.path:
            self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def _json(self, code, payload):
        raw = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        if self.path.startswith("/api/health"):
            return self._json(200, {"ok": True, "heroes": len(HEROES), "items": len(ITEMS)})
        return super().do_GET()

    def do_POST(self):
        length = int(self.headers.get("Content-Length") or 0)
        try:
            body = json.loads(self.rfile.read(length) or b"{}")
            if body.get("hero") not in HEROES:
                return self._json(400, {"error": "unknown hero"})
            if self.path == "/api/evaluate":
                return self._json(200, evaluate(body))
            if self.path == "/api/optimize":
                if not _OPT_LOCK.acquire(blocking=False):
                    return self._json(429, {"error": "an optimisation is already running"})
                try:
                    return self._json(200, optimize(body))
                finally:
                    _OPT_LOCK.release()
            return self._json(404, {"error": "unknown endpoint"})
        except Exception as exc:  # report, don't kill the server
            return self._json(500, {"error": f"{type(exc).__name__}: {exc}"})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8777)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"serving {WEB} with model API on http://localhost:{args.port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
