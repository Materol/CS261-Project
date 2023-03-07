"""Extra utilities functions for predictions."""

from typing import Dict, List

from predictions.critical_success_factors import CSF, ALL_CSFS
from predictions.success_metrics import SuccessMetric, ALL_SUCCESS_METRICS


def create_csf_map(values=None) -> Dict[CSF, int]:
    """Create a mapping from CSFs to a default value of 0.

    Note that actaul values will be between 1.0 and 5.0."""
    if values != None:
        return {csf: value for csf, value in zip(ALL_CSFS, values)}
    return {csf: 0 for csf in ALL_CSFS}


def create_prediction_map() -> Dict[SuccessMetric, float]:
    """Create a mapping from success metrics to 0.0.

    Note that actaul values will be between 1.0 and 5.0."""
    return {sm: 0.0 for sm in ALL_SUCCESS_METRICS}


def extract_csf_values(csf_or_success_metrics: Dict[CSF, int]) -> List[int]:
    """Extract and order CSFs values.

    These values are ordered by their in appearance `ALL_CSFS`.
    Values that do not appear in `ALL_CSFS` are ignored.
    """
    return [csf_or_success_metrics[csf] for csf in ALL_CSFS]


def extract_success_values(
        csf_or_success_metrics: Dict[SuccessMetric, float]) -> List[int]:
    """Extract and order SuccessMetrics values.

    These values are ordered by their in appearance `ALL_SUCCESS_METRICS`.
    Values that do not appear in `ALL_SUCCESS_METRICS` are ignored.
    """
    return [csf_or_success_metrics[sm] for sm in ALL_SUCCESS_METRICS]
