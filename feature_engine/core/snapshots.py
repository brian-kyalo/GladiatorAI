"""
Snapshot utilities.

Provides helper functions for reading
the latest historical snapshot of a fighter.
"""

from __future__ import annotations

import pandas as pd

from feature_engine.constants import (
    R_FIGHTER,
    B_FIGHTER,
)


def latest_snapshot(
    history: pd.DataFrame,
    fighter: str
):
    """
    Returns

    (latest_row, corner)

    where corner is

    "Red"

    or

    "Blue"
    """

    if history.empty:
        raise ValueError(
            "History is empty."
        )

    latest = history.iloc[0]

    if latest[R_FIGHTER] == fighter:
        return latest, "Red"

    if latest[B_FIGHTER] == fighter:
        return latest, "Blue"

    raise ValueError(
        f"{fighter} not found in supplied history."
    )