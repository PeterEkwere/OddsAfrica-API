#!/usr/bin/python
"""
    This Module contains all the functions for 1xbet/paripesa/22bet/frapapa data parsing and cleaning
    Author: Peter Ekwere
"""
import sys
from datetime import datetime
sys.path.append("..") 


def extract(json_data):
        """ This Method Handles the extracting of needed Data(games, odds, markets) from a 1xbet response

        Args:
            json_data (dict): This is the json data returned from the 1xbet API 
        """
        result_dict = {}
        
        for a_game_dict in json_data['Value']:
            team_1 = a_game_dict["O1"]
            team_2 = a_game_dict["O2"]
            game = f"{team_1} VS {team_2}"
            if "L" in a_game_dict:
                country_name, league = a_game_dict["L"].split(maxsplit=1) if " " in a_game_dict["L"] else (None, a_game_dict["L"])
            else:
                country_name, league = (None, None)
            timestamp = a_game_dict["S"]
            start_time = datetime.utcfromtimestamp(timestamp)
            start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")
            for entry in a_game_dict.get("AE", []):
                entries = entry["ME"]

                for a_market_entry in entries:
                    odds = a_market_entry["C"]
                    market_id = a_market_entry["G"]
                    outcome_id = a_market_entry["T"]

                    if market_id == 2:
                        # Handicap market
                        market = "Handicap"
                        if "P" in a_market_entry:
                            handicap_value = a_market_entry["P"]
                            outcome_name = f"{handicap_value}"
                        else:
                            outcome_name = "NO Line"
                    elif market_id == 17:
                        # Over/ Under Market
                        if "P" in a_market_entry:
                            goal_line = a_market_entry["P"]
                            if outcome_id == 9:
                                market = "Over"
                                outcome_name = f"{goal_line}"
                            elif outcome_id == 10:
                                market = "Under"
                                outcome_name = f"{goal_line}"
                            else:
                                pass
                    else:
                        Outcome_name = "Don't Know The Outcome"
                        print("I will handle this condition later")

                    if league not in result_dict:
                        result_dict[league] = {}
                    if game not in result_dict[league]:
                        result_dict[league][game] = {}
                    if "time" not in result_dict[league][game]:
                        result_dict[league][game]["time"] = {}
                    if market not in result_dict[league][game]:
                        result_dict[league][game][market] = {}
                    if outcome_name not in result_dict[league][game][market]:
                        result_dict[league][game][market][outcome_name] = {}
                    result_dict[league][game][market][outcome_name] = odds
                    result_dict[league][game]["time"] = start_time

            for entry in a_game_dict.get("E", []):
                odds = entry["C"]
                market_id = entry["G"]
                Outcome_id = entry["T"]

                if market_id == 1:
                    market = "1X2"
                    if Outcome_id == 1:
                        Outcome_name = "1"
                    elif Outcome_id == 2:
                        Outcome_name = "X"
                    elif Outcome_id == 3:
                        Outcome_name = "2"
                    else:
                        pass
                elif market_id == 19:
                    market = "GG/NG"
                    if Outcome_id == 180:
                        Outcome_name = "GG"
                    elif Outcome_id == 181:
                        Outcome_name = "NG"
                    else:
                        pass
                elif market_id == 8:
                    market = "Double Chance"
                    if Outcome_id == 4:
                        Outcome_name = "1X"
                    elif Outcome_id == 5:
                        Outcome_name = "12"
                    elif Outcome_id == 6:
                        Outcome_name = "2X"
                    else:
                        pass
                else:
                    pass

                if Outcome_id in [1, 2, 3, 4, 5, 6, 180, 181]:
                    if league not in result_dict:
                        result_dict[league] = {}
                    if game not in result_dict[league]:
                        result_dict[league][game] = {}
                    if market not in result_dict[league][game]:
                        result_dict[league][game][market] = {}
                    if Outcome_name not in result_dict[league][game][market]:
                        result_dict[league][game][market][Outcome_name] = {}
                    result_dict[league][game][market][Outcome_name] = odds
                    
        return result_dict
