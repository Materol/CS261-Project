"""Train some model."""

import numpy as np

from predictions.critical_success_factors import CSF
from predictions.model import Model
from predictions.success_metrics import SuccessMetric
from predictions.data_processing.dataset import load_dataset, split_dataset, to_numpy, replace_zeros


class Trainer:
    """Train a model on the provided dataset."""

    def __init__(self):
        """Initialize the trainer by loading the dataset."""
        self.dataset = load_dataset()
        csfs, success_metrics = to_numpy(self.dataset)
        csfs = replace_zeros(csfs)
        success_metrics = replace_zeros(success_metrics)
        self.dataset = [csfs, success_metrics]

        # Split the dataset into train and test.
        train, test = split_dataset(self.dataset, 0.7)
        self.train_x, self.train_y = train
        self.test_x, self.test_y = test


    def train_model(
        self,
        model: Model,
    ):
        """Train the model on the provided dataset."""
        model.train(self.train_x, self.train_y, self.test_x, self.test_y)
