#!/usr/bin/python
"""
    This Module contains all the functions for betpawa data parsing and cleaning
    Author: Peter Ekwere
"""
import sys
from datetime import datetime
sys.path.append("..") 

def convert_market_data(old_data):
    data = old_data
    result_dict = {}
    for game in data:
        game_name = game.get("name", "Unable to get name")
        startTime = game.get("startTime", "Unable to get start time")
        markets = game.get("markets", [])
        for market in markets:
            outcome_dict = {}
            market_name = market.get("marketType").get("name")
            market_id = market.get("marketType").get("id")
            outcomes = market.get("prices")
            
            if game_name not in result_dict:
                result_dict[game_name] = {}
            if market_name not in result_dict[game_name]:
                result_dict[game_name][market_name] = {}
            for outcome in outcomes:
                outcome_name = outcome.get("name")
                outcome_odd = outcome.get("price")
                outcome_dict[outcome_name] = outcome_odd
                
                if outcome_name not in result_dict[game_name][market_name]:
                    result_dict[game_name][market_name] = outcome_dict 
                
    return result_dict

def extract_betpawa(json_data):
        """ This Method Handles the extracting of needed Data(games, odds, markets) from a betpawa response

        Args:
            json_data (list): This is the json data returned from the betpawa API 
        """
        result_dict = convert_market_data(json_data)
        #league_name = old_data.get("data", {}).get("sport", {}).get("category", {}).get("name", "Unknown")
        #league_name = json_data.get("data", {}).get("tournaments", {})[0].get("name", "Could not get league name")       #output_dict = {
            #league_name: result_dict
        #}

        return result_dict
        