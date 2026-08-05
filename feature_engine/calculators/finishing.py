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
    Builds finishing statistics from
    a fighter's historical wins.
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

            # We only care about victories
            if fight_result(fight, fighter) != "WIN":
                continue

            total_wins += 1

            finish = finish_category(
                fight[FINISH]
            )

            if finish == "KO":
                ko_wins += 1

            elif finish == "SUBMISSION":
                submission_wins += 1

            elif finish == "DECISION":
                decision_wins += 1

        if total_wins == 0:

            ko_rate = 0.0
            submission_rate = 0.0
            decision_rate = 0.0
            finish_rate = 0.0

        else:

            ko_rate = ko_wins / total_wins

            submission_rate = (
                submission_wins /
                total_wins
            )

            decision_rate = (
                decision_wins /
                total_wins
            )

            finish_rate = (
                ko_wins +
                submission_wins
            ) / total_wins

        return FinishingStats(

            ko_wins=ko_wins,

            submission_wins=submission_wins,

            decision_wins=decision_wins,

            finish_rate=round(
                finish_rate,
                3
            ),

            ko_rate=round(
                ko_rate,
                3
            ),

            submission_rate=round(
                submission_rate,
                3
            ),

            decision_rate=round(
                decision_rate,
                3
            )
        )