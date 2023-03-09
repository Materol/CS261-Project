"""
A naive model that uses a weighted sum of the Critical Success Factors and their
correlations with the mean of the project's success metrics.
"""

from typing import Dict
from predictions.critical_success_factors import CSF, OF4, OF5, OF6, TF1, TF2, PF5
from predictions.feedback import Feedback
from predictions.model import Model
from predictions.success_metrics import SuccessMetric, OVERALL
from predictions.utils import create_prediction_map


class ModelNaive(Model):
    """
    A naive model that uses a weighted sum of the Critical Success Factors and
    their correlations with the mean of the project's success metrics.
    """

    def __init__(self):
        self.correlations = {
            OF4: 0.29,
            OF5: 0.32,
            OF6: 0.29,
            TF1: 0.22,
            TF2: 0.27,
            PF5: -0.10,
        }

    def predict(
        self,
        critical_success_factors_values: Dict[CSF, int],
    ) -> Dict[SuccessMetric, float]:
        # We use OF.04, OF.05, OF.06, TF.01, TF.02 to positively correlate with
        # the mean of the success metrics. We then use and PF.05 to negatively
        # correlate with the mean of the success metrics.
        summed = critical_success_factors_values[OF4] * self.correlations[OF4]
        summed += critical_success_factors_values[OF5] * self.correlations[OF5]
        summed += critical_success_factors_values[OF6] * self.correlations[OF6]
        summed += critical_success_factors_values[TF1] * self.correlations[TF1]
        summed += critical_success_factors_values[TF2] * self.correlations[TF2]

        summed += critical_success_factors_values[PF5] * self.correlations[PF5]

        success_metrics = create_prediction_map()
        success_metrics[OVERALL] = self.normalise(summed)

        return success_metrics

    def give_feedback(self, csf_values: Dict[CSF, int]) -> Feedback:
        """Give feedback on how to improve the project."""
        max_diff = None
        max_diff_csf = None
        for csf, correlation in self.correlations.items():
            weighted_diff = (5 - csf_values[csf]) * correlation

            if max_diff is None or weighted_diff > max_diff:
                max_diff = weighted_diff
                max_diff_csf = csf

        prediction = self.predict(csf_values)

        text_feedback = ""
        if prediction[OVERALL] >= 5:
            text_feedback += (
                "Your project's success is very likely. We recommend you "
                "continue with your current strategy.")
        elif max_diff_csf == PF5:
            text_feedback += (
                f"Your project's {max_diff_csf} is too high. The description "
                "of this CSF is: {max_diff_csf.description}. Decreasing this "
                "CSF will have the most impact on your project's success.")
        else:
            text_feedback += (
                f"Your project's {max_diff_csf} is too low. The description "
                "of this CSF is: {max_diff_csf.description}. Increasing this "
                "CSF will have the most impact on your project's success.")

        if prediction[OVERALL] <= 2:
            text_feedback += (
                "Your project is likely to fail. We recommend you consider "
                "changing your strategy rapidly.")

        feedback = Feedback(
            feedback=text_feedback,
            predictions=prediction,
        )
        return feedback

    def normalise(self, value):
        """Normalise outputs to be between 1 and 5."""
        self.max_value = 0
        self.min_value = 0
        for correlation in self.correlations.values():
            if correlation > 0:
                self.max_value += correlation * 5
                self.min_value += correlation * 1
            else:
                self.min_value += correlation * 5
                self.max_value += correlation * 1

        norm = (value - self.min_value) / (self.max_value - self.min_value)
        return norm * 4 + 1
