"""
GladiatorAI Matchup Engine

Compares two PreFightProfiles and produces
a MatchupProfile ready for machine learning.

The Matchup Engine NEVER knows anything about
the UFC dataset.

Its only job is:

Profile A
        vs
Profile B

↓

MatchupProfile
"""

from dataclasses import asdict
import pandas as pd

from feature_engine.models import PreFightProfile
from feature_engine.matchup_models import MatchupProfile

from feature_engine.comparison import (
    difference,
    absolute_difference,
    normalized_difference,
)


class MatchupEngine:
    """
    Compares two PreFightProfiles.

    The Red profile is always treated as
    Fighter A.

    The Blue profile is always treated as
    Fighter B.
    """

    def __init__(self):
        pass

    # =====================================================
    # BUILD MATCHUP
    # =====================================================

    def compare(
        self,
        red_profile: PreFightProfile,
        blue_profile: PreFightProfile,
        winner: str
    ) -> MatchupProfile:
        """
        Creates one matchup.

        Parameters
        ----------
        red_profile

        blue_profile

        winner
            "Red" or "Blue"

        Returns
        -------
        MatchupProfile
        """

        matchup = MatchupProfile(

            # -------------------------------------
            # Metadata
            # -------------------------------------

            red_fighter=red_profile.fighter,

            blue_fighter=blue_profile.fighter,

            snapshot_date=str(
                red_profile.snapshot_date.date()
            ),

            winner=winner,

            # -------------------------------------
            # Physical
            # -------------------------------------

            age_diff=0.0,

            height_diff=0.0,

            reach_diff=0.0,

            # -------------------------------------
            # Experience
            # -------------------------------------

            experience_diff=difference(

                red_profile.experience_score,

                blue_profile.experience_score

            ),

            wins_diff=difference(

                red_profile.wins,

                blue_profile.wins

            ),

            losses_diff=difference(

                red_profile.losses,

                blue_profile.losses

            ),

            win_rate_diff=difference(

                red_profile.win_rate,

                blue_profile.win_rate

            ),

            # -------------------------------------
            # Momentum
            # -------------------------------------

            win_streak_diff=difference(

                red_profile.current_win_streak,

                blue_profile.current_win_streak

            ),

            lose_streak_diff=difference(

                red_profile.current_lose_streak,

                blue_profile.current_lose_streak

            ),

            momentum_diff=difference(

                red_profile.momentum_score,

                blue_profile.momentum_score

            ),

            # -------------------------------------
            # Finishing
            # -------------------------------------

            ko_rate_diff=difference(

                red_profile.ko_rate,

                blue_profile.ko_rate

            ),

            submission_rate_diff=difference(

                red_profile.submission_rate,

                blue_profile.submission_rate

            ),

            decision_rate_diff=difference(

                red_profile.decision_rate,

                blue_profile.decision_rate

            ),

            # -------------------------------------
            # Performance
            # -------------------------------------

            fight_time_diff=difference(

                red_profile.average_fight_time,

                blue_profile.average_fight_time

            ),

            sig_strike_diff=difference(

                red_profile.average_sig_strikes,

                blue_profile.average_sig_strikes

            ),

            takedown_diff=difference(

                red_profile.average_takedowns,

                blue_profile.average_takedowns

            ),

            submission_attempt_diff=difference(

                red_profile.average_submissions,

                blue_profile.average_submissions

            )

        )

        return matchup

    # =====================================================
    # CONVERT TO DICTIONARY
    # =====================================================

    @staticmethod
    def to_dict(
        matchup: MatchupProfile
    ) -> dict:
        """
        Converts MatchupProfile into
        a Python dictionary.
        """

        return asdict(matchup)

    # =====================================================
    # CONVERT TO DATAFRAME
    # =====================================================

    @staticmethod
    def to_dataframe(
        matchup: MatchupProfile
    ) -> pd.DataFrame:
        """
        Converts one matchup into
        a single-row dataframe.
        """

        return pd.DataFrame(

            [asdict(matchup)]

        )

    # =====================================================
    # PRINT SCOUT CARD
    # =====================================================

    @staticmethod
    def scout_card(
        matchup: MatchupProfile
    ):
        """
        Prints an easy-to-read
        comparison card.

        Useful for debugging and
        manual inspection.
        """

        print()

        print("=" * 60)

        print("GLADIATOR AI MATCHUP")

        print("=" * 60)

        print()

        print(

            f"{matchup.red_fighter}"

            "\n"

            "vs"

            "\n"

            f"{matchup.blue_fighter}"

        )

        print()

        print("-" * 60)

        print("EXPERIENCE")

        print("-" * 60)

        print(

            "Difference:",

            matchup.experience_diff

        )

        print()

        print("RECORD")

        print(

            "Win Rate:",

            matchup.win_rate_diff

        )

        print(

            "Wins:",

            matchup.wins_diff

        )

        print(

            "Losses:",

            matchup.losses_diff

        )

        print()

        print("-" * 60)

        print("MOMENTUM")

        print("-" * 60)

        print(

            "Win Streak:",

            matchup.win_streak_diff

        )

        print(

            "Lose Streak:",

            matchup.lose_streak_diff

        )

        print(

            "Momentum:",

            matchup.momentum_diff

        )

        print()

        print("-" * 60)

        print("FINISHING")

        print("-" * 60)

        print(

            "KO Rate:",

            matchup.ko_rate_diff

        )

        print(

            "Submission Rate:",

            matchup.submission_rate_diff

        )

        print(

            "Decision Rate:",

            matchup.decision_rate_diff

        )

        print()

        print("-" * 60)

        print("PERFORMANCE")

        print("-" * 60)

        print(

            "Fight Time:",

            matchup.fight_time_diff

        )

        print(

            "Significant Strikes:",

            matchup.sig_strike_diff

        )

        print(

            "Takedowns:",

            matchup.takedown_diff

        )

        print(

            "Submission Attempts:",

            matchup.submission_attempt_diff

        )

        print()

        print("=" * 60)

        print(

            "Historical Winner:",

            matchup.winner

        )

        print("=" * 60)