#!/usr/bin/python
"""
    This Module will hold funcitions for extracting and arranging the needed markets for football cross market arb
"""
import os
import traceback
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
        '1': markets.get("1X2", {}).get("1",  "None"),
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
        'H1(-0.5)' : markets.get("Handicap Home", {}).get("-0.5", "None"),
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
        'H1(-0.5)' : markets.get("Handicap Home", {}).get("-0.5", "None"),
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

def extract_bet9ja_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("1", "None"),
        '1X': markets.get("1X", "None"),
        '2' : markets.get("2", "None"),
        '2X': markets.get("X2", "None"),
        'X' : markets.get("X", "None"),
        '12' : markets.get("12", "None"),
        'Over(1.5)' : markets.get("1.5_O", "None"),
        'Under(1.5)' : markets.get("1.5_U", "None"),
        'Over(2.5)' : markets.get("2.5_O", "None"),
        'Under(2.5)' : markets.get("2.5_U", "None"),
        'Over(3.5)' : markets.get("3.5_O", "None"),
        'Under(3.5)' : markets.get("3.5_U", "None"),
        'Over(4.5)' : markets.get("4.5_O", "None"),
        'Under(4.5)' : markets.get("4.5_U", "None"),
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
        '1(Draw no bet)' : markets.get("Draw No Bet", {}).get("1 DNB", "None"),
        '2(Draw no bet)': markets.get("Draw No Bet", {}).get("2 DNB", "None"),
        'Over(1.5)' : markets.get("Total Goals 1.5", {}).get("Over", "None"),
        'Under(1.5)' : markets.get("Total Goals 1.5", {}).get("Under", "None"),
        'Over(2.5)' : markets.get("Total Goals 2.5", {}).get("Over", "None"),
        'Under(2.5)' : markets.get("Total Goals 2.5", {}).get("Under", "None"),
        'Over(3.5)' : markets.get("Total Goals 3.5", {}).get("Over", "None"),
        'Under(3.5)' : markets.get("Total Goals 3.5", {}).get("Under", "None"),
        'Over(4.5)' : markets.get("Total Goals 4.5", {}).get("Over", "None"),
        'Under(4.5)' : markets.get("Total Goals 4.5", {}).get("Under", "None"),
        'GG': markets.get("GG/NG", {}).get("GG", "None"),
        'NG': markets.get("GG/NG", {}).get("NG", "None")    
    } 
    return found_markets

def extract_betpawa_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("1X2 - FT", {}).get("1", "None"),
        '1X': markets.get("Double Chance - FT", {}).get("1X", "None"),
        '2' : markets.get("1X2 - FT", {}).get("2", "None"),
        '2X': markets.get("Double Chance - FT", {}).get("X2", "None"),
        'X' : markets.get("1X2 - FT", {}).get("X", "None"),
        '12' : markets.get("Double Chance - FT", {}).get("12", "None"),
        '1(Draw no bet)' : markets.get("Draw No Bet - FT", {}).get("1", "None"),
        '2(Draw no bet)': markets.get("Draw No Bet - FT", {}).get("2", "None"),
        'Odd Goals': markets.get("Odd / Even - FT", {}).get("Odd", "None"),
        'Even Goals': markets.get("Odd / Even - FT", {}).get("Even", "None"),
        'GG': markets.get("Both Teams To Score - FT", {}).get("Yes", "None"),
        'NG': markets.get("Both Teams To Score - FT", {}).get("No", "None"),
        'Total Booking 0-3': markets.get("Total Bookings - FT", {}).get("0-3")
        
    } 
    return found_markets

