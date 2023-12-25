import requests
import json
from utils.parser.bookies_parsers.merrybet_parser import extract_merrybet

#url = "https://www.merrybet.com/rest/market/categories/multi/1060/events"
#res = requests.get(url)
with open("merrybet_test.json", "r") as file:
    data = json.load(file)
    dict = extract_merrybet(data)

with open("extracted.json", "w") as file:
    json.dump(dict, file, indent=2)
