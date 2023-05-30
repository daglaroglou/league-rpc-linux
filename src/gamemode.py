import requests

import urllib3
urllib3.disable_warnings()

def GameMode():
    try:
        data = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify=False)
        parsed_data = data.json()
        game_mode = parsed_data["gameData"]["gameMode"]
    except:
        data = False
        game_mode = False
    if game_mode == 'PRACTICETOOL':
        return 'Summoner\'s Rift (Custom)'
    elif game_mode == 'ARAM':
        return 'Howling Abyss (ARAM)'
    elif game_mode == 'CLASSIC':
        return 'Summoner\'s Rift (Normal)'
    elif game_mode == 'TUTORIAL':
        return 'Summoner\'s Rift (Tutorial)'
    elif game_mode == 'URF':
        return 'Summoner\'s Rift (URF)'
    else:
        return '???'