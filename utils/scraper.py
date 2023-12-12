#!/usr/bin/python
"""
    This Module Contains the Scraper class 
    Author: Peter Ekwere 
"""
import requests
from retrying import retry

    


class Scraper:
    """ This Class handles holds headers attribute and requests methods for all bookies
    Returns:
    """
    
    def __init__(self):
        pass
    
    
    @retry(wait_fixed=2000, stop_max_attempt_number=3)
    def make_request(self, url):
        session = requests.Session()
        headers = self.headers
        response = session.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    
    def Get_games(self, url):
        """ This Function querys the endpoint and return a json response

        Args:
            url (str): This is a league's endpoint
        """
        try:
            data = Scraper.make_request(self, url)
            return data
        except Exception as e:
            print(f"Error making request: {e}")
            return None