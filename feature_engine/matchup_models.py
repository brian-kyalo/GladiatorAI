"""
GladiatorAI Matchup Models

Objects representing a fight
between two pre-fight profiles.
"""

from dataclasses import dataclass


@dataclass
class MatchupProfile:
    """
    Represents one historical matchup.

    This object eventually becomes
    one row inside the machine learning
    training dataset.
    """

    # ==========================================
    # Metadata
    # ==========================================

    red_fighter: str

    blue_fighter: str

    snapshot_date: str

    winner: str

    # ==========================================
    # Physical Differences
    # ==========================================

    age_diff: float = 0.0

    height_diff: float = 0.0

    reach_diff: float = 0.0

    # ==========================================
    # Record
    # ==========================================

    experience_diff: float = 0.0

    wins_diff: float = 0.0

    losses_diff: float = 0.0

    win_rate_diff: float = 0.0

    # ==========================================
    # Momentum
    # ==========================================

    win_streak_diff: float = 0.0

    lose_streak_diff: float = 0.0

    momentum_diff: float = 0.0

    # ==========================================
    # Finishing Ability
    # ==========================================

    ko_rate_diff: float = 0.0

    submission_rate_diff: float = 0.0

    decision_rate_diff: float = 0.0

    # ==========================================
    # Performance
    # ==========================================

    fight_time_diff: float = 0.0

    sig_strike_diff: float = 0.0

    takedown_diff: float = 0.0

    submission_attempt_diff: float = 0.0