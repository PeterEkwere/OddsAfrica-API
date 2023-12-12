#!/usr/bin/python
"""
    This Module contains calculation for the implied win % of stated odds.
    Author: Peter Ekwere
"""
from ArbBrain.odds import decimal_odds


def decimal_implied_win_prob(odds):
    """
    :param odds: Float. Odds expressed in Decimal terms.
    :return: Float. The implied win % of stated odds.
    """
    return round(1 / decimal_odds(odds), 3)