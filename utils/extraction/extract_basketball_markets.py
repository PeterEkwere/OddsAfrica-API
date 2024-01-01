#!/usr/bin/python
"""
    This Module will hold funcitions for extracting and arranging the needed markets 
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
        "Over 227": markets.get("Over", {}).get("227", "None"),
       "Over 227.5":markets.get("Over", {}).get("227.5", "None"),
       "Over 228":markets.get("Over", {}).get("228", "None"),
       "Over 228.5":markets.get("Over", {}).get("228.5", "None"),
       "Over 229":markets.get("Over", {}).get("229", "None"),
       "Over 229.5":markets.get("Over", {}).get("229.5", "None"),
       "Over 230":markets.get("Over", {}).get("230", "None"),
       "Over 230.5":markets.get("Over", {}).get("230.5", "None"),
       "Over 231": markets.get("Over", {}).get("231", "None"),
       "Over 231.5": markets.get("Over", {}).get("231.5", "None"),
       "Over 232": markets.get("Over", {}).get("232", "None"),
       "Over 232.5": markets.get("Over", {}).get("232.5", "None"),
       "Over 233": markets.get("Over", {}).get("233", "None"),
       "Over 233.5": markets.get("Over", {}).get("233.5", "None"),
       "Over 234": markets.get("Over", {}).get("234", "None"),
       "Over 234.5": markets.get("Over", {}).get("234.5", "None"),
       "Over 235": markets.get("Over", {}).get("235", "None"),
        "Over 200": markets.get("Over", {}).get("200", "None"),
        "Over 201":markets.get("Over", {}).get("201", "None"),
        "Over 202":markets.get("Over", {}).get("202", "None"),
        "Over 203":markets.get("Over", {}).get("203", "None"),
        "Over 204":markets.get("Over", {}).get("204", "None"),
        "Over 205":markets.get("Over", {}).get("205", "None"),
        "Over 206":markets.get("Over", {}).get("206", "None"),
        "Over 207":markets.get("Over", {}).get("207", "None"),
        "Over 208": markets.get("Over", {}).get("208", "None"),
        "Over 209": markets.get("Over", {}).get("209", "None"),
        "Over 210": markets.get("Over", {}).get("210", "None"),
        "Over 211": markets.get("Over", {}).get("211", "None"),
        "Over 212": markets.get("Over", {}).get("212", "None"),
        "Over 213": markets.get("Over", {}).get("213", "None"),
        "Over 214": markets.get("Over", {}).get("214", "None"),
        "Over 215": markets.get("Over", {}).get("215", "None"),
        "Over 216": markets.get("Over", {}).get("216", "None"),
        # Next Is Under        
        "Under 227": markets.get("Under", {}).get("227", "None"),
       "Under 227.5":markets.get("Under", {}).get("227.5", "None"),
       "Under 228":markets.get("Under", {}).get("228", "None"),
       "Under 228.5":markets.get("Under", {}).get("228.5", "None"),
       "Under 229":markets.get("Under", {}).get("229", "None"),
       "Under 229.5":markets.get("Under", {}).get("229.5", "None"),
       "Under 230":markets.get("Under", {}).get("230", "None"),
       "Under 230.5":markets.get("Under", {}).get("230.5", "None"),
       "Under 231": markets.get("Under", {}).get("231", "None"),
       "Under 231.5": markets.get("Under", {}).get("231.5", "None"),
       "Under 232": markets.get("Under", {}).get("232", "None"),
       "Under 232.5": markets.get("Under", {}).get("232.5", "None"),
       "Under 233": markets.get("Under", {}).get("233", "None"),
       "Under 233.5": markets.get("Under", {}).get("233.5", "None"),
       "Under 234": markets.get("Under", {}).get("234", "None"),
       "Under 234.5": markets.get("Under", {}).get("234.5", "None"),
       "Under 235": markets.get("Under", {}).get("235", "None"),
        "Under 200": markets.get("Under", {}).get("200", "None"),
        "Under 201":markets.get("Under", {}).get("201", "None"),
        "Under 202":markets.get("Under", {}).get("202", "None"),
        "Under 203":markets.get("Under", {}).get("203", "None"),
        "Under 204":markets.get("Under", {}).get("204", "None"),
        "Under 205":markets.get("Under", {}).get("205", "None"),
        "Under 206":markets.get("Under", {}).get("206", "None"),
        "Under 207":markets.get("Under", {}).get("207", "None"),
        "Under 208": markets.get("Under", {}).get("208", "None"),
        "Under 209": markets.get("Under", {}).get("209", "None"),
        "Under 210": markets.get("Under", {}).get("210", "None"),
        "Under 211": markets.get("Under", {}).get("211", "None"),
        "Under 212": markets.get("Under", {}).get("212", "None"),
        "Under 213": markets.get("Under", {}).get("213", "None"),
        "Under 214": markets.get("Under", {}).get("214", "None"),
        "Under 215": markets.get("Under", {}).get("215", "None"),
        "Under 216": markets.get("Under", {}).get("216", "None"),
        "H1(-21)" : markets.get("Handicap Home", {}).get("-21", "None"),
        "H1(-20.5)" : markets.get("Handicap Home", {}).get("-20.5", "None"),
        "H1(-20)" : markets.get("Handicap Home", {}).get("-20", "None"),
        "H1(-19.5)" : markets.get("Handicap Home", {}).get("-19.5", "None"),
        "H1(-19)" : markets.get("Handicap Home", {}).get("-19", "None"),
        "H1(-18.5)" : markets.get("Handicap Home", {}).get("-18.5", "None"),
        "H1(-18)" : markets.get("Handicap Home", {}).get("-18", "None"),
        "H1(-17.5)" : markets.get("Handicap Home", {}).get("-17.5", "None"),
        "H1(-17)" : markets.get("Handicap Home", {}).get("-17", "None"),
        "H1(-16.5)" : markets.get("Handicap Home", {}).get("-16.5", "None"),
        "H1(-16)" : markets.get("Handicap Home", {}).get("-16", "None"),
        "H1(-15.5)" : markets.get("Handicap Home", {}).get("-15.5", "None"),
        "H1(-15)" : markets.get("Handicap Home", {}).get("-15", "None"),
        "H1(-14.5)" : markets.get("Handicap Home", {}).get("-14.5", "None"),
        "H1(-14)" : markets.get("Handicap Home", {}).get("-14", "None"),
        "H1(-13.5)" : markets.get("Handicap Home", {}).get("-13.5", "None"),
        "H1(-13)" : markets.get("Handicap Home", {}).get("-13", "None"),
        "H2(-21)" : markets.get("Handicap Away", {}).get("-21", "None"),
        "H2(-20.5)" : markets.get("Handicap Away", {}).get("-20.5", "None"),
        "H2(-20)" : markets.get("Handicap Away", {}).get("-20", "None"),
        "H2(-19.5)" : markets.get("Handicap Away", {}).get("-19.5", "None"),
        "H2(-19)" : markets.get("Handicap Away", {}).get("-19", "None"),
        "H2(-18.5)" : markets.get("Handicap Away", {}).get("-18.5", "None"),
        "H2(-18)" : markets.get("Handicap Away", {}).get("-18", "None"),
        "H2(-17.5)" : markets.get("Handicap Away", {}).get("-17.5", "None"),
        "H2(-17)" : markets.get("Handicap Away", {}).get("-17", "None"),
        "H2(-16.5)" : markets.get("Handicap Away", {}).get("-16.5", "None"),
        "H2(-16)" : markets.get("Handicap Away", {}).get("-16", "None"),
        "H2(-15.5)" : markets.get("Handicap Away", {}).get("-15.5", "None"),
        "H2(-15)" : markets.get("Handicap Away", {}).get("-15", "None"),
        "H2(-14.5)" : markets.get("Handicap Away", {}).get("-14.5", "None"),
        "H2(-14)" : markets.get("Handicap Away", {}).get("-14", "None"),
        "H2(-13.5)" : markets.get("Handicap Away", {}).get("-13.5", "None"),
        "H2(-13)" : markets.get("Handicap Away", {}).get("-13", "None"),
        "H1(+21)" : markets.get("Handicap Home", {}).get("+21", "None"),
        "H1(+20.5)" : markets.get("Handicap Home", {}).get("+20.5", "None"),
        "H1(+20)" : markets.get("Handicap Home", {}).get("+20", "None"),
        "H1(+19.5)" : markets.get("Handicap Home", {}).get("+19.5", "None"),
        "H1(+19)" : markets.get("Handicap Home", {}).get("+19", "None"),
        "H1(+18.5)" : markets.get("Handicap Home", {}).get("+18.5", "None"),
        "H1(+18)" : markets.get("Handicap Home", {}).get("+18", "None"),
        "H1(+17.5)" : markets.get("Handicap Home", {}).get("+17.5", "None"),
        "H1(+17)" : markets.get("Handicap Home", {}).get("+17", "None"),
        "H1(+16.5)" : markets.get("Handicap Home", {}).get("+16.5", "None"),
        "H1(+16)" : markets.get("Handicap Home", {}).get("+16", "None"),
        "H1(+15.5)" : markets.get("Handicap Home", {}).get("+15.5", "None"),
        "H1(+15)" : markets.get("Handicap Home", {}).get("+15", "None"),
        "H1(+14.5)" : markets.get("Handicap Home", {}).get("+14.5", "None"),
        "H1(+14)" : markets.get("Handicap Home", {}).get("+14", "None"),
        "H1(+13.5)" : markets.get("Handicap Home", {}).get("+13.5", "None"),
        "H1(+13)" : markets.get("Handicap Home", {}).get("+13", "None"),
        "H2(+21)" : markets.get("Handicap Away", {}).get("+21", "None"),
        "H2(+20.5)" : markets.get("Handicap Away", {}).get("+20.5", "None"),
        "H2(+20)" : markets.get("Handicap Away", {}).get("+20", "None"),
        "H2(+19.5)" : markets.get("Handicap Away", {}).get("+19.5", "None"),
        "H2(+19)" : markets.get("Handicap Away", {}).get("+19", "None"),
        "H2(+18.5)" : markets.get("Handicap Away", {}).get("+18.5", "None"),
        "H2(+18)" : markets.get("Handicap Away", {}).get("+18", "None"),
        "H2(+17.5)" : markets.get("Handicap Away", {}).get("+17.5", "None"),
        "H2(+17)" : markets.get("Handicap Away", {}).get("+17", "None"),
        "H2(+16.5)" : markets.get("Handicap Away", {}).get("+16.5", "None"),
        "H2(+16)" : markets.get("Handicap Away", {}).get("+16", "None"),
        "H2(+15.5)" : markets.get("Handicap Away", {}).get("+15.5", "None"),
        "H2(+15)" : markets.get("Handicap Away", {}).get("+15", "None"),
        "H2(+14.5)" : markets.get("Handicap Away", {}).get("+14.5", "None"),
        "H2(+14)" : markets.get("Handicap Away", {}).get("+14", "None"),
        "H2(+13.5)" : markets.get("Handicap Away", {}).get("+13.5", "None"),
        "H2(+13)" : markets.get("Handicap Away", {}).get("+13", "None"),

    } 
    return found_markets

def extract_bet22_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    
    found_markets = {
        "Over 227": markets.get("Over", {}).get("227", "None"),
       "Over 227.5":markets.get("Over", {}).get("227.5", "None"),
       "Over 228":markets.get("Over", {}).get("228", "None"),
       "Over 228.5":markets.get("Over", {}).get("228.5", "None"),
       "Over 229":markets.get("Over", {}).get("229", "None"),
       "Over 229.5":markets.get("Over", {}).get("229.5", "None"),
       "Over 230":markets.get("Over", {}).get("230", "None"),
       "Over 230.5":markets.get("Over", {}).get("230.5", "None"),
       "Over 231": markets.get("Over", {}).get("231", "None"),
       "Over 231.5": markets.get("Over", {}).get("231.5", "None"),
       "Over 232": markets.get("Over", {}).get("232", "None"),
       "Over 232.5": markets.get("Over", {}).get("232.5", "None"),
       "Over 233": markets.get("Over", {}).get("233", "None"),
       "Over 233.5": markets.get("Over", {}).get("233.5", "None"),
       "Over 234": markets.get("Over", {}).get("234", "None"),
       "Over 234.5": markets.get("Over", {}).get("234.5", "None"),
       "Over 235": markets.get("Over", {}).get("235", "None"),
        "Over 200": markets.get("Over", {}).get("200", "None"),
        "Over 201":markets.get("Over", {}).get("201", "None"),
        "Over 202":markets.get("Over", {}).get("202", "None"),
        "Over 203":markets.get("Over", {}).get("203", "None"),
        "Over 204":markets.get("Over", {}).get("204", "None"),
        "Over 205":markets.get("Over", {}).get("205", "None"),
        "Over 206":markets.get("Over", {}).get("206", "None"),
        "Over 207":markets.get("Over", {}).get("207", "None"),
        "Over 208": markets.get("Over", {}).get("208", "None"),
        "Over 209": markets.get("Over", {}).get("209", "None"),
        "Over 210": markets.get("Over", {}).get("210", "None"),
        "Over 211": markets.get("Over", {}).get("211", "None"),
        "Over 212": markets.get("Over", {}).get("212", "None"),
        "Over 213": markets.get("Over", {}).get("213", "None"),
        "Over 214": markets.get("Over", {}).get("214", "None"),
        "Over 215": markets.get("Over", {}).get("215", "None"),
        "Over 216": markets.get("Over", {}).get("216", "None"),
        # Next Is Under        
        "Under 227": markets.get("Under", {}).get("227", "None"),
       "Under 227.5":markets.get("Under", {}).get("227.5", "None"),
       "Under 228":markets.get("Under", {}).get("228", "None"),
       "Under 228.5":markets.get("Under", {}).get("228.5", "None"),
       "Under 229":markets.get("Under", {}).get("229", "None"),
       "Under 229.5":markets.get("Under", {}).get("229.5", "None"),
       "Under 230":markets.get("Under", {}).get("230", "None"),
       "Under 230.5":markets.get("Under", {}).get("230.5", "None"),
       "Under 231": markets.get("Under", {}).get("231", "None"),
       "Under 231.5": markets.get("Under", {}).get("231.5", "None"),
       "Under 232": markets.get("Under", {}).get("232", "None"),
       "Under 232.5": markets.get("Under", {}).get("232.5", "None"),
       "Under 233": markets.get("Under", {}).get("233", "None"),
       "Under 233.5": markets.get("Under", {}).get("233.5", "None"),
       "Under 234": markets.get("Under", {}).get("234", "None"),
       "Under 234.5": markets.get("Under", {}).get("234.5", "None"),
       "Under 235": markets.get("Under", {}).get("235", "None"),
        "Under 200": markets.get("Under", {}).get("200", "None"),
        "Under 201":markets.get("Under", {}).get("201", "None"),
        "Under 202":markets.get("Under", {}).get("202", "None"),
        "Under 203":markets.get("Under", {}).get("203", "None"),
        "Under 204":markets.get("Under", {}).get("204", "None"),
        "Under 205":markets.get("Under", {}).get("205", "None"),
        "Under 206":markets.get("Under", {}).get("206", "None"),
        "Under 207":markets.get("Under", {}).get("207", "None"),
        "Under 208": markets.get("Under", {}).get("208", "None"),
        "Under 209": markets.get("Under", {}).get("209", "None"),
        "Under 210": markets.get("Under", {}).get("210", "None"),
        "Under 211": markets.get("Under", {}).get("211", "None"),
        "Under 212": markets.get("Under", {}).get("212", "None"),
        "Under 213": markets.get("Under", {}).get("213", "None"),
        "Under 214": markets.get("Under", {}).get("214", "None"),
        "Under 215": markets.get("Under", {}).get("215", "None"),
        "Under 216": markets.get("Under", {}).get("216", "None"),
        "H1(-21)" : markets.get("Handicap Home", {}).get("-21", "None"),
        "H1(-20.5)" : markets.get("Handicap Home", {}).get("-20.5", "None"),
        "H1(-20)" : markets.get("Handicap Home", {}).get("-20", "None"),
        "H1(-19.5)" : markets.get("Handicap Home", {}).get("-19.5", "None"),
        "H1(-19)" : markets.get("Handicap Home", {}).get("-19", "None"),
        "H1(-18.5)" : markets.get("Handicap Home", {}).get("-18.5", "None"),
        "H1(-18)" : markets.get("Handicap Home", {}).get("-18", "None"),
        "H1(-17.5)" : markets.get("Handicap Home", {}).get("-17.5", "None"),
        "H1(-17)" : markets.get("Handicap Home", {}).get("-17", "None"),
        "H1(-16.5)" : markets.get("Handicap Home", {}).get("-16.5", "None"),
        "H1(-16)" : markets.get("Handicap Home", {}).get("-16", "None"),
        "H1(-15.5)" : markets.get("Handicap Home", {}).get("-15.5", "None"),
        "H1(-15)" : markets.get("Handicap Home", {}).get("-15", "None"),
        "H1(-14.5)" : markets.get("Handicap Home", {}).get("-14.5", "None"),
        "H1(-14)" : markets.get("Handicap Home", {}).get("-14", "None"),
        "H1(-13.5)" : markets.get("Handicap Home", {}).get("-13.5", "None"),
        "H1(-13)" : markets.get("Handicap Home", {}).get("-13", "None"),
        "H2(-21)" : markets.get("Handicap Away", {}).get("-21", "None"),
        "H2(-20.5)" : markets.get("Handicap Away", {}).get("-20.5", "None"),
        "H2(-20)" : markets.get("Handicap Away", {}).get("-20", "None"),
        "H2(-19.5)" : markets.get("Handicap Away", {}).get("-19.5", "None"),
        "H2(-19)" : markets.get("Handicap Away", {}).get("-19", "None"),
        "H2(-18.5)" : markets.get("Handicap Away", {}).get("-18.5", "None"),
        "H2(-18)" : markets.get("Handicap Away", {}).get("-18", "None"),
        "H2(-17.5)" : markets.get("Handicap Away", {}).get("-17.5", "None"),
        "H2(-17)" : markets.get("Handicap Away", {}).get("-17", "None"),
        "H2(-16.5)" : markets.get("Handicap Away", {}).get("-16.5", "None"),
        "H2(-16)" : markets.get("Handicap Away", {}).get("-16", "None"),
        "H2(-15.5)" : markets.get("Handicap Away", {}).get("-15.5", "None"),
        "H2(-15)" : markets.get("Handicap Away", {}).get("-15", "None"),
        "H2(-14.5)" : markets.get("Handicap Away", {}).get("-14.5", "None"),
        "H2(-14)" : markets.get("Handicap Away", {}).get("-14", "None"),
        "H2(-13.5)" : markets.get("Handicap Away", {}).get("-13.5", "None"),
        "H2(-13)" : markets.get("Handicap Away", {}).get("-13", "None"),
        "H1(+21)" : markets.get("Handicap Home", {}).get("+21", "None"),
        "H1(+20.5)" : markets.get("Handicap Home", {}).get("+20.5", "None"),
        "H1(+20)" : markets.get("Handicap Home", {}).get("+20", "None"),
        "H1(+19.5)" : markets.get("Handicap Home", {}).get("+19.5", "None"),
        "H1(+19)" : markets.get("Handicap Home", {}).get("+19", "None"),
        "H1(+18.5)" : markets.get("Handicap Home", {}).get("+18.5", "None"),
        "H1(+18)" : markets.get("Handicap Home", {}).get("+18", "None"),
        "H1(+17.5)" : markets.get("Handicap Home", {}).get("+17.5", "None"),
        "H1(+17)" : markets.get("Handicap Home", {}).get("+17", "None"),
        "H1(+16.5)" : markets.get("Handicap Home", {}).get("+16.5", "None"),
        "H1(+16)" : markets.get("Handicap Home", {}).get("+16", "None"),
        "H1(+15.5)" : markets.get("Handicap Home", {}).get("+15.5", "None"),
        "H1(+15)" : markets.get("Handicap Home", {}).get("+15", "None"),
        "H1(+14.5)" : markets.get("Handicap Home", {}).get("+14.5", "None"),
        "H1(+14)" : markets.get("Handicap Home", {}).get("+14", "None"),
        "H1(+13.5)" : markets.get("Handicap Home", {}).get("+13.5", "None"),
        "H1(+13)" : markets.get("Handicap Home", {}).get("+13", "None"),
        "H2(+21)" : markets.get("Handicap Away", {}).get("+21", "None"),
        "H2(+20.5)" : markets.get("Handicap Away", {}).get("+20.5", "None"),
        "H2(+20)" : markets.get("Handicap Away", {}).get("+20", "None"),
        "H2(+19.5)" : markets.get("Handicap Away", {}).get("+19.5", "None"),
        "H2(+19)" : markets.get("Handicap Away", {}).get("+19", "None"),
        "H2(+18.5)" : markets.get("Handicap Away", {}).get("+18.5", "None"),
        "H2(+18)" : markets.get("Handicap Away", {}).get("+18", "None"),
        "H2(+17.5)" : markets.get("Handicap Away", {}).get("+17.5", "None"),
        "H2(+17)" : markets.get("Handicap Away", {}).get("+17", "None"),
        "H2(+16.5)" : markets.get("Handicap Away", {}).get("+16.5", "None"),
        "H2(+16)" : markets.get("Handicap Away", {}).get("+16", "None"),
        "H2(+15.5)" : markets.get("Handicap Away", {}).get("+15.5", "None"),
        "H2(+15)" : markets.get("Handicap Away", {}).get("+15", "None"),
        "H2(+14.5)" : markets.get("Handicap Away", {}).get("+14.5", "None"),
        "H2(+14)" : markets.get("Handicap Away", {}).get("+14", "None"),
        "H2(+13.5)" : markets.get("Handicap Away", {}).get("+13.5", "None"),
        "H2(+13)" : markets.get("Handicap Away", {}).get("+13", "None"),
    } 
    return found_markets



def extract_betking_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    
    found_markets = {
        '1 (Over Time)' : markets.get("Moneyline", {}).get("1", "None"),
        '2 (Over Time)' : markets.get("Moneyline", {}).get("2", "None"),
        '1 (Regular Time)': markets.get("1X2 - Regular Time", {}).get("1", "None"),
        'X (Regular Time)': markets.get("1X2 - Regular Time", {}).get("X", "None"),
        '2 (Regular Time)': markets.get("1X2 - Regular Time", {}).get("2", "None"),
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
        "Over 227": markets.get("Over", {}).get("227", "None"),
       "Over 227.5":markets.get("Over", {}).get("227.5", "None"),
       "Over 228":markets.get("Over", {}).get("228", "None"),
       "Over 228.5":markets.get("Over", {}).get("228.5", "None"),
       "Over 229":markets.get("Over", {}).get("229", "None"),
       "Over 229.5":markets.get("Over", {}).get("229.5", "None"),
       "Over 230":markets.get("Over", {}).get("230", "None"),
       "Over 230.5":markets.get("Over", {}).get("230.5", "None"),
       "Over 231": markets.get("Over", {}).get("231", "None"),
       "Over 231.5": markets.get("Over", {}).get("231.5", "None"),
       "Over 232": markets.get("Over", {}).get("232", "None"),
       "Over 232.5": markets.get("Over", {}).get("232.5", "None"),
       "Over 233": markets.get("Over", {}).get("233", "None"),
       "Over 233.5": markets.get("Over", {}).get("233.5", "None"),
       "Over 234": markets.get("Over", {}).get("234", "None"),
       "Over 234.5": markets.get("Over", {}).get("234.5", "None"),
       "Over 235": markets.get("Over", {}).get("235", "None"),
        "Over 200": markets.get("Over", {}).get("200", "None"),
        "Over 201":markets.get("Over", {}).get("201", "None"),
        "Over 202":markets.get("Over", {}).get("202", "None"),
        "Over 203":markets.get("Over", {}).get("203", "None"),
        "Over 204":markets.get("Over", {}).get("204", "None"),
        "Over 205":markets.get("Over", {}).get("205", "None"),
        "Over 206":markets.get("Over", {}).get("206", "None"),
        "Over 207":markets.get("Over", {}).get("207", "None"),
        "Over 208": markets.get("Over", {}).get("208", "None"),
        "Over 209": markets.get("Over", {}).get("209", "None"),
        "Over 210": markets.get("Over", {}).get("210", "None"),
        "Over 211": markets.get("Over", {}).get("211", "None"),
        "Over 212": markets.get("Over", {}).get("212", "None"),
        "Over 213": markets.get("Over", {}).get("213", "None"),
        "Over 214": markets.get("Over", {}).get("214", "None"),
        "Over 215": markets.get("Over", {}).get("215", "None"),
        "Over 216": markets.get("Over", {}).get("216", "None"),
        # Next Is Under        
        "Under 227": markets.get("Under", {}).get("227", "None"),
       "Under 227.5":markets.get("Under", {}).get("227.5", "None"),
       "Under 228":markets.get("Under", {}).get("228", "None"),
       "Under 228.5":markets.get("Under", {}).get("228.5", "None"),
       "Under 229":markets.get("Under", {}).get("229", "None"),
       "Under 229.5":markets.get("Under", {}).get("229.5", "None"),
       "Under 230":markets.get("Under", {}).get("230", "None"),
       "Under 230.5":markets.get("Under", {}).get("230.5", "None"),
       "Under 231": markets.get("Under", {}).get("231", "None"),
       "Under 231.5": markets.get("Under", {}).get("231.5", "None"),
       "Under 232": markets.get("Under", {}).get("232", "None"),
       "Under 232.5": markets.get("Under", {}).get("232.5", "None"),
       "Under 233": markets.get("Under", {}).get("233", "None"),
       "Under 233.5": markets.get("Under", {}).get("233.5", "None"),
       "Under 234": markets.get("Under", {}).get("234", "None"),
       "Under 234.5": markets.get("Under", {}).get("234.5", "None"),
       "Under 235": markets.get("Under", {}).get("235", "None"),
        "Under 200": markets.get("Under", {}).get("200", "None"),
        "Under 201":markets.get("Under", {}).get("201", "None"),
        "Under 202":markets.get("Under", {}).get("202", "None"),
        "Under 203":markets.get("Under", {}).get("203", "None"),
        "Under 204":markets.get("Under", {}).get("204", "None"),
        "Under 205":markets.get("Under", {}).get("205", "None"),
        "Under 206":markets.get("Under", {}).get("206", "None"),
        "Under 207":markets.get("Under", {}).get("207", "None"),
        "Under 208": markets.get("Under", {}).get("208", "None"),
        "Under 209": markets.get("Under", {}).get("209", "None"),
        "Under 210": markets.get("Under", {}).get("210", "None"),
        "Under 211": markets.get("Under", {}).get("211", "None"),
        "Under 212": markets.get("Under", {}).get("212", "None"),
        "Under 213": markets.get("Under", {}).get("213", "None"),
        "Under 214": markets.get("Under", {}).get("214", "None"),
        "Under 215": markets.get("Under", {}).get("215", "None"),
        "Under 216": markets.get("Under", {}).get("216", "None"),
        "H1(-21)" : markets.get("Handicap Home", {}).get("-21", "None"),
        "H1(-20.5)" : markets.get("Handicap Home", {}).get("-20.5", "None"),
        "H1(-20)" : markets.get("Handicap Home", {}).get("-20", "None"),
        "H1(-19.5)" : markets.get("Handicap Home", {}).get("-19.5", "None"),
        "H1(-19)" : markets.get("Handicap Home", {}).get("-19", "None"),
        "H1(-18.5)" : markets.get("Handicap Home", {}).get("-18.5", "None"),
        "H1(-18)" : markets.get("Handicap Home", {}).get("-18", "None"),
        "H1(-17.5)" : markets.get("Handicap Home", {}).get("-17.5", "None"),
        "H1(-17)" : markets.get("Handicap Home", {}).get("-17", "None"),
        "H1(-16.5)" : markets.get("Handicap Home", {}).get("-16.5", "None"),
        "H1(-16)" : markets.get("Handicap Home", {}).get("-16", "None"),
        "H1(-15.5)" : markets.get("Handicap Home", {}).get("-15.5", "None"),
        "H1(-15)" : markets.get("Handicap Home", {}).get("-15", "None"),
        "H1(-14.5)" : markets.get("Handicap Home", {}).get("-14.5", "None"),
        "H1(-14)" : markets.get("Handicap Home", {}).get("-14", "None"),
        "H1(-13.5)" : markets.get("Handicap Home", {}).get("-13.5", "None"),
        "H1(-13)" : markets.get("Handicap Home", {}).get("-13", "None"),
        "H2(-21)" : markets.get("Handicap Away", {}).get("-21", "None"),
        "H2(-20.5)" : markets.get("Handicap Away", {}).get("-20.5", "None"),
        "H2(-20)" : markets.get("Handicap Away", {}).get("-20", "None"),
        "H2(-19.5)" : markets.get("Handicap Away", {}).get("-19.5", "None"),
        "H2(-19)" : markets.get("Handicap Away", {}).get("-19", "None"),
        "H2(-18.5)" : markets.get("Handicap Away", {}).get("-18.5", "None"),
        "H2(-18)" : markets.get("Handicap Away", {}).get("-18", "None"),
        "H2(-17.5)" : markets.get("Handicap Away", {}).get("-17.5", "None"),
        "H2(-17)" : markets.get("Handicap Away", {}).get("-17", "None"),
        "H2(-16.5)" : markets.get("Handicap Away", {}).get("-16.5", "None"),
        "H2(-16)" : markets.get("Handicap Away", {}).get("-16", "None"),
        "H2(-15.5)" : markets.get("Handicap Away", {}).get("-15.5", "None"),
        "H2(-15)" : markets.get("Handicap Away", {}).get("-15", "None"),
        "H2(-14.5)" : markets.get("Handicap Away", {}).get("-14.5", "None"),
        "H2(-14)" : markets.get("Handicap Away", {}).get("-14", "None"),
        "H2(-13.5)" : markets.get("Handicap Away", {}).get("-13.5", "None"),
        "H2(-13)" : markets.get("Handicap Away", {}).get("-13", "None"),
        "H1(+21)" : markets.get("Handicap Home", {}).get("+21", "None"),
        "H1(+20.5)" : markets.get("Handicap Home", {}).get("+20.5", "None"),
        "H1(+20)" : markets.get("Handicap Home", {}).get("+20", "None"),
        "H1(+19.5)" : markets.get("Handicap Home", {}).get("+19.5", "None"),
        "H1(+19)" : markets.get("Handicap Home", {}).get("+19", "None"),
        "H1(+18.5)" : markets.get("Handicap Home", {}).get("+18.5", "None"),
        "H1(+18)" : markets.get("Handicap Home", {}).get("+18", "None"),
        "H1(+17.5)" : markets.get("Handicap Home", {}).get("+17.5", "None"),
        "H1(+17)" : markets.get("Handicap Home", {}).get("+17", "None"),
        "H1(+16.5)" : markets.get("Handicap Home", {}).get("+16.5", "None"),
        "H1(+16)" : markets.get("Handicap Home", {}).get("+16", "None"),
        "H1(+15.5)" : markets.get("Handicap Home", {}).get("+15.5", "None"),
        "H1(+15)" : markets.get("Handicap Home", {}).get("+15", "None"),
        "H1(+14.5)" : markets.get("Handicap Home", {}).get("+14.5", "None"),
        "H1(+14)" : markets.get("Handicap Home", {}).get("+14", "None"),
        "H1(+13.5)" : markets.get("Handicap Home", {}).get("+13.5", "None"),
        "H1(+13)" : markets.get("Handicap Home", {}).get("+13", "None"),
        "H2(+21)" : markets.get("Handicap Away", {}).get("+21", "None"),
        "H2(+20.5)" : markets.get("Handicap Away", {}).get("+20.5", "None"),
        "H2(+20)" : markets.get("Handicap Away", {}).get("+20", "None"),
        "H2(+19.5)" : markets.get("Handicap Away", {}).get("+19.5", "None"),
        "H2(+19)" : markets.get("Handicap Away", {}).get("+19", "None"),
        "H2(+18.5)" : markets.get("Handicap Away", {}).get("+18.5", "None"),
        "H2(+18)" : markets.get("Handicap Away", {}).get("+18", "None"),
        "H2(+17.5)" : markets.get("Handicap Away", {}).get("+17.5", "None"),
        "H2(+17)" : markets.get("Handicap Away", {}).get("+17", "None"),
        "H2(+16.5)" : markets.get("Handicap Away", {}).get("+16.5", "None"),
        "H2(+16)" : markets.get("Handicap Away", {}).get("+16", "None"),
        "H2(+15.5)" : markets.get("Handicap Away", {}).get("+15.5", "None"),
        "H2(+15)" : markets.get("Handicap Away", {}).get("+15", "None"),
        "H2(+14.5)" : markets.get("Handicap Away", {}).get("+14.5", "None"),
        "H2(+14)" : markets.get("Handicap Away", {}).get("+14", "None"),
        "H2(+13.5)" : markets.get("Handicap Away", {}).get("+13.5", "None"),
        "H2(+13)" : markets.get("Handicap Away", {}).get("+13", "None"),
    } 
    return found_markets


def extract_merrybet_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    
    found_markets = {
        "1 (Regular Time)": markets.get("1X2", {}).get("1", "None"),
        "X (Regular Time)": markets.get("1X2", {}).get("X", "None"),
        "2 (Regular Time)": markets.get("1X2", {}).get("2", "None"),

        "1 (First Half)": markets.get("1st half - 1x2", {}).get("1", "None"),
        "X (First Half)": markets.get("1st half - 1x2", {}).get("X", "None"),
        "2 (First Half)": markets.get("1st half - 1x2", {}).get("2", "None")
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
        "1 (Over Time)": markets.get("Match winner", {}).get("1", "None"),
        "2 (Over Time)": markets.get("Match winner", {}).get("2", "None"),

        "1 (First Half)": markets.get("1st Half Winner", {}).get("1", "None"),
        "X (First Half)": markets.get("1st Half Winner", {}).get("X", "None"),
        "2 (First Half)": markets.get("1st Half Winner", {}).get("2", "None"),

        "H2 (+1.5) (First Quater)": markets.get("1st Quarter Handicap", {}).get("2 +1.5", "None"),
        "H1 (-1.5) (First Quater)": markets.get("1st Quarter Handicap", {}).get("1 -1.5", "None"),

        "1 (First Quater)": markets.get("1st Quarter Betting", {}).get("1", "None"),
        "X (First Quater)": markets.get("1st Quarter Betting", {}).get("X", "None"),
        "2 (First Quater)": markets.get("1st Quarter Betting", {}).get("2", "None"),
        
        "1 (Regular Time)": markets.get("Match Result (No OT)", {}).get("1", "None"),
        "X (Regular Time)": markets.get("Match Result (No OT)", {}).get("X", "None"),
        "2 (Regular Time)": markets.get("Match Result (No OT)", {}).get("2", "None"),
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
        "Over 227": markets.get("Over", {}).get("227", "None"),
       "Over 227.5":markets.get("Over", {}).get("227.5", "None"),
       "Over 228":markets.get("Over", {}).get("228", "None"),
       "Over 228.5":markets.get("Over", {}).get("228.5", "None"),
       "Over 229":markets.get("Over", {}).get("229", "None"),
       "Over 229.5":markets.get("Over", {}).get("229.5", "None"),
       "Over 230":markets.get("Over", {}).get("230", "None"),
       "Over 230.5":markets.get("Over", {}).get("230.5", "None"),
       "Over 231": markets.get("Over", {}).get("231", "None"),
       "Over 231.5": markets.get("Over", {}).get("231.5", "None"),
       "Over 232": markets.get("Over", {}).get("232", "None"),
       "Over 232.5": markets.get("Over", {}).get("232.5", "None"),
       "Over 233": markets.get("Over", {}).get("233", "None"),
       "Over 233.5": markets.get("Over", {}).get("233.5", "None"),
       "Over 234": markets.get("Over", {}).get("234", "None"),
       "Over 234.5": markets.get("Over", {}).get("234.5", "None"),
       "Over 235": markets.get("Over", {}).get("235", "None"),
        "Over 200": markets.get("Over", {}).get("200", "None"),
        "Over 201":markets.get("Over", {}).get("201", "None"),
        "Over 202":markets.get("Over", {}).get("202", "None"),
        "Over 203":markets.get("Over", {}).get("203", "None"),
        "Over 204":markets.get("Over", {}).get("204", "None"),
        "Over 205":markets.get("Over", {}).get("205", "None"),
        "Over 206":markets.get("Over", {}).get("206", "None"),
        "Over 207":markets.get("Over", {}).get("207", "None"),
        "Over 208": markets.get("Over", {}).get("208", "None"),
        "Over 209": markets.get("Over", {}).get("209", "None"),
        "Over 210": markets.get("Over", {}).get("210", "None"),
        "Over 211": markets.get("Over", {}).get("211", "None"),
        "Over 212": markets.get("Over", {}).get("212", "None"),
        "Over 213": markets.get("Over", {}).get("213", "None"),
        "Over 214": markets.get("Over", {}).get("214", "None"),
        "Over 215": markets.get("Over", {}).get("215", "None"),
        "Over 216": markets.get("Over", {}).get("216", "None"),
        # Next Is Under        
        "Under 227": markets.get("Under", {}).get("227", "None"),
       "Under 227.5":markets.get("Under", {}).get("227.5", "None"),
       "Under 228":markets.get("Under", {}).get("228", "None"),
       "Under 228.5":markets.get("Under", {}).get("228.5", "None"),
       "Under 229":markets.get("Under", {}).get("229", "None"),
       "Under 229.5":markets.get("Under", {}).get("229.5", "None"),
       "Under 230":markets.get("Under", {}).get("230", "None"),
       "Under 230.5":markets.get("Under", {}).get("230.5", "None"),
       "Under 231": markets.get("Under", {}).get("231", "None"),
       "Under 231.5": markets.get("Under", {}).get("231.5", "None"),
       "Under 232": markets.get("Under", {}).get("232", "None"),
       "Under 232.5": markets.get("Under", {}).get("232.5", "None"),
       "Under 233": markets.get("Under", {}).get("233", "None"),
       "Under 233.5": markets.get("Under", {}).get("233.5", "None"),
       "Under 234": markets.get("Under", {}).get("234", "None"),
       "Under 234.5": markets.get("Under", {}).get("234.5", "None"),
       "Under 235": markets.get("Under", {}).get("235", "None"),
        "Under 200": markets.get("Under", {}).get("200", "None"),
        "Under 201":markets.get("Under", {}).get("201", "None"),
        "Under 202":markets.get("Under", {}).get("202", "None"),
        "Under 203":markets.get("Under", {}).get("203", "None"),
        "Under 204":markets.get("Under", {}).get("204", "None"),
        "Under 205":markets.get("Under", {}).get("205", "None"),
        "Under 206":markets.get("Under", {}).get("206", "None"),
        "Under 207":markets.get("Under", {}).get("207", "None"),
        "Under 208": markets.get("Under", {}).get("208", "None"),
        "Under 209": markets.get("Under", {}).get("209", "None"),
        "Under 210": markets.get("Under", {}).get("210", "None"),
        "Under 211": markets.get("Under", {}).get("211", "None"),
        "Under 212": markets.get("Under", {}).get("212", "None"),
        "Under 213": markets.get("Under", {}).get("213", "None"),
        "Under 214": markets.get("Under", {}).get("214", "None"),
        "Under 215": markets.get("Under", {}).get("215", "None"),
        "Under 216": markets.get("Under", {}).get("216", "None"),
        "H1(-21)" : markets.get("Handicap Home", {}).get("-21", "None"),
        "H1(-20.5)" : markets.get("Handicap Home", {}).get("-20.5", "None"),
        "H1(-20)" : markets.get("Handicap Home", {}).get("-20", "None"),
        "H1(-19.5)" : markets.get("Handicap Home", {}).get("-19.5", "None"),
        "H1(-19)" : markets.get("Handicap Home", {}).get("-19", "None"),
        "H1(-18.5)" : markets.get("Handicap Home", {}).get("-18.5", "None"),
        "H1(-18)" : markets.get("Handicap Home", {}).get("-18", "None"),
        "H1(-17.5)" : markets.get("Handicap Home", {}).get("-17.5", "None"),
        "H1(-17)" : markets.get("Handicap Home", {}).get("-17", "None"),
        "H1(-16.5)" : markets.get("Handicap Home", {}).get("-16.5", "None"),
        "H1(-16)" : markets.get("Handicap Home", {}).get("-16", "None"),
        "H1(-15.5)" : markets.get("Handicap Home", {}).get("-15.5", "None"),
        "H1(-15)" : markets.get("Handicap Home", {}).get("-15", "None"),
        "H1(-14.5)" : markets.get("Handicap Home", {}).get("-14.5", "None"),
        "H1(-14)" : markets.get("Handicap Home", {}).get("-14", "None"),
        "H1(-13.5)" : markets.get("Handicap Home", {}).get("-13.5", "None"),
        "H1(-13)" : markets.get("Handicap Home", {}).get("-13", "None"),
        "H2(-21)" : markets.get("Handicap Away", {}).get("-21", "None"),
        "H2(-20.5)" : markets.get("Handicap Away", {}).get("-20.5", "None"),
        "H2(-20)" : markets.get("Handicap Away", {}).get("-20", "None"),
        "H2(-19.5)" : markets.get("Handicap Away", {}).get("-19.5", "None"),
        "H2(-19)" : markets.get("Handicap Away", {}).get("-19", "None"),
        "H2(-18.5)" : markets.get("Handicap Away", {}).get("-18.5", "None"),
        "H2(-18)" : markets.get("Handicap Away", {}).get("-18", "None"),
        "H2(-17.5)" : markets.get("Handicap Away", {}).get("-17.5", "None"),
        "H2(-17)" : markets.get("Handicap Away", {}).get("-17", "None"),
        "H2(-16.5)" : markets.get("Handicap Away", {}).get("-16.5", "None"),
        "H2(-16)" : markets.get("Handicap Away", {}).get("-16", "None"),
        "H2(-15.5)" : markets.get("Handicap Away", {}).get("-15.5", "None"),
        "H2(-15)" : markets.get("Handicap Away", {}).get("-15", "None"),
        "H2(-14.5)" : markets.get("Handicap Away", {}).get("-14.5", "None"),
        "H2(-14)" : markets.get("Handicap Away", {}).get("-14", "None"),
        "H2(-13.5)" : markets.get("Handicap Away", {}).get("-13.5", "None"),
        "H2(-13)" : markets.get("Handicap Away", {}).get("-13", "None"),
        "H1(+21)" : markets.get("Handicap Home", {}).get("+21", "None"),
        "H1(+20.5)" : markets.get("Handicap Home", {}).get("+20.5", "None"),
        "H1(+20)" : markets.get("Handicap Home", {}).get("+20", "None"),
        "H1(+19.5)" : markets.get("Handicap Home", {}).get("+19.5", "None"),
        "H1(+19)" : markets.get("Handicap Home", {}).get("+19", "None"),
        "H1(+18.5)" : markets.get("Handicap Home", {}).get("+18.5", "None"),
        "H1(+18)" : markets.get("Handicap Home", {}).get("+18", "None"),
        "H1(+17.5)" : markets.get("Handicap Home", {}).get("+17.5", "None"),
        "H1(+17)" : markets.get("Handicap Home", {}).get("+17", "None"),
        "H1(+16.5)" : markets.get("Handicap Home", {}).get("+16.5", "None"),
        "H1(+16)" : markets.get("Handicap Home", {}).get("+16", "None"),
        "H1(+15.5)" : markets.get("Handicap Home", {}).get("+15.5", "None"),
        "H1(+15)" : markets.get("Handicap Home", {}).get("+15", "None"),
        "H1(+14.5)" : markets.get("Handicap Home", {}).get("+14.5", "None"),
        "H1(+14)" : markets.get("Handicap Home", {}).get("+14", "None"),
        "H1(+13.5)" : markets.get("Handicap Home", {}).get("+13.5", "None"),
        "H1(+13)" : markets.get("Handicap Home", {}).get("+13", "None"),
        "H2(+21)" : markets.get("Handicap Away", {}).get("+21", "None"),
        "H2(+20.5)" : markets.get("Handicap Away", {}).get("+20.5", "None"),
        "H2(+20)" : markets.get("Handicap Away", {}).get("+20", "None"),
        "H2(+19.5)" : markets.get("Handicap Away", {}).get("+19.5", "None"),
        "H2(+19)" : markets.get("Handicap Away", {}).get("+19", "None"),
        "H2(+18.5)" : markets.get("Handicap Away", {}).get("+18.5", "None"),
        "H2(+18)" : markets.get("Handicap Away", {}).get("+18", "None"),
        "H2(+17.5)" : markets.get("Handicap Away", {}).get("+17.5", "None"),
        "H2(+17)" : markets.get("Handicap Away", {}).get("+17", "None"),
        "H2(+16.5)" : markets.get("Handicap Away", {}).get("+16.5", "None"),
        "H2(+16)" : markets.get("Handicap Away", {}).get("+16", "None"),
        "H2(+15.5)" : markets.get("Handicap Away", {}).get("+15.5", "None"),
        "H2(+15)" : markets.get("Handicap Away", {}).get("+15", "None"),
        "H2(+14.5)" : markets.get("Handicap Away", {}).get("+14.5", "None"),
        "H2(+14)" : markets.get("Handicap Away", {}).get("+14", "None"),
        "H2(+13.5)" : markets.get("Handicap Away", {}).get("+13.5", "None"),
        "H2(+13)" : markets.get("Handicap Away", {}).get("+13", "None"),        

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
        "1 (Over Time)": markets.get("Winner (incl. overtime)", {}).get("1", "None"),
        "2 (Over Time)": markets.get("Winner (incl. overtime)", {}).get("2", "None"),

        "Over 217.5": markets.get("Over/Under (incl. overtime) 217.5", {}).get("Over 217.5", "None"),
        "Under 217.5": markets.get("Over/Under (incl. overtime) 217.5", {}).get("Under 217.5", "None"),

        "Over 218.5": markets.get("Over/Under (incl. overtime) 218.5", {}).get("Over 218.5", "None"),
        "Under 218.5": markets.get("Over/Under (incl. overtime) 218.5", {}).get("Under 218.5", "None"),

        "Over 219.5": markets.get("Over/Under (incl. overtime) 219.5", {}).get("Over 219.5", "None"),
        "Under 219.5": markets.get("Over/Under (incl. overtime) 219.5", {}).get("Under 219.5", "None"),

        "Over 220.5": markets.get("Over/Under (incl. overtime) 220.5", {}).get("Over 220.5", "None"),
        "Under 220.5": markets.get("Over/Under (incl. overtime) 220.5", {}).get("Under 220.5", "None"),

        "Over 221.5": markets.get("Over/Under (incl. overtime) 221.5", {}).get("Over 221.5", "None"),
        "Under 221.5": markets.get("Over/Under (incl. overtime) 221.5", {}).get("Under 221.5", "None"),

        "Over 222.5": markets.get("Over/Under (incl. overtime) 222.5", {}).get("Over 222.5", "None"),
        "Under 222.5": markets.get("Over/Under (incl. overtime) 222.5", {}).get("Under 222.5", "None"),

        "Over 223.5": markets.get("Over/Under (incl. overtime) 223.5", {}).get("Over 223.5", "None"),
        "Under 223.5": markets.get("Over/Under (incl. overtime) 223.5", {}).get("Under 223.5", "None"),

        "Over 224.5": markets.get("Over/Under (incl. overtime) 224.5", {}).get("Over 224.5", "None"),
        "Under 224.5": markets.get("Over/Under (incl. overtime) 224.5", {}).get("Under 224.5", "None"),

        "Over 225.5": markets.get("Over/Under (incl. overtime) 225.5", {}).get("Over 225.5", "None"),
        "Under 225.5": markets.get("Over/Under (incl. overtime) 225.5", {}).get("Under 225.5", "None"),

        "Over 226.5": markets.get("Over/Under (incl. overtime) 226.5", {}).get("Over 226.5", "None"),
        "Under 226.5": markets.get("Over/Under (incl. overtime) 226.5", {}).get("Under 226.5", "None"),

        "Over 227.5": markets.get("Over/Under (incl. overtime) 227.5", {}).get("Over 227.5", "None"),
        "Under 227.5": markets.get("Over/Under (incl. overtime) 227.5", {}).get("Under 227.5", "None"),

        "Over 228.5": markets.get("Over/Under (incl. overtime) 228.5", {}).get("Over 228.5", "None"),
        "Under 228.5": markets.get("Over/Under (incl. overtime) 228.5", {}).get("Under 228.5", "None"),

        "Over 229.5": markets.get("Over/Under (incl. overtime) 229.5", {}).get("Over 229.5", "None"),
        "Under 229.5": markets.get("Over/Under (incl. overtime) 229.5", {}).get("Under 229.5", "None"),

        "Over 230.5": markets.get("Over/Under (incl. overtime) 230.5", {}).get("Over 230.5", "None"),
        "Under 230.5": markets.get("Over/Under (incl. overtime) 230.5", {}).get("Under 230.5", "None"),
        
        "Over 231.5": markets.get("Over/Under (incl. overtime) 231.5", {}).get("Over 231.5", "None"),
        "Under 231.5": markets.get("Over/Under (incl. overtime) 231.5", {}).get("Under 231.5", "None"),

        "Over 232.5": markets.get("Over/Under (incl. overtime) 232.5", {}).get("Over 232.5", "None"),
        "Under 232.5": markets.get("Over/Under (incl. overtime) 232.5", {}).get("Under 232.5", "None"),

        "Over 233.5": markets.get("Over/Under (incl. overtime) 233.5", {}).get("Over 233.5", "None"),
        "Under 233.5": markets.get("Over/Under (incl. overtime) 233.5", {}).get("Under 233.5", "None"),

        "Over 234.5": markets.get("Over/Under (incl. overtime) 234.5", {}).get("Over 234.5", "None"),
        "Under 234.5": markets.get("Over/Under (incl. overtime) 234.5", {}).get("Under 234.5", "None"),

        "Over 235.5": markets.get("Over/Under (incl. overtime) 235.5", {}).get("Over 235.5", "None"),
        "Under 235.5": markets.get("Over/Under (incl. overtime) 235.5", {}).get("Under 235.5", "None"),

        "Over 236.5": markets.get("Over/Under (incl. overtime) 236.5", {}).get("Over 236.5", "None"),
        "Under 236.5": markets.get("Over/Under (incl. overtime) 236.5", {}).get("Under 236.5", "None"),

        "Over 237.5": markets.get("Over/Under (incl. overtime) 237.5", {}).get("Over 237.5", "None"),
        "Under 237.5": markets.get("Over/Under (incl. overtime) 237.5", {}).get("Under 237.5", "None"),

        "Over 238.5": markets.get("Over/Under (incl. overtime) 238.5", {}).get("Over 238.5", "None"),
        "Under 238.5": markets.get("Over/Under (incl. overtime) 238.5", {}).get("Under 238.5", "None"),

        "Over 239.5": markets.get("Over/Under (incl. overtime) 239.5", {}).get("Over 239.5", "None"),
        "Under 239.5": markets.get("Over/Under (incl. overtime) 239.5", {}).get("Under 239.5", "None"),

        "Over 240.5": markets.get("Over/Under (incl. overtime) 240.5", {}).get("Over 240.5", "None"),
        "Under 240.5": markets.get("Over/Under (incl. overtime) 240.5", {}).get("Under 240.5", "None"),

        "Over 241.5": markets.get("Over/Under (incl. overtime) 241.5", {}).get("Over 241.5", "None"),
        "Under 241.5": markets.get("Over/Under (incl. overtime) 241.5", {}).get("Under 241.5", "None"),

        "Over 242.5": markets.get("Over/Under (incl. overtime) 242.5", {}).get("Over 242.5", "None"),
        "Under 242.5": markets.get("Over/Under (incl. overtime) 242.5", {}).get("Under 242.5", "None"),

        "Over 243.5": markets.get("Over/Under (incl. overtime) 243.5", {}).get("Over 243.5", "None"),
        "Under 243.5": markets.get("Over/Under (incl. overtime) 243.5", {}).get("Under 243.5", "None"),

        "Over 244.5": markets.get("Over/Under (incl. overtime) 244.5", {}).get("Over 244.5", "None"),
        "Under 244.5": markets.get("Over/Under (incl. overtime) 244.5", {}).get("Under 244.5", "None"),

        "Over 245.5": markets.get("Over/Under (incl. overtime) 245.5", {}).get("Over 245.5", "None"),
        "Under 245.5": markets.get("Over/Under (incl. overtime) 245.5", {}).get("Under 245.5", "None"),

        "1 (First Half) Over 107.5": markets.get("1st Half - Over/Under", {}).get("Over 107.5", "None"),
        "1 (First Half) Under 107.5": markets.get("1st Half - Over/Under", {}).get("Under 107.5", "None"),

        "1 (First Half) Over 108.5": markets.get("1st Half - Over/Under", {}).get("Over 108.5", "None"),
        "1 (First Half) Under 108.5": markets.get("1st Half - Over/Under", {}).get("Under 108.5", "None"),

        "1 (First Half) Over 109.5": markets.get("1st Half - Over/Under", {}).get("Over 109.5", "None"),
        "1 (First Half) Under 109.5": markets.get("1st Half - Over/Under", {}).get("Under 109.5", "None"),

        "1 (First Half) Over 110.5": markets.get("1st Half - Over/Under", {}).get("Over 110.5", "None"),
        "1 (First Half) Under 110.5": markets.get("1st Half - Over/Under", {}).get("Under 110.5", "None"),

        "1 (First Half) Over 111.5": markets.get("1st Half - Over/Under", {}).get("Over 111.5", "None"),
        "1 (First Half) Under 111.5": markets.get("1st Half - Over/Under", {}).get("Under 111.5", "None"),

        "1 (First Half) Over 112.5": markets.get("1st Half - Over/Under", {}).get("Over 112.5", "None"),
        "1 (First Half) Under 112.5": markets.get("1st Half - Over/Under", {}).get("Under 112.5", "None"),

        "1 (First Half) Over 113.5": markets.get("1st Half - Over/Under", {}).get("Over 113.5", "None"),
        "1 (First Half) Under 113.5": markets.get("1st Half - Over/Under", {}).get("Under 113.5", "None"),

        "1 (First Half) Over 114.5": markets.get("1st Half - Over/Under", {}).get("Over 114.5", "None"),
        "1 (First Half) Under 114.5": markets.get("1st Half - Over/Under", {}).get("Under 114.5", "None"),

        "1 (First Half) Over 115.5": markets.get("1st Half - Over/Under", {}).get("Over 115.5", "None"),
        "1 (First Half) Under 115.5": markets.get("1st Half - Over/Under", {}).get("Under 115.5", "None"),

        "1 (First Half) Over 116.5": markets.get("1st Half - Over/Under", {}).get("Over 116.5", "None"),
        "1 (First Half) Under 116.5": markets.get("1st Half - Over/Under", {}).get("Under 116.5", "None"),

        "1 (First Half) Over 117.5": markets.get("1st Half - Over/Under", {}).get("Over 117.5", "None"),
        "1 (First Half) Under 117.5": markets.get("1st Half - Over/Under", {}).get("Under 117.5", "None"),

        "1 (First Half) Over 118.5": markets.get("1st Half - Over/Under", {}).get("Over 118.5", "None"),
        "1 (First Half) Under 118.5": markets.get("1st Half - Over/Under", {}).get("Under 118.5", "None"),

        "1 (First Half) Over 119.5": markets.get("1st Half - Over/Under", {}).get("Over 119.5", "None"),
        "1 (First Half) Under 119.5": markets.get("1st Half - Over/Under", {}).get("Under 119.5", "None"),


        "H1(-10.5)" : markets.get("Handicap (incl. overtime) -10.5", {}).get("1 (-10.5)", "None"),
        "H2(+10.5)": markets.get("Handicap (incl. overtime) -10.5", {}).get("2 (+10.5)", "None"),

        "H1(-11.5)" : markets.get("Handicap (incl. overtime) -11.5", {}).get("1 (-11.5)", "None"),
        "H2(+11.5)": markets.get("Handicap (incl. overtime) -11.5", {}).get("2 (+11.5)", "None"),
        
        "H1(-12.5)" : markets.get("Handicap (incl. overtime) -12.5", {}).get("1 (-12.5)", "None"),
        "H2(+12.5)": markets.get("Handicap (incl. overtime) -12.5", {}).get("2 (+12.5)", "None"),
        
        "H1(-13.5)" : markets.get("Handicap (incl. overtime) -13.5", {}).get("1 (-13.5)", "None"),
        "H2(+13.5)": markets.get("Handicap (incl. overtime) -13.5", {}).get("2 (+13.5)", "None"),
        
        "H1(-14.5)" : markets.get("Handicap (incl. overtime) -14.5", {}).get("1 (-14.5)", "None"),
        "H2(+14.5)": markets.get("Handicap (incl. overtime) -14.5", {}).get("2 (+14.5)", "None"),
        
        "H1(-15.5)" : markets.get("Handicap (incl. overtime) -15.5", {}).get("1 (-15.5)", "None"),
        "H2(+15.5)": markets.get("Handicap (incl. overtime) -15.5", {}).get("2 (+15.5)", "None"),
        
        "H1(-16.5)" : markets.get("Handicap (incl. overtime) -16.5", {}).get("1 (-16.5)", "None"),
        "H2(+16.5)": markets.get("Handicap (incl. overtime) -16.5", {}).get("2 (+16.5)", "None"),
        
        "H1(-17.5)" : markets.get("Handicap (incl. overtime) -17.5", {}).get("1 (-17.5)", "None"),
        "H2(+17.5)": markets.get("Handicap (incl. overtime) -17.5", {}).get("2 (+17.5)", "None"),
        
        "H1(-18.5)" : markets.get("Handicap (incl. overtime) -18.5", {}).get("1 (-18.5)", "None"),
        "H2(+18.5)": markets.get("Handicap (incl. overtime) -18.5", {}).get("2 (+18.5)", "None"),
        
        "H1(-19.5)" : markets.get("Handicap (incl. overtime) -19.5", {}).get("1 (-19.5)", "None"),
        "H2(+19.5)": markets.get("Handicap (incl. overtime) -19.5", {}).get("2 (+19.5)", "None"),
        
        "H1(-20.5)" : markets.get("Handicap (incl. overtime) -20.5", {}).get("1 (-20.5)", "None"),
        "H2(+20.5)": markets.get("Handicap (incl. overtime) -20.5", {}).get("2 (+20.5)", "None"),

        "H1(-21.5)" : markets.get("Handicap (incl. overtime) -21.5", {}).get("1 (-21.5)", "None"),
        "H2(+21.5)": markets.get("Handicap (incl. overtime) -21.5", {}).get("2 (+21.5)", "None"),

        "H1(-22.5)" : markets.get("Handicap (incl. overtime) -22.5", {}).get("1 (-22.5)", "None"),
        "H2(+22.5)": markets.get("Handicap (incl. overtime) -22.5", {}).get("2 (+22.5)", "None"),
        
        "H1(-23.5)" : markets.get("Handicap (incl. overtime) -23.5", {}).get("1 (-23.5)", "None"),
        "H2(+23.5)": markets.get("Handicap (incl. overtime) -23.5", {}).get("2 (+23.5)", "None"),
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
        "1 (Over Time)": markets.get("Money line", {}).get("1", "None"),
        "2 (Over Time)": markets.get("Money line", {}).get("2", "None"),

        "Over 188.5": markets.get("Over/under", {}).get("Over 188.5", "None"),
        "Under 188.5": markets.get("Over/under", {}).get("Under 188.5", "None"),
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

def process_basketball(sport_file_path):
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
            bookie_data = {}
            for bookie, market_data in bookies_data.items():
                try:
                    if bookie in special_functions:
                        bookie_extracted_data = special_functions[bookie](market_data)
                        bookie_data[bookie] = bookie_extracted_data  
                    else:
                        log_error(f" No special extraction function for this {bookie}.",)
                except Exception as e:
                    log_exception(f"Error Extracting markets for {bookie} game name: {game} ERROR: {e}",)
        all_markets[game] = bookie_data  
    return all_markets   


