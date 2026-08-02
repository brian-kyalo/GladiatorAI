"""
GladiatorAI Profile Engine

Builds a fighter's statistical profile using ONLY
information available before the snapshot date.
"""

import pandas as pd

from feature_engine.models import PreFightProfile

from feature_engine.calculators import (
    calculate_record,
    calculate_current_win_streak,
    calculate_current_lose_streak,
    calculate_finish_stats,
    calculate_average_fight_time,
    calculate_average_sig_strikes,
    calculate_average_takedowns,
    calculate_average_submissions,
    calculate_experience_score,
    calculate_momentum_score
)


class ProfileEngine:

    """
    Orchestrates GladiatorAI feature calculators
    and assembles the final PreFightProfile.
    """

    def build_profile(
        self,
        history: pd.DataFrame,
        fighter: str,
        snapshot_date
    ) -> PreFightProfile:

        snapshot_date = pd.to_datetime(
            snapshot_date
        )

        # ==========================================
        # SAFETY CHECK
        # ==========================================

        history = history.copy()

        history["date"] = pd.to_datetime(
            history["date"]
        )

        # Prevent future information leaking
        # into this fighter profile.

        history = history[
            history["date"] < snapshot_date
        ]

        # ==========================================
        # RECORD
        # ==========================================

        record = calculate_record(
            history,
            fighter
        )

        # ==========================================
        # STREAKS
        # ==========================================

        win_streak = calculate_current_win_streak(
            history,
            fighter
        )

        lose_streak = calculate_current_lose_streak(
            history,
            fighter
        )

        # ==========================================
        # FINISHING
        # ==========================================

        finish_stats = calculate_finish_stats(
            history,
            fighter
        )

        # ==========================================
        # PERFORMANCE
        # ==========================================

        average_fight_time = (
            calculate_average_fight_time(
                history
            )
        )

        average_sig_strikes = (
            calculate_average_sig_strikes(
                history,
                fighter
            )
        )

        average_takedowns = (
            calculate_average_takedowns(
                history,
                fighter
            )
        )

        average_submissions = (
            calculate_average_submissions(
                history,
                fighter
            )
        )

        # ==========================================
        # EXPERIENCE
        # ==========================================

        experience_score = (
            calculate_experience_score(
                record
            )
        )

        # ==========================================
        # MOMENTUM
        # ==========================================

        momentum_score = (
            calculate_momentum_score(
                win_streak,
                lose_streak
            )
        )

        # ==========================================
        # FINAL PROFILE
        # ==========================================

        return PreFightProfile(

            fighter=fighter,

            snapshot_date=snapshot_date,

            total_fights=record.total_fights,

            wins=record.wins,

            losses=record.losses,

            draws=record.draws,

            no_contests=record.no_contests,

            win_rate=record.win_rate,

            current_win_streak=win_streak,

            current_lose_streak=lose_streak,

            ko_wins=finish_stats["ko_wins"],

            submission_wins=(
                finish_stats["submission_wins"]
            ),

            decision_wins=(
                finish_stats["decision_wins"]
            ),

            ko_rate=finish_stats["ko_rate"],

            submission_rate=(
                finish_stats["submission_rate"]
            ),

            decision_rate=(
                finish_stats["decision_rate"]
            ),

            average_fight_time=(
                average_fight_time
            ),

            average_sig_strikes=(
                average_sig_strikes
            ),

            average_takedowns=(
                average_takedowns
            ),

            average_submissions=(
                average_submissions
            ),

            experience_score=(
                experience_score
            ),

            momentum_score=(
                momentum_score
            )
        )