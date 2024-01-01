#!/usr/bin/python
"""
    This Module will hold funcitions for extracting and arranging the needed markets  for ice hockey cross market arb
"""
import os
from utils.arrange import load_json
from utils.logger.log import log_error, log_exception, log_success


def extract_xbet_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    found_markets["StartTime"] = markets.get("time", "None")
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("1X2", {}).get("1", "None"),
        '1X': markets.get("Double Chance", {}).get("1X", "None"),
        '2' : markets.get("1X2", {}).get("2", "None"),
        '2X': markets.get("Double Chance", {}).get("2X", "None"),
        'X' : markets.get("1X2", {}).get("X", "None"),
        '12' : markets.get("Double Chance", {}).get("12", "None"),
        'H1(-1.5)' : markets.get("Handicap Home", {}).get("-1.5", "None"),
        'H2(+0.5)' : markets.get("Handicap Home", {}).get("0.5", "None"),
        'H1(-2.5)' : markets.get("Handicap Home", {}).get("-2.5", "None"),
        'H2(+1.5)' : markets.get("Handicap Away", {}).get("1.5", "None"),
        'H1(-2.5)' : markets.get("Handicap Home", {}).get("-2.5", "None"),
        'H1(-3.5)' : markets.get("Handicap Home", {}).get("-3.5", "None"),
        'H2(+2.5)' : markets.get("Handicap Away", {}).get("2.5", "None"),
        'H2(-0.5)' : markets.get("Handicap Away", {}).get("-0.5", "None"),
        'H1(+0.5)' : markets.get("Handicap Home", {}).get("0.5", "None"),
        'H2(-1.5)' : markets.get("Handicap Away", {}).get("-1.5", "None"),
        'H1(+1.5)' : markets.get("Handicap Home", {}).get("1.5", "None"),
        'H2(-2.5)' : markets.get("Handicap Away", {}).get("-2.5", "None"),
        'H1(+2.5)' : markets.get("Handicap Home", {}).get("2.5", "None"),
        'H2(-3.5)' : markets.get("Handicap Away", {}).get("-3.5", "None"),
        'H1(0)' : markets.get("Handicap Home", {}).get("0", "None"),
        'H2(0)' : markets.get("Handicap Away", {}).get("0", "None"),
        'H1(-1)' : markets.get("Handicap Home", {}).get("-1", "None"),
        'H2(-1)' : markets.get("Handicap Away", {}).get("-1", "None"),
        'H1(-2)' : markets.get("Handicap Home", {}).get("-2", "None"),
        'H2(-2)' : markets.get("Handicap Away", {}).get("-2", "None"),
        'H1(-3)' : markets.get("Handicap Home", {}).get("-3", "None"),
        'H1(+1)' : markets.get("Handicap Home", {}).get("1", "None"),
        'H2(+1)' : markets.get("Handicap Away", {}).get("1", "None"),
        'H1(+2)' : markets.get("Handicap Home", {}).get("2", "None"),
        'H2(+2)' : markets.get("Handicap Away", {}).get("2", "None"),
        'H1(+3)' : markets.get("Handicap Home", {}).get("3", "None"),
        'H1(-0.25)' : markets.get("AH Home", {}).get("-0.25", "None"),
        'H2(-0.25)' : markets.get("AH Away", {}).get("-0.25", "None"),
        'H2(+0.25)' : markets.get("AH Away", {}).get("0.25", "None"),
        'H1(+0.25)' : markets.get("AH Home", {}).get("0.25", "None"),
        'H1(-1.25)' : markets.get("AH Home", {}).get("-1.25", "None"),
        'H1(+1.25)' : markets.get("AH Home", {}).get("1.25", "None"),
        'H2(-1.25)' : markets.get("AH Away", {}).get("-1.25", "None"),
        'H2(+1.25)' : markets.get("AH Away", {}).get("1.25", "None"),
        'H1(+2.25)' : markets.get("AH Home", {}).get("+2.25", "None"),
        'H1(-2.25)' : markets.get("AH Home", {}).get("-2.25", "None"),
        'H2(+2.25)' : markets.get("AH Away", {}).get("+2.25", "None"),
        'H2(-2.25)' : markets.get("AH Away", {}).get("-2.25", "None"),
        'H1(+0.75)' : markets.get("AH Home", {}).get("0.75", "None"),
        'H1(-0.75)' : markets.get("AH Home", {}).get("-0.75", "None"),
        'H2(+0.75)' : markets.get("AH Away", {}).get("0.75", "None"),
        'H2(-0.75)' : markets.get("AH Away", {}).get("-0.75", "None"),
        'H1(+1.75)' : markets.get("AH Home", {}).get("1.75", "None"),
        'H1(-1.75)' : markets.get("AH Home", {}).get("-1.75", "None"),
        'H2(+1.75)' : markets.get("AH Away", {}).get("1.75", "None"),
        'H2(-1.75)' : markets.get("AH Away", {}).get("-1.75", "None"),
        'Over(1.5)' : markets.get("Over", {}).get("1.5", "None"),
        'Over(1.75)' : markets.get("Asian Over", {}).get("1.75", "None"),
        'Under(1.5)' : markets.get("Under", {}).get("1.5", "None"),
        'Under(1.75)' : markets.get("Asian under", {}).get("1.75", "None"),
        'Over(2.5)' : markets.get("Over", {}).get("2.5", "None"),
        'Over(2.25)' : markets.get("Asian Over", {}).get("2.25", "None"),
        'Over(2.75)' : markets.get("Asian Over", {}).get("2.75", "None"),
        'Under(2.5)' : markets.get("Under", {}).get("2.5", "None"),
        'Under(2.25)' : markets.get("Asian under", {}).get("2.25", "None"),
        'Under(2.75)' : markets.get("Asian under", {}).get("2.75", "None"),
        'Over(3.5)' : markets.get("Over", {}).get("3.5", "None"),
        'Over(3.25)' : markets.get("Asian Over", {}).get("3.25", "None"),
        'Over(3.75)' : markets.get("Asian Over", {}).get("3.75", "None"),
        'Under(3.5)' : markets.get("Under", {}).get("3.5", "None"),
        'Under(3.25)' : markets.get("Asian under", {}).get("3.25", "None"),
        'Under(3.75)' : markets.get("Asian under", {}).get("3.75", "None"),
        'Over(4.5)' : markets.get("Over", {}).get("4.5", "None"),
        'Under(4.5)' : markets.get("Under", {}).get("4.5", "None"),
        'Over(2)' : markets.get("Over", {}).get("2", "None"),
        'Under(2)' : markets.get("Under", {}).get("2", "None"),
        'Over(3)' : markets.get("Over", {}).get("3", "None"),
        'Under(3)' : markets.get("Under", {}).get("3", "None"),
        'Over(4)' : markets.get("Over", {}).get("4", "None"),
        'Under(4)' : markets.get("Under", {}).get("4", "None"),
        'GG': markets.get("GG/NG", {}).get("GG", "None"),
        'NG': markets.get("GG/NG", {}).get("NG", "None")    
    } 
    return found_markets

