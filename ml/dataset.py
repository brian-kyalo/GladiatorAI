"""
GladiatorAI ML Dataset

Loads the engineered training dataset and
separates predictive features from metadata
and the target variable.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


FEATURE_COLUMNS = [
    "age_diff",
    "height_diff",
    "reach_diff",

    "experience_diff",
    "wins_diff",
    "losses_diff",
    "win_rate_diff",

    "win_streak_diff",
    "lose_streak_diff",
    "momentum_diff",

    "ko_rate_diff",
    "submission_rate_diff",
    "decision_rate_diff",

    "fight_time_diff",
    "sig_strike_diff",

    "takedown_diff",
    "submission_attempt_diff",
]

TARGET_COLUMN = "winner"


@dataclass
class MLDataset:
    """
    Represents a prepared machine-learning dataset.
    """

    X: pd.DataFrame

    y: pd.Series

    dates: pd.Series

    feature_names: list[str]


def load_dataset(
    path: str,
) -> MLDataset:
    """
    Load the engineered GladiatorAI dataset.

    Parameters
    ----------
    path:
        Path to gladiator_training.csv.

    Returns
    -------
    MLDataset
    """

    dataframe = pd.read_csv(path)

    required_columns = (
        FEATURE_COLUMNS
        + [
            TARGET_COLUMN,
            "snapshot_date",
        ]
    )

    missing_columns = [
        column
        for column in required_columns
        if column not in dataframe.columns
    ]

    if missing_columns:

        raise ValueError(
            "Dataset is missing required "
            f"columns: {missing_columns}"
        )

    X = dataframe[
        FEATURE_COLUMNS
    ].copy()

    y = dataframe[
        TARGET_COLUMN
    ].copy()

    dates = pd.to_datetime(
        dataframe["snapshot_date"]
    )

    invalid_targets = ~y.isin(
        ["Red", "Blue"]
    )

    if invalid_targets.any():

        invalid_values = y[
            invalid_targets
        ].unique()

        raise ValueError(
            "Unexpected target values: "
            f"{invalid_values}"
        )

    return MLDataset(
        X=X,
        y=y,
        dates=dates,
        feature_names=FEATURE_COLUMNS.copy(),
    )