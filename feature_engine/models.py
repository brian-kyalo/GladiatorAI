"""
GladiatorAI Domain Models

Every major concept in GladiatorAI is represented
by a dataclass.

Design Principle:
One dataclass = One concept.
"""

from dataclasses import dataclass, field
import pandas as pd


# ==========================================================
# PHYSICAL
# ==========================================================

@dataclass
class PhysicalStats:
    """
    Physical characteristics of a fighter
    immediately before a fight.
    """

    age: float = 0.0
    height: float = 0.0
    reach: float = 0.0


# ==========================================================
# RECORD
# ==========================================================

@dataclass
class RecordStats:
    """
    Career record before the snapshot date.
    """

    wins: int = 0
    losses: int = 0
    draws: int = 0
    no_contests: int = 0

    total_fights: int = 0

    win_rate: float = 0.0


# ==========================================================
# MOMENTUM
# ==========================================================

@dataclass
class MomentumStats:
    """
    Recent form.
    """

    current_win_streak: int = 0

    current_lose_streak: int = 0

    last_five_win_rate: float = 0.0

    momentum_score: float = 0.0


# ==========================================================
# FINISHING
# ==========================================================

@dataclass
class FinishingStats:
    """
    How a fighter wins.
    """

    ko_wins: int = 0

    submission_wins: int = 0

    decision_wins: int = 0

    finish_rate: float = 0.0

    ko_rate: float = 0.0

    submission_rate: float = 0.0

    decision_rate: float = 0.0


# ==========================================================
# STRIKING
# ==========================================================

@dataclass
class StrikingStats:
    """
    Offensive striking metrics.
    """

    average_sig_strikes: float = 0.0

    strike_accuracy: float = 0.0

    strike_defence: float = 0.0

    strike_differential: float = 0.0


# ==========================================================
# GRAPPLING
# ==========================================================

@dataclass
class GrapplingStats:
    """
    Wrestling and grappling metrics.
    """

    average_takedowns: float = 0.0

    takedown_accuracy: float = 0.0

    takedown_defence: float = 0.0

    average_submission_attempts: float = 0.0


# ==========================================================
# DURABILITY
# ==========================================================

@dataclass
class DurabilityStats:
    """
    Ability to survive damage.
    """

    average_fight_time: float = 0.0

    average_sig_strikes_absorbed: float = 0.0


# ==========================================================
# ACTIVITY
# ==========================================================

@dataclass
class ActivityStats:
    """
    Recent activity.
    """

    days_since_last_fight: int = 0

    fights_last_year: int = 0


# ==========================================================
# PRE FIGHT PROFILE
# ==========================================================

@dataclass
class PreFightProfile:
    """
    Complete snapshot of a fighter
    immediately before one fight.

    This object is the heart of GladiatorAI.
    """

    fighter: str

    snapshot_date: pd.Timestamp

    physical: PhysicalStats = field(
        default_factory=PhysicalStats
    )

    record: RecordStats = field(
        default_factory=RecordStats
    )

    momentum: MomentumStats = field(
        default_factory=MomentumStats
    )

    finishing: FinishingStats = field(
        default_factory=FinishingStats
    )

    striking: StrikingStats = field(
        default_factory=StrikingStats
    )

    grappling: GrapplingStats = field(
        default_factory=GrapplingStats
    )

    durability: DurabilityStats = field(
        default_factory=DurabilityStats
    )

    activity: ActivityStats = field(
        default_factory=ActivityStats
    )