def extract_bet22_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("1X2", {}).get("1", "None"),
        '1X': markets.get("Double Chance", {}).get("1X", "None"),
        '2' : markets.get("1X2", {}).get("2", "None"),
        '2X': markets.get("Double Chance", {}).get("2X", "None"),
        'X' : markets.get("1X2", {}).get("X", "None"),
        '12' : markets.get("Double Chance", {}).get("12", "None"),
        'H1(-1.5)' : markets.get("Handicap Home", {}).get("-1.5", "None"),
        'H2(+0.5)' : markets.get("Handicap Home", {}).get("0.5", "None"),
        'H1(-2.5)' : markets.get("Handicap Home", {}).get("-2.5", "None"),
        'H2(+1.5)' : markets.get("Handicap Away", {}).get("1.5", "None"),
        'H1(-2.5)' : markets.get("Handicap Home", {}).get("-2.5", "None"),
        'H1(-3.5)' : markets.get("Handicap Home", {}).get("-3.5", "None"),
        'H2(+2.5)' : markets.get("Handicap Away", {}).get("2.5", "None"),
        'H2(-0.5)' : markets.get("Handicap Away", {}).get("-0.5", "None"),
        'H1(+0.5)' : markets.get("Handicap Home", {}).get("0.5", "None"),
        'H2(-1.5)' : markets.get("Handicap Away", {}).get("-1.5", "None"),
        'H1(+1.5)' : markets.get("Handicap Home", {}).get("1.5", "None"),
        'H2(-2.5)' : markets.get("Handicap Away", {}).get("-2.5", "None"),
        'H1(+2.5)' : markets.get("Handicap Home", {}).get("2.5", "None"),
        'H2(-3.5)' : markets.get("Handicap Away", {}).get("-3.5", "None"),
        'H1(0)' : markets.get("Handicap Home", {}).get("0", "None"),
        'H2(0)' : markets.get("Handicap Away", {}).get("0", "None"),
        'H1(-1)' : markets.get("Handicap Home", {}).get("-1", "None"),
        'H2(-1)' : markets.get("Handicap Away", {}).get("-1", "None"),
        'H1(-2)' : markets.get("Handicap Home", {}).get("-2", "None"),
        'H2(-2)' : markets.get("Handicap Away", {}).get("-2", "None"),
        'H1(-3)' : markets.get("Handicap Home", {}).get("-3", "None"),
        'H1(+1)' : markets.get("Handicap Home", {}).get("1", "None"),
        'H2(+1)' : markets.get("Handicap Away", {}).get("1", "None"),
        'H1(+2)' : markets.get("Handicap Home", {}).get("2", "None"),
        'H2(+2)' : markets.get("Handicap Away", {}).get("2", "None"),
        'H1(+3)' : markets.get("Handicap Home", {}).get("3", "None"),
        'H1(-0.25)' : markets.get("AH Home", {}).get("-0.25", "None"),
        'H2(-0.25)' : markets.get("AH Away", {}).get("-0.25", "None"),
        'H2(+0.25)' : markets.get("AH Away", {}).get("0.25", "None"),
        'H1(+0.25)' : markets.get("AH Home", {}).get("0.25", "None"),
        'H1(-1.25)' : markets.get("AH Home", {}).get("-1.25", "None"),
        'H1(+1.25)' : markets.get("AH Home", {}).get("1.25", "None"),
        'H2(-1.25)' : markets.get("AH Away", {}).get("-1.25", "None"),
        'H2(+1.25)' : markets.get("AH Away", {}).get("1.25", "None"),
        'H1(+2.25)' : markets.get("AH Home", {}).get("+2.25", "None"),
        'H1(-2.25)' : markets.get("AH Home", {}).get("-2.25", "None"),
        'H2(+2.25)' : markets.get("AH Away", {}).get("+2.25", "None"),
        'H2(-2.25)' : markets.get("AH Away", {}).get("-2.25", "None"),
        'H1(+0.75)' : markets.get("AH Home", {}).get("0.75", "None"),
        'H1(-0.75)' : markets.get("AH Home", {}).get("-0.75", "None"),
        'H2(+0.75)' : markets.get("AH Away", {}).get("0.75", "None"),
        'H2(-0.75)' : markets.get("AH Away", {}).get("-0.75", "None"),
        'H1(+1.75)' : markets.get("AH Home", {}).get("1.75", "None"),
        'H1(-1.75)' : markets.get("AH Home", {}).get("-1.75", "None"),
        'H2(+1.75)' : markets.get("AH Away", {}).get("1.75", "None"),
        'H2(-1.75)' : markets.get("AH Away", {}).get("-1.75", "None"),
        'Over(1.5)' : markets.get("Over", {}).get("1.5", "None"),
        'Over(1.75)' : markets.get("Asian Over", {}).get("1.75", "None"),
        'Under(1.5)' : markets.get("Under", {}).get("1.5", "None"),
        'Under(1.75)' : markets.get("Asian under", {}).get("1.75", "None"),
        'Over(2.5)' : markets.get("Over", {}).get("2.5", "None"),
        'Over(2.25)' : markets.get("Asian Over", {}).get("2.25", "None"),
        'Over(2.75)' : markets.get("Asian Over", {}).get("2.75", "None"),
        'Under(2.5)' : markets.get("Under", {}).get("2.5", "None"),
        'Under(2.25)' : markets.get("Asian under", {}).get("2.25", "None"),
        'Under(2.75)' : markets.get("Asian under", {}).get("2.75", "None"),
        'Over(3.5)' : markets.get("Over", {}).get("3.5", "None"),
        'Over(3.25)' : markets.get("Asian Over", {}).get("3.25", "None"),
        'Over(3.75)' : markets.get("Asian Over", {}).get("3.75", "None"),
        'Under(3.5)' : markets.get("Under", {}).get("3.5", "None"),
        'Under(3.25)' : markets.get("Asian under", {}).get("3.25", "None"),
        'Under(3.75)' : markets.get("Asian under", {}).get("3.75", "None"),
        'Over(4.5)' : markets.get("Over", {}).get("4.5", "None"),
        'Under(4.5)' : markets.get("Under", {}).get("4.5", "None"),
        'Over(2)' : markets.get("Over", {}).get("2", "None"),
        'Under(2)' : markets.get("Under", {}).get("2", "None"),
        'Over(3)' : markets.get("Over", {}).get("3", "None"),
        'Under(3)' : markets.get("Under", {}).get("3", "None"),
        'Over(4)' : markets.get("Over", {}).get("4", "None"),
        'Under(4)' : markets.get("Under", {}).get("4", "None"),
        'GG': markets.get("GG/NG", {}).get("GG", "None"),
        'NG': markets.get("GG/NG", {}).get("NG", "None")    
    } 
    return found_markets

