"""
GladiatorAI Durability Engine

Calculates durability-related features.

Current Features
----------------
- Average Fight Time
"""

from __future__ import annotations

import pandas as pd

from feature_engine.models import DurabilityStats

from feature_engine.constants import TOTAL_FIGHT_TIME

from feature_engine.core import safe_float


class DurabilityEngine:
    """
    Calculates durability metrics
    from historical fights.
    """

    def build(
        self,
        history: pd.DataFrame
    ) -> DurabilityStats:

        if history.empty:
            return DurabilityStats()

        average_fight_time = safe_float(

            history[
                TOTAL_FIGHT_TIME
            ].mean()

        )

        return DurabilityStats(

            average_fight_time=round(
                average_fight_time,
                2
            )
        )