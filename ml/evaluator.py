"""
GladiatorAI Model Evaluation

Evaluation metrics for binary UFC
fight outcome prediction.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    confusion_matrix,
    log_loss,
    roc_auc_score,
)


@dataclass
class EvaluationResult:
    """
    Stores model evaluation metrics.
    """

    accuracy: float

    balanced_accuracy: float

    roc_auc: float

    log_loss_value: float

    confusion_matrix: np.ndarray


def evaluate_binary_classifier(
    y_true,
    y_pred,
    y_probability,
) -> EvaluationResult:
    """
    Evaluate a binary Red/Blue classifier.

    Parameters
    ----------
    y_true:
        Actual target labels.

    y_pred:
        Predicted target labels.

    y_probability:
        Probability of the positive class,
        where Red is treated as positive.
    """

    accuracy = float(
        accuracy_score(
            y_true,
            y_pred,
        )
    )

    balanced_accuracy = float(
        balanced_accuracy_score(
            y_true,
            y_pred,
        )
    )

    roc_auc = float(
        roc_auc_score(
            y_true,
            y_probability,
        )
    )

    probabilities = np.column_stack(
        [
            1.0 - np.asarray(
                y_probability,
                dtype=float,
            ),
            np.asarray(
                y_probability,
                dtype=float,
            ),
        ]
    )

    log_loss_value = float(
        log_loss(
            y_true,
            probabilities,
        )
    )

    matrix = confusion_matrix(
        y_true,
        y_pred,
        labels=[
            "Blue",
            "Red",
        ],
    )

    return EvaluationResult(
        accuracy=accuracy,
        balanced_accuracy=balanced_accuracy,
        roc_auc=roc_auc,
        log_loss_value=log_loss_value,
        confusion_matrix=matrix,
    )