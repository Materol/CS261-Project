"""
Abstract class for all models. Each model has a name, description, and a
prediction function, mapping Critical Success Factors to some prediction of
project success.
"""

from typing import Dict, List

from predictions.critical_success_factors import CSF
from predictions.success_metrics import SuccessMetric


class Model:

    def predict(
        self,
        critical_success_factors_values: Dict[CSF, int],
    ) -> Dict[SuccessMetric, float]:
        """Predict success of a project given a mapping of CSFs to values."""
        raise NotImplementedError("Model.predict() not implemented.")
