#!/usr/bin/python
"""
    This Module will hold funcitions for extracting and arranging the needed markets  for darts cross market arb
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
            "1" : markets.get("1X2", {}).get("1"),
            "2" : markets.get("1X2", {}).get("2")
    } 
    return found_markets

def extract_bet22_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    
    found_markets = {
            "1" : markets.get("1X2", {}).get("1"),
            "2" : markets.get("1X2", {}).get("2")
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
            "1" : markets.get("1X2", {}).get("1"),
            "2" : markets.get("1X2", {}).get("2")
    }
    return found_markets

def extract_merrybet_markets(markets):
    """ This Function  Extracts the needed markets in respect to the formula library

    Args:
        markets (dicts): This is are the markets on 1xbet that are present for the corresponding game
    """
    found_markets = {}
    
    found_markets = {
        "1" : markets.get("Winner", {}).get("1"),
        "2" : markets.get("Winner", {}).get("2") 
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
            "1" : markets.get("1X2", {}).get("1"),
            "2" : markets.get("1X2", {}).get("2")
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
            "1" : markets.get("Winner", {}).get("1"),
            "2" : markets.get("Winner", {}).get("2")
    } 
    return found_markets


special_functions = {
    "1xbet" : extract_xbet_markets,
    "22bet" : extract_bet22_markets,
    "betwinner": extract_betwinner_markets,
    "livescorebet": extract_livescorebet_markets,
    "merrybet": extract_merrybet_markets,
    "paripesa": extract_paripesa_markets,
}

def process_darts(sport_file_path):
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
