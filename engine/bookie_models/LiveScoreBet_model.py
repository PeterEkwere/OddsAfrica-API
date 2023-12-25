#!/usr/bin/python
"""
    This module houses the class for nairabet
    Author: Peter Ekwere
"""
from utils.logger.log import log_exception, log_error, log_success
import requests
from utils.parser.scrub import Parse
from engine.storage_engine.vault import Vault
from utils.library.url_library.livescorebet_urls import FOOTBALL, VOLLEYBALL, BASKETBALL, ICEHOCKEY, DARTS, TENNIS



class livescorebet:
    """ This Class contains methods meant to get/manipulate/save Data
    """
    Sports = {
        'football': FOOTBALL,
        'icehockey': ICEHOCKEY,
        'darts': DARTS,
        'tennis': TENNIS,
        'volleyball': VOLLEYBALL,
        'basketball': BASKETBALL
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
        'Referer': 'https://m.betking.com/',
        'Accept-Language': 'en-EN,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        }
    
    def __init__(self):
        self.bookie_name = "livescorebet"
    
    def Get_games(self, Sport):
        """ This method gets all the games based on the country 

        Args:
            Country (string): The Country to be Queried
            Sport: The Sport to be Queried
        """
        all_leagues = {}
        for country, league_ids in livescorebet.Sports.get(Sport).items():
            league_dict = {}
            for league_id in league_ids:
                #games = []
                try:
                    league_json = livescorebet.get_league_games(league_id, livescorebet.headers)
                    result_dict, league = Parse.clean(self, league_json, self.bookie_name)
                    league_dict[league] = result_dict
                    log_success(f"Scraped {league}")
                except Exception as e:
                    log_exception(f"Error getting games for {country}, league id: {league_id}, Error: {e}")
            all_leagues[country] = league_dict
        Vault.save_games(self, all_leagues, self.bookie_name, Sport)
        log_success(f"Successfully Scraped and Saved {self.bookie_name} {Sport}")
    
    def get_league_games(league_id, headers):
        """ Every league returned from the livescorebet API has an id 
            This method method will query a league endpoint using that id
        Args:
            league_id (integer): This is the league id for each league
            headers (dict): This is the header to be passed to request
        Returns:
            league_json (dict): This are the games in a league
        """
        session = requests.Session()
        url = f"https://gateway-ng.livescorebet.com/sportsbook/gateway/v3/view/events/matches?categoryid={league_id}&interval=ALL&lang=en-ng"
        response = session.get(url, headers=headers)
        data = response.json()
        return data