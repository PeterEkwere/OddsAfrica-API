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
from utils.arrange import arrange_games
from utils.process import process_games
from utils.combine import Combine_markets
from utils.calculate_arb import get_arbs
from utils.logger.log import log_exception, log_success, log_error
#from timeout_decorator import timeout

# Defining the bookies and available sports
bookies_and_sports = [
    #(Betpawa(), ["football", "basketball"]),
    #(bet22(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    #(bet9ja(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    #(betking(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    #(betwinner(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    #(livescorebet(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    #(merrybet(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    #(nairabet(), ["soccer", "basketball", "volleyball", "darts", "ice_hockey"]),
    #(Paripesa(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
    #(SportyBet(), ["football", "basketball", "volleyball", "darts", "icehockey"]),
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


# Calling The Arrange Function to Prepare available games for processing
try:
    arrange_games()
    log_success("SUCCESS Arranging GAMES\n\n")
except Exception as e:
    log_exception(f"ERROR ARRANGING GAMES\n\n")

# Calling The Process Function to Extract the needed markets for Cross Market Creation
try:
    process_games()
    log_success("SUCCESS PROCESSING THE NEEDED MARKETS FOR CROSS MARKET CREATIONS\n\n")
except Exception as e:
    log_exception(f"ERROR EXTRACTING MARKETS: {e}\n\n")
    
    
# Calling the Combine function to Create the needed cross market combination as per its respective formula and save them as values for each game
try:
    Combine_markets()
    log_success("SUCCESS COMBINING ALL BOOKIES TO CROSS MARKETS FOR EACH GAMES\n\n")
except Exception as e:
    log_exception(f"ERROR COMBINING BOOKIES: {e}\n\n")

#Calling the get arbs function to extract each combination and pass it to a function to calculate if there is an arbitrage opportunity
try:
    get_arbs()
    log_success("SUCCESS FINDING ARBS YOU CAN FIND YOUR ARBS IN THE ARBS FOLDER IN engine/storage_engine/arbs_found file\n\n")
except Exception as e:
    log_exception(f"ERROR Searching For ARBS: {e}\n\n")