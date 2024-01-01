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
    found_markets["StartTime"] = markets.get("time","None")
    
    found_markets = {
        "1" : markets.get("1X2", {}).get("1", "None"),
        "2" : markets.get("1X2", {}).get("2", "None"),
        "Over 177": markets.get("Over", {}).get("177", "None"),
       "Over 177.5":markets.get("Over", {}).get("177.5", "None"),
       "Over 178":markets.get("Over", {}).get("178", "None"),
       "Over 178.5":markets.get("Over", {}).get("178.5", "None"),
       "Over 179":markets.get("Over", {}).get("179", "None"),
       "Over 179.5":markets.get("Over", {}).get("179.5", "None"),
       "Over 180":markets.get("Over", {}).get("180", "None"),
       "Over 180.5":markets.get("Over", {}).get("180.5", "None"),
       "Over 181": markets.get("Over", {}).get("181", "None"),
       "Over 181.5": markets.get("Over", {}).get("181.5", "None"),
       "Over 182": markets.get("Over", {}).get("182", "None"),
       "Over 182.5": markets.get("Over", {}).get("182.5", "None"),
       "Over 183": markets.get("Over", {}).get("183", "None"),
       "Over 183.5": markets.get("Over", {}).get("183.5", "None"),
       "Over 184": markets.get("Over", {}).get("184", "None"),
       "Over 184.5": markets.get("Over", {}).get("184.5", "None"),
       "Over 185": markets.get("Over", {}).get("185", "None"),
        "Over 150": markets.get("Over", {}).get("150", "None"),
        "Over 151":markets.get("Over", {}).get("151", "None"),
        "Over 152":markets.get("Over", {}).get("152", "None"),
        "Over 153":markets.get("Over", {}).get("153", "None"),
        "Over 154":markets.get("Over", {}).get("154", "None"),
        "Over 155":markets.get("Over", {}).get("155", "None"),
        "Over 156":markets.get("Over", {}).get("156", "None"),
        "Over 157":markets.get("Over", {}).get("157", "None"),
        "Over 158": markets.get("Over", {}).get("158", "None"),
        "Over 159": markets.get("Over", {}).get("159", "None"),
        "Over 160": markets.get("Over", {}).get("160", "None"),
        "Over 161": markets.get("Over", {}).get("161", "None"),
        "Over 162": markets.get("Over", {}).get("162", "None"),
        "Over 163": markets.get("Over", {}).get("163", "None"),
        "Over 164": markets.get("Over", {}).get("164", "None"),
        "Over 165": markets.get("Over", {}).get("165", "None"),
        "Over 166": markets.get("Over", {}).get("166", "None"),
        # Next Is Under        
        "Under 177": markets.get("Under", {}).get("177", "None"),
       "Under 177.5":markets.get("Under", {}).get("177.5", "None"),
       "Under 178":markets.get("Under", {}).get("178", "None"),
       "Under 178.5":markets.get("Under", {}).get("178.5", "None"),
       "Under 179":markets.get("Under", {}).get("179", "None"),
       "Under 179.5":markets.get("Under", {}).get("179.5", "None"),
       "Under 180":markets.get("Under", {}).get("180", "None"),
       "Under 180.5":markets.get("Under", {}).get("180.5", "None"),
       "Under 181": markets.get("Under", {}).get("181", "None"),
       "Under 181.5": markets.get("Under", {}).get("181.5", "None"),
       "Under 182": markets.get("Under", {}).get("182", "None"),
       "Under 182.5": markets.get("Under", {}).get("182.5", "None"),
       "Under 183": markets.get("Under", {}).get("183", "None"),
       "Under 183.5": markets.get("Under", {}).get("183.5", "None"),
       "Under 184": markets.get("Under", {}).get("184", "None"),
       "Under 184.5": markets.get("Under", {}).get("184.5", "None"),
       "Under 185": markets.get("Under", {}).get("185", "None"),
        "Under 150": markets.get("Under", {}).get("150", "None"),
        "Under 151":markets.get("Under", {}).get("151", "None"),
        "Under 152":markets.get("Under", {}).get("152", "None"),
        "Under 153":markets.get("Under", {}).get("153", "None"),
        "Under 154":markets.get("Under", {}).get("154", "None"),
        "Under 155":markets.get("Under", {}).get("155", "None"),
        "Under 156":markets.get("Under", {}).get("156", "None"),
        "Under 157":markets.get("Under", {}).get("157", "None"),
        "Under 158": markets.get("Under", {}).get("158", "None"),
        "Under 159": markets.get("Under", {}).get("159", "None"),
        "Under 160": markets.get("Under", {}).get("160", "None"),
        "Under 161": markets.get("Under", {}).get("161", "None"),
        "Under 162": markets.get("Under", {}).get("162", "None"),
        "Under 163": markets.get("Under", {}).get("163", "None"),
        "Under 164": markets.get("Under", {}).get("164", "None"),
        "Under 165": markets.get("Under", {}).get("165", "None"),
        "Under 166": markets.get("Under", {}).get("166", "None"),
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
        "1" : markets.get("1X2", {}).get("1", "None"),
        "2" : markets.get("1X2", {}).get("2", "None"),
        "Over 177": markets.get("Over", {}).get("177", "None"),
       "Over 177.5":markets.get("Over", {}).get("177.5", "None"),
       "Over 178":markets.get("Over", {}).get("178", "None"),
       "Over 178.5":markets.get("Over", {}).get("178.5", "None"),
       "Over 179":markets.get("Over", {}).get("179", "None"),
       "Over 179.5":markets.get("Over", {}).get("179.5", "None"),
       "Over 180":markets.get("Over", {}).get("180", "None"),
       "Over 180.5":markets.get("Over", {}).get("180.5", "None"),
       "Over 181": markets.get("Over", {}).get("181", "None"),
       "Over 181.5": markets.get("Over", {}).get("181.5", "None"),
       "Over 182": markets.get("Over", {}).get("182", "None"),
       "Over 182.5": markets.get("Over", {}).get("182.5", "None"),
       "Over 183": markets.get("Over", {}).get("183", "None"),
       "Over 183.5": markets.get("Over", {}).get("183.5", "None"),
       "Over 184": markets.get("Over", {}).get("184", "None"),
       "Over 184.5": markets.get("Over", {}).get("184.5", "None"),
       "Over 185": markets.get("Over", {}).get("185", "None"),
        "Over 150": markets.get("Over", {}).get("150", "None"),
        "Over 151":markets.get("Over", {}).get("151", "None"),
        "Over 152":markets.get("Over", {}).get("152", "None"),
        "Over 153":markets.get("Over", {}).get("153", "None"),
        "Over 154":markets.get("Over", {}).get("154", "None"),
        "Over 155":markets.get("Over", {}).get("155", "None"),
        "Over 156":markets.get("Over", {}).get("156", "None"),
        "Over 157":markets.get("Over", {}).get("157", "None"),
        "Over 158": markets.get("Over", {}).get("158", "None"),
        "Over 159": markets.get("Over", {}).get("159", "None"),
        "Over 160": markets.get("Over", {}).get("160", "None"),
        "Over 161": markets.get("Over", {}).get("161", "None"),
        "Over 162": markets.get("Over", {}).get("162", "None"),
        "Over 163": markets.get("Over", {}).get("163", "None"),
        "Over 164": markets.get("Over", {}).get("164", "None"),
        "Over 165": markets.get("Over", {}).get("165", "None"),
        "Over 166": markets.get("Over", {}).get("166", "None"),
        # Next Is Under        
        "Under 177": markets.get("Under", {}).get("177", "None"),
       "Under 177.5":markets.get("Under", {}).get("177.5", "None"),
       "Under 178":markets.get("Under", {}).get("178", "None"),
       "Under 178.5":markets.get("Under", {}).get("178.5", "None"),
       "Under 179":markets.get("Under", {}).get("179", "None"),
       "Under 179.5":markets.get("Under", {}).get("179.5", "None"),
       "Under 180":markets.get("Under", {}).get("180", "None"),
       "Under 180.5":markets.get("Under", {}).get("180.5", "None"),
       "Under 181": markets.get("Under", {}).get("181", "None"),
       "Under 181.5": markets.get("Under", {}).get("181.5", "None"),
       "Under 182": markets.get("Under", {}).get("182", "None"),
       "Under 182.5": markets.get("Under", {}).get("182.5", "None"),
       "Under 183": markets.get("Under", {}).get("183", "None"),
       "Under 183.5": markets.get("Under", {}).get("183.5", "None"),
       "Under 184": markets.get("Under", {}).get("184", "None"),
       "Under 184.5": markets.get("Under", {}).get("184.5", "None"),
       "Under 185": markets.get("Under", {}).get("185", "None"),
        "Under 150": markets.get("Under", {}).get("150", "None"),
        "Under 151":markets.get("Under", {}).get("151", "None"),
        "Under 152":markets.get("Under", {}).get("152", "None"),
        "Under 153":markets.get("Under", {}).get("153", "None"),
        "Under 154":markets.get("Under", {}).get("154", "None"),
        "Under 155":markets.get("Under", {}).get("155", "None"),
        "Under 156":markets.get("Under", {}).get("156", "None"),
        "Under 157":markets.get("Under", {}).get("157", "None"),
        "Under 158": markets.get("Under", {}).get("158", "None"),
        "Under 159": markets.get("Under", {}).get("159", "None"),
        "Under 160": markets.get("Under", {}).get("160", "None"),
        "Under 161": markets.get("Under", {}).get("161", "None"),
        "Under 162": markets.get("Under", {}).get("162", "None"),
        "Under 163": markets.get("Under", {}).get("163", "None"),
        "Under 164": markets.get("Under", {}).get("164", "None"),
        "Under 165": markets.get("Under", {}).get("165", "None"),
        "Under 166": markets.get("Under", {}).get("166", "None"),
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
        '1' : markets.get("1-2", {}).get("1", "None"),
        '2' : markets.get("1-2", {}).get("2", "None"),
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
        "1" : markets.get("1X2", {}).get("1", "None"),
        "2" : markets.get("1X2", {}).get("2", "None"),
        "Over 177": markets.get("Over", {}).get("177", "None"),
       "Over 177.5":markets.get("Over", {}).get("177.5", "None"),
       "Over 178":markets.get("Over", {}).get("178", "None"),
       "Over 178.5":markets.get("Over", {}).get("178.5", "None"),
       "Over 179":markets.get("Over", {}).get("179", "None"),
       "Over 179.5":markets.get("Over", {}).get("179.5", "None"),
       "Over 180":markets.get("Over", {}).get("180", "None"),
       "Over 180.5":markets.get("Over", {}).get("180.5", "None"),
       "Over 181": markets.get("Over", {}).get("181", "None"),
       "Over 181.5": markets.get("Over", {}).get("181.5", "None"),
       "Over 182": markets.get("Over", {}).get("182", "None"),
       "Over 182.5": markets.get("Over", {}).get("182.5", "None"),
       "Over 183": markets.get("Over", {}).get("183", "None"),
       "Over 183.5": markets.get("Over", {}).get("183.5", "None"),
       "Over 184": markets.get("Over", {}).get("184", "None"),
       "Over 184.5": markets.get("Over", {}).get("184.5", "None"),
       "Over 185": markets.get("Over", {}).get("185", "None"),
        "Over 150": markets.get("Over", {}).get("150", "None"),
        "Over 151":markets.get("Over", {}).get("151", "None"),
        "Over 152":markets.get("Over", {}).get("152", "None"),
        "Over 153":markets.get("Over", {}).get("153", "None"),
        "Over 154":markets.get("Over", {}).get("154", "None"),
        "Over 155":markets.get("Over", {}).get("155", "None"),
        "Over 156":markets.get("Over", {}).get("156", "None"),
        "Over 157":markets.get("Over", {}).get("157", "None"),
        "Over 158": markets.get("Over", {}).get("158", "None"),
        "Over 159": markets.get("Over", {}).get("159", "None"),
        "Over 160": markets.get("Over", {}).get("160", "None"),
        "Over 161": markets.get("Over", {}).get("161", "None"),
        "Over 162": markets.get("Over", {}).get("162", "None"),
        "Over 163": markets.get("Over", {}).get("163", "None"),
        "Over 164": markets.get("Over", {}).get("164", "None"),
        "Over 165": markets.get("Over", {}).get("165", "None"),
        "Over 166": markets.get("Over", {}).get("166", "None"),
        # Next Is Under        
        "Under 177": markets.get("Under", {}).get("177", "None"),
       "Under 177.5":markets.get("Under", {}).get("177.5", "None"),
       "Under 178":markets.get("Under", {}).get("178", "None"),
       "Under 178.5":markets.get("Under", {}).get("178.5", "None"),
       "Under 179":markets.get("Under", {}).get("179", "None"),
       "Under 179.5":markets.get("Under", {}).get("179.5", "None"),
       "Under 180":markets.get("Under", {}).get("180", "None"),
       "Under 180.5":markets.get("Under", {}).get("180.5", "None"),
       "Under 181": markets.get("Under", {}).get("181", "None"),
       "Under 181.5": markets.get("Under", {}).get("181.5", "None"),
       "Under 182": markets.get("Under", {}).get("182", "None"),
       "Under 182.5": markets.get("Under", {}).get("182.5", "None"),
       "Under 183": markets.get("Under", {}).get("183", "None"),
       "Under 183.5": markets.get("Under", {}).get("183.5", "None"),
       "Under 184": markets.get("Under", {}).get("184", "None"),
       "Under 184.5": markets.get("Under", {}).get("184.5", "None"),
       "Under 185": markets.get("Under", {}).get("185", "None"),
        "Under 150": markets.get("Under", {}).get("150", "None"),
        "Under 151":markets.get("Under", {}).get("151", "None"),
        "Under 152":markets.get("Under", {}).get("152", "None"),
        "Under 153":markets.get("Under", {}).get("153", "None"),
        "Under 154":markets.get("Under", {}).get("154", "None"),
        "Under 155":markets.get("Under", {}).get("155", "None"),
        "Under 156":markets.get("Under", {}).get("156", "None"),
        "Under 157":markets.get("Under", {}).get("157", "None"),
        "Under 158": markets.get("Under", {}).get("158", "None"),
        "Under 159": markets.get("Under", {}).get("159", "None"),
        "Under 160": markets.get("Under", {}).get("160", "None"),
        "Under 161": markets.get("Under", {}).get("161", "None"),
        "Under 162": markets.get("Under", {}).get("162", "None"),
        "Under 163": markets.get("Under", {}).get("163", "None"),
        "Under 164": markets.get("Under", {}).get("164", "None"),
        "Under 165": markets.get("Under", {}).get("165", "None"),
        "Under 166": markets.get("Under", {}).get("166", "None"),
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
        "1": markets.get("Winner", {}).get("1", "None"),
        "2": markets.get("Winner", {}).get("2", "None"),
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
        "1" : markets.get("1X2", {}).get("1", "None"),
        "2" : markets.get("1X2", {}).get("2", "None"),
        "Over 177": markets.get("Over", {}).get("177", "None"),
       "Over 177.5":markets.get("Over", {}).get("177.5", "None"),
       "Over 178":markets.get("Over", {}).get("178", "None"),
       "Over 178.5":markets.get("Over", {}).get("178.5", "None"),
       "Over 179":markets.get("Over", {}).get("179", "None"),
       "Over 179.5":markets.get("Over", {}).get("179.5", "None"),
       "Over 180":markets.get("Over", {}).get("180", "None"),
       "Over 180.5":markets.get("Over", {}).get("180.5", "None"),
       "Over 181": markets.get("Over", {}).get("181", "None"),
       "Over 181.5": markets.get("Over", {}).get("181.5", "None"),
       "Over 182": markets.get("Over", {}).get("182", "None"),
       "Over 182.5": markets.get("Over", {}).get("182.5", "None"),
       "Over 183": markets.get("Over", {}).get("183", "None"),
       "Over 183.5": markets.get("Over", {}).get("183.5", "None"),
       "Over 184": markets.get("Over", {}).get("184", "None"),
       "Over 184.5": markets.get("Over", {}).get("184.5", "None"),
       "Over 185": markets.get("Over", {}).get("185", "None"),
        "Over 150": markets.get("Over", {}).get("150", "None"),
        "Over 151":markets.get("Over", {}).get("151", "None"),
        "Over 152":markets.get("Over", {}).get("152", "None"),
        "Over 153":markets.get("Over", {}).get("153", "None"),
        "Over 154":markets.get("Over", {}).get("154", "None"),
        "Over 155":markets.get("Over", {}).get("155", "None"),
        "Over 156":markets.get("Over", {}).get("156", "None"),
        "Over 157":markets.get("Over", {}).get("157", "None"),
        "Over 158": markets.get("Over", {}).get("158", "None"),
        "Over 159": markets.get("Over", {}).get("159", "None"),
        "Over 160": markets.get("Over", {}).get("160", "None"),
        "Over 161": markets.get("Over", {}).get("161", "None"),
        "Over 162": markets.get("Over", {}).get("162", "None"),
        "Over 163": markets.get("Over", {}).get("163", "None"),
        "Over 164": markets.get("Over", {}).get("164", "None"),
        "Over 165": markets.get("Over", {}).get("165", "None"),
        "Over 166": markets.get("Over", {}).get("166", "None"),
        # Next Is Under        
        "Under 177": markets.get("Under", {}).get("177", "None"),
       "Under 177.5":markets.get("Under", {}).get("177.5", "None"),
       "Under 178":markets.get("Under", {}).get("178", "None"),
       "Under 178.5":markets.get("Under", {}).get("178.5", "None"),
       "Under 179":markets.get("Under", {}).get("179", "None"),
       "Under 179.5":markets.get("Under", {}).get("179.5", "None"),
       "Under 180":markets.get("Under", {}).get("180", "None"),
       "Under 180.5":markets.get("Under", {}).get("180.5", "None"),
       "Under 181": markets.get("Under", {}).get("181", "None"),
       "Under 181.5": markets.get("Under", {}).get("181.5", "None"),
       "Under 182": markets.get("Under", {}).get("182", "None"),
       "Under 182.5": markets.get("Under", {}).get("182.5", "None"),
       "Under 183": markets.get("Under", {}).get("183", "None"),
       "Under 183.5": markets.get("Under", {}).get("183.5", "None"),
       "Under 184": markets.get("Under", {}).get("184", "None"),
       "Under 184.5": markets.get("Under", {}).get("184.5", "None"),
       "Under 185": markets.get("Under", {}).get("185", "None"),
        "Under 150": markets.get("Under", {}).get("150", "None"),
        "Under 151":markets.get("Under", {}).get("151", "None"),
        "Under 152":markets.get("Under", {}).get("152", "None"),
        "Under 153":markets.get("Under", {}).get("153", "None"),
        "Under 154":markets.get("Under", {}).get("154", "None"),
        "Under 155":markets.get("Under", {}).get("155", "None"),
        "Under 156":markets.get("Under", {}).get("156", "None"),
        "Under 157":markets.get("Under", {}).get("157", "None"),
        "Under 158": markets.get("Under", {}).get("158", "None"),
        "Under 159": markets.get("Under", {}).get("159", "None"),
        "Under 160": markets.get("Under", {}).get("160", "None"),
        "Under 161": markets.get("Under", {}).get("161", "None"),
        "Under 162": markets.get("Under", {}).get("162", "None"),
        "Under 163": markets.get("Under", {}).get("163", "None"),
        "Under 164": markets.get("Under", {}).get("164", "None"),
        "Under 165": markets.get("Under", {}).get("165", "None"),
        "Under 166": markets.get("Under", {}).get("166", "None"),
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
        "1": markets.get("Winner", {}).get("1", "None"),
        "2": markets.get("Winner", {}).get("2", "None"),

        "Over 117.5": markets.get("Under/Over 117.5 points", {}).get("Over 117.5 points", "None"),
        "Under 117.5": markets.get("Under/Over 117.5 points", {}).get("Under 117.5 points", "None"),

        "Over 118.5": markets.get("Under/Over 118.5 points", {}).get("Over 118.5 points", "None"),
        "Under 118.5": markets.get("Under/Over 118.5 points", {}).get("Under 118.5 points", "None"),

        "Over 119.5": markets.get("Under/Over 119.5 points", {}).get("Over 119.5 points", "None"),
        "Under 119.5": markets.get("Under/Over 119.5 points", {}).get("Under 119.5 points", "None"),

        "Over 120.5": markets.get("Under/Over 120.5 points", {}).get("Over 120.5 points", "None"),
        "Under 120.5": markets.get("Under/Over 120.5 points", {}).get("Under 120.5 points", "None"),

        "Over 121.5": markets.get("Under/Over 121.5 points", {}).get("Over 121.5 points", "None"),
        "Under 121.5": markets.get("Under/Over 121.5 points", {}).get("Under 121.5 points", "None"),

        "Over 121.5": markets.get("Under/Over 121.5 points", {}).get("Over 121.5 points", "None"),
        "Under 121.5": markets.get("Under/Over 121.5 points", {}).get("Under 121.5 points", "None"),

        "Over 123.5": markets.get("Under/Over 123.5 points", {}).get("Over 123.5 points", "None"),
        "Under 123.5": markets.get("Under/Over 123.5 points", {}).get("Under 123.5 points", "None"),

        "Over 124.5": markets.get("Under/Over 124.5 points", {}).get("Over 124.5 points", "None"),
        "Under 124.5": markets.get("Under/Over 124.5 points", {}).get("Under 124.5 points", "None"),

        "Over 125.5": markets.get("Under/Over 125.5 points", {}).get("Over 125.5 points", "None"),
        "Under 125.5": markets.get("Under/Over 125.5 points", {}).get("Under 125.5 points", "None"),

        "Over 126.5": markets.get("Under/Over 126.5 points", {}).get("Over 126.5 points", "None"),
        "Under 126.5": markets.get("Under/Over 126.5 points", {}).get("Under 126.5 points", "None"),

        "Over 127.5": markets.get("Under/Over 127.5 points", {}).get("Over 127.5 points", "None"),
        "Under 127.5": markets.get("Under/Over 127.5 points", {}).get("Under 127.5 points", "None"),

        "Over 128.5": markets.get("Under/Over 128.5 points", {}).get("Over 128.5 points", "None"),
        "Under 128.5": markets.get("Under/Over 128.5 points", {}).get("Under 128.5 points", "None"),

        "Over 129.5": markets.get("Under/Over 129.5 points", {}).get("Over 129.5 points", "None"),
        "Under 129.5": markets.get("Under/Over 129.5 points", {}).get("Under 129.5 points", "None"),

        "Over 130.5": markets.get("Under/Over 130.5 points", {}).get("Over 130.5 points", "None"),
        "Under 130.5": markets.get("Under/Over 130.5 points", {}).get("Under 130.5 points", "None"),
        
        "Over 131.5": markets.get("Under/Over 131.5 points", {}).get("Over 131.5 points", "None"),
        "Under 131.5": markets.get("Under/Over 131.5 points", {}).get("Under 131.5 points", "None"),

        "Over 132.5": markets.get("Under/Over 132.5 points", {}).get("Over 132.5 points", "None"),
        "Under 132.5": markets.get("Under/Over 132.5 points", {}).get("Under 132.5 points", "None"),

        "Over 133.5": markets.get("Under/Over 133.5 points", {}).get("Over 133.5 points", "None"),
        "Under 133.5": markets.get("Under/Over 133.5 points", {}).get("Under 133.5 points", "None"),

        "Over 134.5": markets.get("Under/Over 134.5 points", {}).get("Over 134.5 points", "None"),
        "Under 134.5": markets.get("Under/Over 134.5 points", {}).get("Under 134.5 points", "None"),

        "Over 135.5": markets.get("Under/Over 135.5 points", {}).get("Over 135.5 points", "None"),
        "Under 135.5": markets.get("Under/Over 135.5 points", {}).get("Under 135.5 points", "None"),

        "Over 136.5": markets.get("Under/Over 136.5 points", {}).get("Over 136.5 points", "None"),
        "Under 136.5": markets.get("Under/Over 136.5 points", {}).get("Under 136.5 points", "None"),

        "Over 137.5": markets.get("Under/Over 137.5 points", {}).get("Over 137.5 points", "None"),
        "Under 137.5": markets.get("Under/Over 137.5 points", {}).get("Under 137.5 points", "None"),

        "Over 138.5": markets.get("Under/Over 138.5 points", {}).get("Over 138.5 points", "None"),
        "Under 138.5": markets.get("Under/Over 138.5 points", {}).get("Under 138.5 points", "None"),

        "Over 139.5": markets.get("Under/Over 139.5 points", {}).get("Over 139.5 points", "None"),
        "Under 139.5": markets.get("Under/Over 139.5 points", {}).get("Under 139.5 points", "None"),

        "Over 140.5": markets.get("Under/Over 140.5 points", {}).get("Over 140.5 points", "None"),
        "Under 140.5": markets.get("Under/Over 140.5 points", {}).get("Under 140.5 points", "None"),

        "Over 141.5": markets.get("Under/Over 141.5 points", {}).get("Over 141.5 points", "None"),
        "Under 141.5": markets.get("Under/Over 141.5 points", {}).get("Under 141.5 points", "None"),

        "Over 142.5": markets.get("Under/Over 142.5 points", {}).get("Over 142.5 points", "None"),
        "Under 142.5": markets.get("Under/Over 142.5 points", {}).get("Under 142.5 points", "None"),

        "Over 143.5": markets.get("Under/Over 143.5 points", {}).get("Over 143.5 points", "None"),
        "Under 143.5": markets.get("Under/Over 143.5 points", {}).get("Under 143.5 points", "None"),

        "Over 144.5": markets.get("Under/Over 144.5 points", {}).get("Over 144.5 points", "None"),
        "Under 144.5": markets.get("Under/Over 144.5 points", {}).get("Under 144.5 points", "None"),

        "Over 145.5": markets.get("Under/Over 145.5 points", {}).get("Over 145.5 points", "None"),
        "Under 145.5": markets.get("Under/Over 145.5 points", {}).get("Under 145.5 points", "None"),
    } 
    return found_markets


special_functions = {
    "1xbet" : extract_xbet_markets,
    "22bet" : extract_bet22_markets,
    "betking": extract_betking_markets,
    "betwinner": extract_betwinner_markets,
    "merrybet": extract_merrybet_markets,
    "paripesa": extract_paripesa_markets,
    "sportybet": extract_sportybet_markets
}

def process_volleyball(sport_file_path):
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
                        log_error(f" No special extraction function for this {bookie}.",)
                except Exception as e:
                    message = f"{e}"
                    log_exception(f"Error Extracting markets for {bookie} game name: {game}",)  
    return all_markets   
