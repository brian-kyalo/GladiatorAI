"""
GladiatorAI Momentum Engine

Measures a fighter's recent form
before a snapshot date.

Features
--------
- Current Win Streak
- Current Lose Streak
- Last Five Win Rate
- Momentum Score
"""

from __future__ import annotations

import pandas as pd

from feature_engine.constants import (
    R_FIGHTER,
    B_FIGHTER,
    WINNER,
)

from feature_engine.models import MomentumStats


from feature_engine.core import fight_result


class MomentumEngine:
    """
    Calculates recent performance.

    The supplied history must already
    be sorted from newest to oldest.
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str
    ) -> MomentumStats:

        if history.empty:
            return MomentumStats()

        results = self._results(
            history,
            fighter
        )

        win_streak = self._win_streak(results)

        lose_streak = self._lose_streak(results)

        last_five_rate = self._last_five(results)

        momentum = float(
            win_streak - lose_streak
        )

        return MomentumStats(

            current_win_streak=win_streak,

            current_lose_streak=lose_streak,

            last_five_win_rate=round(
                last_five_rate,
                3
            ),

            momentum_score=momentum
        )

    # ======================================
    # PRIVATE HELPERS
    # ======================================

    def _results(
        self,
        history,
        fighter
    ):
        """
        Converts every fight into

        WIN

        LOSS

        DRAW

        NC
        """

        output = []

        for _, fight in history.iterrows():

            output.append(
                fight_result(
                    fight,
                    fighter
                )
            )
        return output

    def _win_streak(
        self,
        results
    ):

        streak = 0

        for result in results:

            if result == "WIN":

                streak += 1

            else:

                break

        return streak

    def _lose_streak(
        self,
        results
    ):

        streak = 0

        for result in results:

            if result == "LOSS":

                streak += 1

            else:

                break

        return streak

    def _last_five(
        self,
        results
    ):

        recent = results[:5]

        if len(recent) == 0:

            return 0

        wins = recent.count("WIN")

        return wins / len(recent)