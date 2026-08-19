"""
GladiatorAI Profile Engine

Builds a complete PreFightProfile using
all Feature Engineering calculators.

The ProfileEngine orchestrates the calculators
and does not calculate individual features itself.
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
    Builds a complete fighter profile immediately
    before a specified fight.
    """

    def __init__(self) -> None:

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
        snapshot_date,
        fallback_fight: pd.Series | None = None,
    ) -> PreFightProfile:
        """
        Build a complete pre-fight profile.

        fallback_fight is used for fighters with
        no previous UFC history, such as UFC debutants.
        """

        snapshot_date = pd.to_datetime(
            snapshot_date
        )

        profile = PreFightProfile(
            fighter=fighter,
            snapshot_date=snapshot_date,
        )

        # =============================================
        # RECORD
        # =============================================

        profile.record = self.record_engine.build(
            history=history,
            fighter=fighter,
        )

        # =============================================
        # PHYSICAL
        # =============================================

        profile.physical = self.physical_engine.build(
            history=history,
            fighter=fighter,
            fallback_fight=fallback_fight,
        )

        # =============================================
        # ACTIVITY
        # =============================================

        profile.activity = self.activity_engine.build(
            history=history,
            snapshot_date=snapshot_date,
        )

        # =============================================
        # MOMENTUM
        # =============================================

        profile.momentum = self.momentum_engine.build(
            history=history,
            fighter=fighter,
        )

        # =============================================
        # FINISHING
        # =============================================

        profile.finishing = self.finishing_engine.build(
            history=history,
            fighter=fighter,
        )

        # =============================================
        # STRIKING
        # =============================================

        profile.striking = self.striking_engine.build(
            history=history,
            fighter=fighter,
        )

        # =============================================
        # GRAPPLING
        # =============================================

        profile.grappling = self.grappling_engine.build(
            history=history,
            fighter=fighter,
        )

        # =============================================
        # DURABILITY
        # =============================================

        profile.durability = self.durability_engine.build(
            history=history
        )

        return profile