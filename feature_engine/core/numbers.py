"""
Numeric helper functions.

Used across every calculator to safely
convert dataset values into floats.
"""

from __future__ import annotations

import pandas as pd


def safe_float(value, default=0.0):
    """
    Safely converts a value to float.

    Missing values become the supplied default.
    """

    if pd.isna(value):
        return float(default)

    return float(value)