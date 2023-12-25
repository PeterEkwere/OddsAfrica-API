#!/usr/bin/python
"""
    This Module will contain a bookie class for betpawa
    Author: Peter Ekwere
"""
import time
import requests
from utils.logger.log import log_exception, log_success
from utils.scraper import Scraper
from utils.parser.scrub import Parse
from engine.storage_engine.vault import Vault
from utils.library.url_library.betpawa_url import FOOTBALL, BASKETBALL



class Betpawa:
    """
        This Class will handle scraping and parsing for the SportyBet site
    """
    Sports = {
        'football': FOOTBALL,
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
        'Referer': 'https://www.betpawa.ng/',
        'X-Pawa-Brand': 'betpawa-nigeria',
        'X-Pawa-Language': 'en',
        'Accept-Language': 'en-EN,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'lng=en; flaglng=en; is_rtl=1; fast_coupon=true; v3tr=1; typeBetNames=full; auid=BbblOWFXM1ESU8VHB/1dAg==; sh.session_be98639c=04c362af-da44-4e0e-a384-ca2529fa5712; SESSION=4d9c3757128519eb87309f34d670d560; visit=1-378d9869df866ea72e6818eb52cb9af1; coefview=0; blocks=1%2C1%2C1%2C1%2C1%2C1%2C1%2C1; completed_user_settings=true; ggru=160; right_side=right; pushfree_status=canceled; _glhf=1633191759'
       }
    
    def __init__(self):
        self.bookie_name = "betpawa"
    
    def Get_games(self, Sport):
        """ This method gets all the games based on the country 

        Args:
            Country (string): The Country to be Queried
            Sport: The Sport to be Queried
        """
        all_leagues = {}
        
        for country , value in Betpawa.Sports.get(Sport).get("countries").items():
            try:
                league_dict = {}
                sport_id = Betpawa.Sports.get(Sport).get("id")
                #country_id = value.get("id")
                leagues =  value
                for league_id in leagues:
                    league_games, league_name = Betpawa.get_league_games(sport_id, league_id, Betpawa.headers)
                    result_dict = Parse.clean(self, league_games, self.bookie_name)     
                    league_dict[league_name] = result_dict
                    log_success(f"Scraped {league_name}")
            except Exception as e:
                log_exception(f"Error getting games for {country}, league: {leagues}, Error: {e}")
            all_leagues[country] = league_dict 
        Vault.save_games(self, all_leagues, self.bookie_name, Sport)
        log_success(f"Successfully Scraped and Saved {self.bookie_name} {Sport}")
                
                
    
    def get_league_games(sport_id, league_id, headers):
        """ This method takes a sport id and league id and uses each id to query a url endpoint
            And get the markets associated with that league

        Args:
            sport_id (str): This is the sport id
            league_id (str): This is the league id
        Returns:
            data: This is a list of Dictionaries where each dictionary contains the markets associated with a game
        """
        session =  requests.Session()
        url = f'https://www.betpawa.ng/api/sportsbook/v1/events/list/pages/by-query?q={{"onlyPopular":false,"marketFilters":{{"marketPreference":"DEFINED","marketTypeIds":["5000"]}},"take":20,"competitions":[{league_id}],"categoryId":"{sport_id}"}}'
        league_json = session.get(url, headers=headers)
        data =  league_json.json()
        league_name = data.get("meta", {}).get("competitions", [])[0].get("name", "Competition name") 
        league_games =  data.get("events", [])
        game_id_list = []
        games_market_list = []   
        for game in league_games:
            game_id = game.get("id", "Couldnt get game id")
            game_id_list.append(game_id)
        
        for id in game_id_list:
            url = f"https://www.betpawa.ng/api/sportsbook/v1/events/{id}"
            res = session.get(url, headers=headers)
            games_market_list.append(res.json())
        
        return games_market_list, league_name