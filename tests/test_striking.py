"""
Tests for StrikingEngine.
"""

from feature_engine.calculators import StrikingEngine


def test_striking_engine_uses_latest_snapshot(
    history,
    fighter
):
    """
    Latest snapshot

    2024-06-01
    """

    engine = StrikingEngine()

    striking = engine.build(
        history,
        fighter
    )

    #
    # Latest Red corner statistics
    #

    assert striking.average_sig_strikes == 5.2

    assert striking.strike_accuracy == 0.55