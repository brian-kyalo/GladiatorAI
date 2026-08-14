"""
GladiatorAI Finishing Engine

Calculates how a fighter wins.

Features
--------
- KO Wins
- Submission Wins
- Decision Wins
- Finish Rate
- KO Rate
- Submission Rate
- Decision Rate
"""

from __future__ import annotations

import pandas as pd

from feature_engine.constants import FINISH

from feature_engine.models import FinishingStats

from feature_engine.core import (
    fight_result,
    finish_category,
)


class FinishingEngine:
    """
    Calculates finishing statistics
    from a fighter's historical victories.
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str
    ) -> FinishingStats:

        if history.empty:
            return FinishingStats()

        ko_wins = 0
        submission_wins = 0
        decision_wins = 0
        total_wins = 0

        for _, fight in history.iterrows():

            if fight_result(fight, fighter) != "WIN":
                continue

            total_wins += 1

            category = finish_category(
                fight[FINISH]
            )

            if category == "KO":
                ko_wins += 1

            elif category == "SUBMISSION":
                submission_wins += 1

            elif category == "DECISION":
                decision_wins += 1

        if total_wins == 0:

            return FinishingStats()

        return FinishingStats(

            ko_wins=ko_wins,

            submission_wins=submission_wins,

            decision_wins=decision_wins,

            finish_rate=round(
                (ko_wins + submission_wins)
                / total_wins,
                3
            ),

            ko_rate=round(
                ko_wins / total_wins,
                3
            ),

            submission_rate=round(
                submission_wins / total_wins,
                3
            ),

            decision_rate=round(
                decision_wins / total_wins,
                3
            )
        )