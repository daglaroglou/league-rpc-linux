from pypresence import Presence
from src.champion import ChampionAsset, ChampionName
from src.gamemode import GameMode
from src.kda import KDA, kills, deaths, assists
import psutil
import time
import os

class Colors:
    dred = "\033[31m"
    dgreen = "\033[32m"
    yellow = "\033[33m"
    dblue = "\033[34m"
    dmagenta = "\033[35m"
    dcyan = "\033[36m"
    lgrey = "\033[37m"
    dgray = "\033[90m"
    red = "\033[91m"
    green = "\033[92m"
    orange = "\033[93m"
    blue = "\033[94m"
    magenta = "\033[95m"
    cyan = "\033[96m"
    white = "\033[97m"
    reset = "\033[0m"

print(Colors.yellow+'Checking if Discord is running...')
time.sleep(2)

def clear():
    os.system('clear')

def process_exists(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

if process_exists('Discord') or process_exists('DiscordPTB') or process_exists('DiscordCanary') == True:
    print(Colors.green+'Discord is running!'+Colors.dgray+'(1/2)'+Colors.reset)
    RPC = Presence('401518684763586560')
    RPC.connect()
else:
    print(Colors.red+'Discord not running!'+Colors.reset)
    exit()

print(Colors.yellow+'Checking if LeagueClient.exe is running...')
if process_exists('LeagueClient.exe') or process_exists('LeagueClientUx.exe') == True:
    print(Colors.green+'LeagueClient.exe is running!'+Colors.dgray+'(2/2)'+Colors.reset)
else:
    print(Colors.red+'LeagueClient.exe is not running!'+Colors.reset)
clear()

def PlayerState():
    if process_exists('LeagueClient.exe') or process_exists('LeagueClientUx.exe') == True:
        if process_exists('League of Legends.exe'): 
            return 'InGame'
        else:
            return 'InLobby'
    else:
        return 'NotLaunched'

champion = ChampionName()
asset = ChampionAsset(Champion=ChampionName())

while True:  
    if PlayerState() == 'InGame':
        start_time = time.time()
        while PlayerState() == 'InGame':
            time.sleep(5)
            RPC.update(
                large_image=asset,
                large_text=champion,
                details=GameMode(),
                state='In Game',
                small_image='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/LoL_icon.svg/2048px-LoL_icon.svg.png',
                small_text=str(kills(parsed_data=KDA()))+'/'+str(deaths(parsed_data=KDA()))+'/'+str(assists(parsed_data=KDA())),
                start=start_time
            )
    elif PlayerState() == 'InLobby':
        start_time = time.time()
        while PlayerState() == 'InLobby':
            time.sleep(5)
            RPC.update(
                large_image='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/LoL_icon.svg/2048px-LoL_icon.svg.png',
                large_text='In Lobby',
                state='In Lobby',
                start=start_time
            )
    elif PlayerState() == 'NotLaunched':
        print('League of Legends is not launched! Please launch it manually an re-run the script.')
        exit()
