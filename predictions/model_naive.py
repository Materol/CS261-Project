"""
A naive model that uses a weighted sum of the Critical Success Factors and their
correlations with the mean of the project's success metrics.
"""

import typing

from predictions.critical_success_factors import CSF
from predictions.model import Model


class ModelNaive(Model):

    def __init__(self, correlations: typing.Dict[CSF, float]):
        # TODO(czarlinski): Implement this function.
        self.correlations = correlations

    def predict(self, critical_success_factors_values: typing.Dict[CSF, int]):
        # TODO(czarlinski): Implement this function.
        pass
