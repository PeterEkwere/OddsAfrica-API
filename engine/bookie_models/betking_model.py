#!/usr/bin/python
"""
    This module houses the class for nairabet
    Author: Peter Ekwere
"""
import requests
from utils.parser.scrub import Parse
from engine.storage_engine.vault import Vault
from utils.library.url_library.betking_urls import FOOTBALL, VOLLEYBALL, BASKETBALL, ICEHOCKEY, DARTS, TENNIS



class betking:
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
        self.bookie_name = "betking"
    
    def Get_games(self, Sport):
        """ This method gets all the games based on the country 

        Args:
            Country (string): The Country to be Queried
            Sport: The Sport to be Queried
        """
        all_leagues = {}
        for country, league_ids in betking.Sports.get(Sport).items():
            league_dict = {}
            for league_id in league_ids:
                games = []
                try:
                    league_games = []
                    league_json = betking.get_league_games(league_id, betking.headers)
                    games_id = betking.get_games_id(league_json)
                    if games_id:
                        for game_id in games_id:
                            a_league_game = betking.get_game_market(game_id, betking.headers)
                            league_games.append(a_league_game)
                        result_dict, league = Parse.clean(self, league_games, self.bookie_name)
                        league_dict[league] = result_dict
                    print(f"Scraped {league}")
                except Exception as e:
                    print(f"Error getting games for {country}, league id: {league_id}, game id: {game_id}, Error: {e}")
            all_leagues[country] = league_dict
            print(f"Finished scraping {country}")
        Vault.save_games(self, all_leagues, self.bookie_name, Sport)
        return games
    
    
    
    def get_games_id(json_data):
        """ This method extracts all the games id from a league json

        Args:
            json_data (dict): this is the json file gotten from querying the league url endpoint
        """
        AM = json_data.get("AreaMatches", [])
        game_list =  []
        if AM:
            games = AM[0].get("Items", [])
            for game in games:
                gameid = game.get("ItemID", "")
                game_list.append(gameid)
            
        return game_list
    
    
    def get_league_games(league_id, headers):
        """ Every game returned from the betking API has an id 
            This method method will qury a league endpoint
        Args:
            league_id (integer): This is the league id for each league
            headers (dict): This is the header to be passed to request
        Returns:
            league_json (dict): This are the games in a league
        """
        session = requests.Session()
        url = f"https://sportsapicdn-mobile.betking.com/api/feeds/prematch/en/4/{league_id}/0/0"
        response = session.get(url, headers=headers)
        data = response.json()
        return data
    
    def get_game_market(game_id, headers):
        """ This method will query the endpoint of a game match

        Args:
            game_id (str): This is the Game id
        """
        url = f"https://sportsapicdn-mobile.betking.com/api/feeds/prematch/event/lite/grouped/{game_id}/1572"
        session = requests.Session()
        response = session.get(url, headers=headers)
        data = response.json()
        return data
        