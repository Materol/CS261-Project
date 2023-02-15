"""
Abstract class for all models. Each model has a name, description, and a
prediction function, mapping Critical Success Factors to some prediction of
project success.
"""

from typing import Dict, List

from critical_success_factors import CSF


class Model:

    def __init__(self, critical_success_factors: List[CSF]) -> None:
        """Initialize a model given a list of valid critical success factors."""
        self.critical_success_factors = critical_success_factors

    def predict(self, critical_success_factors_values: Dict[CSF, int]):
        """Predict success of a project given a mapping of CSFs to values."""
        raise NotImplementedError("Model.predict() not implemented.")
