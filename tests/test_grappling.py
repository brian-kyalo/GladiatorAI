"""
Tests for GrapplingEngine.
"""

from feature_engine.calculators import GrapplingEngine


def test_grappling_engine_uses_latest_snapshot(
    history,
    fighter
):
    """
    Latest snapshot

    2024-06-01
    """

    engine = GrapplingEngine()

    grappling = engine.build(
        history,
        fighter
    )

    #
    # Values from the latest snapshot
    #

    assert grappling.average_takedowns == 1.5

    assert grappling.takedown_accuracy == 0.45

    assert grappling.average_submission_attempts == 0.4