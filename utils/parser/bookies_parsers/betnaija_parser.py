#!/usr/bin/python
"""
    This Module contains all the functions for bet9ja data parsing and cleaning
    Author: Peter Ekwere
"""
import sys
import json
from datetime import datetime
sys.path.append("..") 


def extract_bet9ja(json_data):
        """ This Method Handles the extracting of needed Data(games, odds, markets) from a bet9ja api response

        Args:
            json_data (dict): This is the json data returned from the nairabet API 
        """
        data = json_data
        games = {}

        for match in data["D"]["E"]:
            time = match["STARTDATE"],
            time = str(time)
            game_name = match["DS"],
            game_name = str(game_name)
            league_name = match["GN"]
            markts =  {}

            if league_name not in games:
                games[league_name] = {}
            if game_name not in games[league_name]:
                games[league_name][game_name] = {}
            if "time" not in games[league_name][game_name]:
                games[league_name][game_name]["time"] = str(time) 
            for market_type, market_data in match["O"].items():
                market_name = market_type.replace("S_", "").replace("@", "_")
                market_name = market_name.replace("1X2_", "").replace("DC_", "").replace("OU_", "")
                if market_name not in games[league_name][game_name]:
                    games[league_name][game_name][market_name] = market_data
                    
        return games