def extract_betking_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("1X2", {}).get("1", "None"),
        '1X': markets.get("Double Chance", {}).get("1X", "None"),
        '2' : markets.get("1X2", {}).get("2", "None"),
        '2X': markets.get("Double Chance", {}).get("X2", "None"),
        'X' : markets.get("1X2", {}).get("X", "None"),
        '12' : markets.get("Double Chance", {}).get("12", "None"),
        '1(Draw no bet)' : markets.get("DNB", {}).get("1 DNB", "None"),
        '2(Draw no bet)': markets.get("DNB", {}).get("2 DNB", "None"),   
    } 
    return found_markets

def extract_betwinner_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    found_markets["StartTime"] = markets.get("time", "None")
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("1X2", {}).get("1", "None"),
        '1X': markets.get("Double Chance", {}).get("1X", "None"),
        '2' : markets.get("1X2", {}).get("2", "None"),
        '2X': markets.get("Double Chance", {}).get("2X", "None"),
        'X' : markets.get("1X2", {}).get("X", "None"),
        '12' : markets.get("Double Chance", {}).get("12", "None"),
        'H1(-1.5)' : markets.get("Handicap Home", {}).get("-1.5", "None"),
        'H2(+0.5)' : markets.get("Handicap Home", {}).get("0.5", "None"),
        'H1(-2.5)' : markets.get("Handicap Home", {}).get("-2.5", "None"),
        'H2(+1.5)' : markets.get("Handicap Away", {}).get("1.5", "None"),
        'H1(-2.5)' : markets.get("Handicap Home", {}).get("-2.5", "None"),
        'H1(-3.5)' : markets.get("Handicap Home", {}).get("-3.5", "None"),
        'H2(+2.5)' : markets.get("Handicap Away", {}).get("2.5", "None"),
        'H2(-0.5)' : markets.get("Handicap Away", {}).get("-0.5", "None"),
        'H1(+0.5)' : markets.get("Handicap Home", {}).get("0.5", "None"),
        'H2(-1.5)' : markets.get("Handicap Away", {}).get("-1.5", "None"),
        'H1(+1.5)' : markets.get("Handicap Home", {}).get("1.5", "None"),
        'H2(-2.5)' : markets.get("Handicap Away", {}).get("-2.5", "None"),
        'H1(+2.5)' : markets.get("Handicap Home", {}).get("2.5", "None"),
        'H2(-3.5)' : markets.get("Handicap Away", {}).get("-3.5", "None"),
        'H1(0)' : markets.get("Handicap Home", {}).get("0", "None"),
        'H2(0)' : markets.get("Handicap Away", {}).get("0", "None"),
        'H1(-1)' : markets.get("Handicap Home", {}).get("-1", "None"),
        'H2(-1)' : markets.get("Handicap Away", {}).get("-1", "None"),
        'H1(-2)' : markets.get("Handicap Home", {}).get("-2", "None"),
        'H2(-2)' : markets.get("Handicap Away", {}).get("-2", "None"),
        'H1(-3)' : markets.get("Handicap Home", {}).get("-3", "None"),
        'H1(+1)' : markets.get("Handicap Home", {}).get("1", "None"),
        'H2(+1)' : markets.get("Handicap Away", {}).get("1", "None"),
        'H1(+2)' : markets.get("Handicap Home", {}).get("2", "None"),
        'H2(+2)' : markets.get("Handicap Away", {}).get("2", "None"),
        'H1(+3)' : markets.get("Handicap Home", {}).get("3", "None"),
        'H1(-0.25)' : markets.get("AH Home", {}).get("-0.25", "None"),
        'H2(-0.25)' : markets.get("AH Away", {}).get("-0.25", "None"),
        'H2(+0.25)' : markets.get("AH Away", {}).get("0.25", "None"),
        'H1(+0.25)' : markets.get("AH Home", {}).get("0.25", "None"),
        'H1(-1.25)' : markets.get("AH Home", {}).get("-1.25", "None"),
        'H1(+1.25)' : markets.get("AH Home", {}).get("1.25", "None"),
        'H2(-1.25)' : markets.get("AH Away", {}).get("-1.25", "None"),
        'H2(+1.25)' : markets.get("AH Away", {}).get("1.25", "None"),
        'H1(+2.25)' : markets.get("AH Home", {}).get("+2.25", "None"),
        'H1(-2.25)' : markets.get("AH Home", {}).get("-2.25", "None"),
        'H2(+2.25)' : markets.get("AH Away", {}).get("+2.25", "None"),
        'H2(-2.25)' : markets.get("AH Away", {}).get("-2.25", "None"),
        'H1(+0.75)' : markets.get("AH Home", {}).get("0.75", "None"),
        'H1(-0.75)' : markets.get("AH Home", {}).get("-0.75", "None"),
        'H2(+0.75)' : markets.get("AH Away", {}).get("0.75", "None"),
        'H2(-0.75)' : markets.get("AH Away", {}).get("-0.75", "None"),
        'H1(+1.75)' : markets.get("AH Home", {}).get("1.75", "None"),
        'H1(-1.75)' : markets.get("AH Home", {}).get("-1.75", "None"),
        'H2(+1.75)' : markets.get("AH Away", {}).get("1.75", "None"),
        'H2(-1.75)' : markets.get("AH Away", {}).get("-1.75", "None"),
        'Over(1.5)' : markets.get("Over", {}).get("1.5", "None"),
        'Over(1.75)' : markets.get("Asian Over", {}).get("1.75", "None"),
        'Under(1.5)' : markets.get("Under", {}).get("1.5", "None"),
        'Under(1.75)' : markets.get("Asian under", {}).get("1.75", "None"),
        'Over(2.5)' : markets.get("Over", {}).get("2.5", "None"),
        'Over(2.25)' : markets.get("Asian Over", {}).get("2.25", "None"),
        'Over(2.75)' : markets.get("Asian Over", {}).get("2.75", "None"),
        'Under(2.5)' : markets.get("Under", {}).get("2.5", "None"),
        'Under(2.25)' : markets.get("Asian under", {}).get("2.25", "None"),
        'Under(2.75)' : markets.get("Asian under", {}).get("2.75", "None"),
        'Over(3.5)' : markets.get("Over", {}).get("3.5", "None"),
        'Over(3.25)' : markets.get("Asian Over", {}).get("3.25", "None"),
        'Over(3.75)' : markets.get("Asian Over", {}).get("3.75", "None"),
        'Under(3.5)' : markets.get("Under", {}).get("3.5", "None"),
        'Under(3.25)' : markets.get("Asian under", {}).get("3.25", "None"),
        'Under(3.75)' : markets.get("Asian under", {}).get("3.75", "None"),
        'Over(4.5)' : markets.get("Over", {}).get("4.5", "None"),
        'Under(4.5)' : markets.get("Under", {}).get("4.5", "None"),
        'Over(2)' : markets.get("Over", {}).get("2", "None"),
        'Under(2)' : markets.get("Under", {}).get("2", "None"),
        'Over(3)' : markets.get("Over", {}).get("3", "None"),
        'Under(3)' : markets.get("Under", {}).get("3", "None"),
        'Over(4)' : markets.get("Over", {}).get("4", "None"),
        'Under(4)' : markets.get("Under", {}).get("4", "None"),
        'GG': markets.get("GG/NG", {}).get("GG", "None"),
        'NG': markets.get("GG/NG", {}).get("NG", "None")    
    } 
    return found_markets

