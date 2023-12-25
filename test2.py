#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from engine.bookie_models.betpawa_model import Betpawa
from engine.bookie_models.bet22_model import bet22
from engine.bookie_models.betking_model import betking
from engine.bookie_models.betnaija_model import bet9ja
from engine.bookie_models.betwinner_model import betwinner
from engine.bookie_models.LiveScoreBet_model import livescorebet
from engine.bookie_models.merrybet_model import merrybet
from engine.bookie_models.nairabet_model import nairabet
from engine.bookie_models.paripesa_model import Paripesa
from engine.bookie_models.sportybet_model import SportyBet
from engine.bookie_models.xbet_model import xbet
from utils.logger.log import log_exception, log_success, log_error
import requests
import json
from difflib import SequenceMatcher
import requests
from datetime import datetime
from utils.parser.bookies_parsers.sportybet_parser import extract_Sportybet
from engine.bookie_models.sportybet_model import SportyBet
from urllib.parse import unquote

#def str_similarity(a, b):
	#return SequenceMatcher(None, a, b).ratio()


#result = str_similarity("Everton - Chelsea FC", "Everton VS Chelsea")
#print(result)

log_success("Scraping all Games Initiated ")
try:
    bookie = Betpawa()
    sports = ["football", "basketball"]
    for sport in sports:
        bookie.Get_games(sport)
    log_success(f"SUCCESSFULLY SCRAPED {bookie.bookie_name}")
except:
	log_exception(f"ERROR SCRAPING {bookie.bookie_name}")
try:
    bookie = bet22()
    sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]
    for sport in sports:
        bookie.Get_games(sport)
    log_success(f"SUCCESSFULLY SCRAPED {bookie.bookie_name}")
except:
    log_exception(f"ERROR SCRAPING {bookie.bookie_name}")
try:
    bookie = bet9ja()
    sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]
    for sport in sports:
        bookie.Get_games(sport)
    log_success(f"SUCCESSFULLY SCRAPED {bookie.bookie_name}")
except:
	log_exception(f"ERROR SCRAPING {bookie.bookie_name}")
try:
    bookie = betking()
    sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey"]
    for sport in sports:
        bookie.Get_games(sport)
    log_success(f"SUCCESSFULLY SCRAPED {bookie.bookie_name}")
except:
	log_exception(f"ERROR SCRAPING {bookie.bookie_name}")
try:
    bookie = betwinner()
    sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]
    for sport in sports:
        bookie.Get_games(sport)
    log_success(f"SUCCESSFULLY SCRAPED {bookie.bookie_name}")
except:
	log_exception(f"ERROR SCRAPING {bookie.bookie_name}")
try:
    bookie = livescorebet()
    sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey"]
    for sport in sports:
        bookie.Get_games(sport)
    log_success(f"SUCCESSFULLY SCRAPED {bookie.bookie_name}")
except:
	log_exception(f"ERROR SCRAPING {bookie.bookie_name}")
try:
    bookie = merrybet()
    sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]
    for sport in sports:
        bookie.Get_games(sport)
    log_success(f"SUCCESSFULLY SCRAPED {bookie.bookie_name}")
except:
	log_exception(f"ERROR SCRAPING {bookie.bookie_name}")
try:
    bookie = nairabet()
    sports = ["soccer", "basketball", "volleyball", "tennis", "darts", "ice_hockey"]
    for sport in sports:
        bookie.Get_games(sport)
    log_success(f"SUCCESSFULLY SCRAPED {bookie.bookie_name}")
except:
    log_exception(f"ERROR SCRAPING {bookie.bookie_name}")
try:
    bookie = Paripesa()
    sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]
    for sport in sports:
        bookie.Get_games(sport)
    log_success(f"SUCCESSFULLY SCRAPED {bookie.bookie_name}")
except:
	log_exception(f"ERROR SCRAPING {bookie.bookie_name}")
try:
    bookie = SportyBet()
    sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey"]
    for sport in sports:
        bookie.Get_games(sport)
    log_success(f"SUCCESSFULLY SCRAPED {bookie.bookie_name}")
except:
	log_exception(f"ERROR SCRAPING {bookie.bookie_name}")
try:
    bookie = xbet()
    sports = ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]
    for sport in sports:
        bookie.Get_games(sport)
    log_success(f"SUCCESSFULLY SCRAPED {bookie.bookie_name}")
except:
	log_exception(f"ERROR SCRAPING {bookie.bookie_name}")
