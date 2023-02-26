"""Testing for the generic model."""

import unittest

from predictions.critical_success_factors import CSF, ALL_CSFS
from predictions.success_metrics import SuccessMetric, ALL_SUCCESS_METRICS


class TestPredictionModel(unittest.TestCase):
    """Tests for generic models and CSF."""

    def test_csf_init(self):
        """Test the CSF class."""
        csf = CSF("test name", "test description")

        self.assertEqual(csf.name, "test name")
        self.assertEqual(csf.description, "test description")

    def test_csf_equality(self):
        """Test that two CSFs are equal if they have the same name."""
        csf1 = CSF("test name", "1")
        csf2 = CSF("test name", "2")

        csf3 = CSF("other name", "1")

        self.assertEqual(csf1, csf2)
        self.assertNotEqual(csf1, csf3)
        self.assertEqual(csf1, "test name")
        self.assertNotEqual(csf1, "other name")

    def test_csf_array(self):
        """Test that we have 24 CSFs in total and that all are unique."""
        csfs = set(ALL_CSFS)

        self.assertEqual(len(csfs), 24)
        self.assertEqual(len(ALL_CSFS), 24)

    def test_success_metric_init(self):
        """Test the SuccessMetric class."""
        sm = SuccessMetric("test name", "test description")

        self.assertEqual(sm.name, "test name")
        self.assertEqual(sm.description, "test description")

    def test_success_metric_equality(self):
        """Test that two SuccessMetrics are equal if they have the same name."""
        sm1 = SuccessMetric("test name", "1")
        sm2 = SuccessMetric("test name", "2")

        sm3 = SuccessMetric("other name", "1")

        self.assertEqual(sm1, sm2)
        self.assertNotEqual(sm1, sm3)

    def test_success_metric_array(self):
        """Test for 18 unique success metrics in total."""
        sms = set(ALL_SUCCESS_METRICS)

        self.assertEqual(len(sms), 18)
        self.assertEqual(len(ALL_SUCCESS_METRICS), 18)


if __name__ == '__main__':
    unittest.main()
