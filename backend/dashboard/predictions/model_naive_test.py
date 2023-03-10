"""Testing for the generic model."""

import json
import unittest

from .critical_success_factors import OF1, OF4, OF5, OF6, TF1, TF2, PF5
from .feedback import Feedback
from .model_naive import ModelNaive
from .success_metrics import OVERALL
from .utils import create_csf_map, create_prediction_map


class TestModelNaive(unittest.TestCase):
    """Tests for generic models and CSF."""

    def test_min(self):
        """Test the naive model wth the lowest possible values."""
        model = ModelNaive()
        data = create_csf_map()

        # This combination of values should result in an overall score of 1.0 as
        # all positive factors are at their minimum value, and the negative
        # factor is at its maximum value.
        data[OF4] = 1
        data[OF5] = 1
        data[OF6] = 1
        data[TF1] = 1
        data[TF2] = 1
        data[PF5] = 5

        actual_prediction = model.predict(data)

        test_prediction = create_prediction_map()
        test_prediction[OVERALL] = 1.0

        self.assertEqual(actual_prediction, test_prediction)

    def test_max(self):
        """Test the naive model with the highest possible values."""
        model = ModelNaive()
        data = create_csf_map()

        # This combination of values should result in an overall score of 5.0 as
        # all positive factors are at their maximum value, and the negative
        # factor is at its minimum value.
        data[OF4] = 5
        data[OF5] = 5
        data[OF6] = 5
        data[TF1] = 5
        data[TF2] = 5
        data[PF5] = 1

        actual_prediction = model.predict(data)

        test_prediction = create_prediction_map()
        test_prediction[OVERALL] = 5.0

        self.assertEqual(actual_prediction, test_prediction)

    def test_ignore_other(self):
        """Test the naive model with the highest possible values."""
        model = ModelNaive()
        data = create_csf_map()
        data[OF4] = 5
        data[OF5] = 5
        data[OF6] = 5
        data[TF1] = 5
        data[TF2] = 5
        data[PF5] = 1

        # OF1 is not used in the model, so it should be ignored.
        data[OF1] = 5

        actual_prediction = model.predict(data)

        test_prediction = create_prediction_map()
        test_prediction[OVERALL] = 5.0

        self.assertEqual(actual_prediction, test_prediction)

    def test_feedback(self):
        """Test the naive model feedback."""
        model = ModelNaive()
        data = create_csf_map()
        data[OF4] = 5
        data[OF5] = 5
        data[OF6] = 5
        data[TF1] = 5
        data[TF2] = 5
        data[PF5] = 1
        actual_feedback = model.give_feedback(data)
        actual_msg = actual_feedback.get_feedback()

        expected_prediction = create_prediction_map()
        expected_prediction[OVERALL] = 5.0

        expected_msg = (
            "Your project's success is very likely. We recommend you "
            "continue with your current strategy.")
        expected_feedback = Feedback(
            feedback=expected_msg,
            predictions=expected_prediction,
        )

        overall_feedback = json.loads(actual_msg)['overall_success']

        self.assertEqual(overall_feedback, expected_feedback.get_feedback())
        self.assertEqual(actual_feedback.get_predictions(),
                         expected_feedback.get_predictions())


if __name__ == '__main__':
    unittest.main()
