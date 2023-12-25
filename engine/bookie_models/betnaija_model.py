#!/usr/bin/python
"""
    This module houses the class for betnaija
    Author: Peter Ekwere
"""
import requests
from utils.logger.log import log_exception, log_success
from utils.parser.scrub import Parse
from engine.storage_engine.vault import Vault
from utils.library.url_library.betnaija_url import FOOTBALL, VOLLEYBALL, BASKETBALL, ICEHOCKEY, DARTS, TENNIS, ESOCCER



class bet9ja:
    """ This Class contains methods meant to get/manipulate/save Data
    """
    
    Sports = {
        'football': FOOTBALL,
        'icehockey': ICEHOCKEY,
        'darts': DARTS,
        'tennis': TENNIS,
        'volleyball': VOLLEYBALL,
        'basketball': BASKETBALL,
        'icehockey': ICEHOCKEY,
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
        'Referer': 'https://sports.bet9ja.com/',
        'Accept-Language': 'en-EN,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        }
    
    def __init__(self):
        self.bookie_name = "bet9ja"
    
    def Get_games(self, Sport):
        """ This method gets all the games based on the country 

        Args:
            Country (string): The Country to be Queried
            Sport: The Sport to be Queried
        """
        all_leagues = {}
        for country, league_ids in bet9ja.Sports.get(Sport).items():
            games = []
            for league_id in league_ids:
                try:
                    league_games = bet9ja.get_league_games(league_id, bet9ja.headers)
                    log_success(f"Scraping {country} {Sport}")
                    games.append(Parse.clean(self, league_games, self.bookie_name))
                except Exception as e:
                    log_exception(f"Error getting games for {country}, league id: {league_id}, Error: {e}")
            all_leagues[country] = games  
        Vault.save_games(self, all_leagues, self.bookie_name, Sport)
        log_success(f"Successfully Scraped and Saved {self.bookie_name} {Sport}")
    
    
    
    def get_league_games(league_id, headers):
        """ Every league in the nairabet response has a league id 
            this method will use the league id to returns all the games by id for that league

        Args:
            league_id (int): This is a league id
            sport (str): This is the sport type that will be converted to uppercase and passed to the endpoint url 
            headers (dict): this is the headers to be passed to request 
        """
        session = requests.Session()
        url = f"https://sports.bet9ja.com/desktop/feapi/PalimpsestAjax/GetEventsInGroupV2?GROUPID={league_id}&DISP=0&GROUPMARKETID=1&matches=false&v_cache_version=1.244.0.136"
        response = session.get(url, headers=headers)
        data = response.json()
        return data
        