def extract_betwinner_markets(markets):
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
        'H1(-0.5)' : markets.get("Handicap Home", {}).get("-0.5", "None"),
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
        'Over(1.5)' : markets.get("Under/Over 1.5 goals", {}).get("Over 1.5 goals", "None"),
        'Under(1.5)' : markets.get("Under/Over 1.5 goals", {}).get("Under 1.5 goals", "None"),
        'Over(2.5)' : markets.get("Under/Over 2.5 goals", {}).get("Over 2.5 goals", "None"),
        'Under(2.5)' : markets.get("Under/Over 2.5 goals", {}).get("Under 2.5 goals", "None"),
        'Over(3.5)' : markets.get("Under/Over 3.5 goals", {}).get("Over 3.5 goals", "None"),
        'Under(3.5)' : markets.get("Under/Over 3.5 goals", {}).get("Under 3.5 goals", "None"),
        'Over(4.5)' : markets.get("Under/Over 4.5 goals", {}).get("Over 4.5 goals", "None"),
        'Under(4.5)' : markets.get("Under/Over 4.5 goals", {}).get("Under 4.5 goals", "None"),
        'GG': markets.get("Both teams to score", {}).get("Yes", "None"),
        'NG': markets.get("Both teams to score", {}).get("No", "None"),
        'Corners Over (6.5)': markets.get("Under/Over 6.5 corners", {}).get("over 6.5", "None"),
        'Corners Under(6.5)': markets.get("Under/Over 6.5 corners", {}).get("under 6.5", "None"),
        'Corners Over (7.5)': markets.get("Under/Over 7.5 corners", {}).get("over 7.5", "None"),
        'Corners Under (7.5)': markets.get("Under/Over 7.5 corners", {}).get("under 7.5", "None"),
        'Corners Over(8.5)': markets.get("Under/Over 8.5 corners", {}).get("over 8.5", "None"),
        'Corners Under(8.5)': markets.get("Under/Over 8.5 corners", {}).get("under 8.5", "None"),
        'Corners Over(9.5)': markets.get("Under/Over 9.5 corners", {}).get("over 9.5", "None"),
        'Corners Under(9.5)': markets.get("Under/Over 9.5 corners", {}).get("under 9.5", "None"),
        'Corners Over(10.5)': markets.get("Under/Over 10.5 corners", {}).get("over 10.5", "None"),
        'Corners Under(10.5)': markets.get("Under/Over 10.5 corners", {}).get("under 10.5", "None"),
        'Corners Over(11.5)': markets.get("Under/Over 11.5 corners", {}).get("over 11.5", "None"),
        'Corners Under(11.5)': markets.get("Under/Over 11.5 corners", {}).get("under 11.5", "None"),
        'Corners Over(12.5)': markets.get("Under/Over 12.5 corners", {}).get("over 12.5", "None"),
        'Corners Under(12.5)': markets.get("Under/Over 12.5 corners", {}).get("under 12.5", "None"),
    } 
    return found_markets


