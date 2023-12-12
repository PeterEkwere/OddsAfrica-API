#!/usr/bin/python
"""
    This module contains
    Author: Peter
"""
from fractions import Fraction



def decimal_odds(odds):
    """
    :param odds: Integer (e.g., -350) or String (e.g., '3/1' or '5/4').
    :return: Float. Odds expressed in Decimal terms.
    """
    if isinstance(odds, float):
        return odds

    elif isinstance(odds, int):
        if odds >= 100:
            return abs(1 + (odds / 100))
        elif odds <= -101 :
            return 100 / abs(odds) + 1
        else:
            return float(odds)

    elif "/" in odds:
        odds = Fraction(odds)
        return round((odds.numerator / odds.denominator) + 1, 2)