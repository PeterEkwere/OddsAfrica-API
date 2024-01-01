#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from utils.logger.log import log_exception, log_success, log_error
import requests
import json
import re
from difflib import SequenceMatcher
import requests
from datetime import datetime
from timeout_decorator import timeout
import os
import json
import difflib
from engine.ArbBrain.arb import Find_arbitrage
from utils.process import process_games
from utils.arrange import arrange_games
from collections import OrderedDict
from utils.arrange import save_json, load_json
from utils.combine import Combine_markets
from engine.ArbBrain.arb import Find_arbitrage




def get_arbs():
    """ This function combines all the found markets in a game to mimic the sports formula
    """
    combined_sports_folder = "engine/storage_engine/combined_data/"
    for sport_file in os.listdir(combined_sports_folder):
        try:
            sport_folder_path = os.path.join(combined_sports_folder, sport_file)
            if os.path.isfile(sport_folder_path):
                filename = f"{sport_file}"
                sport_name, t = sport_file.split(".")
                filepath = f"engine/storage_engine/arbs_found/"
                try:
                    original_umask = os.umask(0)
                    os.makedirs(filepath, exist_ok=True, mode=0o770)
                except Exception as e:
                    message = "Problem With Creating File Path For Processing Data"
                    log_error(message)
                finally:
                    os.umask(original_umask)
                    data = load_json(sport_folder_path)
                    count = 0
                    arb_dict = {}
                    for game, game_data in  data.items():
                        for formula, combinations in game_data.items():
                            for combination in combinations:
                                a_dict = {}
                                market_list = []
                                type_list = []
                                if combination:
                                    if formula == "1" and len(combination) == 2:
                                        for a_market in combination:
                                            for bookie, market in a_market.items():
                                                if bookie in a_dict:
                                                    a_dict[f"{bookie}"] = market
                                                else:
                                                    a_dict[bookie] = market
                                                for market_type, odds in market.items():
                                                    market_list.append(odds)
                                                    type_list.append(market_type)
                                        L = Find_arbitrage(formula, market_list)
                                        if L == None: L = 1
                                        if L < 1:
                                            perc = "{}%".format(100 - (L * 100))
                                            a_dict["Percent Profit"] = perc
                                            a_dict["Formula Type"] = formula
                                            arb_dict[game] = a_dict
                                            count += 1
                                    elif formula != "1" and len(combination) == 3:
                                        for a_market in combination:
                                            for bookie, market in a_market.items():
                                                if bookie in a_dict:
                                                    a_dict[f"+ {bookie}"] = market
                                                else:
                                                    a_dict[bookie] = market
                                                for market_type, odds in market.items():
                                                    market_list.append(odds)
                                                    type_list.append(market_type)
                                        L = Find_arbitrage(formula, market_list)
                                        if L == None: L = 1
                                        if L < 1:
                                            perc = "{}%".format(100 - (L * 100))
                                            a_dict["Percent Profit"] = perc
                                            a_dict["Formula Type"] = formula
                                            arb_dict[game] = a_dict
                                            count += 1
                                    else:
                                        pass
                                else:
                                    pass
                    file = f"{filepath}/{filename}"           
                    log_success(f"Number of Arbitrage found in this historical data is {count}") 
                    save_json(sport_folder_path, file, arb_dict)
        except Exception as e:
            message = f"Error with finding arbs in {sport_folder_path}, filename: {filename}"
            log_exception(message)
   

get_arbs()

