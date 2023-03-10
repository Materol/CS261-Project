"""
Abstract class for all models. Each model has a name, description, and a
prediction function, mapping Critical Success Factors to some prediction of
project success.
"""

from typing import Dict

from .critical_success_factors import CSF
from .success_metrics import SuccessMetric
from .feedback import Feedback


class Model:

    def predict(
        self,
        critical_success_factors_values: Dict[CSF, int],
    ) -> Dict[SuccessMetric, float]:
        """Predict success of a project given a mapping of CSFs to values."""
        raise NotImplementedError("Model.predict() not implemented.")

    def train(train_x, train_y, test_x, test_y):
        """Train the model."""
        raise NotImplementedError("Model.train() not implemented.")

    def give_feedback(self) -> Feedback:
        """Give feedback on how to improve the output.

        Output should be a JSON string mapping SuccessMetrics to feedback.
        """
        raise NotImplementedError("Model.give_feedback() not implemented.")
