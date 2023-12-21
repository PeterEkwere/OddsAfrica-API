#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from engine.bookie_models.betking_model import betking
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

#Today = betking()
#sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey"]
#for sport in sports:
    #league_games = Today.Get_games(sport)
    
#url = "https://gateway-ng.livescorebet.com/sportsbook/gateway/v3/view/sport/competitions?interval=ALL&lang=en-ng&sportcategoryid=SBTC1_1"
#res = requests.get(url)
with open("livescorebet_countries.json", "r") as file:
    data = json.load(file)
    result_dict = {}
    competions_list = data.get("competitions", [])
    competions_data = []
    competitions = []
    if competions_list:
        competions_data = competions_list[0]
    competitions = competions_data.get("childs", [])
    if competitions:
        for competition in competitions:
            country_name = competition.get("countryName", "NULL COUNTRY NAME")
            league_name =  competition.get("name", "NULL LEAGUE NAME")
            league_id = competition.get("id", "NUll LEAGUE ID")
            if country_name not in result_dict:
                result_dict[country_name] = league_id
    with open("livescore_urls.json", "w") as a_file:
        json.dump(result_dict, a_file, indent=2)
