"""Testing for the generic model."""

import unittest

from predictions.critical_success_factors import CSF, ALL_CSFS


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

    def test_csf_array(self):
        """Test that we have 24 CSFs in total and that all are unique."""
        csfs = set(ALL_CSFS)

        self.assertEqual(len(csfs), 24)
        self.assertEqual(len(ALL_CSFS), 24)


if __name__ == '__main__':
    unittest.main()
