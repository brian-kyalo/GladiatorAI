"""
Global pytest fixtures.

Automatically available
to every test.
"""

import pytest

from tests.fixtures import (
    load_dataframe,
    build_history,
)


@pytest.fixture
def dataframe():
    """
    Returns the synthetic dataframe.
    """

    return load_dataframe()


@pytest.fixture
def history():
    """
    Returns John Smith's history
    before 2025.
    """

    return build_history()


@pytest.fixture
def fighter():
    """
    Default fighter used
    throughout the tests.
    """

    return "John Smith"


@pytest.fixture
def snapshot_date():
    """
    Common snapshot date.
    """

    return "2025-01-01"