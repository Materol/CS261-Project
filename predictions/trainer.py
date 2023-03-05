"""Train some model."""

import numpy as np

from predictions.critical_success_factors import CSF
from predictions.model import Model
from predictions.success_metrics import SuccessMetric
from predictions.data_processing.dataset import load_dataset, split_dataset, to_numpy, replace_zeros


class Trainer:
    """Train a model on the provided dataset."""

    def train_model(
        self,
        model: Model,
    ):
        """Train the model on the provided dataset."""
        # Load the dataset.
        dataset = load_dataset()
        csfs, success_metrics = to_numpy(dataset)
        csfs = replace_zeros(csfs)
        success_metrics = replace_zeros(success_metrics)
        dataset = [csfs, success_metrics]

        # Split the dataset into training and test data.
        train, test = split_dataset(dataset, 0.7)
        train_x, train_y = train
        test_x, test_y = test

        # Train the model.
        model.train(train_x, train_y, test_x, test_y)
