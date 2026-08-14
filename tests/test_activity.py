"""
Tests for ActivityEngine.
"""

from feature_engine.calculators import ActivityEngine


def test_activity_engine_calculates_recent_activity(
    history,
    snapshot_date
):
    """
    John Smith's latest fight was

    2024-06-01

    Snapshot

    2025-01-01
    """

    engine = ActivityEngine()

    activity = engine.build(
        history,
        snapshot_date
    )

    #
    # Days from 2024-06-01
    # to 2025-01-01
    #

    assert activity.days_since_last_fight == 214

    #
    # Fights during the previous year:
    #
    # 2024
    # 2023
    #

    assert activity.fights_last_year == 1