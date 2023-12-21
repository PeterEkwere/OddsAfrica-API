#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from engine.bookie_models.LiveScoreBet_model import livescorebet
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

Today = livescorebet()
sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey"]
for sport in sports:
    Today.Get_games(sport)


#premier_league_url = "https://gateway-ng.livescorebet.com/sportsbook/gateway/v3/view/events/matches?categoryid=SBTC3_40253&interval=ALL&lang=en-ng"


#a_game_url = "https://gateway-ng.livescorebet.com/sportsbook/gateway/v1/view/event?eventid=SBTE_29817231&lang=en-ng"
#res = requests.get(a_game_url)
#data = res.json()


"""
with open("league_games.json", "r") as a_file:
    data = json.load(a_file)
    result_dict = {}
    event = data.get("events", {})
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
            for outcome in outcomes:
                outcome_name = outcome.get("name", "Error getting name")
                outcome_odd = outcome.get("odds")
                outcome_dict[outcome_name] = outcome_odd
            
            if league not in result_dict:
                result_dict[league] = {}
            if game_name not in result_dict[league]:
                result_dict[league][game_name] = {}
            if "time" not in result_dict[league][game_name]:
                result_dict[league][game_name]["time"] = time
            if market_name not in result_dict[league][game_name]:
                result_dict[league][game_name][market_name] = {}
            if outcome_name not in result_dict[league][game_name][market_name]:
                result_dict[league][game_name][market_name][outcome_name] = {}
            result_dict[league][game_name][market_name] = outcome_dict
            
with open("edit.json", "w") as file:
    json.dump(result_dict, file, indent=2)
"""