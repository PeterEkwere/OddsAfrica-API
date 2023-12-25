#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
import requests
from utils.scraper import Scraper
from utils.parser.scrub import Parse
from engine.storage_engine.vault import Vault
from utils.library.url_library.xbet_urls import FOOTBALL, VOLLEYBALL, BASKETBALL, ICEHOCKEY, DARTS, TENNIS, ESOCCER
from utils.logger.log import log_error, log_exception, log_success


class xbet:
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
        'Referer': 'https://1xbet.com/en/line/',
        'Accept-Language': 'en-EN,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'lng=en; flaglng=en; is_rtl=1; fast_coupon=true; v3tr=1; typeBetNames=full; auid=BbblOWFXM1ESU8VHB/1dAg==; sh.session_be98639c=04c362af-da44-4e0e-a384-ca2529fa5712; SESSION=4d9c3757128519eb87309f34d670d560; visit=1-378d9869df866ea72e6818eb52cb9af1; coefview=0; blocks=1%2C1%2C1%2C1%2C1%2C1%2C1%2C1; completed_user_settings=true; ggru=160; right_side=right; pushfree_status=canceled; _glhf=1633191759'
        }
    
    def __init__(self):
        self.bookie_name = "1xbet"
    
    def Get_games(self, Sport):
        """ This method gets all the games based on the country 

        Args:
            Country (string): The Country to be Queried
            Sport: The Sport to be Queried
        """
        all_leagues = {}
        for country, league_urls in xbet.Sports.get(Sport).items():
            league_dict = {}
            for url in league_urls:
                games = []
                try:
                    league_games = Scraper.Get_games(self, url)
                    games_id = xbet.get_games_id(league_games)
                    markets = xbet.get_games_market(games_id, xbet.headers)
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
            url = f"https://ng.1x001.com/service-api/LineFeed/GetGameZip?id={id}&lng=en&isSubGames=true&GroupEvents=true&countevents=250&grMode=4&partner=159&topGroups=&country=132&marketType=1"
            response = session.get(url, headers=headers)
            markets.append(response.json())
        return markets
        
        