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
    R_TD,
    B_TD,
    R_TD_ACC,
    B_TD_ACC,
    R_SUB,
    B_SUB,
)

from feature_engine.models import GrapplingStats

from feature_engine.core import (
    latest_snapshot,
    safe_float,
)


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

        latest, corner = latest_snapshot(
            history,
            fighter
        )

        if corner == "Red":
            average_takedowns = latest[R_TD]

            takedown_accuracy = latest[R_TD_ACC]

            average_submission_attempts = latest[R_SUB]

        else:

            average_takedowns = latest[
                B_TD ]

            takedown_accuracy = latest[
                B_TD_ACC ]

            average_submission_attempts = latest[
                B_SUB ]

        return GrapplingStats(

            average_takedowns=safe_float(
                average_takedowns
            ),

            takedown_accuracy=safe_float(
                takedown_accuracy
            ),

            average_submission_attempts=safe_float(
                average_submission_attempts
            )
        )

   