def extract_merrybet_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("1x2", {}).get("1", "None"),
        '1X': markets.get("Double chance", {}).get("1X", "None"),
        '2' : markets.get("1x2", {}).get("2", "None"),
        '2X': markets.get("Double chance", {}).get("X2", "None"),
        'X' : markets.get("1x2", {}).get("X", "None"),
        '12' : markets.get("Double chance", {}).get("12", "None"),
        'H1(-0.5)' : markets.get("Handicap -0.5 / +0.5", {}).get("1 (-0.5", "None"),
        'H2(+0.5)' : markets.get("Handicap -0.5 / +0.5", {}).get("2 (+0.5", "None"),
        'H1(-1.5)' : markets.get("Handicap -1.5 / +1.5", {}).get("1 (-1.5", "None"),
        'H2(+1.5)' : markets.get("Handicap -1.5 / +1.5", {}).get("2 (+1.5", "None"),
        'H1(+0.5)' : markets.get("Handicap +0.5 / -0.5", {}).get("1 (+0.5", "None"),
        'H2(-0.5)' : markets.get("Handicap +0.5 / -0.5", {}).get("2 (-0.5", "None"),
        'H1(+1.5)' : markets.get("Handicap +1.5 / -1.5", {}).get("1 (+1.5", "None"),
        'H2(-0.5)' : markets.get("Handicap +1.5 / -1.5", {}).get("2 (-1.5", "None"),
        'Over(1.5)' : markets.get("Under/Over 1.5 goals", {}).get("Over 1.5 goals", "None"),
        'Under(1.5)' : markets.get("Under/Over 1.5 goals", {}).get("Under 1.5 goals", "None"),
        'Over(2.5)' : markets.get("Under/Over 2.5 goals", {}).get("Over 2.5 goals", "None"),
        'Under(2.5)' : markets.get("Under/Over 2.5 goals", {}).get("Under 2.5 goals", "None"),
        'Over(3.5)' : markets.get("Under/Over 3.5 goals", {}).get("Over 3.5 goals", "None"),
        'Under(3.5)' : markets.get("Under/Over 3.5 goals", {}).get("Under 3.5 goals", "None"),
        'Over(4.5)' : markets.get("Under/Over 4.5 goals", {}).get("Over 4.5 goals", "None"),
        'Under(4.5)' : markets.get("Under/Over 4.5 goals", {}).get("Under 4.5 goals", "None"),
        'GG': markets.get("Both teams to score", {}).get("Yes", "None"),
        'NG': markets.get("Both teams to score", {}).get("No", "None")
    } 
    return found_markets


