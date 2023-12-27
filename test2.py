#!/usr/bin/python
"""
    This module houses the class for 1xbet
    Author: Peter Ekwere
"""
from utils.logger.log import log_exception, log_success, log_error
import requests
import json
from difflib import SequenceMatcher
import requests
from datetime import datetime
from timeout_decorator import timeout
import os
import json
import difflib
from utils.process import process_games

process_games()

