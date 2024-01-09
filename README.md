# OddsAfrica-API
The is the first version of this API project with more versions coming later, The aim of this projects was to collectively cover fundamental concepts of higher level programming. The goal of The project is to eventually provide odds from all markets in each game across all the main betsites in Africa.
If you found this Repo Helpfull please dont hesitate to drop a star🙏😌

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [Usage](#usage)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)


## Environment
This project is interpreted/tested on Windows using the GitBash cmd using Python (version 3.11.3)

## Installation
* Clone this repository: `git clone https://github.com/PeterEkwere/OddsAfrica-API.git`
* Access OddsAfrica-API directory: `cd OddsAfrica-API`



## Usage
There Are Two way to use this API

### Example 1

```
$ python run.py 
```
##### You can find the output in [bookie_storage](/engine/storage_engine/bookie_storage)


### Example 2

Import the needed bookmaker:
```
from engine.bookie_models.sportybet_model import SportyBet
```
Then Access the bookmaker

```
bookie = Sportybet()
```

Then get the needed games:
Note: inorder to get the specific sport you will need to pass them as Arguments to the get_games method
```
data = bookie.Get_games("football").
print(data)
```

#### OUTPUT
```
  "Australia": {
    "A-League, Women": {
      "Brisbane Roar FC vs Wellington Phoenix": {
        "1X2": {
          "1": 2.1,
          "X": 3.6,
          "2": 2.9
        },
        "Over/Under": {
          "Over 1.5": 1.19,
          "Under 1.5": 4.0,
          "Over 2.5": 1.63,
          "Under 2.5": 2.1,
          "Over 3.5": 2.55,
          "Under 3.5": 1.43
        },
        "Double Chance": {
          "1X": 1.33,
          "12": 1.25,
          "X2": 1.59
        },
        "Handicap 0:1": {
          "1 (0:1)": 3.75,
          "X (0:1)": 4.0,
          "2 (0:1)": 1.64
        },
        "GG/NG": {
          "Yes": 1.54,
          "No": 2.15
        },
        "Draw No Bet": {
          "1": 1.57,
          "2": 2.15
        }..
```

## Supported betsites and Sports
```
BETSITES                       SPORTS
betpawa                        football
bet9ja                         basketball
paripesa                       ice Hockey
22bet                          volleyball
1xbet                          darts
sportybet                      esoccer
nairabet
betwinner
betking
livescorebet
merrybet
```
##### more betsites and sports comming soon...

## Bugs
No known bugs at this time. 

## Authors
Ekwere Peter - [Github](https://github.com/PeterEkwere)
