"""
GladiatorAI Matchup Engine 

Compares two PreFightProfiles and produces
a MatchupProfile ready for machine learning.

The Matchup Engine does not calculate fighter
statistics itself.

Its responsibility is:

    PreFightProfile
            +
    PreFightProfile
            ↓
      MatchupProfile

"""

from __future__ import annotations

from dataclasses import asdict

import pandas as pd

from feature_engine.models import PreFightProfile
from feature_engine.matchup_models import MatchupProfile

from feature_engine.comparison import difference

class MatchupEngine: 
    """
    Compares two pre-fight fighter profiles.

    Red and Blue are kept in their original
    UFC corner orientation.
    """

    def compare(
            self,
            red_profile: PreFightProfile,
            blue_profile: PreFightProfile,
            winner: str,

    ) -> MatchupProfile: 
        """
        Compare two pre-fight profiles 

        All features are rep as:

             Red value - Blue value 

        The winner is kept separately as the
        supervised-learning target.
        """

        return MatchupProfile(
            # ---------------------------------------------
            # Metadata
            # ---------------------------------------------

            red_fighter=red_profile.fighter,

            blue_fighter=blue_profile.fighter,

            snapshot_date=str(
                red_profile.snapshot_date.date()
            ),

            winner=winner,

            # ---------------------------------------------
            # Physical
            # ---------------------------------------------

            age_diff=difference(
                red_profile.physical.age,
                blue_profile.physical.age,
            ),

            height_diff=difference(
                red_profile.physical.height,
                blue_profile.physical.height,
            ),

            reach_diff=difference(
                red_profile.physical.reach,
                blue_profile.physical.reach,
            ),

            # ---------------------------------------------
            # Record / Experience
            # ---------------------------------------------

            experience_diff=difference(
                red_profile.record.total_fights,
                blue_profile.record.total_fights,
            ),

            wins_diff=difference(
                red_profile.record.wins,
                blue_profile.record.wins,
            ),

            losses_diff=difference(
                red_profile.record.losses,
                blue_profile.record.losses,
            ),

            win_rate_diff=difference(
                red_profile.record.win_rate,
                blue_profile.record.win_rate,
            ),

            # ---------------------------------------------
            # Momentum
            # ---------------------------------------------

            win_streak_diff=difference(
                red_profile.momentum.current_win_streak,
                blue_profile.momentum.current_win_streak,
            ),

            lose_streak_diff=difference(
                red_profile.momentum.current_lose_streak,
                blue_profile.momentum.current_lose_streak,
            ),

            momentum_diff=difference(
                red_profile.momentum.momentum_score,
                blue_profile.momentum.momentum_score,
            ),

            # ---------------------------------------------
            # Finishing
            # ---------------------------------------------

            ko_rate_diff=difference(
                red_profile.finishing.ko_rate,
                blue_profile.finishing.ko_rate,
            ),

            submission_rate_diff=difference(
                red_profile.finishing.submission_rate,
                blue_profile.finishing.submission_rate,
            ),

            decision_rate_diff=difference(
                red_profile.finishing.decision_rate,
                blue_profile.finishing.decision_rate,
            ),

            # ---------------------------------------------
            # Striking
            # ---------------------------------------------

            fight_time_diff=difference(
                red_profile.durability.average_fight_time,
                blue_profile.durability.average_fight_time,
            ),

            sig_strike_diff=difference(
                red_profile.striking.average_sig_strikes,
                blue_profile.striking.average_sig_strikes,
            ),

            # ---------------------------------------------
            # Grappling
            # ---------------------------------------------

            takedown_diff=difference(
                red_profile.grappling.average_takedowns,
                blue_profile.grappling.average_takedowns,
            ),

            submission_attempt_diff=difference(
                red_profile.grappling.average_submission_attempts,
                blue_profile.grappling.average_submission_attempts,
            ),
        )

    # =====================================================
    # CONVERSION HELPERS
    # =====================================================

    @staticmethod
    def to_dict(
        matchup: MatchupProfile,
    ) -> dict:
        """
        Convert a MatchupProfile into
        a standard Python dictionary.
        """

        return asdict(matchup)

    @staticmethod
    def to_dataframe(
        matchup: MatchupProfile,
    ) -> pd.DataFrame:
        """
        Convert one MatchupProfile into
        a one-row DataFrame.
        """

        return pd.DataFrame(
            [asdict(matchup)]
        )

    # =====================================================
    # SCOUT CARD
    # =====================================================

    @staticmethod
    def scout_card(
        matchup: MatchupProfile,
    ) -> None:
        """
        Display a human-readable matchup
        summary for inspection.
        """

        print()
        print("=" * 60)
        print("GLADIATOR AI MATCHUP")
        print("=" * 60)

        print()
        print(matchup.red_fighter)
        print("vs")
        print(matchup.blue_fighter)

        print()
        print("-" * 60)
        print("PHYSICAL")
        print("-" * 60)

        print("Age Difference:", matchup.age_diff)
        print("Height Difference:", matchup.height_diff)
        print("Reach Difference:", matchup.reach_diff)

        print()
        print("-" * 60)
        print("EXPERIENCE")
        print("-" * 60)

        print("Experience Difference:", matchup.experience_diff)
        print("Wins Difference:", matchup.wins_diff)
        print("Losses Difference:", matchup.losses_diff)
        print("Win Rate Difference:", matchup.win_rate_diff)

        print()
        print("-" * 60)
        print("MOMENTUM")
        print("-" * 60)

        print("Win Streak Difference:", matchup.win_streak_diff)
        print("Lose Streak Difference:", matchup.lose_streak_diff)
        print("Momentum Difference:", matchup.momentum_diff)

        print()
        print("-" * 60)
        print("FINISHING")
        print("-" * 60)

        print("KO Rate Difference:", matchup.ko_rate_diff)
        print(
            "Submission Rate Difference:",
            matchup.submission_rate_diff,
        )
        print(
            "Decision Rate Difference:",
            matchup.decision_rate_diff,
        )

        print()
        print("-" * 60)
        print("PERFORMANCE")
        print("-" * 60)

        print(
            "Fight Time Difference:",
            matchup.fight_time_diff,
        )

        print(
            "Significant Strike Difference:",
            matchup.sig_strike_diff,
        )

        print(
            "Takedown Difference:",
            matchup.takedown_diff,
        )

        print(
            "Submission Attempt Difference:",
            matchup.submission_attempt_diff,
        )

        print()
        print("=" * 60)
        print("Historical Winner:", matchup.winner)
        print("=" * 60)