"""
GladiatorAI Grappling Engine

Builds grappling statistics from the
latest historical snapshot available
before the snapshot date.

Features
--------
- Average Takedowns
- Takedown Accuracy
- Average Submission Attempts
"""

from __future__ import annotations

import pandas as pd

from feature_engine.constants import (
    R_FIGHTER,
    B_FIGHTER,
    R_TD,
    B_TD,
    R_TD_ACC,
    B_TD_ACC,
    R_SUB,
    B_SUB,
)

from feature_engine.models import GrapplingStats


class GrapplingEngine:
    """
    Retrieves grappling statistics
    from the latest historical snapshot.
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str
    ) -> GrapplingStats:

        if history.empty:
            return GrapplingStats()

        latest = history.iloc[0]

        if latest[R_FIGHTER] == fighter:

            average_takedowns = latest.get(
                R_TD,
                0
            )

            takedown_accuracy = latest.get(
                R_TD_ACC,
                0
            )

            average_submission_attempts = latest.get(
                R_SUB,
                0
            )

        else:

            average_takedowns = latest.get(
                B_TD,
                0
            )

            takedown_accuracy = latest.get(
                B_TD_ACC,
                0
            )

            average_submission_attempts = latest.get(
                B_SUB,
                0
            )

        return GrapplingStats(

            average_takedowns=self._safe(
                average_takedowns
            ),

            takedown_accuracy=self._safe(
                takedown_accuracy
            ),

            average_submission_attempts=self._safe(
                average_submission_attempts
            )
        )

    # ------------------------------------------

    def _safe(self, value):

        if pd.isna(value):
            return 0.0

        return float(value)