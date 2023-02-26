"""
A naive model that uses a weighted sum of the Critical Success Factors and their
correlations with the mean of the project's success metrics.
"""

import typing

from predictions.critical_success_factors import CSF, OF4, OF5, OF6, TF1, TF2, PF5
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
        critical_success_factors_values: typing.Dict[CSF, int],
    ) -> typing.Dict[SuccessMetric, float]:
        # We use OF.04, OF.05, OF.06, TF.01, TF.02 to positively correlate with
        # the mean of the success metrics. We then use and PF.05 to negatively
        # correlate with the mean of the success metrics.
        summed = critical_success_factors_values[OF4] * 0.29
        summed += critical_success_factors_values[OF5] * 0.32
        summed += critical_success_factors_values[OF6] * 0.29
        summed += critical_success_factors_values[TF1] * 0.22
        summed += critical_success_factors_values[TF2] * 0.27

        summed -= critical_success_factors_values[PF5] * 0.10

        success_metrics = create_prediction_map()
        success_metrics[OVERALL] = self.normalise(summed)

        return success_metrics

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
