import requests
import urllib3
urllib3.disable_warnings()

def ChampionName(Name):
    champ = '???'
    while champ == '???':
        try:
            data = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify=False)
            parsed_data = data.json()
            champ = parsed_data["allPlayers"][0]["championName"]
        except:
            champ = '???'
    if champ == 'Renata Glasc':
        champ = 'Renata'
    if champ == 'Dr. Mundo':
        champ = 'DrMundo'
    if champ == 'Miss Fortune':
        champ = 'MissFortune'
    if champ == "Kai'Sa":
        champ = 'KaiSa'
    if champ == "Kog'Maw":
        champ = 'KogMaw'
    if champ == "Rek'Sai":
        champ = 'RekSai'
    if champ == "K'Sante":
        champ = 'KSante'
    if champ == "Nunu & Willump":
        champ = 'Nunu'
    if champ == 'Twisted Fate':
        champ = 'TwistedFate'
    if champ == "Vel'Koz":
        champ = 'Velkoz'
    if champ == 'Xin Zhao':
        champ = 'XinZhao'
    if champ == 'Master Yi':
        champ == 'MasterYi'
        
    return champ

def ChampionAsset(Champion):
    try:
        icon = f"http://ddragon.leagueoflegends.com/cdn/13.10.1/img/champion/{Champion}.png"
    except:
        icon = 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/-1.png'
    return icon
