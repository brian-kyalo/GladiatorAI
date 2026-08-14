"""
Tests for DurabilityEngine.
"""

from feature_engine.calculators import DurabilityEngine


def test_durability_engine_calculates_average_fight_time(
    history
):
    """
    Average fight duration.

    Synthetic fight times:

    300
    900
    420
    240
    900
    """

    engine = DurabilityEngine()

    durability = engine.build(
        history
    )

    expected = round(

        (
            300 +
            900 +
            420 +
            240 +
            900
        ) / 5,

        2

    )

    assert durability.average_fight_time == expected