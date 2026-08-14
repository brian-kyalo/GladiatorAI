"""
GladiatorAI Momentum Engine

Calculates a fighter's recent form
immediately before a specified snapshot date.

Features
--------
- Current Win Streak
- Current Lose Streak
- Last Five Win Rate
- Momentum Score
"""

from __future__ import annotations

import pandas as pd

from feature_engine.models import MomentumStats
from feature_engine.core import fight_result


class MomentumEngine:
    """
    Calculates momentum-related features.

    The supplied history must already be
    sorted from newest to oldest.
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str
    ) -> MomentumStats:
        """
        Builds the fighter's momentum profile.
        """

        if history.empty:
            return MomentumStats()

        results = self._results(
            history,
            fighter
        )

        win_streak = self._win_streak(results)

        lose_streak = self._lose_streak(results)

        last_five_rate = self._last_five(results)

        momentum_score = float(
            win_streak - lose_streak
        )

        return MomentumStats(

            current_win_streak=win_streak,

            current_lose_streak=lose_streak,

            last_five_win_rate=round(
                last_five_rate,
                3
            ),

            momentum_score=momentum_score
        )

    # =====================================================
    # PRIVATE HELPERS
    # =====================================================

    def _results(
        self,
        history: pd.DataFrame,
        fighter: str
    ) -> list[str]:
        """
        Converts every historical fight into one of:

        WIN
        LOSS
        DRAW
        NC

        The returned list is ordered from
        newest fight to oldest fight.
        """

        results = []

        for _, fight in history.iterrows():

            results.append(

                fight_result(
                    fight,
                    fighter
                )

            )

        return results

    def _win_streak(
        self,
        results: list[str]
    ) -> int:
        """
        Counts consecutive wins starting
        from the fighter's most recent fight.
        """

        streak = 0

        for result in results:

            if result != "WIN":
                break

            streak += 1

        return streak

    def _lose_streak(
        self,
        results: list[str]
    ) -> int:
        """
        Counts consecutive losses starting
        from the fighter's most recent fight.
        """

        streak = 0

        for result in results:

            if result != "LOSS":
                break

            streak += 1

        return streak

    def _last_five(
        self,
        results: list[str]
    ) -> float:
        """
        Calculates the win percentage over
        the fighter's five most recent fights.
        """

        recent = results[:5]

        if not recent:
            return 0.0

        wins = recent.count("WIN")

        return wins / len(recent)