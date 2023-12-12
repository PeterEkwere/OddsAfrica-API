#!/usr/bin/python
"""
    This module contains functions for arbitrage calculations
    Author: PeterEkwere
"""
from ArbBrain.probs import decimal_implied_win_prob
from ArbBrain.odds import decimal_odds


def arb_percentage(odds):
    """
    :param odds: List of Floats. Pair of odds for a single matchup - Player 1 and Player 2.
    :return: List of Floats. Sum of implied win probabilities and win_probs for Player 1 and Player 2
    """
    try:
        if len(odds) == 2:
            pass
    except ValueError:
        print("Odds input needs to be a list of length 2 (odds bet 1 / odds bet 2")

    bet1 = decimal_implied_win_prob(decimal_odds(odds[0]))
    bet2 = decimal_implied_win_prob(decimal_odds(odds[1]))
    arb_percent = bet1 + bet2

    return [arb_percent, bet1, bet2]


def arb_profit(arb_percent, stake):
    """
    :param arb_percent: List. Helper function must be used with arb_percentage. This is sum of combined implied probabilities < 100% mean arb opportunity
    :param stake: Float. How much you intend to throw down on the wager.
    :return: Float. Riskless profit if executed at the terms of the parameters.
    """
    return stake / arb_percent[0] - stake


def basic_arbitrage(odds, stake):
    """
    A basic arbitrage calculator. Riskless profits generally implemented at two separate sportsbooks.

    :param odds: Float. A pair of odds Player 1 and their opponent. Odds generally from different sites.
    :param stake: Float. How much you intend to throw down.
    :return: List of Floats. Profit Arb'd. Wager for Player 1; Wager for Player 2.
    """
    try:
        if len(odds) != 2:
            return None

        arb_percent = arb_percentage(odds)

        if arb_percent[0] > 1.0:
            return None
        else:
            arb_prof = arb_profit(arb_percent, stake)
            bet1_size = (arb_percent[1] * stake) / arb_percent[0]
            bet2_size = (arb_percent[2] * stake) / arb_percent[0]
            return [round(arb_prof, 2), round(bet1_size, 2), round(bet2_size, 2)]
    except ValueError:
        print("You probably fed too many or too few values into the Odds parameter")
