"""
Tests for MomentumEngine.
"""

from feature_engine.calculators import MomentumEngine


def test_momentum_engine_calculates_recent_form(
    history,
    fighter
):
    """
    Synthetic history

    WIN
    WIN
    LOSS
    WIN
    WIN
    """

    engine = MomentumEngine()

    momentum = engine.build(
        history,
        fighter
    )

    #
    # Recent sequence
    #
    # W
    # W
    # L
    # W
    # W
    #

    assert momentum.current_win_streak == 2

    assert momentum.current_lose_streak == 0

    assert momentum.last_five_win_rate == 0.8

    assert momentum.momentum_score == 2.0