def extract_nairabet_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("Match Winner", {}).get("1", "None"),
        '1X': markets.get("Double Chance", {}).get("1X", "None"),
        '2' : markets.get("Match Winner", {}).get("2", "None"),
        '2X': markets.get("Double Chance", {}).get("2 or X", "None"),
        'X' : markets.get("Match Winner", {}).get("X", "None"),
        '12' : markets.get("Double Chance", {}).get("12", "None"),
        '1(Draw no bet)' : markets.get("Draw No Bet", {}).get("1", "None"),
        '2(Draw no bet)': markets.get("Draw No Bet", {}).get("2", "None"),
        '2(+1)': markets.get("Handicap", {}).get("2 +1", "None"),
        '1(-1)': markets.get("Handicap", {}).get("1 -1", "None"),
        '2(+2)' : markets.get("Handicap", {}).get("2 +2", "None"),
        '1(-2)': markets.get("Handicap", {}).get("1 -2", "None"),
        '2(+3)': markets.get("Handicap", {}).get("2 +3", "None"),
        '1(+1)': markets.get("Handicap", {}).get("1 +1", "None"),
        '1(+2)' : markets.get("Handicap", {}).get("1 +2", "None"),
        '1(-3)' : markets.get("Handicap", {}).get("1 -3", "None"),
        '2(-1)' : markets.get("Handicap", {}).get("2 -1", "None"),
        '1(+3)' : markets.get("Handicap", {}).get("1 +3", "None"),
        '2(-2)' : markets.get("Handicap", {}).get("2 -2", "None"),
        '2(-3)' : markets.get("Handicap", {}).get("2 -3", "None"),
        'X1(-1)' : markets.get("Handicap", {}).get("X (1 -1)", "None"),
        'X2(-1)' : markets.get("Handicap", {}).get("X (2 -1)", "None"),
        'X1(-2)' : markets.get("Handicap", {}).get("X (1 -2)", "None"),
        'X2(-2)' : markets.get("Handicap", {}).get("X (2 -2)", "None"),
        'X1(-3)' : markets.get("Handicap", {}).get("X (1 -3)", "None"),
        'X1(+1)' : markets.get("Handicap", {}).get("X (1 +1)", "None"),
        'X2(+1)' : markets.get("Handicap", {}).get("X (2 +1)", "None"),
        'X1(+2)' : markets.get("Handicap", {}).get("X (1 +2)", "None"),
        'X2(+2)' : markets.get("Handicap", {}).get("X (2 +2)", "None"),
        'X1(+3)' : markets.get("Handicap", {}).get("X (1 +3)", "None"),
        'Over(1.5)' : markets.get("Total Goals - Total Goals 1.5", {}).get("Over 1.5 goals", "None"),
        'Under(1.5)' : markets.get("Total Goals - Total Goals 1.5", {}).get("Under 1.5 goals", "None"),
        'Over(2.5)' : markets.get("Total Goals - Total Goals 2.5", {}).get("Over 2.5 goals", "None"),
        'Under(2.5)' : markets.get("Total Goals - Total Goals 2.5", {}).get("Under 2.5 goals", "None"),
        'Over(3.5)' : markets.get("Total Goals - Total Goals 3.5", {}).get("Over 3.5 goals", "None"),
        'Under(3.5)' : markets.get("Total Goals - Total Goals 3.5", {}).get("Under 3.5 goals", "None"),
        'Over(4.5)' : markets.get("Total Goals - Total Goals 4.5", {}).get("Over 4.5 goals", "None"),
        'Under(4.5)' : markets.get("Total Goals - Total Goals 4.5", {}).get("Under 4.5 goals", "None"),
        'GG': markets.get("Both Teams To Score", {}).get("Yes", "None"),
        'NG': markets.get("Both Teams To Score", {}).get("No", "None"),
        'Bookings Over(3.5)': markets.get("Total Bookings - Over/Under 3.5 - bou2", {}).get("Over 3.5 bookings", "None"),
        'Corners Over (6.5)': markets.get("Total Corners", {}).get("Over 6.5 Corners", "None"),
        'Corners Under(6.5)': markets.get("Total Corners", {}).get("Under 6.5 Corners", "None"),
        'Corners Over (7.5)': markets.get("Total Corners", {}).get("Over 7.5 Corners", "None"),
        'Corners Under (7.5)': markets.get("Total Corners", {}).get("Under 7.5 Corners", "None"),
        'Corners Over(8.5)': markets.get("Total Corners", {}).get("Over 8.5 Corners", "None"),
        'Corners Under(8.5)': markets.get("Total Corners", {}).get("Under 8.5 Corners", "None"),
        'Corners Over(9.5)': markets.get("Total Corners", {}).get("Over 9.5 Corners", "None"),
        'Corners Under(9.5)': markets.get("Total Corners", {}).get("Under 9.5 Corners", "None"),
        'Corners Over(10.5)': markets.get("Total Corners", {}).get("Over 10.5 Corners", "None"),
        'Corners Under(10.5)': markets.get("Total Corners", {}).get("Under 10.5 Corners", "None"),
        'Corners Over(11.5)': markets.get("Total Corners", {}).get("Over 11.5 Corners", "None"),
        'Corners Under(11.5)': markets.get("Total Corners", {}).get("Under 11.5 Corners", "None"),
        'Corners Over(12.5)': markets.get("Total Corners", {}).get("Over 12.5 Corners", "None"),
        'Corners Under(12.5)': markets.get("Total Corners", {}).get("Under 12.5 Corners", "None"),
    } 
    return found_markets


