"""The Feedback class is used to provide human readable feedback to the user."""

from typing import Dict
from predictions.success_metrics import SuccessMetric


class Feedback:
    """This is intended to be used as a data structure to store feedback.

    It stores:
        - `feedback`: a human readable string of how to improve a certain
          project based on the CSFs. This should be based on how the model uses
          the CSFs to predict the success metrics.

        - `predictions`: a dictionary of SuccessMetrics to their predicted
          values. This is used to display the predicted values to the user.
    """

    def __init__(self, feedback=None, predictions=None):
        self.feedback = feedback
        self.predictions = predictions

    def set_feedback(self, feedback: str):
        """Set the feedback string, which is a JSON mapping SuccessMetrics."""
        self.feedback = feedback

    def set_predictions(self, predictions: Dict[SuccessMetric, float]):
        self.predictions = predictions

    def get_feedback(self) -> str:
        return self.feedback

    def get_predictions(self) -> Dict[SuccessMetric, float]:
        return self.predictions
