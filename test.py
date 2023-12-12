#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from engine.bookie_models.nairabet_model import nairabet
import requests
import json



"""
url = "https://sports-api.nairabet.com/v2/competitions?country=NG&locale=en&group=g3&platform=desktop&timeOffset=-60&sportId=DARTS"
response = requests.get(url)
data = response.json()

result_dict = {}

# Iterate through each country in the data
for country_data in data["categories"]:
    country_id = country_data["id"]
    country_name = country_data["name"]
    league_ids = []

    # Iterate through each competition in the country
    for competition in country_data["competitions"]:
        league_id = competition["id"]
        league_ids.append(league_id)

    # Add the country and league IDs to the result dictionary
    result_dict[country_name] = league_ids
        
                        
with open("nairadart.json", "w") as file:
    json.dump(result_dict, file, indent=2)
"""


Today = nairabet()
sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey"]
for sport in sports:
    league_games = Today.Get_games(sport)
    
    
#def split_team_names(team_names):
    #return [name.strip() for name in team_names.split('-')]

#url = "https://sports-api.nairabet.com/v2/events/6683046?country=NG&locale=en&group=g3&platform=mobile"
#response = requests.get(url)
#data = response.json()
#with open("market.json", "w") as file:
    #json.dump(data, file, indent=2)


"""  
with open("market.json", "r") as file:
    result_dict = {}
    data = json.load(file)
    game_list = data.get("eventNames", [])
    game_name = f"{game_list[0]} vs {game_list[1]}"
    time = data.get("startTime", None)
    country = data.get("categoryName", None)
    league = data.get("competitionName", None)

    # Iterate over market groups
    for market_group in data.get("marketGroups", []):
        market_group_name = market_group.get("name")

        # Iterate over markets within the market group
        for market in market_group["markets"]:
                market_name = market.get("name")
                if market_name not in result_dict.get(country, {}).get(league, {}).get(game_name, {}):
                    result_dict.setdefault(country, {}).setdefault(league, {}).setdefault(game_name, {}).setdefault(market_name, {})
                    
                for outcome in market.get("outcomes", []):
                    outcome_name = outcome.get("name")
                    odds = outcome.get("value")
                    
                    if outcome_name not in result_dict[country][league][game_name][market_name]:
                        result_dict[country][league][game_name][market_name][outcome_name] = odds
                        
with open("new_naira.json", "w") as file:
    json.dump(result_dict, file, indent=2)            
"""