def extract_paripesa_markets(markets):
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
        'H1(-0.5)' : markets.get("Handicap Home", {}).get("-0.5", "None"),
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
    
    found_markets = {
        "time": markets.get("time", "None"),
        '1': markets.get("1X2", {}).get("1", "None"),
        '1X': markets.get("Double Chance", {}).get("1X", "None"),
        '2' : markets.get("1X2", {}).get("2", "None"),
        '2X': markets.get("Double Chance", {}).get("X2", "None"),
        'X' : markets.get("1X2", {}).get("X", "None"),
        '12' : markets.get("Double Chance", {}).get("12", "None"),
        '1(Draw no bet)' : markets.get("Draw No Bet", {}).get("1", "None"),
        '2(Draw no bet)': markets.get("Draw No Bet", {}).get("2", "None"),
        '2(+1)': markets.get("Handicap 0:1", {}).get("2 (0:1)", "None"),
        '1(-1)': markets.get("Handicap 0:1", {}).get("1 (0:1)", "None"),
        '2(+2)' : markets.get("Handicap 0:2", {}).get("2 (0:2)", "None"),
        '1(-2)': markets.get("Handicap 0:2", {}).get("1 (0:2)", "None"),
        '2(+3)': markets.get("Handicap 0:3", {}).get("2 (0:3)", "None"),
        '1(+1)': markets.get("Handicap 1:0", {}).get("1 (1:0)", "None"),
        '1(+2)' : markets.get("Handicap 2:0", {}).get("1 (2:0)", "None"),
        '1(-3)' : markets.get("Handicap 0:3", {}).get("1 (0:3)", "None"),
        '2(-1)' : markets.get("Handicap 1:0", {}).get("2 (1:0)", "None"),
        '1(+3)' : markets.get("Handicap 3:0", {}).get("1 (3:0)", "None"),
        '2(-2)' : markets.get("Handicap 2:0", {}).get("2 (2:0)", "None"),
        '2(-3)' : markets.get("Handicap 3:0", {}).get("2 (3:0)", "None"),
        #'X1(-1)' : markets.get("Handicap 0:1", {}).get("X (0:1)", "None"),
        #'X2(-1)' : markets.get("Handicap 1:0", {}).get("X (1:0)", "None"),
        #'X1(-2)' : markets.get("Handicap 0:2", {}).get("X (0:2)", "None"),
        #'X2(-2)' : markets.get("Handicap 2:0", {}).get("X (2:0)", "None"),
        #'X1(-3)' : markets.get("Handicap 0:3", {}).get("X (0:3)", "None"),
        #'X1(+1)' : markets.get("Handicap 1:0", {}).get("X (1:0)", "None"),
        #'X2(+1)' : markets.get("Handicap 0:1", {}).get("X (0:1)", "None"),
        #'X1(+2)' : markets.get("1X2", {}).get("X (2:0)", "None"),
        #'X2(+2)' : markets.get("1X2", {}).get("X (0:2)", "None"),
        #'X1(+3)' : markets.get("1X2", {}).get("X (3:0)", "None"),
        'Over(1.5)' : markets.get("Over/Under", {}).get("Over 1.5", "None"),
        'Under(1.5)' : markets.get("Over/Under", {}).get("Under 1.5", "None"),
        'Over(2.5)' : markets.get("Over/Under", {}).get("Over 2.5", "None"),
        'Under(2.5)' : markets.get("Over/Under", {}).get("Under 2.5", "None"),
        'Over(3.5)' : markets.get("Over/Under", {}).get("Over 3.5", "None"),
        'Under(3.5)' : markets.get("Over/Under", {}).get("Under 3.5", "None"),
        'Over(4.5)' : markets.get("Over/Under", {}).get("Over 4.5", "None"),
        'Under(4.5)' : markets.get("Over/Under", {}).get("Under 4.5", "None"),
        'Over(2)' : markets.get("Over/Under", {}).get("Over 2", "None"),
        'Under(2)' : markets.get("Over/Under", {}).get("Under 2", "None"),
        'Over(3)' : markets.get("Over/Under", {}).get("Over 3", "None"),
        'Under(3)' : markets.get("Over/Under", {}).get("Under 3", "None"),
        'Over(4)' : markets.get("Over/Under", {}).get("Over 4", "None"),
        'Under(4)' : markets.get("Over/Under", {}).get("Under 4", "None"),
        'GG': markets.get("GG/NG", {}).get("Yes", "None"),
        'NG': markets.get("GG/NG", {}).get("No", "None")    
    } 
    return found_markets

