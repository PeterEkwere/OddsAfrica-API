#!/usr/bin/python
"""
    This Module contains all the functions for nairabet data parsing and cleaning
    Author: Peter Ekwere
"""
import sys
import json
from datetime import datetime
sys.path.append("..") 


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
            print(f"time is {time}")
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
                        
                        for outcome in market.get("outcomes", []):
                            outcome_name = outcome.get("name")
                            odds = outcome.get("value")
                        
                            if "time" not in result_dict[league][game_name]:
                                result_dict[league][game_name]["time"] = 1 #start_time
                            if outcome_name not in result_dict[league][game_name][market_name]:
                                result_dict[league][game_name][market_name][outcome_name] = odds
                        
        return result_dict