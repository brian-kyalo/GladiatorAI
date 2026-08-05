"""
Fight Finish Utilities

Converts raw UFC finish labels
into standardized finish categories.
"""


def finish_category(finish: str) -> str:
    """
    Converts UFC finish labels into
    GladiatorAI finish categories.

    Returns
    -------
    KO
    SUBMISSION
    DECISION
    OTHER
    """

    if finish == "KO/TKO":
        return "KO"

    if finish == "SUB":
        return "SUBMISSION"

    if finish in (
        "U-DEC",
        "S-DEC",
        "M-DEC",
    ):
        return "DECISION"

    return "OTHER"