"""
GladiatorAI Striking Engine

Retrieves striking statistics from the
latest valid pre-fight snapshot.

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
    snapshot_value,
    safe_float,
)


class StrikingEngine:
    """
    Retrieves offensive striking statistics.
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str,
        fallback_fight: pd.Series | None = None,
    ) -> StrikingStats:

        average_sig_strikes = snapshot_value(
            history=history,
            fighter=fighter,
            red_column=R_SIG_STR,
            blue_column=B_SIG_STR,
            fallback_fight=fallback_fight,
        )

        strike_accuracy = snapshot_value(
            history=history,
            fighter=fighter,
            red_column=R_SIG_ACC,
            blue_column=B_SIG_ACC,
            fallback_fight=fallback_fight,
        )

        return StrikingStats(
            average_sig_strikes=safe_float(
                average_sig_strikes
            ),
            strike_accuracy=safe_float(
                strike_accuracy
            ),
        )