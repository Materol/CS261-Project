"""Collection of error metrics for predictions."""


class Errors:

    def mean_absolute_error(predictions, actual):
        """Calculate the mean absolute error.

        This is a regression metric."""
        sum_error = 0.0
        for prediction, test_label in zip(predictions, actual):
            sum_error += abs(prediction - test_label)

        return sum_error / len(predictions)

    def mean_squared_error(predictions, actual):
        """Calculate the mean squared error.

        This is a regression metric."""
        sum_error = 0.0
        for prediction, test_label in zip(predictions, actual):
            sum_error += (prediction - test_label)**2

        return sum_error / len(predictions)

    def root_mean_squared_error(predictions, actual):
        """Calculate the root mean squared error.

        This is a regression metric.
        """
        return Errors.mean_squared_error(predictions, actual)**0.5

    def mean_absolute_percentage_error(predictions, actual):
        """Calculate the mean absolute percentage error.

        This is a regression metric.
        """
        sum_error = 0.0
        for prediction, test_label in zip(predictions, actual):
            sum_error += abs((prediction - test_label) / test_label)

        return sum_error / len(predictions)

    def custom_error(predictions, actual):
        """Calculate a custom loss function.

        Values are casted to integers, as if they were classes. This error
        function also gives lenciency if the prediction is within 1 class of the
        actual value.

        The error is calculated as follows:

        sum (
            0, if abs(prediction - actual) <= 1
            abs(prediction - actual) ** 2, otherwise
        ) / len(predictions)
        """
        sum_error = 0.0
        for prediction, test_label in zip(predictions, actual):
            abs_diff = abs(int(prediction) - int(test_label))
            if abs_diff > 1:
                sum_error += abs_diff**2

        return sum_error / len(predictions)
