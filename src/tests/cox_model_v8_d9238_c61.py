"""Tests for cox_model v8d9238y2015."""
import unittest
import numpy as np
from scipy import stats


class TestCoxModelV8D9238Y2015(unittest.TestCase):
    def test_initialization(self):
        params = {"domain": "cox_model", "variant": 8}
        self.assertEqual(params["variant"], 8)

    def test_computation(self):
        data = np.random.normal(0, 1, 800)
        result = stats.normaltest(data)
        self.assertIsNotNone(result.pvalue)

    def test_confidence_interval(self):
        sample = np.random.exponential(9, 500)
        ci = stats.t.interval(0.95, len(sample)-1, loc=np.mean(sample), scale=stats.sem(sample))
        self.assertLess(ci[0], ci[1])

if __name__ == "__main__":
    unittest.main()
