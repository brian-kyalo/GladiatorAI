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

        latest = history.sort_values(

            "date",

            ascending=False

        ).iloc[0]

        if latest[R_FIGHTER] == fighter:

            age = latest.get(R_AGE, 0)

            height = latest.get(R_HEIGHT, 0)

            reach = latest.get(R_REACH, 0)

        else:

            age = latest.get(B_AGE, 0)

            height = latest.get(B_HEIGHT, 0)

            reach = latest.get(B_REACH, 0)

        return PhysicalStats(

            age=self._safe(age),

            height=self._safe(height),

            reach=self._safe(reach)
        )

    # ------------------------------------

    def _safe(self, value):

        if pd.isna(value):

            return 0.0

        return float(value)