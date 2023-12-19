#!/usr/bin/python
"""
    This Module contains all the functions for 1xbet/paripesa/22bet/frapapa data parsing and cleaning
    Author: Peter Ekwere
"""
import sys
from datetime import datetime
sys.path.append("..") 


def extract_22bet(data):
        """ This Method Handles the extracting of needed Data(games, odds, markets) from a 1xbet response

        Args:
            json_data (dict): This is the json data returned from the 1xbet API 
        """
        result_dict = {}
        for json_data in data:
            a_game_dict  = json_data.get('Value', {})
            team_1 = a_game_dict.get('O1', "")
            team_2 = a_game_dict.get('O2', "")
            game = f"{team_1} VS {team_2}"
                    
            if "L" in a_game_dict:
                country_name, league = a_game_dict["L"].split(maxsplit=1) if " " in a_game_dict["L"] else (None, a_game_dict["L"])
            else:
                country_name, league = (None, None)
                        
            timestamp = a_game_dict.get("S", 0)
            start_time = datetime.utcfromtimestamp(timestamp)
            start_time = start_time.strftime("%Y-%m-%d %H:%M:%S")

            for all_markets in a_game_dict.get("GE", []):

                    for market in all_markets.get("E", []):
                        market_id = all_markets.get("G", 0)
                        for a_dict in market:
                            odds = a_dict.get("C", 0)
                            outcome_id = a_dict.get("T", 0)
                            goal_line = a_dict.get("P", 0)

                            if market_id == 3:
                                # Handicap market
                                market_name = "Handicap Home" if outcome_id == 7 else "Handicap Away"
                                outcome_name = f"{goal_line}"
                            elif market_id == 4:
                                # Over/Under Market
                                market_name = "Over" if outcome_id == 9 else "Under"
                                outcome_name = f"{goal_line}"
                            elif market_id == 1008:
                                # Asian Handicap market
                                market_name = "AH Home" if outcome_id == 3829 else "AH Away"
                                outcome_name = f"{goal_line}"
                            elif market_id == 1007:
                                # Asian Over/under market
                                market_name = "Asian Over" if outcome_id ==  3827 else "Asian under"
                                outcome_name = f"{goal_line}"
                            else:
                                outcome_name = "Don't Know The Outcome"
                                market_name = "Dont Know market name"

                            
                            if game not in result_dict:
                                result_dict[game] = {}
                            if "time" not in result_dict[game]:
                                result_dict[game]["time"] = {}
                            if market_name not in result_dict[game]:
                                result_dict[game][market_name] = {}
                            if outcome_name not in result_dict[game][market_name]:
                                result_dict[game][market_name][outcome_name] = {}
                            result_dict[game][market_name][outcome_name] = odds
                            result_dict[game]["time"] = start_time

                    for all_markets in a_game_dict.get("GE", []):

                        for market in all_markets.get("E", []):
                            market_id = all_markets.get("G", 0)
                            for a_dict in market:
                                    odds = a_dict.get("C", 0)
                                    market_id = a_dict.get("G", 0)
                                    outcome_id = a_dict.get("T", 0)

                                    if market_id == 1:
                                        market_name = "1X2"
                                        if outcome_id == 1:
                                            outcome_name = "1"
                                        elif outcome_id == 2:
                                            outcome_name = "X"
                                        elif outcome_id == 3:
                                            outcome_name = "2"
                                    elif market_id == 21:
                                        market_name = "GG/NG"
                                        outcome_name = "GG" if outcome_id == 180 else "NG"
                                    elif market_id == 2:
                                        market_name = "Double Chance"
                                        if outcome_id == 4:
                                            outcome_name = "1X"
                                        elif outcome_id == 5:
                                            outcome_name = "12"
                                        elif outcome_id == 6:
                                            outcome_name = "2X"
                                    else:
                                        pass

                                    if outcome_id in [1, 2, 3, 4, 5, 6, 180, 181]:
                                        if game not in result_dict:
                                            result_dict[game] = {}
                                        if market_name not in result_dict[game]:
                                            result_dict[game][market_name] = {}
                                        if outcome_name not in result_dict[game][market_name]:
                                            result_dict[game][market_name][outcome_name] = {}
                                        result_dict[game][market_name][outcome_name] = odds

        return result_dict, league