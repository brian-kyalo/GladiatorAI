"""
GladiatorAI Baseline Model

First machine-learning model for UFC
fight outcome prediction.

Model
-----
SimpleImputer
    ↓
StandardScaler
    ↓
LogisticRegression
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
import joblib

from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from ml.dataset import load_dataset
from ml.evaluator import (
    EvaluationResult,
    evaluate_binary_classifier,
)


@dataclass
class BaselineResult:
    """
    Complete result from baseline training.
    """

    model: Pipeline

    evaluation: EvaluationResult

    train_rows: int

    test_rows: int

    cutoff_date: pd.Timestamp


def train_baseline(
    dataset_path: str,
) -> BaselineResult:
    """
    Train the first GladiatorAI baseline.

    A chronological split is used so the
    model learns from older fights and is
    evaluated on newer fights.
    """

    dataset = load_dataset(
        dataset_path
    )

    dataframe = dataset.X.copy()

    dataframe["winner"] = dataset.y.to_numpy()

    dataframe["snapshot_date"] = pd.to_datetime(
        dataset.dates
    ).to_numpy()

    dataframe = dataframe.sort_values(
        "snapshot_date"
    ).reset_index(
        drop=True
    )

    # ------------------------------------------------------
    # Chronological cutoff
    # ------------------------------------------------------

    split_index = int(
        len(dataframe) * 0.80
    )

    # Convert the pandas scalar into a real
    # Timestamp using the dataframe's date column.
    cutoff_value = dataframe[
        "snapshot_date"
    ].iloc[split_index]

    cutoff_date = pd.Timestamp(
        str(cutoff_value)
    )

    # ------------------------------------------------------
    # Train / test split
    # ------------------------------------------------------

    train = dataframe[
        dataframe["snapshot_date"]
        < cutoff_date
    ].copy()

    test = dataframe[
        dataframe["snapshot_date"]
        >= cutoff_date
    ].copy()

    # ------------------------------------------------------
    # Features / target
    # ------------------------------------------------------

    X_train = train[
        dataset.feature_names
    ]

    X_test = test[
        dataset.feature_names
    ]

    y_train = train[
        "winner"
    ]

    y_test = test[
        "winner"
    ]

    # ------------------------------------------------------
    # ML pipeline
    # ------------------------------------------------------

    model = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(
                    strategy="median"
                ),
            ),
            (
                "scaler",
                StandardScaler(),
            ),
            (
                "classifier",
                LogisticRegression(
                    max_iter=2000,
                    random_state=42,
                ),
            ),
        ]
    )

    # ------------------------------------------------------
    # Train
    # ------------------------------------------------------

    model.fit(
        X_train,
        y_train,
    )

    # ------------------------------------------------------
    # Predictions
    # ------------------------------------------------------

    predictions = model.predict(
        X_test
    )

    probabilities = model.predict_proba(
        X_test
    )

    # sklearn stores class labels in sorted order:
    #
    # ["Blue", "Red"]
    #
    # Therefore the Red probability is the
    # column associated with "Red".

    classes = list(
        model.classes_
    )

    red_index = classes.index(
        "Red"
    )

    red_probability = probabilities[
        :,
        red_index
    ]

    # ------------------------------------------------------
    # Evaluation
    # ------------------------------------------------------

    evaluation = evaluate_binary_classifier(
        y_true=y_test,
        y_pred=predictions,
        y_probability=red_probability,
    )

    return BaselineResult(
        model=model,
        evaluation=evaluation,
        train_rows=int(
            len(train)
        ),
        test_rows=int(
            len(test)
        ),
        cutoff_date=cutoff_date,
    )


def save_model(
    model: Pipeline,
    path: str,
) -> None:
    """
    Save the trained model to disk.
    """

    joblib.dump(
        model,
        path,
    )