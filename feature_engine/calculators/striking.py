"""
GladiatorAI Striking Engine

Builds striking statistics from the
latest historical snapshot available
before the snapshot date.
"""

from __future__ import annotations

import pandas as pd

from feature_engine.constants import *

from feature_engine.models import StrikingStats


class StrikingEngine:
    """
    Retrieves offensive striking statistics
    from the latest historical fight.
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str
    ) -> StrikingStats:

        if history.empty:
            return StrikingStats()

        latest = history.iloc[0]

        if latest[R_FIGHTER] == fighter:

            avg_sig_strikes = latest.get(
                R_SIG_STR,
                0
            )

            strike_accuracy = latest.get(
                R_SIG_ACC,
                0
            )

        else:

            avg_sig_strikes = latest.get(
                B_SIG_STR,
                0
            )

            strike_accuracy = latest.get(
                B_SIG_ACC,
                0
            )

        return StrikingStats(

            average_sig_strikes=self._safe(
                avg_sig_strikes
            ),

            strike_accuracy=self._safe(
                strike_accuracy
            )
        )

    # -----------------------------------

    def _safe(self, value):

        if pd.isna(value):
            return 0.0

        return float(value)