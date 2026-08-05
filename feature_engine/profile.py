"""
GladiatorAI Profile Engine

Builds a complete PreFightProfile using
all Feature Engineering calculators.

This class is the public entry point for
creating fighter profiles.
"""

from __future__ import annotations

import pandas as pd

from feature_engine.models import PreFightProfile

from feature_engine.calculators import (
    RecordEngine,
    PhysicalEngine,
    ActivityEngine,
    MomentumEngine,
    FinishingEngine,
    StrikingEngine,
    GrapplingEngine,
    DurabilityEngine,
)


class ProfileEngine:
    """
    Builds a complete fighter profile
    immediately before a given fight.

    This class orchestrates all
    calculator engines.
    """

    def __init__(self):

        self.record_engine = RecordEngine()

        self.physical_engine = PhysicalEngine()

        self.activity_engine = ActivityEngine()

        self.momentum_engine = MomentumEngine()

        self.finishing_engine = FinishingEngine()

        self.striking_engine = StrikingEngine()

        self.grappling_engine = GrapplingEngine()

        self.durability_engine = DurabilityEngine()

    def build(
        self,
        history: pd.DataFrame,
        fighter: str,
        snapshot_date
    ) -> PreFightProfile:

        snapshot_date = pd.to_datetime(snapshot_date)

        profile = PreFightProfile(

            fighter=fighter,

            snapshot_date=snapshot_date
        )

        # ---------------------------------
        # Feature Groups
        # ---------------------------------

        profile.record = self.record_engine.build(
            history,
            fighter
        )

        profile.physical = self.physical_engine.build(
            history,
            fighter
        )

        profile.activity = self.activity_engine.build(
            history,
            snapshot_date
        )

        profile.momentum = self.momentum_engine.build(
            history,
            fighter
        )

        profile.finishing = self.finishing_engine.build(
            history,
            fighter
        )

        profile.striking = self.striking_engine.build(
            history,
            fighter
        )

        profile.grappling = self.grappling_engine.build(
            history,
            fighter
        )

        profile.durability = self.durability_engine.build(
            history
        )

        return profile