"""
GladiatorAI Physical Engine

Builds a fighter's physical profile.

Unlike RecordEngine,
physical attributes do not require
iterating through an entire career.

They are taken from the most recent
known record before the snapshot date.
"""

from __future__ import annotations

import pandas as pd

from feature_engine.constants import *

from feature_engine.models import PhysicalStats

from feature_engine.core import (
    latest_snapshot,
    safe_float,
)


class PhysicalEngine:
    """
    Calculates physical characteristics.

    Age

    Height

    Reach
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str
    ) -> PhysicalStats:

        if history.empty:

            return PhysicalStats()

        latest, corner = latest_snapshot(
            history,
            fighter
        )

        if corner == "Red":

            age = latest[R_AGE]

            height = latest[R_HEIGHT]

            reach = latest[R_REACH]

        else:

            age = latest[B_AGE]

            height = latest[B_HEIGHT]

            reach = latest[B_REACH]

        return PhysicalStats(

            age=safe_float(age),

            height=safe_float(height),

            reach=safe_float(reach)
        )