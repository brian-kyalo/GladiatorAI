"""
Fight Result Utilities

Converts UFC Red/Blue outcomes into
fighter-centric outcomes.
"""

from feature_engine.constants import (
    R_FIGHTER,
    B_FIGHTER,
    WINNER,
)


def fight_result(fight, fighter):
    """
    Returns the fighter's result.

    Returns
    -------
    WIN
    LOSS
    DRAW
    NC
    """

    if fight[R_FIGHTER] == fighter:
        corner = "Red"

    elif fight[B_FIGHTER] == fighter:
        corner = "Blue"

    else:
        raise ValueError(
            f"{fighter} not found in supplied fight."
        )

    winner = fight[WINNER]

    if winner == "Draw":
        return "DRAW"

    if winner not in ("Red", "Blue"):
        return "NC"

    if winner == corner:
        return "WIN"

    return "LOSS"