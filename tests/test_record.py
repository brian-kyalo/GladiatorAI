"""
Tests for RecordEngine.
"""

from feature_engine.calculators import RecordEngine


def test_record_engine(history, fighter):
    """
    John Smith's synthetic history:

    WIN
    WIN
    LOSS
    WIN
    WIN
    """

    engine = RecordEngine()

    record = engine.build(
        history,
        fighter
    )

    assert record.wins == 4

    assert record.losses == 1

    assert record.draws == 0

    assert record.no_contests == 0

    assert record.total_fights == 5

    assert record.win_rate == 0.800