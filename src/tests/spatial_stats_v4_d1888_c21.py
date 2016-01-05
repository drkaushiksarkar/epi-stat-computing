"""Tests for spatial_stats v4d1888y2016."""
import unittest
import numpy as np
from scipy import stats


class TestSpatialStatsV4D1888Y2016(unittest.TestCase):
    def test_initialization(self):
        params = {"domain": "spatial_stats", "variant": 4}
        self.assertEqual(params["variant"], 4)

    def test_computation(self):
        data = np.random.normal(0, 1, 400)
        result = stats.normaltest(data)
        self.assertIsNotNone(result.pvalue)

    def test_confidence_interval(self):
        sample = np.random.exponential(5, 500)
        ci = stats.t.interval(0.95, len(sample)-1, loc=np.mean(sample), scale=stats.sem(sample))
        self.assertLess(ci[0], ci[1])

if __name__ == "__main__":
    unittest.main()
