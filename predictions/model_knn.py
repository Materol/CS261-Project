"""Creates a k-nearest neighbors model for predicting SuccessMetrics.
"""

import numpy as np

from typing import Dict
from predictions.model import Model
from predictions.critical_success_factors import CSF
from predictions.metrics.analyse import Analyser
from predictions.success_metrics import ALL_SUCCESS_METRICS, SuccessMetric, OVERALL
from predictions.utils import extract_csf_values, create_prediction_map
from sklearn.neighbors import KNeighborsClassifier


class ModelKNN(Model):

    def __init__(self):
        self.trained_params = None
        self.models = None

    def train(
        self,
        train_x: np.ndarray,
        train_y: np.ndarray,
        test_x: np.ndarray,
        test_y: np.ndarray,
    ):
        # Search between k = 1 and k = 25 to find the best k value for the
        # model. The best k value is the one that has the lowest error rate.
        # There might also be different k values for different success metrics,
        # so we train a model for each success metric. We only need to do this
        # once, so training time is not a concern. Prediction time might be
        # slower, but we can optimise this later, potentially by running the
        # models in parallel, or by using a single model if the difference in
        # error rate is not statistically significant.
        # Note that we do not predict the overall success metric, as this is
        # just the average of the other success metrics.
        remove_overall = ALL_SUCCESS_METRICS.copy()
        remove_overall.remove(OVERALL)

        trained_params = {}
        for i, sm in enumerate(remove_overall):
            current_sm_models = []

            # Create a model for the current success metric.
            for j in range(1, 26):
                model = KNeighborsClassifier(n_neighbors=j)
                model.fit(train_x, train_y[:, i])
                current_sm_models.append(model)

            # Analyse the models for the current success metric.
            report = Analyser.test_models(
                models=current_sm_models,
                test_data=test_x,
                test_labels=test_y[:, i],
            )

            sum_errors = [sum(error_vals.values()) for error_vals in report]

            best_k = np.argmin(sum_errors) + 1
            trained_params[sm] = best_k

        self.trained_params = trained_params

        # Loop through the trained parameters and create a model for each
        # success metric.
        models = {}
        index = 0
        for sm, k in self.trained_params.items():
            model = KNeighborsClassifier(n_neighbors=k)
            model.fit(train_x, train_y[:, index])
            index += 1
            models[sm] = model

        self.models = models

    def predict(
        self,
        critical_success_factors_values: Dict[CSF, int],
    ) -> Dict[SuccessMetric, float]:
        """Predict the success metrics values.

        Returns a dictionary of success metrics and their predicted values given
        the critical success factors values. The overall success metric is
        calculated by averaging the other success metrics.

        Note that you must train the model before predicting. This can be done
        by calling the train method or by using the Trainer class as seen in the
        tests.
        """
        if self.trained_params is None:
            raise Exception("ModelKNN has not been trained.")
        if self.models is None:
            raise Exception("ModelKNN has not been trained.")

        # Create a numpy array from the critical success factors values.
        csf_values = extract_csf_values(critical_success_factors_values)
        csf_values = np.array(csf_values)
        csf_values = csf_values.reshape(1, -1)

        # Create a numpy array to store the predicted success metrics values.
        success_values = create_prediction_map()

        # Loop through the models and predict the success metrics values.
        for sm, model in self.models.items():
            success_values[sm] = model.predict(csf_values)

        # Predict the overall success metric by averaging.
        values = []
        for sm, value in success_values.items():
            if sm != OVERALL:
                values.append(value)
        overall = np.mean(values)
        success_values[OVERALL] = overall

        return success_values
