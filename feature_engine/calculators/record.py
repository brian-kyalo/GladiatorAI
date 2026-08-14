"""
GladiatorAI Record Engine

Builds a fighter's professional record
using only fights that occurred before
the supplied snapshot date.

Design Principles
-----------------
1. One engine = one responsibility.
2. Pure calculations.
3. No side effects.
4. Returns a typed RecordStats object.
"""

from __future__ import annotations

import pandas as pd

from feature_engine.models import RecordStats
from feature_engine.core import fight_result


class RecordEngine:
    """
    Calculates a fighter's professional record
    from historical fight outcomes.
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str
    ) -> RecordStats:
        """
        Builds the fighter's career record.
        """

        if history.empty:
            return RecordStats()

        wins = 0
        losses = 0
        draws = 0
        no_contests = 0

        for _, fight in history.iterrows():

            result = fight_result(
                fight,
                fighter
            )

            if result == "WIN":

                wins += 1

            elif result == "LOSS":

                losses += 1

            elif result == "DRAW":

                draws += 1

            else:

                no_contests += 1

        total_fights = (
            wins +
            losses +
            draws +
            no_contests
        )

        decisive_fights = wins + losses

        win_rate = (
            wins / decisive_fights
            if decisive_fights
            else 0.0
        )

        return RecordStats(

            wins=wins,

            losses=losses,

            draws=draws,

            no_contests=no_contests,

            total_fights=total_fights,

            win_rate=round(
                win_rate,
                3
            )
        )