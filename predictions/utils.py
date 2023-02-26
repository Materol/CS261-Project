"""Extra utilities functions for predictions."""

from typing import Dict

from predictions.critical_success_factors import CSF, ALL_CSFS
from predictions.success_metrics import SuccessMetric, ALL_SUCCESS_METRICS


def create_csf_map() -> Dict[CSF, int]:
    """Create a mapping from CSFs to 0.

    Note that actaul values will be between 1.0 and 5.0."""
    return {csf: 0 for csf in ALL_CSFS}


def create_prediction_map() -> Dict[SuccessMetric, float]:
    """Create a mapping from success metrics to 0.0.

    Note that actaul values will be between 1.0 and 5.0."""
    return {sm: 0.0 for sm in ALL_SUCCESS_METRICS}
