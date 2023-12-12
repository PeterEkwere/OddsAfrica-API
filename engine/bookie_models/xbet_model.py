#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from utils.scraper import Scraper
from utils.parser.scrub import Parse
from engine.storage_engine.vault import Vault
from utils.library.url_library.xbet_urls import FOOTBALL, VOLLEYBALL, BASKETBALL, ICEHOCKEY, DARTS, TENNIS, ESOCCER



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
            games = []
            for url in league_urls:
                try:
                    response = Scraper.Get_games(self, url)
                    games.append(Parse.clean(self, response, self.bookie_name))
                except Exception as e:
                    print(f"Error getting games for {country}, URL: {url}, Error: {e}")
            all_leagues[country] = games    
        Vault.save_games(self, all_leagues, self.bookie_name, Sport)
        return games