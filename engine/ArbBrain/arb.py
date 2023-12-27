#!/usr/bin/python
"""
    This module contains functions for arbitrage calculations
    Author: PeterEkwere
"""
from probs import decimal_implied_win_prob
from odds import decimal_odds
import sys
sys.path.append('..')
from utils.logger.log import log_error, log_exception, log_success


"""
def arb_percentage(odds):
    :param odds: List of Floats. Pair of odds for a single matchup - Player 1 and Player 2.
    :return: List of Floats. Sum of implied win probabilities and win_probs for Player 1 and Player 2
    try:
        if len(odds) <= 1:
            log_error(f"Amount of Odds Passed To ArB Function is <= 1")
            return None
        if len(odds) == 2:
            bet1 = decimal_implied_win_prob(decimal_odds(odds[0]))
            bet2 = decimal_implied_win_prob(decimal_odds(odds[1]))
        elif len(odds) == 3:
            bet1 = decimal_implied_win_prob(decimal_odds(odds[0]))
            bet2 = decimal_implied_win_prob(decimal_odds(odds[1]))
            bet2 = decimal_implied_win_prob(decimal_odds(odds[2]))
        else:
            log_error(f"Amount of Odds Passed To Arb Percentage is >= 4")
    except ValueError:
        log_error("Odds input needs to be a list of length 2 (odds bet 1 / odds bet 2 or length 3")

    bet1 = decimal_implied_win_prob(decimal_odds(odds[0]))
    bet2 = decimal_implied_win_prob(decimal_odds(odds[1]))
    arb_percent = bet1 + bet2

    return [arb_percent, bet1, bet2]
"""

def arb_profit(arb_percent, stake):
    """
    :param arb_percent: List. Helper function must be used with arb_percentage. This is sum of combined implied probabilities < 100% mean arb opportunity
    :param stake: Float. How much you intend to throw down on the wager.
    :return: Float. Riskless profit if executed at the terms of the parameters.
    """
    return stake / arb_percent[0] - stake


def Find_arbitrage(n, odds):
    """
    An Adavnced arbitrage calculator. Riskless profits generally implemented at two or Three separate sportsbooks.

    :param odds: Float. A pair of odds Player 1 and their opponent. Odds generally from different sites.
    :return: arbitrage Percentage.
    """
    try:
        if len(odds) <= 1:
            log_error(f"Amount of Odds Passed To ArB Function is <= 1")
            return None
        if len(odds) == 2:
            k1 = decimal_odds(odds[0])
            k2 = decimal_odds(odds[1])
        elif len(odds) == 3:
            k1 = decimal_odds(odds[0])
            k2 = decimal_odds(odds[1])
            k3 = decimal_odds(odds[3])
        else:
            log_error(f"Amount of Odds Passed To Arb Function is >= 4")
            return None
        
        
        L = 1
        
        if n == '1':
            L = 1 / k1 + 1 / k2
        elif n == '2':
            L = 1 / k1 + 1 / k2 + 1 / k3
        elif n == '3':
            L = 1 / k1 + 1 / k3 + (k1 - 1) / (k1 * k2)
        elif n == '4':
            L = 1 / k1 + 1 / (k1 * k3) + (k1 - 1) / (k1 * k2)
        elif n == '5':
            L = 1 / k1 + 1 / k3 + (k1 - 1/2) / (k1 * k2)
        elif n == '6':
            L = 1 / k1 + 1 / (2 * k1 * k3) + (k1 - 1/2) / (k1 * k2)
        elif n == '7':
            L = 1 / k1 + 1 / k3 + (k1 - 1) / (2 * k1 * k2)
        elif n == '8':
            L = 1 / k1 + (k1 - 1) / (2 * k1 * k2) + (k1 + 1)/(2 * k1 * k3)
        elif n == '9':
            L = 1 / k1 + 1 / k3 + (2 * k1 * k3 - k3 - 2 * k1) / (2 * k1 * k2 * k3)    
        elif n == '10':
            L = 1 / k1 + 1 / (2 * k1 * (k3-1)) + 1 / k2 - 1 / (2 * k2 * k1) - 1 / (2 * (k3 - 1) * k2 * k1)
        elif n == '11':
            L = 1 / k1 + 1 / k2 + 1 / k3 - 1 / (2 * k2 * k1) - 1 / (2 * k2 * k3) 
        elif n == '12':
            L = 1 / k1 + 1 / k2 + 1 / ((2 * k3 - 1) * k1) - 1 / (2 * k2 * k1) - 1 / (2 * (2 * k3 - 1) * k2 * k1)
        elif n == '13':
            L = 1 / k1 + 2 * (k1 - 1) / (k1 * (k2 + 1)) + 1 / k3 - 2 * k2 * (k1 - 1) / (k1 * k3 * (k2 + 1))
        elif n == '14':
            L = 1 / k1 + 1 / k2 - 1 / (k1 * k2) - 1 / (2 * k1 * k2 * (k3 - 0.5)) + 1 / (k1 * (k3 - 0.5))
        elif n == '15':
            L =  1 / 2 + 1 / (2 * k1) + 1 / k3 - k2 * (k1 - 1) / (2 * k3 * k1)
        elif n == '16':
            L = 1 / k1 + 1 / k2 + 1 / k3
        elif n == '17':
            L = 1 / k1 + 1 / k2 + 1 / (k1 * k2) + 2 / k3
        elif n == '18':
            L = (2 * k1 + (k1 + k3) / k2 + 2 * k3) / (2 * k1 * k3 + k1 + k3)
        elif n == '19':
            L = (1 / k3 + 1 / (k1 * k2))
        elif n == '20':
            L = 2 - (k1 + k2 * ((1 + ((k3 + 1) * k1)/ (2 * k3) - k1) / k2)) / (1 + ((1 + ((k3 + 1) * k1)/(2 * k3) - k1) / k2) + (k1 / k3))
        
        return L
    except ValueError:
        log_error("You probably fed too many or too few values into the Odds parameter")
        return None
    except Exception as e:
        message = f"Error calculating arb: {e}\n"
        log_exception(message)
        return None


print(f"Percentage found is {Find_arbitrage('15', [1.384, 2.512, 16])}")