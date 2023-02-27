"""Create a testing suite for model performance."""

from predictions.metrics.errors import Errors


class Analyser:
    """Analyse the performance of a model."""

    def test_models(self, models, test_data, test_labels):
        """Test a list of models on a test dataset."""
        for model in models:
            predictions = model.predict(test_data)
            model_errors = self.analyse_model(predictions, test_labels)
            print(model_errors)

    def analyse_model(self, predictions, test_labels):
        """Analyse the performance of a model by calculating error metrics."""
        errors = {
            'MAE':
                Errors.mean_absolute_error(predictions, test_labels),
            'MSE':
                Errors.mean_squared_error(predictions, test_labels),
            'RMSE':
                Errors.root_mean_squared_error(predictions, test_labels),
            'MAPE':
                Errors.mean_absolute_percentage_error(predictions, test_labels),
            'CUSTOM':
                Errors.custom_error(predictions, test_labels),
        }

        return errors
