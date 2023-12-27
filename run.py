#!/usr/bin/python
"""
    This is The Main Module that will handle Web Sraping and organizing 
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
from timeout_decorator import timeout



# Define the timeout value in seconds
timeout_value = 60 * 10 # This will Allocate 10 mins per betsite

# Decorating the function with the timeout
@timeout(timeout_value)
def scrape_bookie(bookie, sports):
    try:
        for sport in sports:
            bookie.Get_games(sport)
        message = f"SUCCESSFULLY SCRAPED {bookie.bookie_name}"
        log_success(f"\033[1m\033[36m{message}\033[0m")
    except Exception as e:
        message = f"ERROR SCRAPING {bookie.bookie_name}, Error: {e}"
        log_exception(f"\033[1m\033[36m{message}\033[0m")

# Defining the bookies and sports
bookies_and_sports = [
    (Betpawa(), ["football", "basketball"]),
    (bet22(), ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]),
    (bet9ja(), ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]),
    (betking(), ["football", "basketball", "volleyball", "tennis", "darts", "icehockey"]),
    (betwinner(), ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]),
    (livescorebet(), ["football", "basketball", "volleyball", "tennis", "darts", "icehockey"]),
    (merrybet(), ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]),
    (nairabet(), ["soccer", "basketball", "volleyball", "tennis", "darts", "ice_hockey"]),
    (Paripesa(), ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"]),
    (SportyBet(), ["football", "basketball", "volleyball", "tennis", "darts", "icehockey"]),
    (xbet(), ["football", "basketball", "volleyball", "tennis", "darts", "icehockey", "esoccer"])
    # ... Repeat for other bookies ...
]

# Loop through bookies and scrape
for bookie, sports in bookies_and_sports:
    try:
        scrape_bookie(bookie, sports)
    except TimeoutError:
        log_exception(f"TimeoutError: Scraping {bookie.bookie_name} took too long. Moving to the next bookie.")
    except Exception as e:
        log_exception(f"Unexpected error: {e}")
