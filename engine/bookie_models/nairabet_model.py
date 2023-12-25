#!/usr/bin/python
"""
    This module houses the class for nairabet
    Author: Peter Ekwere
"""
from utils.logger.log import log_error, log_success, log_exception
import requests
from utils.parser.scrub import Parse
from engine.storage_engine.vault import Vault
from utils.library.url_library.nairabet_urls import SOCCER, VOLLEYBALL, BASKETBALL, ICE_HOCKEY, DARTS, TENNIS



class nairabet:
    """ This Class contains methods meant to get/manipulate/save Data
    """
    
    Sports = {
        'soccer': SOCCER,
        'ice_hockey': ICE_HOCKEY,
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
        'Referer': 'https://www.nairabet.com/',
        'Accept-Language': 'en-EN,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        }
    
    def __init__(self):
        self.bookie_name = "nairabet"
    
    def Get_games(self, Sport):
        """ This method gets all the games based on the country 

        Args:
            Country (string): The Country to be Queried
            Sport: The Sport to be Queried
        """
        all_leagues = {}
        for country, league_ids in nairabet.Sports.get(Sport).items():
            games = []
            for league_id in league_ids:
                try:
                    league_games = []
                    games_count = 0
                    games_id = nairabet.get_league_games(league_id, Sport, nairabet.headers)
                    for game_id in games_id:
                        games_count += 1
                        a_league_game = nairabet.get_markets_for_game(game_id, nairabet.headers)
                        league_games.append(a_league_game)
                    log_success(f"Scraping {country} {Sport}")
                    games.append(Parse.clean(self, league_games, self.bookie_name))
                except Exception as e:
                    log_exception(f"Error getting games for {country}, league id: {league_id}, game id: {game_id}, Error: {e}")
            all_leagues[country] = games 
        if Sport == 'soccer':
            Sport = 'football'
        elif Sport == 'ice_hockey':
            Sport = "icehockey"   
        Vault.save_games(self, all_leagues, self.bookie_name, Sport)
        log_success(f"Successfully Scraped and Saved {self.bookie_name} {Sport}")
    
    
    
    def get_league_games(league_id, sport, headers):
        """ Every league in the nairabet response has a league id 
            this method will use the league id to returns all the games by id for that league

        Args:
            league_id (int): This is a league id
            sport (str): This is the sport type that will be converted to uppercase and passed to the endpoint url 
            headers (dict): this is the headers to be passed to request 
        """
        session = requests.Session()
        u_sport = sport.upper()
        url = f"https://sports-api.nairabet.com/v2/events?country=NG&locale=en&group=g3&platform=desktop&sportId={u_sport}&competitionId={league_id}&limit=20"
        response = session.get(url, headers=headers)
        data = response.json()
        games = []

        #for game in data.get("data", {}).get("categories", [])[0].get("competitions", [])[0].get("events", []):
            #game_id = game["id"]
            #games.append(game_id)
        
        # Check if "data" key exists and has "categories" with at least one element
        if "data" in data and "categories" in data["data"] and data["data"]["categories"]:
            # Check if "categories" has at least one element and "competitions" key exists
            categories = data["data"]["categories"]
            if categories and "competitions" in categories[0]:
                competitions = categories[0]["competitions"]
                # Check if "competitions" has at least one element and "events" key exists
                if competitions and "events" in competitions[0]:
                    events = competitions[0]["events"]
                    for game in events:
                        game_id = game.get("id")
                        if game_id is not None:
                            games.append(game_id)

        return games
    
    def get_markets_for_game(game_id, headers):
        """ Every game returned from the nairabet API has an id 

        Args:
            game_id (integer): This is the game id for each game in a league
            headers (dict): This is the header to be passed to request
        Returns:
            markets (list): This are the markets for each games
        """
        session = requests.Session()
        url = f"https://sports-api.nairabet.com/v2/events/{game_id}?country=NG&locale=en&group=g3&platform=desktop"
        response = session.get(url, headers=headers)
        data = response.json()
        return data

        