"""
GladiatorAI Dataset Builder

Transforms historical UFC fights into
machine-learning training examples.

The Dataset Builder does NOT calculate
fighter features itself.

It orchestrates:

    Historical Fight
          ↓
    HistoryEngine
          ↓
    ProfileEngine
          ↓
    MatchupEngine
          ↓
    Training Row
"""

from __future__ import annotations

from typing import Optional

import pandas as pd

from feature_engine.constants import (
    DATE,
    R_FIGHTER,
    B_FIGHTER,
    WINNER,
)

from feature_engine.history import HistoryEngine
from feature_engine.profile import ProfileEngine
from feature_engine.matchup import MatchupEngine
from feature_engine.matchup_models import MatchupProfile

from .models import (
    DatasetBuildResult,
    SkippedFight,
)


class DatasetBuilder:
    """
    Builds a machine-learning dataset from
    historical UFC fights.
    """

    def __init__(
        self,
        dataframe: pd.DataFrame
    ) -> None:

        self.dataframe = dataframe.copy()

        self.dataframe[DATE] = pd.to_datetime(
            self.dataframe[DATE]
        )

        self.history_engine = HistoryEngine(
            self.dataframe
        )

        self.profile_engine = ProfileEngine()

        self.matchup_engine = MatchupEngine()

    # =====================================================
    # SINGLE FIGHT
    # =====================================================

    def build_fight(
        self,
        row_index: int,
        fight: pd.Series,
    ) -> tuple[
        Optional[MatchupProfile],
        Optional[SkippedFight],
    ]:
        """
        Convert one historical fight into
        one machine-learning matchup.

        Returns
        -------
        (MatchupProfile, None)
            when the fight can be used.

        (None, SkippedFight)
            when the fight must be excluded.
        """

        red_fighter = fight[R_FIGHTER]

        blue_fighter = fight[B_FIGHTER]

        fight_date = pd.to_datetime(
            fight[DATE]
        )

        winner = fight[WINNER]

        # =================================================
        # BASIC VALIDATION
        # =================================================

        if winner not in ("Red", "Blue"):

            return (
                None,

                SkippedFight(
                    row_index=row_index,

                    red_fighter=str(
                        red_fighter
                    ),

                    blue_fighter=str(
                        blue_fighter
                    ),

                    fight_date=str(
                        fight_date.date()
                    ),

                    reason=(
                        "Fight does not have a "
                        "standard Red/Blue winner."
                    ),
                ),
            )

        # =================================================
        # RED FIGHTER HISTORY
        # =================================================

        red_history = (
            self.history_engine.get_history(
                fighter=red_fighter,
                before_date=fight_date,
            )
        )

        # =================================================
        # BLUE FIGHTER HISTORY
        # =================================================

        blue_history = (
            self.history_engine.get_history(
                fighter=blue_fighter,
                before_date=fight_date,
            )
        )

        # =================================================
        # PRE-FIGHT PROFILES
        # =================================================

        red_profile = (
            self.profile_engine.build(
                history=red_history,
                fighter=red_fighter,
                snapshot_date=fight_date,
                fallback_fight=fight,
            )
        )

        blue_profile = (
            self.profile_engine.build(
                history=blue_history,
                fighter=blue_fighter,
                snapshot_date=fight_date,
                fallback_fight=fight,
            )
        )

        # =================================================
        # MATCHUP
        # =================================================

        matchup = self.matchup_engine.compare(
            red_profile=red_profile,
            blue_profile=blue_profile,
            winner=winner,
        )

        return matchup, None

    # =====================================================
    # COMPLETE DATASET
    # =====================================================

    def build(self) -> DatasetBuildResult:
        """
        Process every fight in the supplied
        historical dataset.
        """

        rows: list[dict] = []

        skipped: list[SkippedFight] = []

        # enumerate() gives us a guaranteed integer
        # row number independent of the DataFrame's
        # actual index type.
        for row_number, (_, fight) in enumerate(
            self.dataframe.iterrows()
        ):

            matchup, skipped_fight = (
                self.build_fight(
                    row_index=row_number,
                    fight=fight,
                )
            )

            # ---------------------------------------------
            # Fight was intentionally skipped
            # ---------------------------------------------

            if skipped_fight is not None:

                skipped.append(
                    skipped_fight
                )

                continue

            # ---------------------------------------------
            # Safety check
            # ---------------------------------------------

            if matchup is None:

                raise RuntimeError(
                    "DatasetBuilder received neither "
                    "a matchup nor a skipped-fight record."
                )

            # ---------------------------------------------
            # Convert matchup into one ML row
            # ---------------------------------------------

            rows.append(
                self.matchup_engine.to_dict(
                    matchup
                )
            )

        # ---------------------------------------------
        # Build final dataframe
        # ---------------------------------------------

        dataframe = pd.DataFrame(rows)

        return DatasetBuildResult(
            rows=dataframe,
            skipped=skipped,
        )