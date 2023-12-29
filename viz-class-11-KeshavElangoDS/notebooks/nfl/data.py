import json
import pathlib
import time

import pandas as pd
import requests

access_level = 'trial'
version = 'v5'
language_code = 'en'
format = 'json'
your_api_key = '5a3fk94xfdhr5hgyrspdp43k'

def get_season_schedule() -> dict:
    """Get all games for the season
    """

    data_file = pathlib.Path('data/season_schedule.json')
    if not data_file.exists():
        data_file.parent.mkdir(exist_ok=True)
        with open(data_file, 'w') as season_schedule:
            uri = f'https://api.sportradar.us/nfl/official/{access_level}/{version}/{language_code}/games/current_season/schedule.{format}?api_key={your_api_key}'
            resp = requests.get(uri)
            json.dump(resp.json(), season_schedule)
            time.sleep(1) # rate limit is 1 request per second 
            #this is to make the request not exceed rate limit
            # sleep artificially

    with open(data_file) as season_schedule:
        return json.load(season_schedule)


def get_play_by_play(game_id: str) -> dict:
    """
    """
    data_file = pathlib.Path(f'data/game_{game_id}.json')
    if not data_file.exists():
        data_file.parent.mkdir(exist_ok=True)
        with open(data_file, 'w') as play_by_play:
            uri = f'https://api.sportradar.us/nfl/official/{access_level}/{version}/{language_code}/games/{game_id}/pbp.{format}?api_key={your_api_key}'
            resp = requests.get(uri)
            json.dump(resp.json(), play_by_play)        
            time.sleep(1)

    with open(data_file) as play_by_play:
        return json.load(play_by_play)


def get_game_rosters(game_id: str) -> dict:
    """
    """
    data_file = pathlib.Path(f'data/rosters_{game_id}.json')
    if not data_file.exists():
        data_file.parent.mkdir(exist_ok=True)
        with open(data_file, 'w') as play_by_play:
            uri = f'https://api.sportradar.us/nfl/official/{access_level}/{version}/{language_code}/games/{game_id}/roster.{format}?api_key={your_api_key}'
            resp = requests.get(uri)
            json.dump(resp.json(), play_by_play)        
            time.sleep(1)

    with open(data_file) as play_by_play:
        return json.load(play_by_play)