def extract_nairabet_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    found_markets["StartTime"] = markets.get("time", "None")
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("Match Result (No OT)", {}).get("1", "None"),
        '2' : markets.get("Match Result (No OT)", {}).get("2", "None"),
        'X' : markets.get("Match Result (No OT)", {}).get("X", "None"),
        '1(OverTime)(Including penalties)' : markets.get("Match Result (Inc OT)", {}).get("1", "None"),
        '2(OverTime)(Including penalties)': markets.get("Match Result (Inc OT)", {}).get("2", "None"),
        'Over(1.5)' : markets.get("Total Goals (O/U)", {}).get("Over 1.5", "None"),
        'Under(1.5)' : markets.get("Total Goals (O/U)", {}).get("Under 1.5", "None"),
        'Over(2.5)' : markets.get("Total Goals (O/U)", {}).get("Over 2.5", "None"),
        'Under(2.5)' : markets.get("Total Goals (O/U)", {}).get("Under 2.5", "None"),
        'Over(3.5)' : markets.get("Total Goals (O/U)", {}).get("Over 3.5", "None"),
        'Under(3.5)' : markets.get("Total Goals (O/U)", {}).get("Under 3.5", "None"),
        'Over(4.5)' : markets.get("Total Goals (O/U)", {}).get("Over 4.5", "None"),
        'Under(4.5)' : markets.get("Total Goals (O/U)", {}).get("Under 4.5", "None"),
        'GG': markets.get("Both Teams To Score", {}).get("Yes", "None"),
        'NG': markets.get("Both Teams To Score", {}).get("No", "None")
    } 
    return found_markets


