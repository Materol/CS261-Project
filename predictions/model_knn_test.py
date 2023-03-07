"""Testing for the KNN model."""

import unittest

from predictions.model_knn import ModelKNN
from predictions.utils import create_csf_map, create_prediction_map
from predictions.trainer import Trainer


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

if __name__ == '__main__':
    unittest.main()
