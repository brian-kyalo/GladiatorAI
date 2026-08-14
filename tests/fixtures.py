"""
Reusable testing fixtures.

These helpers provide deterministic
data for every unit test.
"""

from pathlib import Path

import pandas as pd

from feature_engine.history import HistoryEngine


TEST_DATA = (
    Path(__file__).parent
    / "data"
    / "synthetic_history.csv"
)


def load_dataframe() -> pd.DataFrame:
    """
    Loads the synthetic UFC dataset.
    """

    return pd.read_csv(
        TEST_DATA,
        parse_dates=["date"]
    )


def build_history(
    fighter: str = "John Smith",
    before_date: str = "2025-01-01"
):
    """
    Returns a fighter's history
    using the real HistoryEngine.
    """

    dataframe = load_dataframe()

    engine = HistoryEngine(dataframe)

    return engine.get_history(
        fighter=fighter,
        before_date=before_date
    )