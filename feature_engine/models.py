"""
GladiatorAI Models

Domain Models used throughout GladiatorAI.
"""

from dataclasses import dataclass
import pandas as pd


# ==========================================================
# RECORD STATISTICS
# ==========================================================

@dataclass
class RecordStats:
    """
    Fighter career record before a snapshot date.
    """

    wins: int
    losses: int
    draws: int
    no_contests: int
    total_fights: int
    win_rate: float


# ==========================================================
# PRE-FIGHT PROFILE
# ==========================================================

@dataclass
class PreFightProfile:
    """
    Snapshot of a fighter immediately before a fight.
    """

    fighter: str

    snapshot_date: pd.Timestamp

    total_fights: int = 0

    wins: int = 0
    losses: int = 0
    draws: int = 0
    no_contests: int = 0

    win_rate: float = 0.0

    current_win_streak: int = 0
    current_lose_streak: int = 0

    ko_wins: int = 0
    submission_wins: int = 0
    decision_wins: int = 0

    ko_rate: float = 0.0
    submission_rate: float = 0.0
    decision_rate: float = 0.0

    average_fight_time: float = 0.0

    average_sig_strikes: float = 0.0
    average_takedowns: float = 0.0
    average_submissions: float = 0.0

    experience_score: float = 0.0
    momentum_score: float = 0.05