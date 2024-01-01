#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from utils.logger.log import log_exception, log_success, log_error
import os
import json
import difflib




def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(sport_name, file_path, data):
    with open(file_path, 'w') as file:
        log_success(f"Saving {sport_name}")
        json.dump(data, file, indent=2)
        
def similar_strings(string1, string2):
    matcher = difflib.SequenceMatcher(None, string1, string2)
    return matcher.ratio()

def find_similar_items(list1, list2, similarity_threshold=0.8):
    """ This Function takes two lists and compares every value in them using difflib

    Args:
        list1 (list): This is list 1
        list2 (list): This is list 2
        similarity_threshold (float, optional): similarity ratio must be minimum of 0.8. Defaults to 0.8.

    Returns:
        similar items: a list of list with each similar items grouped with each other
    """
    similar_items = []
    for item1 in list1:
        for item2 in list2:
            ratio = similar_strings(item1.lower(), item2.lower())
            #ratio = difflib.SequenceMatcher(None, item1, item2).ratio()
            if ratio >= similarity_threshold:
                similar_items.append([item1, item2])

    return similar_items


def arrange_betsite_files(folder_path):
    """ This Function takes the path to the folder containing all the scraped data
       Gathered from all the betsites For a particular sport

    Args:
        folder_path (str): This is the path to the data

    Returns:
        found_games (dict): a dictionary containg all the games with the 
                            values as all the combined data from all betsites partaining to that game
    """
    found_games = {}
    betsite_files = os.listdir(folder_path)
    
    #print(f"betsite_files are \n{betsite_files}")

    for i in range(len(betsite_files) - 1):
        for j in range(i + 1, len(betsite_files)):
            convert_list_dict1 = {}
            convert_list_dict2 = {}
            #print(f"Comparing {betsite_files[i]} -- {betsite_files[j]}")
            file1_path = os.path.join(folder_path, betsite_files[i])
            file2_path = os.path.join(folder_path, betsite_files[j])
            betsite1_data = load_json(file1_path)
            betsite2_data = load_json(file2_path)
            
            similar_countries = find_similar_items(betsite1_data.keys(), betsite2_data.keys())
            for country in similar_countries:
                # Assuming betsite data is a list, extract the first dictionary from it
                if isinstance(betsite1_data[country[0]], list) and betsite1_data[country[0]]:
                    for leagues in betsite1_data[country[0]]:
                        for key, value in leagues.items():
                            convert_list_dict1[key] = value
                    betsite1_data[country[0]] = convert_list_dict1
                elif isinstance(betsite1_data[country[0]], list) and not betsite1_data[country[0]]:
                    betsite1_data[country[0]] = {}
                else:
                    pass

                if isinstance(betsite2_data[country[1]], list) and betsite2_data[country[1]]:
                    for leagues in betsite2_data[country[1]]:
                        for key, value in leagues.items():
                            convert_list_dict2[key] = value
                    betsite2_data[country[1]] = convert_list_dict2
                elif isinstance(betsite2_data[country[1]], list) and not betsite2_data[country[1]]:
                    betsite2_data[country[1]] = {}
                else:
                    pass
                similar_leagues = find_similar_items(betsite1_data[country[0]].keys(), betsite2_data[country[1]].keys())

                for league in similar_leagues: 
                    similar_games = find_similar_items(betsite1_data[country[0]][league[0]].keys(), betsite2_data[country[1]][league[1]].keys())
                    for game in similar_games:
                        if game[0] not in found_games:
                            if "time" in betsite1_data[country[0]][league[0]][game[0]]:
                                time = betsite1_data[country[0]][league[0]][game[0]]["time"]
                            else:
                                time = "00:00"
                            filename = betsite_files[i]
                            betsite1_name = filename.split('_')[0]
                            filename2 = betsite_files[j]
                            betsite2_name = filename2.split('_')[0]
                            found_games[game[0]] = {
                                betsite1_name : betsite1_data[country[0]][league[0]][game[0]],
                                betsite2_name : betsite2_data[country[1]][league[1]][game[1]]
                            }
                        elif game[0] in found_games:
                            filename = betsite_files[i]
                            betsite1_name = filename.split('_')[0]
                            filename2 = betsite_files[j]
                            betsite2_name = filename2.split('_')[0]
                            if betsite1_name not in found_games[game[0]]:
                                found_games[game[0]][betsite1_name] = betsite1_data[country[0]][league[0]][game[0]]
                            if betsite2_name not in found_games[game[0]]:
                                found_games[game[0]][betsite2_name] = betsite2_data[country[1]][league[1]][game[1]]
                        else:
                            pass
    return found_games


def arrange_games():
    """ This function arrange all games data from all sports and saves them in their respective directory
    """
    sports_folder = 'engine/storage_engine/bookie_storage/'

    for sport_folder in os.listdir(sports_folder):
        try:
            sport_folder_path = os.path.join(sports_folder, sport_folder)
            if os.path.isdir(sport_folder_path):
                filename = f"{sport_folder}.json"
                filepath = f"engine/storage_engine/arranged_data/"
                try:
                    original_umask = os.umask(0)
                    os.makedirs(filepath, exist_ok=True, mode=0o770)
                except Exception as e:
                    message = "Problem With Creating File Path"
                finally:
                    os.umask(original_umask)
                found_games = arrange_betsite_files(sport_folder_path)
                file = f"{filepath}/{filename}"
                save_json(sport_folder, file, found_games)
        except Exception as e:
            message = f"Error with processing {sport_folder_path}, filename: {filename}, found_games dict is {found_games}"
            log_exception(message)
    