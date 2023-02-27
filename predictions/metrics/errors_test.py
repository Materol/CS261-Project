"""Testing for validitiy of the error metrics."""

import unittest

from predictions.metrics.errors import Errors
from predictions.utils import create_prediction_map


class TestErrors(unittest.TestCase):
    """Tests for generic models and CSF."""

    def __init__(self, *args, **kwargs):
        super(TestErrors, self).__init__(*args, **kwargs)
        self.test_actual = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.test_prediction = [1.0, 2.0, 3.0, 3.0, 3.0]

    def test_mae(self):
        """Test MAE error."""

        mae = Errors.mean_absolute_error(self.test_prediction, self.test_actual)
        actual_mae = (0.0 + 0.0 + 0.0 + 1.0 + 2.0) / 5.0
        self.assertEqual(mae, actual_mae)

    def test_mse(self):
        """Test MSE error."""

        mse = Errors.mean_squared_error(self.test_prediction, self.test_actual)
        actual_mse = (0.0 + 0.0 + 0.0 + 1.0 + 4.0) / 5.0
        self.assertEqual(mse, actual_mse)

    def test_rmse(self):
        """Test RMSE error."""

        rmse = Errors.root_mean_squared_error(
            self.test_prediction,
            self.test_actual,
        )
        actual_rmse = (0.0 + 0.0 + 0.0 + 1.0 + 4.0) / 5.0
        self.assertEqual(rmse, actual_rmse**0.5)

    def test_mape(self):
        """Test MAPE error."""

        mape = Errors.mean_absolute_percentage_error(
            self.test_prediction,
            self.test_actual,
        )
        actual_mape = (0.0 + 0.0 + 0.0 + 0.25 + 0.4) / 5.0
        self.assertEqual(mape, actual_mape)

    def test_custom_error(self):
        """Test custom error."""

        custom_error = Errors.custom_error(
            self.test_prediction,
            self.test_actual,
        )
        actual_custom_error = (0.0 + 0.0 + 0.0 + 0.0 + 4.0) / 5.0
        self.assertEqual(custom_error, actual_custom_error)


if __name__ == '__main__':
    unittest.main()
