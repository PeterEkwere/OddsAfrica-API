#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from engine.bookie_models.bet22_model import bet22
import requests
import json
from difflib import SequenceMatcher
import requests
from datetime import datetime
from utils.parser.bookies_parsers.xbet_parser import extract

#def str_similarity(a, b):
	#return SequenceMatcher(None, a, b).ratio()


#result = str_similarity("Everton - Chelsea FC", "Everton VS Chelsea")
#print(result)

Today = bet22()
sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey"]
for sport in sports:
    league_games = Today.Get_games(sport)
"""
def extract(json_data):
    result_dict = {}
    
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
                        print("I will handle this condition later")

                    
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

league_url = "https://22bet.ng/LineFeed/Get1x2_VZip?sports=1&champs=88637&count=50&lng=en&tz=1&mode=4&country=132&partner=151&getEmpty=true&gr=502"
leagues = requests.get(league_url)
json_data = leagues.json()
game_ids = [game.get("CI") for game in json_data.get("Value", [])]
print(f"game ids are {game_ids}")
new_data_list = []
data_list = []
result_dict = {}
for game_id in game_ids:
    # Fetch data for each game ID
    url = f"https://22bet.ng/LineFeed/GetGameZip?id={game_id}&lng=en&tzo=1&isSubGames=true&GroupEvents=true&countevents=100&partner=151&grMode=2&country=132&fcountry=132&marketType=1&mobi=true"
    res = requests.get(url)
    data = res.json()
    data_list.append(data)
    new_data, league = extract(data)
    new_data_list.append(new_data)

result_dict[league] = new_data_list
# Write data to "extracted.json"
with open("extracted.json", "w") as file:
    json.dump(data_list, file, indent=2)

with open("clean_data.json", "w") as file:
    json.dump(result_dict, file, indent=2)
    
"""