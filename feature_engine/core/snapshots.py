"""
GladiatorAI Snapshot Utilities

Provides access to the latest valid pre-fight
snapshot for a fighter.

The system prefers the most recent historical
value. If a specific feature is missing or
invalid in that historical snapshot, the
current pre-fight row can provide a fallback.

Important:

    Unknown != zero
"""

from __future__ import annotations

import math

import pandas as pd

from feature_engine.constants import (
    R_FIGHTER,
    B_FIGHTER,
)


def latest_snapshot(
    history: pd.DataFrame,
    fighter: str,
    fallback_fight: pd.Series | None = None,
) -> tuple[pd.Series | None, str]:
    """
    Return the latest historical snapshot and
    the fighter's corner.

    If no historical snapshot exists, the current
    fight row is used as the fallback.

    Returns
    -------
    (snapshot, corner)
    """

    if not history.empty:

        snapshot = history.iloc[0]

    elif fallback_fight is not None:

        snapshot = fallback_fight

    else:

        return None, ""

    if snapshot[R_FIGHTER] == fighter:

        return snapshot, "Red"

    if snapshot[B_FIGHTER] == fighter:

        return snapshot, "Blue"

    raise ValueError(
        f"{fighter} was not found in supplied snapshot."
    )


def snapshot_value(
    history: pd.DataFrame,
    fighter: str,
    red_column: str,
    blue_column: str,
    fallback_fight: pd.Series | None = None,
):
    """
    Retrieve one fighter-specific value.

    Priority:

    1. Latest historical value if valid.
    2. Current fight value if historical value
       is missing or invalid.
    3. NaN if neither is usable.

    This is the key protection against values
    such as:

        missing → 0.0 → fake matchup advantage
    """

    snapshot, corner = latest_snapshot(
        history=history,
        fighter=fighter,
        fallback_fight=fallback_fight,
    )

    if snapshot is None:

        return float("nan")

    column = (
        red_column
        if corner == "Red"
        else blue_column
    )

    value = snapshot.get(column)

    if _valid_number(value):

        return value

    # -----------------------------------------
    # Historical value invalid.
    # Try current fight fallback.
    # -----------------------------------------

    if fallback_fight is not None:

        fallback_value = fallback_fight.get(
            column
        )

        if _valid_number(fallback_value):

            return fallback_value

    return float("nan")


def _valid_number(value) -> bool:
    """
    Returns True when a value is a usable
    finite non-zero numeric measurement.

    For physical/performance snapshot
    features, zero is treated as invalid.
    """

    if value is None:
        return False

    try:
        numeric_value = float(value)

    except (TypeError, ValueError):

        return False

    if not math.isfinite(numeric_value):

        return False

    if numeric_value == 0:

        return False

    return True