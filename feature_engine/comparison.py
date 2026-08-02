"""
GladiatorAI Comparison Utilities

Small reusable mathematical
comparison functions.

Every comparison performed inside
the Matchup Engine should come
through this file.
"""

import math


# =====================================================
# BASIC DIFFERENCE
# =====================================================

def difference(red, blue):
    """
    Returns

    Red - Blue

    Example

    15 - 10 = 5
    """

    return round(red - blue, 3)


# =====================================================
# ABSOLUTE DIFFERENCE
# =====================================================

def absolute_difference(red, blue):

    return round(abs(red - blue), 3)


# =====================================================
# SAFE RATIO
# =====================================================

def ratio(red, blue):

    if blue == 0:

        return 0.0

    return round(red / blue, 3)


# =====================================================
# PERCENT DIFFERENCE
# =====================================================

def percent_difference(red, blue):

    if red == blue:

        return 0.0

    denominator = (red + blue) / 2

    if denominator == 0:

        return 0.0

    return round(

        ((red - blue) / denominator) * 100,

        3

    )


# =====================================================
# NORMALIZED DIFFERENCE
# =====================================================

def normalized_difference(red, blue):

    denominator = max(

        abs(red),

        abs(blue),

        1

    )

    return round(

        (red - blue) / denominator,

        3

    )


# =====================================================
# SAFE LOG DIFFERENCE
# =====================================================

def log_difference(red, blue):

    red = max(red, 1)

    blue = max(blue, 1)

    return round(

        math.log(red) -

        math.log(blue),

        3

    )