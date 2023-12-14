#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from engine.bookie_models.betnaija_model import bet9ja
import requests
import json
from difflib import SequenceMatcher
import requests

#def str_similarity(a, b):
	#return SequenceMatcher(None, a, b).ratio()


#result = str_similarity("Everton - Chelsea FC", "Everton VS Chelsea")
#print(result)

#Today = bet9ja()
#sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]
#for sport in sports:
    #league_games = Today.Get_games(sport)
    
url = "https://sportsapicdn-mobile.betking.com/api/feeds/prematch/matches/custommenu/en/4"
res = requests.get(url)
print()
    
