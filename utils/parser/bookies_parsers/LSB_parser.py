#!/usr/bin/python
"""
    This Module contains all the functions for LiveScoreBet data parsing and cleaning
    Author: Peter Ekwere
"""
import sys
from datetime import datetime
import re
from utils.logger.log import log_exception
sys.path.append("..") 

def split_team_names(team_names):
            the_list = [name.strip() for name in team_names.split('vs')]
            if len(the_list) == 2:
                return the_list
            elif len(the_list) > 2:
                return the_list[0], the_list[1]
            else:
                return the_list[0], "split function returned only one team name" 

"""
def replace_outcome_name(outcome_name, home_team, away_team):
    # Define replacement patterns
    patterns = {
        f"{home_team} or draw": "1X",
        f"{home_team} or {away_team}": "12",
        f"draw or {away_team}": "X2",
        f"{home_team}": "1",
        f"{away_team}": "2",
        "draw": "X",
        "Draw 0-0": "0-0"
    }

    # Apply replacements using regular expressions
    for pattern, replacement in patterns.items():
        outcome_name = re.sub(re.escape(pattern), replacement, outcome_name, flags=re.IGNORECASE)

    return outcome_name
"""


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
                
                try:
                    home_team, away_team = split_team_names(game_name)
                except ValueError as e:
                    # Handle the case where split_team_names returns more than two values
                    log_exception(f"Error splitting team names In livescorebet home_team and away_team now set to None: {e}")
                    home_team = away_team = None
                
                for outcome in outcomes:
                    outcome_name = outcome.get("name", "Error getting name")
                    outcome_odd = outcome.get("odds")
                
                    outcome_name = outcome_name.replace(f"{home_team} or Tie", "1X") \
                                    .replace(f"{home_team} or {away_team}", "12") \
                                    .replace(f"Tie or {away_team}", "X2")\
                                    .replace(f"{home_team}", "1")\
                                    .replace(f"{away_team}", "2")\
                                    .replace(f"Draw", "X")
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