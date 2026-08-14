"""
Tests for FinishingEngine.
"""

from feature_engine.calculators import FinishingEngine


def test_finishing_engine_calculates_finishing_statistics(
    history,
    fighter
):
    """
    Synthetic history

    WIN (KO)
    WIN (DEC)
    LOSS (SUB)
    WIN (KO)
    WIN (DEC)

    Winning finishes:

    KO = 2
    DEC = 2
    SUB = 0
    """

    engine = FinishingEngine()

    finishing = engine.build(
        history,
        fighter
    )

    # Raw counts

    assert finishing.ko_wins == 2

    assert finishing.submission_wins == 0

    assert finishing.decision_wins == 2

    # Rates

    assert finishing.finish_rate == 0.5

    assert finishing.ko_rate == 0.5

    assert finishing.submission_rate == 0.0

    assert finishing.decision_rate == 0.5