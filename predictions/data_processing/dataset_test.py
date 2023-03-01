"""Tests for dataset functions."""

import unittest

from predictions.data_processing.dataset import load_dataset
from predictions.critical_success_factors import ALL_CSFS
from predictions.success_metrics import ALL_SUCCESS_METRICS


class TestDataset(unittest.TestCase):
    """Tests for dataset functions."""

    def test_dataset_load(self):
        """Test loading the dataset."""
        data = load_dataset()

        # There should be 101 projects in the dataset
        self.assertEqual(len(data), 101)

        # Each project should have 42 columns
        len_success_metrics = len(data[0][1])
        len_critical_success_factors = len(data[0][0])
        total_columns = len_critical_success_factors + len_success_metrics

        expected_columns = len(ALL_CSFS) + len(ALL_SUCCESS_METRICS)

        self.assertEqual(total_columns, expected_columns)


if __name__ == '__main__':
    unittest.main()
