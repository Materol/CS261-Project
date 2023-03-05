"""Creates a k-nearest neighbors model for predicting SuccessMetrics.
"""

import numpy as np

from typing import Dict
from predictions.model import Model
from predictions.critical_success_factors import CSF
from predictions.metrics.analyse import Analyser
from predictions.success_metrics import ALL_SUCCESS_METRICS, SuccessMetric, OVERALL
from sklearn.neighbors import KNeighborsClassifier


class ModelKNN(Model):

    def train(
        self,
        train_x: np.ndarray,
        train_y: np.ndarray,
        test_x: np.ndarray,
        test_y: np.ndarray,
    ):
        # Search between k = 1 and k = 20 to find the best k value for the
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


    def predict(
        self,
        critical_success_factors_values: Dict[CSF, int],
    ) -> Dict[SuccessMetric, float]:
        # TODO(czarlinski): implement once training is done.
        raise NotImplementedError("ModelKNN.predict() not implemented.")
