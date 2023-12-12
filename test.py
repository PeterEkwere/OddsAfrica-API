#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from engine.bookie_models.nairabet_model import nairabet
import requests
import json
from difflib import SequenceMatcher



def str_similarity(a, b):
	return SequenceMatcher(None, a, b).ratio()


result = str_similarity("Everton - Chelsea FC", "Everton VS Chelsea")
print(result)

#Today = nairabet()
#sports = ["soccer", "basketball", "volleyball", "tennis", "darts", "ice_hockey"]
#for sport in sports:
    #league_games = Today.Get_games(sport)
    
