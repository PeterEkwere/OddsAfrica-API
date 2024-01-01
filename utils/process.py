#!/usr/bin/python
"""
    This module houses the Funcition for processing and extracting the need markets 
    Author: Peter Ekwere
"""
from utils.logger.log import log_error, log_exception, log_success
from utils.arrange import arrange_games
from engine.ArbBrain.arb import Find_arbitrage
from utils.extraction.extract_football_markets import process_football
from utils.extraction.extract_basketball_markets import process_basketball
from utils.extraction.extract_ice_hockey_markets import process_ice_hockey
from utils.extraction.extract_volleyball_markets import process_volleyball
from utils.extraction.extract_dart_markets import process_darts
from utils.arrange import save_json
import logging
import os




def process_games():
    """ This function processes the games to get the needed markets we will need from each bookie in a game
    """
    arranged_sports_folder = 'engine/storage_engine/arranged_data/'
    
    Special_function = {
        "volleyball": process_volleyball,
        "basketball": process_basketball,
        "football": process_football,
        "icehockey": process_ice_hockey,
        "darts": process_darts,
    }

    for sport_file in os.listdir(arranged_sports_folder):
        try:
            sport_folder_path = os.path.join(arranged_sports_folder, sport_file)
            if os.path.isfile(sport_folder_path):
                filename = f"{sport_file}"
                sport_name, t = sport_file.split(".")
                filepath = f"engine/storage_engine/processed_data/"
                try:
                    original_umask = os.umask(0)
                    os.makedirs(filepath, exist_ok=True, mode=0o770)
                except Exception as e:
                    message = "Problem With Creating File Path For Processing Data"
                    log_error(message)
                finally:
                    os.umask(original_umask)
                    if sport_name in Special_function:
                        clean_games = Special_function[sport_name](sport_folder_path)
                        file = f"{filepath}/{filename}"
                        save_json(sport_folder_path, file, clean_games)
                    else:
                        log_error(f"Sport File {sport_name} is not in special function")
        except Exception as e:
            message = f"Error with processing {sport_folder_path}, filename: {filename}"
            log_exception(message)  
