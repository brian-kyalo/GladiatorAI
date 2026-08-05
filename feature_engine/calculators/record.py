"""
GladiatorAI Record Engine

Builds a fighter's professional record
using ONLY fights that occurred before
the supplied snapshot date.

Author:
GladiatorAI

Design Principles
-----------------
1. One class = one responsibility.
2. Pure calculations.
3. No printing.
4. No notebook code.
5. No side effects.
"""

from __future__ import annotations

import pandas as pd

from feature_engine.constants import (
    R_FIGHTER,
    B_FIGHTER,
    WINNER,
)

from feature_engine.models import RecordStats

from feature_engine.core import fight_result


class RecordEngine:
    """
    Calculates a fighter's career record.

    Parameters
    ----------
    history : DataFrame

        Historical fights already filtered
        by HistoryEngine.

    fighter : str

        Fighter whose record should be built.

    Returns
    -------
    RecordStats
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str
    ) -> RecordStats:

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
            wins
            + losses
            + draws
            + no_contests
        )

        decisive = wins + losses

        if decisive == 0:
            win_rate = 0.0
        else:
            win_rate = wins / decisive

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