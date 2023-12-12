#!/usr/bin/python
"""
    This is The Main Module that will handle 
"""
from bookies_models.sportybet import SportyBet


league_list = ['football', 'basketball', 'iceHockey', 'tennis']
tennis_market_list = [' 2 Way O/U ', 'Over/Under']
iceHockey_market_list = ['3 Way & O/U ', 'Double Chance', 'Odd/Even', 'Over/Under']
football_market_list = ['Double Chance', 'GG/NG', 'Draw No Bet', '3 Way & O/U ', 'Over/Under']
basketball_market_list = [' 2 Way O/U ', 'Draw No Bet', ' 3 Way ', 'Over/Under']
myGames = SportyBet()
myGames.GetTodayGames(league_list[0], basketball_market_list[3])