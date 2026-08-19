"""
GladiatorAI Physical Engine

Builds a fighter's physical profile from
the latest valid pre-fight information.

Features
--------
- Age
- Height
- Reach
"""

from __future__ import annotations

import math

import pandas as pd

from feature_engine.constants import (
    R_AGE,
    B_AGE,
    R_HEIGHT,
    B_HEIGHT,
    R_REACH,
    B_REACH,
)

from feature_engine.models import PhysicalStats

from feature_engine.core import snapshot_value


class PhysicalEngine:
    """
    Retrieves physical characteristics from
    the latest valid pre-fight information.
    """

    def build(
        self,
        history: pd.DataFrame,
        fighter: str,
        fallback_fight: pd.Series | None = None,
    ) -> PhysicalStats:

        age = snapshot_value(
            history=history,
            fighter=fighter,
            red_column=R_AGE,
            blue_column=B_AGE,
            fallback_fight=fallback_fight,
        )

        height = snapshot_value(
            history=history,
            fighter=fighter,
            red_column=R_HEIGHT,
            blue_column=B_HEIGHT,
            fallback_fight=fallback_fight,
        )

        reach = snapshot_value(
            history=history,
            fighter=fighter,
            red_column=R_REACH,
            blue_column=B_REACH,
            fallback_fight=fallback_fight,
        )

        return PhysicalStats(
            age=self._measurement(age),
            height=self._measurement(height),
            reach=self._measurement(reach),
        )

    @staticmethod
    def _measurement(value) -> float:
        """
        Convert a valid measurement to float.

        Missing or invalid measurements remain NaN.
        """

        if pd.isna(value):

            return float("nan")

        try:

            value = float(value)

        except (TypeError, ValueError):

            return float("nan")

        if not math.isfinite(value):

            return float("nan")

        return value