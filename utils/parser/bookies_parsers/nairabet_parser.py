#!/usr/bin/python
"""
    This Module contains all the functions for nairabet data parsing and cleaning
    Author: Peter Ekwere
"""
from utils.logger.log import log_exception
import sys
import json
from datetime import datetime
sys.path.append("..") 


def split_team_names(team_names):
            the_list = [name.strip() for name in team_names.split('vs')]
            if len(the_list) == 2:
                return the_list
            elif len(the_list) > 2:
                return the_list[0], the_list[1]
            else:
                return the_list[0], "split function returned only one team name" 

def extract_nairabet(json_data):
        """ This Method Handles the extracting of needed Data(games, odds, markets) from a nairabet api response

        Args:
            json_data (dict): This is the json data returned from the nairabet API 
        """
        result_dict = {} 
        for data  in json_data:
            game_list = data.get("eventNames", [])
            game_name = f"{game_list[0]} vs {game_list[1]}"
            time = data.get("startTime", None)
            time_sec = time / 1000
            start_time = datetime.utcfromtimestamp(time_sec)
            start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
            country = data.get("categoryName", None)
            league = data.get("competitionName", None)

            # Iterate over market groups
            for market_group in data.get("marketGroups", []):

                # Iterate over markets within the market group
                for market in market_group["markets"]:
                        market_name = market.get("entityName")
                        if market_name not in result_dict.get(league, {}).get(game_name, {}):
                            result_dict.setdefault(league, {}).setdefault(game_name, {}).setdefault(market_name, {})
                        
                        try:
                            home_team, away_team = split_team_names(game_name)
                        except ValueError as e:
                            # Handle the case where split_team_names returns more than two values
                            log_exception(f"Error splitting team names In nairabet home_team and away_team now set to None: {e}")
                        for outcome in market.get("outcomes", []):
                            outcome_name = outcome.get("name")
                            odds = outcome.get("value")

                            outcome_name = outcome_name.replace(f"{home_team} or draw", "1X") \
                                        .replace(f"{home_team} or {away_team}", "12") \
                                        .replace(f"draw or {away_team}", "X2")\
                                        .replace(f"{home_team}", "1")\
                                        .replace(f"{away_team}", "2")\
                                        .replace(f"draw", "X")\
                                        .replace("Draw 0-0", "0-0")
                            
                            if "time" not in result_dict[league][game_name]:
                                result_dict[league][game_name]["time"] = start_time
                            if outcome_name not in result_dict[league][game_name][market_name]:
                                result_dict[league][game_name][market_name][outcome_name] = odds
                        
        return result_dict