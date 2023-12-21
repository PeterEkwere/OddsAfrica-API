#!/usr/bin/python
"""
    This module Contain the Parse Class
    Author: Peter Ekwere 
"""
import sys
sys.path.append("..")
from utils.parser.bookies_parsers.xbet_parser import extract
from utils.parser.bookies_parsers.merrybet_parser import extract_merrybet
from utils.parser.bookies_parsers.nairabet_parser import extract_nairabet
from utils.parser.bookies_parsers.betnaija_parser import extract_bet9ja
from utils.parser.bookies_parsers.bet22_parser import extract_22bet
from utils.parser.bookies_parsers.betking_parser import extract_betking
from utils.parser.bookies_parsers.LSB_parser import extract_LSB


class Parse:
    """
        This Class will handle everything from cleaning data to extracting data
    """
    
    def __init__(self):
        pass
    
    
    def clean(self, data, bookie_name):
        """ This Method cleans the data into readable data

        Args:
            data (dict): This is meant to be  the response data to be cleaned for readability
            bookie_name (str): This is the name of the bookie
        """
        try:   
            if bookie_name == "1xbet":
                clean_data, league = extract(data)
                return clean_data, league
            if bookie_name == "paripesa":
                clean_data = extract(data)
                return clean_data
            if bookie_name == "betwinner":
                clean_data, league = extract(data)
                return clean_data, league
            if bookie_name == "22bet":
                clean_data, league = extract_22bet(data)
                return clean_data, league
            if bookie_name == "merrybet":
                clean_data = extract_merrybet(data)
                return      
            if bookie_name == "nairabet":
                clean_data = extract_nairabet(data)
                return clean_data 
            if bookie_name == "bet9ja":
                clean_data = extract_bet9ja(data)
                return clean_data
            if bookie_name == "betking":
                clean_data, league = extract_betking(data)
                return clean_data, league
            if bookie_name == "livescorebet":
                clean_data, league = extract_LSB(data)
                return clean_data, league
        except Exception as e:
            print(f"Error cleaning Data: {e}")
            return None         
    
