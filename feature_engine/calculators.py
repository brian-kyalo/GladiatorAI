"""
GladiatorAI Feature Calculators

Calculates fighter features from historical UFC fights.

RULE:
The history supplied to these functions must contain ONLY
fights that happened before the prediction snapshot date.
"""

from __future__ import annotations

import pandas as pd

from feature_engine.constants import *
from feature_engine.models import RecordStats


# ==========================================================
# INTERNAL HELPERS
# ==========================================================

def _is_missing(value) -> bool:
    return pd.isna(value)


def _safe_float(value, default=0.0) -> float:
    if _is_missing(value):
        return default

    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _safe_mean(values) -> float:
    cleaned = [
        float(value)
        for value in values
        if not _is_missing(value)
    ]

    if not cleaned:
        return 0.0

    return sum(cleaned) / len(cleaned)


def get_fighter_corner(fight, fighter: str) -> str | None:
    """
    Return the fighter's corner in this fight.
    """

    if fight[R_FIGHTER] == fighter:
        return "Red"

    if fight[B_FIGHTER] == fighter:
        return "Blue"

    return None


def get_fighter_result(fight, fighter: str) -> str:
    """
    Convert UFC Red/Blue results into a result
    from the fighter's perspective.
    """

    corner = get_fighter_corner(fight, fighter)

    if corner is None:
        return "UNKNOWN"

    winner = fight[WINNER]

    if winner == "Draw":
        return "DRAW"

    # Anything other than Red/Blue/Draw is treated
    # as a non-standard result such as NC.
    if winner not in ("Red", "Blue"):
        return "NC"

    if winner == corner:
        return "WIN"

    return "LOSS"


def _fighter_value(fight, fighter: str, red_column: str, blue_column: str):
    """
    Read the correct value regardless of whether
    the fighter competed from Red or Blue corner.
    """

    corner = get_fighter_corner(fight, fighter)

    if corner == "Red":
        return fight.get(red_column)

    if corner == "Blue":
        return fight.get(blue_column)

    return None


# ==========================================================
# RECORD
# ==========================================================

def calculate_record(
    history: pd.DataFrame,
    fighter: str
) -> RecordStats:

    wins = 0
    losses = 0
    draws = 0
    no_contests = 0

    for _, fight in history.iterrows():

        result = get_fighter_result(fight, fighter)

        if result == "WIN":
            wins += 1

        elif result == "LOSS":
            losses += 1

        elif result == "DRAW":
            draws += 1

        elif result == "NC":
            no_contests += 1

    total = wins + losses + draws + no_contests

    # Win rate is calculated from decisive fights.
    decisive_fights = wins + losses

    win_rate = (
        wins / decisive_fights
        if decisive_fights > 0
        else 0.0
    )

    return RecordStats(
        wins=wins,
        losses=losses,
        draws=draws,
        no_contests=no_contests,
        total_fights=total,
        win_rate=round(win_rate, 3)
    )


# ==========================================================
# STREAKS
# ==========================================================

def calculate_current_win_streak(
    history: pd.DataFrame,
    fighter: str
) -> int:

    ordered = history.sort_values(
        DATE,
        ascending=False
    )

    streak = 0

    for _, fight in ordered.iterrows():

        result = get_fighter_result(
            fight,
            fighter
        )

        if result == "WIN":
            streak += 1

        elif result in ("DRAW", "NC"):
            # Ignore non-decisive results.
            continue

        else:
            break

    return streak


def calculate_current_lose_streak(
    history: pd.DataFrame,
    fighter: str
) -> int:

    ordered = history.sort_values(
        DATE,
        ascending=False
    )

    streak = 0

    for _, fight in ordered.iterrows():

        result = get_fighter_result(
            fight,
            fighter
        )

        if result == "LOSS":
            streak += 1

        elif result in ("DRAW", "NC"):
            continue

        else:
            break

    return streak


# ==========================================================
# FINISH STATISTICS
# ==========================================================

def calculate_finish_stats(
    history: pd.DataFrame,
    fighter: str
) -> dict:

    ko_wins = 0
    submission_wins = 0
    decision_wins = 0

    for _, fight in history.iterrows():

        if get_fighter_result(fight, fighter) != "WIN":
            continue

        finish = str(
            fight.get("finish", "")
        ).upper()

        if "KO" in finish or "TKO" in finish:

            ko_wins += 1

        elif "SUB" in finish:

            submission_wins += 1

        elif "DEC" in finish:

            decision_wins += 1

    total_wins = (
        ko_wins
        + submission_wins
        + decision_wins
    )

    if total_wins == 0:

        ko_rate = 0.0
        submission_rate = 0.0
        decision_rate = 0.0

    else:

        ko_rate = ko_wins / total_wins
        submission_rate = submission_wins / total_wins
        decision_rate = decision_wins / total_wins

    return {
        "ko_wins": ko_wins,
        "submission_wins": submission_wins,
        "decision_wins": decision_wins,

        "ko_rate": round(ko_rate, 3),

        "submission_rate": round(
            submission_rate,
            3
        ),

        "decision_rate": round(
            decision_rate,
            3
        )
    }


# ==========================================================
# FIGHT TIME
# ==========================================================

def calculate_average_fight_time(
    history: pd.DataFrame
) -> float:

    column = "total_fight_time_secs"

    if column not in history.columns:
        return 0.0

    values = pd.to_numeric(
        history[column],
        errors="coerce"
    )

    if values.dropna().empty:
        return 0.0

    return round(
        values.mean(),
        2
    )


# ==========================================================
# STRIKING
# ==========================================================

def calculate_average_sig_strikes(
    history: pd.DataFrame,
    fighter: str
) -> float:

    values = []

    for _, fight in history.iterrows():

        value = _fighter_value(
            fight,
            fighter,
            "R_avg_SIG_STR_landed",
            "B_avg_SIG_STR_landed"
        )

        if not _is_missing(value):
            values.append(value)

    return round(
        _safe_mean(values),
        3
    )


# ==========================================================
# TAKEDOWNS
# ==========================================================

def calculate_average_takedowns(
    history: pd.DataFrame,
    fighter: str
) -> float:

    values = []

    for _, fight in history.iterrows():

        value = _fighter_value(
            fight,
            fighter,
            "R_avg_TD_landed",
            "B_avg_TD_landed"
        )

        if not _is_missing(value):
            values.append(value)

    return round(
        _safe_mean(values),
        3
    )


# ==========================================================
# SUBMISSION ATTEMPTS
# ==========================================================

def calculate_average_submissions(
    history: pd.DataFrame,
    fighter: str
) -> float:

    values = []

    for _, fight in history.iterrows():

        value = _fighter_value(
            fight,
            fighter,
            "R_avg_SUB_ATT",
            "B_avg_SUB_ATT"
        )

        if not _is_missing(value):
            values.append(value)

    return round(
        _safe_mean(values),
        3
    )


# ==========================================================
# EXPERIENCE
# ==========================================================

def calculate_experience_score(
    record: RecordStats
) -> float:
    """
    Simple V1 experience metric.

    More UFC fights = more UFC experience.

    Kept interpretable intentionally.
    """

    return float(
        record.total_fights
    )


# ==========================================================
# MOMENTUM
# ==========================================================

def calculate_momentum_score(
    win_streak: int,
    lose_streak: int
) -> float:
    """
    Positive = winning momentum.

    Negative = losing momentum.
    """

    return float(
        win_streak - lose_streak
    )