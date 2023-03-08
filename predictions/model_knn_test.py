"""Testing for the KNN model."""

import unittest

from predictions.model_knn import ModelKNN
from predictions.utils import create_csf_map, create_prediction_map
from predictions.trainer import Trainer

expected_msg = (
    """We cannot find an improvement for Success Metric 'budget' right now.
Success Metric 'schedule' is doing poorly. We recommend you allocate fewer resources to 'Top-level management support'. This will improve the 'schedule' score by 2.00 points.
We cannot find an improvement for Success Metric 'scope' right now.
We cannot find an improvement for Success Metric 'team_building_and_dynamics' right now.
We cannot find an improvement for Success Metric 'overall_quality' right now.
We cannot find an improvement for Success Metric 'business_and_revenue_generated' right now.
We cannot find an improvement for Success Metric 'functional_suitability' right now.
We cannot find an improvement for Success Metric 'reliability' right now.
Success Metric 'performance_efficiency' is doing poorly and we recommend you allocate more resources to 'Top-level management support'. This will improve the 'performance_efficiency' score by 1.00 points.
We cannot find an improvement for Success Metric 'operability' right now.
Success Metric 'security' is doing poorly and we recommend you allocate more resources to 'Top-level management support'. This will improve the 'security' score by 1.00 points.
We cannot find an improvement for Success Metric 'compatibility' right now.
Success Metric 'maintainability' is doing poorly and we recommend you allocate more resources to 'Organizational culture and management style'. This will improve the 'maintainability' score by 1.00 points.
Success Metric 'transferability' is doing poorly. We recommend you allocate fewer resources to 'Software development methodologies'. This will improve the 'transferability' score by 1.00 points.
We cannot find an improvement for Success Metric 'user_satisfaction' right now.
We cannot find an improvement for Success Metric 'team_satisfaction' right now.
We cannot find an improvement for Success Metric 'top_management_satisfaction' right now.
Success Metric 'overall_success' is doing poorly and we recommend you allocate more resources to 'Customer skill, training and education in IT'. This will improve the 'overall_success' score by 0.18 points.
""")


class TestModelKNN(unittest.TestCase):
    """Testing for the KNN model."""

    def __init__(self, *args, **kwargs):
        super(TestModelKNN, self).__init__(*args, **kwargs)

        # Create a trainer object, which loads the data.
        self.trainer = Trainer()

    def test_train(self):
        """Test the training of the model."""
        model = ModelKNN()

        self.trainer.train_model(model)

        test_prediction = create_prediction_map()

        # Test that we indeed have trained parameters.
        self.assertNotEqual(model.trained_params, None)

        # We do not train for the overall success metric, so we should have
        # one less trained parameter than the number of success metrics.
        self.assertEqual(len(model.trained_params), len(test_prediction) - 1)

    def test_predict(self):
        """Test the prediction of the model."""
        model = ModelKNN()
        self.trainer.train_model(model)

        csfs, _ = self.trainer.dataset
        inputs_csfs = create_csf_map(list(csfs[0]))

        result = model.predict(inputs_csfs)

        # Test that we indeed have a prediction.
        self.assertNotEqual(result, None)

        # Test that the prediction has the correct success metrics as keys.
        self.assertEqual(result.keys(), create_prediction_map().keys())

    def test_feedback(self):
        """Test the feedback of the model."""
        model = ModelKNN()
        self.trainer.train_model(model)

        csfs, _ = self.trainer.dataset

        # Project 41 gives a good example of feedback.
        inputs_csfs = create_csf_map(list(csfs[41]))

        feedback = model.give_feedback(inputs_csfs)

        self.assertEqual(feedback.get_feedback(), expected_msg)


if __name__ == '__main__':
    unittest.main()
