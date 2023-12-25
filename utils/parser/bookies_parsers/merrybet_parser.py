#!/usr/bin/python
"""
    This Module contains all the functions for merrybet data parsing and cleaning
    Author: Peter Ekwere
"""
import sys
import json
from datetime import datetime
sys.path.append("..") 


def extract_merrybet(json_data):
        """ This Method Handles the extracting of needed Data(games, odds, markets) from a merrybet api response

        Args:
            json_data (dict): This is the json data returned from the merrybet API 
        """
        def split_team_names(team_names):
            return [name.strip() for name in team_names.split('-')]
        
        result_dict = {}
        data = json_data
        for game in data["data"]:
            league = game["category3Name"]
            gamename = game["eventName"]
            #time = game.get("eventStart", None)
            #start_time = #datetime.utcfromtimestamp(time)
            start_time = "" #start_time.strftime("%Y-%m-%d %H:%M:%S")
            for markets in game["eventGames"]:
                market = markets["gameName"]
                if market not in result_dict.get(league, {}).get(gamename, {}):
                    result_dict.setdefault(league, {}).setdefault(gamename, {}).setdefault(market, {})
                home_team, away_team = split_team_names(gamename)
                for outcomes in markets["outcomes"]:
                    outcome_name = outcomes["outcomeName"]
                    odds = outcomes["outcomeOdds"]
                    
                    outcome_name = outcome_name.replace(f"{home_team} or draw", "1X") \
                                        .replace(f"{home_team} or {away_team}", "12") \
                                        .replace(f"draw or {away_team}", "X2")\
                                        .replace(f"{home_team}", "1")\
                                        .replace(f"{away_team}", "2")\
                                        .replace(f"draw", "X")
                    if "time" not in result_dict[league][gamename]:
                        result_dict[league][gamename]["time"] = start_time
                    if outcome_name not in result_dict[league][gamename][market]:
                        result_dict[league][gamename][market][outcome_name] = {}

                    result_dict[league][gamename][market][outcome_name] = odds
                    
        return result_dict
                    
                    #if league not in result_dict:
                        #result_dict[league] = {}
                    #if gamename not in result_dict[league]:
                        #result_dict[league][gamename] = {}
                    #if "time" not in result_dict[league][gamename]:
                        #result_dict[league][gamename]["time"] = start_time
                    #home_team, away_team = split_team_names(gamename)
                    #outcome_name = outcome_name.replace(f"{home_team} or draw", "1X") \
                                        #.replace(f"{home_team} or {away_team}", "12") \
                                        #.replace(f"draw or {away_team}", "X2")
                    #if market not in result_dict[league][gamename]:
                        #result_dict[league][gamename][market] = {}
                    #if outcome_name not in result_dict[league][gamename][market]:
                        #result_dict[league][gamename][market][outcome_name] = {}
                    #result_dict[league][gamename][market][outcome_name] = odds