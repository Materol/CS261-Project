"""Test the Analyser class."""

import unittest

from predictions.metrics.analyse import Analyser


class TestAnalyser(unittest.TestCase):
    """Test the Analyser class."""

    def test_analyse_model(self):
        """Test the analyse_model method."""
        analyser = Analyser()
        predictions = [1.0, 2.0, 3.0, 4.0, 5.0]
        test_labels = [1.0, 2.0, 3.0, 3.0, 3.0]
        errors = analyser.analyse_model(predictions, test_labels)
        actual_errors = {
            'MAE': 0.6,
            'MSE': 1.0,
            'RMSE': 1.0,
            'MAPE': 0.2,
            'CUSTOM': 0.8,
        }
        self.assertEqual(errors, actual_errors)

if __name__ == '__main__':
    unittest.main()
