#!/usr/bin/env python3

import sys

player = dict[str | None, int, int]

current_player: player = {"name": None, "t_strike": 0, "t_matches" : 0}

for line in sys.stdin:
    player_name, player_strike = line.strip().split("\t")
    player_strike = float(player_strike)
    
    if player_name == current_player.get("name"):
        current_player["t_strike"] += player_strike
        current_player["t_matches"] += 1
	
    else:
        if current_player.get("name"):
            agg_strike = round(current_player.get("t_strike") / current_player.get("t_matches"), 3)
            print(f'{{"name": "{current_player.get("name")}", "strike_rate": {agg_strike}}}')
        current_player = {"name": player_name, "t_strike": player_strike, "t_matches": 1}

if current_player:
    agg_strike = round(current_player.get("t_strike") / current_player.get("t_matches"), 3)
    print(f'{{"name": "{current_player.get("name")}", "strike_rate": {agg_strike}}}')
