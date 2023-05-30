import requests
import urllib3
urllib3.disable_warnings()

def SummonerName():
    try:
        data = requests.get(f'https://127.0.0.1:2999/liveclientdata/activeplayername', verify=False)
        parsed_data = data.json()
    except:
        data = False
        parsed_data = False
    return str(parsed_data)