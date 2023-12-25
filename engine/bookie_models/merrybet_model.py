#!/usr/bin/python
"""
    This module houses the class for merrybet
    Author: Peter Ekwere
"""
from utils.logger.log import log_exception, log_error, log_success
from utils.scraper import Scraper
from utils.parser.scrub import Parse
from engine.storage_engine.vault import Vault
from utils.library.url_library.merrybet_urls import FOOTBALL, VOLLEYBALL, BASKETBALL, ICEHOCKEY, DARTS, TENNIS, ESOCCER



class merrybet:
    """ This Class contains methods meant to get/manipulate/save Data
    """
    
    Sports = {
        'football': FOOTBALL,
        'icehockey': ICEHOCKEY,
        'darts': DARTS,
        'tennis': TENNIS,
        'volleyball': VOLLEYBALL,
        'basketball': BASKETBALL,
        'esoccer': ESOCCER
        }
    
    headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-GPC': '1',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.merrybet.com/sports/',
        'Accept-Language': 'en-EN,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        }
    
    def __init__(self):
        self.bookie_name = "merrybet"
    
    def Get_games(self, Sport):
        """ This method gets all the games based on the country 

        Args:
            Country (string): The Country to be Queried
            Sport: The Sport to be Queried
        """
        all_leagues = {}
        for country, league_urls in merrybet.Sports.get(Sport).items():
            games = []
            for url in league_urls:
                try:
                    response = Scraper.Get_games(self, url)
                    games.append(Parse.clean(self, response, self.bookie_name))
                except Exception as e:
                    log_exception(f"Error getting games for {country}, URL: {url}, Error: {e}")
            all_leagues[country] = games    
        Vault.save_games(self, all_leagues, self.bookie_name, Sport)
        log_success(f"Successfully Scraped and Saved {self.bookie_name} {Sport}")