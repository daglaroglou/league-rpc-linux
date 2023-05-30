import requests
import urllib3
urllib3.disable_warnings()

from src.username import SummonerName

def KDA():
    try:
        data = requests.get(f'https://127.0.0.1:2999/liveclientdata/playerscores?summonerName={SummonerName()}', verify=False)
        parsed_data = data.json()
    except:
        data = False
        parsed_data = False
    return parsed_data
    
def kills(parsed_data):
    if parsed_data != False:
        kills = parsed_data["kills"]
    else:
        kills = '?'
    return kills
def deaths(parsed_data):
    if parsed_data != False:
        deaths = parsed_data["deaths"]
    else:
        deaths = '?'
    return deaths
def assists(parsed_data):
    if parsed_data != False:
        assists = parsed_data["assists"]
    else:
        assists = '?'
    return assists