"""
GladiatorAI Activity Engine

Measures how active a fighter has been
before a snapshot date.

Features
--------
- Days Since Last Fight
- Fights Last Year
"""

from __future__ import annotations

import pandas as pd

from feature_engine.models import ActivityStats


class ActivityEngine:
    """
    Calculates fighter activity.

    Activity describes how recently
    and how frequently a fighter has
    competed.
    """

    def build(
        self,
        history: pd.DataFrame,
        snapshot_date
    ) -> ActivityStats:

        snapshot_date = pd.to_datetime(snapshot_date)

        if history.empty:

            return ActivityStats()

        # -----------------------------
        # Days Since Last Fight
        # -----------------------------

        latest_fight = history.iloc[0]["date"]

        days_since_last_fight = (

            snapshot_date -

            latest_fight

        ).days

        # -----------------------------
        # Fights Last Year
        # -----------------------------

        one_year_ago = (

            snapshot_date -

            pd.Timedelta(days=365)

        )

        fights_last_year = len(

            history[
                history["date"] >= one_year_ago
            ]

        )

        return ActivityStats(

            days_since_last_fight=days_since_last_fight,

            fights_last_year=fights_last_year

        )