def extract_paripesa_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    found_markets["StartTime"] = markets.get("time", "None")
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("1X2", {}).get("1", "None"),
        '1X': markets.get("Double Chance", {}).get("1X", "None"),
        '2' : markets.get("1X2", {}).get("2", "None"),
        '2X': markets.get("Double Chance", {}).get("2X", "None"),
        'X' : markets.get("1X2", {}).get("X", "None"),
        '12' : markets.get("Double Chance", {}).get("12", "None"),
        #'1(Draw no bet)' : None,
        #'2(Draw no bet)': None,
        #'2(+1)': markets.get("1X2", {}).get("1", "None"),
        #'1(-1)': markets.get("1X2", {}).get("1", "None"),
        #'2(+2)' : markets.get("1X2", {}).get("1", "None"),
        #'1(-2)': markets.get("1X2", {}).get("1", "None"),
        #'2(+3)': markets.get("1X2", {}).get("1", "None"),
        #'1(+1)': markets.get("1X2", {}).get("1", "None"),
        #'1(+2)' : markets.get("1X2", {}).get("1", "None"),
        #'1(-3)' : markets.get("1X2", {}).get("1", "None"),
        #'2(-1)' : markets.get("1X2", {}).get("1", "None"),
        #'1(+3)' : markets.get("1X2", {}).get("1", "None"),
        #'2(-2)' : markets.get("1X2", {}).get("1", "None"),
        #'2(-3)' : markets.get("1X2", {}).get("1", "None"),
        #'H1(-0.5)' : markets.get("Handicap Home", {}).get("1", "None"),
        #'H2(-0.5)' : markets.get("1X2", {}).get("1", "None"),
        #'X1(-1)' : markets.get("1X2", {}).get("1", "None"),
        #'X2(-1)' : markets.get("1X2", {}).get("1", "None"),
        #'X1(-2)' : markets.get("1X2", {}).get("1", "None"),
        #'X2(-2)' : markets.get("1X2", {}).get("1", "None"),
        #'X1(-3)' : markets.get("1X2", {}).get("1", "None"),
        #'X1(+1)' : markets.get("1X2", {}).get("1", "None"),
        #'X2(+1)' : markets.get("1X2", {}).get("1", "None"),
        #'X1(+2)' : markets.get("1X2", {}).get("1", "None"),
        #'X2(+2)' : markets.get("1X2", {}).get("1", "None"),
        #'X1(+3)' : markets.get("1X2", {}).get("1", "None"),
        'H1(-1.5)' : markets.get("Handicap Home", {}).get("-1.5", "None"),
        'H2(+0.5)' : markets.get("Handicap Home", {}).get("0.5", "None"),
        'H1(-2.5)' : markets.get("Handicap Home", {}).get("-2.5", "None"),
        'H2(+1.5)' : markets.get("Handicap Away", {}).get("1.5", "None"),
        'H1(-2.5)' : markets.get("Handicap Home", {}).get("-2.5", "None"),
        'H1(-3.5)' : markets.get("Handicap Home", {}).get("-3.5", "None"),
        'H2(+2.5)' : markets.get("Handicap Away", {}).get("2.5", "None"),
        'H2(-0.5)' : markets.get("Handicap Away", {}).get("-0.5", "None"),
        'H1(+0.5)' : markets.get("Handicap Home", {}).get("0.5", "None"),
        'H2(-1.5)' : markets.get("Handicap Away", {}).get("-1.5", "None"),
        'H1(+1.5)' : markets.get("Handicap Home", {}).get("1.5", "None"),
        'H2(-2.5)' : markets.get("Handicap Away", {}).get("-2.5", "None"),
        'H1(+2.5)' : markets.get("Handicap Home", {}).get("2.5", "None"),
        'H2(-3.5)' : markets.get("Handicap Away", {}).get("-3.5", "None"),
        'H1(0)' : markets.get("Handicap Home", {}).get("0", "None"),
        'H2(0)' : markets.get("Handicap Away", {}).get("0", "None"),
        'H1(-1)' : markets.get("Handicap Home", {}).get("-1", "None"),
        'H2(-1)' : markets.get("Handicap Away", {}).get("-1", "None"),
        'H1(-2)' : markets.get("Handicap Home", {}).get("-2", "None"),
        'H2(-2)' : markets.get("Handicap Away", {}).get("-2", "None"),
        'H1(-3)' : markets.get("Handicap Home", {}).get("-3", "None"),
        'H1(+1)' : markets.get("Handicap Home", {}).get("1", "None"),
        'H2(+1)' : markets.get("Handicap Away", {}).get("1", "None"),
        'H1(+2)' : markets.get("Handicap Home", {}).get("2", "None"),
        'H2(+2)' : markets.get("Handicap Away", {}).get("2", "None"),
        'H1(+3)' : markets.get("Handicap Home", {}).get("3", "None"),
        'H1(-0.25)' : markets.get("AH Home", {}).get("-0.25", "None"),
        'H2(-0.25)' : markets.get("AH Away", {}).get("-0.25", "None"),
        'H2(+0.25)' : markets.get("AH Away", {}).get("0.25", "None"),
        'H1(+0.25)' : markets.get("AH Home", {}).get("0.25", "None"),
        'H1(-1.25)' : markets.get("AH Home", {}).get("-1.25", "None"),
        'H1(+1.25)' : markets.get("AH Home", {}).get("1.25", "None"),
        'H2(-1.25)' : markets.get("AH Away", {}).get("-1.25", "None"),
        'H2(+1.25)' : markets.get("AH Away", {}).get("1.25", "None"),
        'H1(+2.25)' : markets.get("AH Home", {}).get("+2.25", "None"),
        'H1(-2.25)' : markets.get("AH Home", {}).get("-2.25", "None"),
        'H2(+2.25)' : markets.get("AH Away", {}).get("+2.25", "None"),
        'H2(-2.25)' : markets.get("AH Away", {}).get("-2.25", "None"),
        'H1(+0.75)' : markets.get("AH Home", {}).get("0.75", "None"),
        'H1(-0.75)' : markets.get("AH Home", {}).get("-0.75", "None"),
        'H2(+0.75)' : markets.get("AH Away", {}).get("0.75", "None"),
        'H2(-0.75)' : markets.get("AH Away", {}).get("-0.75", "None"),
        'H1(+1.75)' : markets.get("AH Home", {}).get("1.75", "None"),
        'H1(-1.75)' : markets.get("AH Home", {}).get("-1.75", "None"),
        'H2(+1.75)' : markets.get("AH Away", {}).get("1.75", "None"),
        'H2(-1.75)' : markets.get("AH Away", {}).get("-1.75", "None"),
        'Over(1.5)' : markets.get("Over", {}).get("1.5", "None"),
        'Over(1.75)' : markets.get("Asian Over", {}).get("1.75", "None"),
        'Under(1.5)' : markets.get("Under", {}).get("1.5", "None"),
        'Under(1.75)' : markets.get("Asian under", {}).get("1.75", "None"),
        'Over(2.5)' : markets.get("Over", {}).get("2.5", "None"),
        'Over(2.25)' : markets.get("Asian Over", {}).get("2.25", "None"),
        'Over(2.75)' : markets.get("Asian Over", {}).get("2.75", "None"),
        'Under(2.5)' : markets.get("Under", {}).get("2.5", "None"),
        'Under(2.25)' : markets.get("Asian under", {}).get("2.25", "None"),
        'Under(2.75)' : markets.get("Asian under", {}).get("2.75", "None"),
        'Over(3.5)' : markets.get("Over", {}).get("3.5", "None"),
        'Over(3.25)' : markets.get("Asian Over", {}).get("3.25", "None"),
        'Over(3.75)' : markets.get("Asian Over", {}).get("3.75", "None"),
        'Under(3.5)' : markets.get("Under", {}).get("3.5", "None"),
        'Under(3.25)' : markets.get("Asian under", {}).get("3.25", "None"),
        'Under(3.75)' : markets.get("Asian under", {}).get("3.75", "None"),
        'Over(4.5)' : markets.get("Over", {}).get("4.5", "None"),
        'Under(4.5)' : markets.get("Under", {}).get("4.5", "None"),
        'Over(2)' : markets.get("Over", {}).get("2", "None"),
        'Under(2)' : markets.get("Under", {}).get("2", "None"),
        'Over(3)' : markets.get("Over", {}).get("3", "None"),
        'Under(3)' : markets.get("Under", {}).get("3", "None"),
        'Over(4)' : markets.get("Over", {}).get("4", "None"),
        'Under(4)' : markets.get("Under", {}).get("4", "None"),
        'GG': markets.get("GG/NG", {}).get("GG", "None"),
        'NG': markets.get("GG/NG", {}).get("NG", "None")
    } 
    return found_markets

