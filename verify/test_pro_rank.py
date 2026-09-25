"""Regression checks for the pro-leaning evidence layer."""

import json
import os
import sys
import unittest


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from model import HEROES  # noqa: E402
from pro_rank import PATCH_START, SENSITIVITY, WEIGHTS, score_components  # noqa: E402


class ProRankingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(os.path.join(ROOT, "data", "pro_meta_source.json"), encoding="utf-8") as handle:
            cls.source = json.load(handle)
        with open(os.path.join(ROOT, "data", "pro_ranking.json"), encoding="utf-8") as handle:
            cls.output = json.load(handle)
        with open(os.path.join(ROOT, "data", "optimization.json"), encoding="utf-8") as handle:
            cls.optimization = json.load(handle)

    def test_weight_profiles_are_normalized(self):
        self.assertAlmostEqual(sum(WEIGHTS.values()), 1.0)
        for name, profile in SENSITIVITY.items():
            with self.subTest(profile=name):
                self.assertAlmostEqual(sum(profile.values()), 1.0)

    def test_patch_window_uses_exact_publication_timestamp(self):
        self.assertEqual(self.source["patch_start"], PATCH_START)
        self.assertIn("min_unix_timestamp=1789589803", self.source["stats_url"])
        self.assertIn("min_average_badge=101", self.source["stats_url"])

    def test_current_snapshots_cover_every_live_hero(self):
        expected = {hero["id"] for hero in HEROES.values()}
        for key in ("hero_stats", "all_stats", "low_stats"):
            with self.subTest(snapshot=key):
                self.assertEqual({row["hero_id"] for row in self.source[key]}, expected)

    def test_published_ranking_recomputes_exactly(self):
        ranking, sample = score_components(self.source, self.optimization)
        self.assertEqual(len(ranking), len(HEROES))
        self.assertEqual([row["rank"] for row in ranking], list(range(1, len(HEROES) + 1)))
        self.assertEqual([row["hero"] for row in ranking],
                         [row["hero"] for row in self.output["ranking"]])
        for actual, published in zip(ranking, self.output["ranking"]):
            self.assertAlmostEqual(actual["score"], published["score"], places=10)
            for value in actual["components"].values():
                self.assertGreaterEqual(value, 0)
                self.assertLessEqual(value, 100)
        self.assertEqual(sample, self.output["sample"])


if __name__ == "__main__":
    unittest.main()
