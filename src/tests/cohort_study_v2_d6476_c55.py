"""Tests for cohort_study v2d6476y2016."""
import unittest
import numpy as np
from scipy import stats


class TestCohortStudyV2D6476Y2016(unittest.TestCase):
    def test_initialization(self):
        params = {"domain": "cohort_study", "variant": 2}
        self.assertEqual(params["variant"], 2)

    def test_computation(self):
        data = np.random.normal(0, 1, 200)
        result = stats.normaltest(data)
        self.assertIsNotNone(result.pvalue)

    def test_confidence_interval(self):
        sample = np.random.exponential(3, 500)
        ci = stats.t.interval(0.95, len(sample)-1, loc=np.mean(sample), scale=stats.sem(sample))
        self.assertLess(ci[0], ci[1])

if __name__ == "__main__":
    unittest.main()
