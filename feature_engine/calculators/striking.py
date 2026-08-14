"""
GladiatorAI Striking Engine

Retrieves striking statistics from the
latest historical snapshot available
before the snapshot date.

Features
--------
- Average Significant Strikes
- Strike Accuracy
"""

from __future__ import annotations

import pandas as pd

from feature_engine.constants import (
    R_SIG_STR,
    B_SIG_STR,
    R_SIG_ACC,
    B_SIG_ACC,
)

from feature_engine.models import StrikingStats

from feature_engine.core import (
    latest_snapshot,
    safe_float,
)


class StrikingEngine:
    """
    Retrieves offensive striking statistics
    from the latest historical snapshot.
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str
    ) -> StrikingStats:
        """
        Builds the fighter's striking profile.
        """

        if history.empty:
            return StrikingStats()

        latest, corner = latest_snapshot(
            history,
            fighter
        )

        if corner == "Red":

            average_sig_strikes = latest[
                R_SIG_STR
            ]

            strike_accuracy = latest[
                R_SIG_ACC
            ]

        else:

            average_sig_strikes = latest[
                B_SIG_STR
            ]

            strike_accuracy = latest[
                B_SIG_ACC
            ]

        return StrikingStats(

            average_sig_strikes=safe_float(
                average_sig_strikes
            ),

            strike_accuracy=safe_float(
                strike_accuracy
            )
        )