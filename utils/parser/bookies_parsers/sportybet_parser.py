#!/usr/bin/python
"""
    This Module contains all the functions for Sportybet data parsing and cleaning
    Author: Peter Ekwere
"""
import sys
from datetime import datetime
sys.path.append("..") 

def convert_market_data(old_data):
    result_dict = {}
    data = old_data.get("data")
    games = data.get("tournaments", [])[0].get("events", [])
    if games:
        for game in games:
            home_team = game.get("homeTeamName")
            away_team = game.get("awayTeamName")
            game_name = f"{home_team} vs {away_team}"
            markets = game.get("markets", [])
            for market in markets:
                market_name = market.get("desc")
                outcomes = market.get("outcomes", [])

                if game_name not in result_dict:
                    result_dict[game_name] = {}
                if market_name not in result_dict[game_name]:
                    result_dict[game_name][market_name] = {}

                for outcome in outcomes:
                    outcome_name = outcome.get("desc")
                    outcome_odd = float(outcome.get("odds"))
                     
                    outcome_name = outcome_name.replace("Home or Draw", "1X") \
                                        .replace(f"Home or Away", "12") \
                                        .replace(f"Draw or Away", "X2")\
                                        .replace("Home", "1")\
                                        .replace(f"Away", "2")\
                                        .replace(f"Draw", "X")
                    if outcome_name not in result_dict[game_name][market_name]:
                        result_dict[game_name][market_name][outcome_name] = outcome_odd

    return result_dict

def extract_Sportybet(json_data):
        """ This Method Handles the extracting of needed Data(games, odds, markets) from a 1xbet response

        Args:
            json_data (list): This is the json data returned from the betking API 
        """
        result_dict = convert_market_data(json_data)
        #league_name = old_data.get("data", {}).get("sport", {}).get("category", {}).get("name", "Unknown")
        league_name = json_data.get("data", {}).get("tournaments", {})[0].get("name", "Could not get league name")       #output_dict = {
            #league_name: result_dict
        #}

        return result_dict, league_name
        