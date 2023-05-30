import requests
import urllib3
urllib3.disable_warnings()

def ChampionName():
    try:
        data = requests.get('https://127.0.0.1:2999/liveclientdata/activeplayer', verify=False)
        parsed_data = data.json()
        champ = parsed_data["abilities"]["E"]["id"][:-1]
    except:
        data = False
        parsed_data = False
        champ = '???'
    return champ

def ChampionAsset(Champion):
    try:
        icon = f"http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/{Champion}.png"
    except:
        icon = 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/-1.png'
    return icon