def extract_sportybet_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    found_markets["StartTime"] = markets.get("time", "None")
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1(OverTime)(Including penalties)': markets.get("Winner (incl. overtime and penalties)", {}).get("1", "None"),
        '2 (OverTime)(Including penalties)' : markets.get("Winner (incl. overtime and penalties)", {}).get("2", "None"),
        'Over(1.5)' : markets.get("Total (incl. overtime and penalties)", {}).get("Over 1.5", "None"),
        'Under(1.5)' : markets.get("Total (incl. overtime and penalties)", {}).get("Under 1.5", "None"),
        'Over(2.5)' : markets.get("Total (incl. overtime and penalties)", {}).get("Over 2.5", "None"),
        'Under(2.5)' : markets.get("Total (incl. overtime and penalties)", {}).get("Under 2.5", "None"),
        'Over(3.5)' : markets.get("Total (incl. overtime and penalties)", {}).get("Over 3.5", "None"),
        'Under(3.5)' : markets.get("Total (incl. overtime and penalties)", {}).get("Under 3.5", "None"),
        'Over(4.5)' : markets.get("Total (incl. overtime and penalties)", {}).get("Over 4.5", "None"),
        'Under(4.5)' : markets.get("Total (incl. overtime and penalties)", {}).get("Under 4.5", "None"),
        'Over(2)' : markets.get("Total (incl. overtime and penalties)", {}).get("Over 2", "None"),
        'Under(2)' : markets.get("Total (incl. overtime and penalties)", {}).get("Under 2", "None"),
        'Over(3)' : markets.get("Total (incl. overtime and penalties)", {}).get("Over 3", "None"),
        'Under(3)' : markets.get("Total (incl. overtime and penalties)", {}).get("Under 3", "None"),
        'Over(4)' : markets.get("Total (incl. overtime and penalties)", {}).get("Over 4", "None"),
        'Under(4)' : markets.get("Total (incl. overtime and penalties)", {}).get("Under 4", "None"),  
    } 
    return found_markets

