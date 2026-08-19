"""
GladiatorAI Dataset Builder

Public interface for dataset generation.
"""

from .builder import DatasetBuilder

from .models import (
    DatasetBuildResult,
    SkippedFight,
)

__all__ = [
    "DatasetBuilder",
    "DatasetBuildResult",
    "SkippedFight",
]