"""Creates a k-nearest neighbors model for predicting SuccessMetrics.
"""

import numpy as np

from typing import Dict
from .model import Model
from .critical_success_factors import CSF, ALL_CSFS
from .feedback import Feedback
from .metrics.analyse import Analyser
from .success_metrics import ALL_SUCCESS_METRICS, SuccessMetric, OVERALL
from .utils import extract_csf_values, create_prediction_map, to_json_feedback
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

    def give_feedback(self, csf_values) -> Feedback:
        """Give feedback on how to improve the output."""

        prediction = self.predict(csf_values)
        feedback = Feedback(predictions=prediction)

        if prediction[OVERALL] >= 5.0:
            feedback_msg = (
                "Your project's success is very likely. We recommend you "
                "continue with your current strategy.\n")
            feedback.set_feedback(feedback_msg)
            return feedback
        elif prediction[OVERALL] <= 2.0:
            feedback_msg += (
                "Your project is likely to fail. We recommend you consider "
                "changing your strategy rapidly.\n")
            feedback.set_feedback(feedback_msg)
            return feedback

        # For each (SuccessMetric - OVERALL), we wish to give feedback on how to
        # improve the output. We do this by searching the CSF allocation space
        # for the CSF allocation that has the highest predicted success metric
        # value.
        #
        # As a heuristic, we only search the CSF allocation space with a hamming
        # distance of 1 from the current CSF allocation. In other words, we only
        # add +1 or -1 to a single CSF value. This is because we want to make
        # changes manageable, and do not want to overwhelm the manager.
        #
        # So for each SuccessMetric, we loop through each CSF at a time with a
        # allocation of +1 or -1 and keep track which CSF allocation has the
        # highest predicted SuccessMetric value.

        # Create a list of CSF allocations to search.
        plus_minus = [1, -1]
        search_space = []
        for csf in ALL_CSFS:
            for pm in plus_minus:
                new_csf_allocation = csf_values.copy()
                new_csf_allocation[csf] += pm

                # Check if the new CSF allocation is valid. Cannot be less than
                # 1 or greater than 5.
                if new_csf_allocation[csf] < 1:
                    continue
                if new_csf_allocation[csf] > 5:
                    continue

                with_metadata = (pm, csf, new_csf_allocation)
                search_space.append(with_metadata)

        # Predict the success metrics for each CSF allocation in the search
        # space.
        search_space_predictions = []
        for pm, csf, csf_allocation in search_space:
            pred = self.predict(csf_allocation)

            with_metadata = (pm, csf, pred)
            search_space_predictions.append(with_metadata)

        # Create a map of success metrics to feedback.
        sm_feedback = create_prediction_map()
        for sm, _ in prediction.items():
            sm_feedback[sm] = ""

        # Find the best CSF allocation for each success metric and construct
        # feedback message.
        for sm, value in prediction.items():
            feedback_msg = ""
            if value >= 5:
                feedback_msg += (
                    f"Success Metric '{sm.name}' is doing well. We recommend "
                    f"you continue with your current strategy.")
                sm_feedback[sm] = feedback_msg
                continue

            # Search new predictions for the best CSF allocation.
            best_allocation = None
            best_value = prediction[sm]

            for pm, csf, pred in search_space_predictions:
                if pred[sm] > best_value:
                    best_allocation = (pm, csf)
                    best_value = pred[sm]

            # If the best CSF allocation is the same as the current CSF
            # allocation, then we cannot improve the success metric using this
            # strategy.
            if best_allocation is None:
                feedback_msg += (
                    f"We cannot find an improvement for Success Metric "
                    f"'{sm.name}' right now.")
                sm_feedback[sm] = feedback_msg
                continue

            improvement = float(best_value - prediction[sm])

            # Construct feedback message.
            pm, csf = best_allocation
            if pm == 1:
                feedback_msg += (
                    f"Success Metric '{sm.name}' is doing poorly and we recommend"
                    f" you allocate more resources to '{csf.description}'. ")
            else:
                feedback_msg += (
                    f"Success Metric '{sm.name}' is doing poorly. We recommend you"
                    f" allocate fewer resources to '{csf.description}'. ")

            # Show impovement to 2 decimal places.
            feedback_msg += (
                f"This will improve the '{sm.name}' score by {improvement:.2f} "
                f"points.")

            sm_feedback[sm] = feedback_msg

        feedback.set_feedback(to_json_feedback(sm_feedback))
        return feedback
