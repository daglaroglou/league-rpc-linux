import requests
import urllib3
urllib3.disable_warnings()

from src.username import SummonerName

def KDA():
    try:
        data = requests.get(f'https://127.0.0.1:2999/liveclientdata/playerscores?summonerName={SummonerName()}', verify=False)
        parsed_data = data.json()
        kills = str(parsed_data["kills"])
        deaths = str(parsed_data["deaths"])
        assists = str(parsed_data["assists"])
    except:
        parsed_data = False
        kills = '?'
        deaths = '?'
        assists = '?'
    return kills+'/'+deaths+'/'+assists