def extract_livescorebet_markets(markets):
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
        '1(Draw no bet)' : markets.get("Draw No Bet", {}).get("1", "None"),
        '2(Draw no bet)': markets.get("Draw No Bet", {}).get("2", "None"),
        'Over(1.5)' : markets.get("Total goals", {}).get("Over 1.5", "None"),
        'Under(1.5)' : markets.get("Total goals", {}).get("Under 1.5", "None"),
        'Over(2.5)' : markets.get("Total goals", {}).get("Over 2.5", "None"),
        'Under(2.5)' : markets.get("Total goals", {}).get("Under 2.5", "None"),
        'Over(3.5)' : markets.get("Total goals", {}).get("Over 3.5", "None"),
        'Under(3.5)' : markets.get("Total goals", {}).get("Under 3.5", "None"),
        'Over(4.5)' : markets.get("Total goals", {}).get("Over 4.5", "None"),
        'Under(4.5)' : markets.get("Total goals", {}).get("Under 4.5", "None"),
        'GG': markets.get("Both Teams to Score", {}).get("Yes", "None"),
        'NG': markets.get("Both Teams to Score", {}).get("No", "None")      
    } 
    return found_markets


special_functions = {
    "1xbet" : extract_xbet_markets,
    "22bet" : extract_bet22_markets,
    "bet9ja": extract_bet9ja_markets,
    "betking": extract_betking_markets,
    "betpawa": extract_betpawa_markets,
    "betwinner": extract_betwinner_markets,
    "livescorebet": extract_livescorebet_markets,
    "merrybet": extract_merrybet_markets,
    "nairabet": extract_nairabet_markets,
    "paripesa": extract_paripesa_markets,
    "sportybet": extract_sportybet_markets
}

def process_football(sport_file_path):
    """ This function will handle processing of every betsite within each game

    Args:
        sport_file_path (_type_): This is the path to the already arranged sport files
    """
    games_data = load_json(sport_file_path)
    all_markets = {}
    for game, bookies_data in games_data.items():
        if game == "Home VS Away":
            pass
        else:
            if game not in all_markets:
                    all_markets[game] = {}
            for bookie, market_data in bookies_data.items():
                if bookie not in all_markets[game]:
                    all_markets[game][bookie] = {}
                try:
                    if bookie in special_functions.keys():
                            if market_data is not None and isinstance(market_data, dict):
                                try:
                                    bookie_extracted_data = special_functions[bookie](market_data)
                                    all_markets[game][bookie] = bookie_extracted_data
                                except Exception as e:
                                    log_exception(f"Error extracting Game: {game} Bookie: {bookie} markets: {e}")
                    else:
                        log_error(f" No special extraction function for this {bookie}.",)
                except Exception as e:
                    log_exception(f"Error Extracting markets for {bookie} game name: {game} ERROR: {e}",)  
    return all_markets   