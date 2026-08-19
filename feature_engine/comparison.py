"""
GladiatorAI Comparison Utilities

Compares individual fighter features while
preserving missing information.

Important:
    Unknown != zero.

When either side of a comparison is missing,
the resulting difference is NaN.
"""

from __future__ import annotations

import math


def difference(
    red_value,
    blue_value,
) -> float:
    """
    Calculate:

        Red - Blue

    If either value is missing, return NaN.

    This prevents missing physical/statistical
    measurements from becoming fake advantages.
    """

    if red_value is None or blue_value is None:
        return float("nan")

    try:
        red = float(red_value)
        blue = float(blue_value)
    except (TypeError, ValueError):
        return float("nan")

    if not math.isfinite(red):
        return float("nan")

    if not math.isfinite(blue):
        return float("nan")

    return red - blue