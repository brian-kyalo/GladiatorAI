"""
GladiatorAI Dataset Builder Models

Domain objects used while constructing
machine-learning training data.

A DatasetBuildResult represents the outcome
of processing a collection of historical fights.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd


@dataclass
class SkippedFight:
    """
    Represents a historical fight that could not
    safely be converted into a training example.
    """

    row_index: int

    red_fighter: str

    blue_fighter: str

    fight_date: str

    reason: str


@dataclass
class DatasetBuildResult:
    """
    Result produced by DatasetBuilder.

    Attributes
    ----------
    rows:
        Machine-learning-ready matchup rows.

    skipped:
        Fights deliberately excluded from
        the generated dataset.
    """

    rows: pd.DataFrame = field(
        default_factory=pd.DataFrame
    )

    skipped: list[SkippedFight] = field(
        default_factory=list
    )

    @property
    def row_count(self) -> int:
        """
        Number of successfully generated
        training examples.
        """

        return len(self.rows)

    @property
    def skipped_count(self) -> int:
        """
        Number of historical fights that
        were skipped.
        """

        return len(self.skipped)

    @property
    def total_processed(self) -> int:
        """
        Total number of fights considered
        by the builder.
        """

        return (
            self.row_count
            + self.skipped_count
        )