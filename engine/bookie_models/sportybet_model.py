#!/usr/bin/python
"""
    This Module will contain a bookie class for sportybet
    Author: Peter Ekwere
"""
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
from utils.scraper import Scraper
from utils.parser.scrub import Parse
from engine.storage_engine.vault import Vault
from utils.library.url_library.sportybet_urls import FOOTBALL, VOLLEYBALL, BASKETBALL, ICEHOCKEY, DARTS, TENNIS



class SportyBet:
    """
        This Class will handle scraping and parsing for the SportyBet site
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
        'Referer': 'https://www.sportybet.com/ng/sport/',
        'Accept-Language': 'en-EN,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'lng=en; flaglng=en; is_rtl=1; fast_coupon=true; v3tr=1; typeBetNames=full; auid=BbblOWFXM1ESU8VHB/1dAg==; sh.session_be98639c=04c362af-da44-4e0e-a384-ca2529fa5712; SESSION=4d9c3757128519eb87309f34d670d560; visit=1-378d9869df866ea72e6818eb52cb9af1; coefview=0; blocks=1%2C1%2C1%2C1%2C1%2C1%2C1%2C1; completed_user_settings=true; ggru=160; right_side=right; pushfree_status=canceled; _glhf=1633191759'
        }
    
    def __init__(self):
        self.bookie_name = "sportybet"
    
    def Get_games(self, Sport):
        """ This method gets all the games based on the country 

        Args:
            Country (string): The Country to be Queried
            Sport: The Sport to be Queried
        """
        all_leagues = {}
        
        for country , value in SportyBet.Sports.get(Sport).get("countries").items():
            try:
                league_dict = {}
                sport_id = SportyBet.Sports.get(Sport).get("id")
                #country_id = value.get("id")
                leagues =  value.get("leagues")
                for league_id in leagues:
                    league_games = SportyBet.get_league_games(sport_id, league_id, SportyBet.headers)
                    result_dict, league = Parse.clean(self, league_games, self.bookie_name)     
                    league_dict[league] = result_dict
                    print(f"Scraped {league}")
            except Exception as e:
                print(f"Error getting games for {country}, league: {leagues}, Error: {e}")
            all_leagues[country] = league_dict
            print(f"Scraped {country}") 
        Vault.save_games(self, all_leagues, self.bookie_name, Sport)
        print(f"Saved {Sport}")
                
                
    
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
        payload = {"tournamentId":[[f"{league_id}"]],"productId":3,"sportId":f"{sport_id}","order":2}
        url = "https://www.sportybet.com/api/ng/factsCenter/wapConfigurableEventsByOrder"
        res = session.post(url, headers=headers, json=payload)
        data = res.json()
        return data
        
        