def extract_livescorebet_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    found_markets["StartTime"] = markets.get("time", "None")
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("Winner", {}).get("1", "None"),
        '2' : markets.get("Winner", {}).get("2", "None"),
        'X' : markets.get("Winner", {}).get("X", "None"),
        'Over(1.5)' : markets.get("Over/under", {}).get("Over 1.5", "None"),
        'Under(1.5)' : markets.get("Over/under", {}).get("Under 1.5", "None"),
        'Over(2.5)' : markets.get("Over/under", {}).get("Over 2.5", "None"),
        'Under(2.5)' : markets.get("Over/under", {}).get("Under 2.5", "None"),
        'Over(3.5)' : markets.get("Over/under", {}).get("Over 3.5", "None"),
        'Under(3.5)' : markets.get("Over/under", {}).get("Under 3.5", "None"),
        'Over(4.5)' : markets.get("Over/under", {}).get("Over 4.5", "None"),
        'Under(4.5)' : markets.get("Over/under", {}).get("Under 4.5", "None"),
    } 
    return found_markets


special_functions = {
    "1xbet" : extract_xbet_markets,
    "22bet" : extract_bet22_markets,
    "betking": extract_betking_markets,
    "betwinner": extract_betwinner_markets,
    "livescorebet": extract_livescorebet_markets,
    "merrybet": extract_merrybet_markets,
    "nairabet": extract_nairabet_markets,
    "paripesa": extract_paripesa_markets,
    "sportybet": extract_sportybet_markets
}

def process_ice_hockey(sport_file_path):
    """ This function will handle processing of every betsite within each game

    Args:
        sport_file_path (_type_): This is the path to the already arranged sport files
    """
    games_data = load_json(sport_file_path)
    all_markets = {}
    for game, bookies_data in games_data.items():
            if game not in all_markets:
                    all_markets[game] = {}
            for bookie, market_data in bookies_data.items():
                try:
                    if bookie in special_functions:
                            if market_data is not None and isinstance(market_data, dict):
                                try:
                                    bookie_extracted_data = special_functions[bookie](market_data)
                                    if bookie not in all_markets[game]:
                                        all_markets[game][bookie] = {}
                                    all_markets[game][bookie] = bookie_extracted_data
                                except Exception as e:
                                      log_exception(f"Error extracting Game: {game} Bookie: {bookie} markets: {e}") 
                    else:
                        log_error(f" No special extraction function for this {bookie}.")
                except Exception as e:
                    log_exception(f"Error Extracting markets for {bookie} game name: {game} ERROR: {e}")  
    return all_markets   
