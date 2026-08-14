"""
GladiatorAI Core

Shared domain logic used throughout
the Feature Engineering library.
"""

from .results import fight_result
from .finishes import finish_category
from .numbers import safe_float
from .snapshots import latest_snapshot

__all__ = [
    "fight_result",
    "finish_category",
    "safe_float",
    "latest_snapshot",
]