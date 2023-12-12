# Both Paripesa/1xbet/betwinner use the same Site/API structure 
#!/usr/bin/python
"""
    This module houses the class for Paripesa
    Author: Peter Ekwere
"""
from utils.scraper import Scraper
from utils.parser.scrub import Parse
from engine.storage_engine.vault import Vault
from utils.library.url_library.betwinner_urls import FOOTBALL, VOLLEYBALL, BASKETBALL, ICEHOCKEY, DARTS, TENNIS, ESOCCER



class betwinner:
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
        'Referer': 'https://betwinner.ng/en/line/',
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
        self.bookie_name = "betwinner"
    
    def Get_games(self, Sport):
        """ This method gets all the games based on the country 

        Args:
            Country (string): The Country to be Queried
            Sport: The Sport to be Queried
        """
        all_leagues = {}
        for country, league_urls in betwinner.Sports.get(Sport).items():
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