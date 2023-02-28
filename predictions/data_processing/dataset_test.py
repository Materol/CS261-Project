"""Tests for dataset functions."""

import unittest

from predictions.data_processing.dataset import load_dataset
from predictions.critical_success_factors import ALL_CSFS
from predictions.success_metrics import ALL_SUCCESS_METRICS
from predictions.utils import extract_csf_values, extract_success_values


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

    def test_dataset_format(self):
        """Test the format of the output of the dataset."""
        data = load_dataset()

        critical_success_factors, success_metrics = data[0]

        extracted_csf_values = extract_csf_values(critical_success_factors)
        extracted_sm_values = extract_success_values(success_metrics)

        # These are ordered by the order of the CSFs and SuccessMetrics
        actual_csf_values = [4, 1, 5, 5, 5, 5]  # OF
        actual_csf_values += [5, 5, 5, 5, 5, 5, 4]  # TF
        actual_csf_values += [3, 3, 3, 4]  # CF
        actual_csf_values += [5, 5, 4, 5, 3, 5, 5]  # PF

        actual_sm_values = [5, 4, 5, 5]  # Process
        actual_sm_values += [5, 5, 5, 5, 5, 5, 5, 5, 5, 2]  # Product
        actual_sm_values += [5, 5, 5]  # Stakeholder
        actual_sm_values += [4.76]  # Overall

        self.assertEqual(extracted_csf_values, actual_csf_values)
        self.assertEqual(extracted_sm_values, actual_sm_values)


if __name__ == '__main__':
    unittest.main()
