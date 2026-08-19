"""
GladiatorAI Grappling Engine

Retrieves grappling statistics from the
latest valid pre-fight snapshot.

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
    snapshot_value,
    safe_float,
)


class GrapplingEngine:
    """
    Retrieves grappling statistics.
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str,
        fallback_fight: pd.Series | None = None,
    ) -> GrapplingStats:

        average_takedowns = snapshot_value(
            history=history,
            fighter=fighter,
            red_column=R_TD,
            blue_column=B_TD,
            fallback_fight=fallback_fight,
        )

        takedown_accuracy = snapshot_value(
            history=history,
            fighter=fighter,
            red_column=R_TD_ACC,
            blue_column=B_TD_ACC,
            fallback_fight=fallback_fight,
        )

        average_submission_attempts = snapshot_value(
            history=history,
            fighter=fighter,
            red_column=R_SUB,
            blue_column=B_SUB,
            fallback_fight=fallback_fight,
        )

        return GrapplingStats(
            average_takedowns=safe_float(
                average_takedowns
            ),
            takedown_accuracy=safe_float(
                takedown_accuracy
            ),
            average_submission_attempts=safe_float(
                average_submission_attempts
            ),
        )