#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from engine.bookie_models.sportybet_model import SportyBet
import requests
import json
from difflib import SequenceMatcher
import requests
from datetime import datetime
from utils.parser.bookies_parsers.sportybet_parser import extract_Sportybet
from engine.bookie_models.sportybet_model import SportyBet

#def str_similarity(a, b):
	#return SequenceMatcher(None, a, b).ratio()


#result = str_similarity("Everton - Chelsea FC", "Everton VS Chelsea")
#print(result)

Today = SportyBet()
sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey"]
for sport in sports:
    Today.Get_games(sport)

"""
headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-GPC': '1',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.sportybet.com/ng/sport/',
        'Accept-Language': 'en-EN,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'lng=en; flaglng=en; is_rtl=1; fast_coupon=true; v3tr=1; typeBetNames=full; auid=BbblOWFXM1ESU8VHB/1dAg==; sh.session_be98639c=04c362af-da44-4e0e-a384-ca2529fa5712; SESSION=4d9c3757128519eb87309f34d670d560; visit=1-378d9869df866ea72e6818eb52cb9af1; coefview=0; blocks=1%2C1%2C1%2C1%2C1%2C1%2C1%2C1; completed_user_settings=true; ggru=160; right_side=right; pushfree_status=canceled; _glhf=1633191759'
       } """
#data = SportyBet.get_games_market("sr:sport:1", "sr:tournament:17", headers)
#payload = {"tournamentId":[["sr:tournament:17"]],"productId":3,"sportId":"sr:sport:1","order":2}
#url = "https://www.sportybet.com/api/ng/factsCenter/wapConfigurableEventsByOrder"

#res = requests.post(url, headers=headers, json=payload)
#clean_data, league = extract_Sportybet(data)
#with open("new_league_games_file.json", "w") as file:
    #json.dump(clean_data, file, indent=2)

"""
with open("game_file.json", "r") as file:
    old_data = json.load(file)
    result_dict = {}
    data = old_data.get("data")
    game_time = data.get("estimateStartTime", "unable to get time")
    game_name = f"{data.get('homeTeamName')} vs {data.get('awayTeamName')}"
    league_name =  data.get("sport", {}).get("category", {}).get("tournament", {}).get("name")
    markets = data.get("markets", [])
    for market in markets:
        outcome_list = []
        outcome_dict = {}
        market_desc = market.get("desc")
        market_name = market.get("name")
        outcomes = market.get("outcomes")
        for outcome in outcomes:
            outcome_name = outcome.get("desc")
            outcome_odd = outcome.get("odds")
            outcome_dict[outcome_name] = outcome_odd
        if league_name not in result_dict:
            result_dict[league_name] = {}
        if game_name not in result_dict[league_name]:
            result_dict[league_name][game_name] = {}
        if "time" not in result_dict[league_name][game_name]:
            result_dict[league_name][game_name]["time"] = game_time
        if market_name not in result_dict[league_name][game_name]:
            result_dict[league_name][game_name][market_name] = {}
        if outcome_name not in result_dict[league_name][game_name][market_name]:
            result_dict[league_name][game_name][market_name][outcome_name] = {}
        outcome_list.append(outcome_dict)  # Append outcome_dict to outcome_list
        result_dict[league_name][game_name][market_name] = outcome_list
            
with open("clean_market.json", "w") as file:
    json.dump(result_dict, file, indent=2)
        
"""
"""
def convert_market_data(old_data):
    result_dict = {}
    data = old_data.get("data")

    for market in data.get("markets", []):
        market_name = market.get("desc")
        outcomes = market.get("outcomes", [])

        if market_name not in result_dict:
            result_dict[market_name] = {}

        for outcome in outcomes:
            outcome_name = outcome.get("desc")
            outcome_odd = float(outcome.get("odds"))

            if outcome_name not in result_dict[market_name]:
                result_dict[market_name][outcome_name] = outcome_odd

    return result_dict
    
    
def save_to_format(old_data):
    result_dict = convert_market_data(old_data)
    #league_name = old_data.get("data", {}).get("sport", {}).get("category", {}).get("name", "Unknown")
    league_name = old_data.get("data", {}).get("sport", {}).get("category", {}).get("tournament", {}).get("name", "Unknown")

    output_dict = {
            league_name: result_dict
    }

    return output_dict

# Example usage
with open("game_file.json", "r") as file:
    old_data = json.load(file)

formatted_data = save_to_format(old_data)
with open("new_cleanmarket.json", "w") as file:
    json.dump(formatted_data, file, indent=2)
"""
