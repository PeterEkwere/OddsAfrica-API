# Both Paripesa and 1xbet use the same Site/API structure 
#!/usr/bin/python
"""
    This module houses the class for Paripesa
    Author: Peter Ekwere
"""
from utils.logger.log import log_success, log_error, log_exception
import requests
from utils.scraper import Scraper
from utils.parser.scrub import Parse
from engine.storage_engine.vault import Vault
from utils.library.url_library.paripesa_urls import FOOTBALL, VOLLEYBALL, BASKETBALL, ICEHOCKEY, DARTS, TENNIS, ESOCCER



class Paripesa:
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
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'Referer': 'https://paripesa.ng/en/line/',
        'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        }
    
    def __init__(self):
        self.bookie_name = "paripesa"
    
    def Get_games(self, Sport):
        """ This method gets all the games based on the country 

        Args:
            Country (string): The Country to be Queried
            Sport: The Sport to be Queried
        """
        all_leagues = {}
        for country, league_urls in Paripesa.Sports.get(Sport).items():
            league_dict = {}
            for url in league_urls:
                games = []
                try:
                    league_games = Scraper.Get_games(self, url)
                    games_id = Paripesa.get_games_id(league_games)
                    markets = Paripesa.get_games_market(games_id, Paripesa.headers)
                    result_dict, league = Parse.clean(self, markets, self.bookie_name)
                    #games.append(result_dict)
                    league_dict[league] = result_dict
                    log_success(f"Scraped {league}")
                except Exception as e:
                    log_exception(f"Error getting games for {country}, URL: {url}, Error: {e}")
            all_leagues[country] = league_dict 
        Vault.save_games(self, all_leagues, self.bookie_name, Sport)
        log_success(f"Successfully Scraped and Saved {self.bookie_name} {Sport}")
    
    
    
    def get_games_id(league_games):
        """ This Method will get all the games id in each league

        Args:
            league_games (int): This is the league games 
            headers (dict): This is the headers that will be passed to the request
        """
        id_list = []
        for a_dict in league_games.get("Value", {}):
            game_id = a_dict.get("CI", "")
            id_list.append(game_id)
            
        return id_list 
    
    def get_games_market(games_id, headers):
        """ This Method takes a list of games id
        and query an endpoint url for all the markets for that games

        Args:
            games_id (list): This is a list of game ids
        """
        session = requests.Session()
        markets = []
        for id in games_id:
            url = f"https://paripesa.ng/service-api/LineFeed/GetGameZip?id={id}&lng=en&isSubGames=true&GroupEvents=true&countevents=250&grMode=4&partner=188&topGroups=&country=132&marketType=1"
            response = session.get(url, headers=headers)
            markets.append(response.json())
        return markets
        
        