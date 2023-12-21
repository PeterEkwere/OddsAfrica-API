#!/usr/bin/python
"""
    This Module contains all the functions for LiveScoreBet data parsing and cleaning
    Author: Peter Ekwere
"""
import sys
from datetime import datetime
sys.path.append("..") 


def extract_LSB(json_data):
        """ This Method Handles the extracting of needed Data(games, odds, markets) from a 1xbet response

        Args:
            json_data (list): This is the json data returned from the betking API 
        """
        result_dict = {}
        event = json_data.get("events", {})
        main_data = event.get("categories", [])[0]
        league = main_data.get("name")
        games = main_data.get("events", [])
        for game in games:
            time = game.get("startTime", "00:00")
            game_name = game.get("name", "Error getting Name")
            game_markets = game.get("markets", [])
            for market in game_markets:
                outcome_dict = {}
                market_name = market.get("name", "Error getting market name")
                outcomes = market.get("selections", [])
                for outcome in outcomes:
                    outcome_name = outcome.get("name", "Error getting name")
                    outcome_odd = outcome.get("odds")
                    outcome_dict[outcome_name] = outcome_odd
                

                if game_name not in result_dict:
                    result_dict[game_name] = {}
                if "time" not in result_dict[game_name]:
                    result_dict[game_name]["time"] = time
                if market_name not in result_dict[game_name]:
                    result_dict[game_name][market_name] = {}
                if outcome_name not in result_dict[game_name][market_name]:
                    result_dict[game_name][market_name][outcome_name] = {}
                result_dict[game_name][market_name] = outcome_dict
                
        return result_dict, league