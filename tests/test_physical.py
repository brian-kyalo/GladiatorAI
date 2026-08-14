"""
Tests for PhysicalEngine.
"""

from feature_engine.calculators import PhysicalEngine


def test_physical_engine(history, fighter):

    engine = PhysicalEngine()

    physical = engine.build(
        history,
        fighter
    )

    #
    # Latest snapshot is
    # 2024-06-01
    #

    assert physical.age == 30

    assert physical.height == 180

    assert physical.reach == 183