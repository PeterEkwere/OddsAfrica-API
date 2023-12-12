#!/usr/bin/python
"""
    This Module Contains the Vault Class
    Author: Peter Ekwere
"""
import os
import json
from fabric.api import local, task


class Vault:
    """ This class Holds methods that will handles all serialization and deserilization of games and arbs
    """
    def __init__(self) -> None:
        pass
    

    
    
    def save_games(self, games, bookie_name, sport):
        """ This Function serializes games
        Args:
            bookie_name (str): This is the name of the bookie from which the games where gotten
            sport (_type_): this is the top of sport the games a played in
        """
        filename = f"{bookie_name}_{sport}.json"
        filepath = f"engine/storage_engine/bookie_storage/{sport}/"
        # Create the directory if it doesn't exist
        try:
            original_umask = os.umask(0)
            os.makedirs(filepath, exist_ok=True, mode=0o770)
        finally:
            os.umask(original_umask)
        file = f"{filepath}/{filename}"
        with open(file, "w") as a_file:          
            json.dump(games, a_file, indent=2)