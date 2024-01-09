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
#from timeout_decorator import timeout

# Defining the bookies and available sports
bookies_and_sports = [
    #(Betpawa(), ["football", "basketball"]),
    #(bet22(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    (bet9ja(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    (betking(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    #(betwinner(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    (livescorebet(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    (merrybet(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    (nairabet(), ["soccer", "basketball", "volleyball", "darts", "ice_hockey"]),
    (Paripesa(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    (SportyBet(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    (xbet(), ["football", "basketball", "volleyball", "darts", "icehockey"])
    # ... Repeat for other bookies ...
]



def scrape_bookie(bookie, sports):
    """ This Function will pass each sport to the bookies Scraper to get the needed Data

    Args:
        bookie (class): This is the Bookie model
        sports (list): This is a list of sports available on the betsite
    """
    try:
        for sport in sports:
            bookie.Get_games(sport)
        message = f"SUCCESSFULLY SCRAPED {bookie.bookie_name}\n\n"
        log_success(f"{message}")
    except Exception as e:
        message = f"ERROR SCRAPING {bookie.bookie_name}, Error: {e}\n"
        log_exception(f"{message}")



# Loop through bookies and scrape the needed Data
for bookie, sports in bookies_and_sports:
    try:
        scrape_bookie(bookie, sports)
    except TimeoutError:
        log_exception(f"TimeoutError: Scraping {bookie.bookie_name} took too long. Moving to the next bookie.")
    except Exception as e:
        log_exception(f"Unexpected error: {e}\n")

