#!/usr/bin/python
"""
    This Module contains all the functions for Betking data parsing and cleaning
    Author: Peter Ekwere
"""
import sys
from datetime import datetime
sys.path.append("..") 


def extract_betking(json_data):
        """ This Method Handles the extracting of needed Data(games, odds, markets) from a 1xbet response

        Args:
            json_data (list): This is the json data returned from the betking API 
        """
        result_dict = {}
        league = None
        for data in json_data:
            AM = data.get("AM", [])
            if AM:
                game = AM[0].get("IT")
                game_name = game[0].get("IN")
                league = game[0].get("TN", "Invalid league name")
                markets = game[0].get("OC", [])
                for market in markets:
                    outcome_dict = {}
                    market_name = market.get("OT", {}).get("ON", "NULL")
                    outcomes = market.get("MO", [])
                    for outcome in outcomes:
                        outcome_name = outcome.get("OA").get("ON")
                        outcome_odd = outcome.get("OT").get("OO")
                        outcome_dict[outcome_name]  = outcome_odd
                    if game_name not in result_dict:
                        result_dict[game_name] = {}
                    if market_name not in result_dict[game_name]:
                        result_dict[game_name][market_name] = {}
                    
                    result_dict[game_name][market_name] = outcome_dict
        return result_dict, league