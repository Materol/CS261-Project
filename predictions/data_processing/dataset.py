"""Dataset loading and processing functions.

The dataset is from the following paper:

Garousi, V., Tarhan, A., Pfahl, D., Coşkunçay, A., & Demirörs, O. (2019, 03).
Correlation of critical success factors with success of software projects: an
empirical investigation. Software Quality Journal, 27, 429-493.
10.1007/s11219-018-9419-5 (https://doi.org/10.1007/s11219-018-9419-5)
"""

import os

from predictions.critical_success_factors import ALL_CSFS
from predictions.success_metrics import ALL_SUCCESS_METRICS
from predictions.utils import create_csf_map, create_prediction_map

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data.csv')


def read_rows(file):
    """Read the rows of a CSV file."""
    rows = []
    with open(file, 'r') as f:
        for line in f:
            row = line.strip().split(',')
            rows.append(row)

    return rows


def load_dataset():
    """Load the dataset from the CSV file to a list of dictionaries for each row

    In the dataset, each row is a project. The first few columns correspond to
    the critical success factors (CSFs) and the last few columns correspond to
    the success metrics (SMs). The CSFs and SMs are defined in the `ALL_CSFS`
    and `ALL_SUCCESS_METRICS` and follow the **same order** as in the CSV file.

    Each row becomes a list of exactly two dictionaries: one for the CSFs and
    one for the SMs. The keys of the dictionaries are the names of the CSFs and
    SMs, respectively.

    For CSFs values are integers 1-5 (inclusive). For SMs values are floats
    between 1.0 and 5.0 (inclusive).

    Blanks are replaced with 0 or 0.0, depending on the type of the column.
    """
    rows = read_rows(DATA_DIR)

    # The first row contains the column names
    column_names = rows[0]

    expected_column_names = [csf for csf in ALL_CSFS
                            ] + [sm for sm in ALL_SUCCESS_METRICS]

    if column_names != expected_column_names:
        raise ValueError(f'Expected column names: {expected_column_names}, '
                         f'found: {column_names}')

    # The rest of the rows contain the data
    data = rows[1:]

    # We can now assume the order of the ALL_CSFS and ALL_SUCCESS_METRICS
    # matches the order of the columns in the CSV file.
    dataset = []
    for row in data:
        csfs = create_csf_map()
        success_metrics = create_prediction_map()

        column = 0
        for csf in ALL_CSFS:
            value = row[column]

            # Ensure valid values
            if value == '':
                value = 0
            value = int(value)

            csfs[csf] = value
            column += 1

        for success_metric in ALL_SUCCESS_METRICS:
            value = row[column]

            # Ensure valid values
            if value == '':
                value = 0.0
            value = float(value)

            success_metrics[success_metric] = value
            column += 1

        dataset.append([csfs, success_metrics])

    return dataset
