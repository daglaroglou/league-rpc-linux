from pypresence import Presence
from src.champion import ChampionAsset, ChampionName
from src.gamemode import GameMode
from src.username import SummonerName
from src.kda import KDA
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

print(f'''
{Colors.yellow}  _                                  {Colors.dblue} _____  _____   _____ {Colors.reset}
{Colors.yellow} | |                                 {Colors.dblue}|  __ \|  __ \ / ____|{Colors.reset}
{Colors.yellow} | |     ___  __ _  __ _ _   _  ___  {Colors.dblue}| |__) | |__) | |     {Colors.reset}
{Colors.yellow} | |    / _ \/ _` |/ _` | | | |/ _ \ {Colors.dblue}|  _  /|  ___/| |     {Colors.reset}
{Colors.yellow} | |___|  __/ (_| | (_| | |_| |  __/ {Colors.dblue}| | \ \| |    | |____ {Colors.reset}
{Colors.yellow} |______\___|\__,_|\__, |\__,_|\___| {Colors.dblue}|_|  \_\_|     \_____|{Colors.reset}
{Colors.yellow}                    __/ |                                                {Colors.reset}
{Colors.yellow}                   |___/                                                 {Colors.reset}
''')
time.sleep(2)

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

if process_exists('Discord') or process_exists('DiscordPTB') or process_exists('DiscordCanary') or process_exists('electron') == True:
    print(Colors.green+'Discord is running!'+Colors.dgray+'(1/2)'+Colors.reset)
    RPC = Presence('401518684763586560')
    RPC.connect()
else:
    print(Colors.red+'Discord not running!'+Colors.reset)
    exit()

attempts = 0

print(Colors.yellow+'Checking if LeagueClient.exe is running... If you\'re launching the game this may take a while.')

while(attempts <= 10):
    time.sleep(6)
    if process_exists('LeagueClient.exe') or process_exists('LeagueClientUx.exe') == True:
        print(Colors.green+'LeagueClient.exe is running!'+Colors.dgray+'(2/2)'+Colors.reset)
        break
    elif (attempts == 9):
        print(Colors.red+'LeagueClient.exe is not running, or was not open in time! Shutting down...'+Colors.reset)
        time.sleep(2)
        exit()
    else:
        attempts += 1


time.sleep(1)

print(f'{Colors.green}\nRich Presence utilized!')

def PlayerState():
    if process_exists('LeagueClient.exe') or process_exists('LeagueClientUx.exe') == True:
        if process_exists('League of Legends.exe'): 
            return 'InGame'
        else:
            return 'InLobby'
    else:
        return 'NotLaunched'

while PlayerState() != 'NotLaunched':
    if PlayerState() == 'InGame':
        start_time = time.time()
        username = SummonerName()
        while username == False:
            username = SummonerName()
            time.sleep(5)
        c = ChampionName(Name=SummonerName())
        c_ = c[:]
        ca = ChampionAsset(Champion=ChampionName(Name=SummonerName()))
        ca_ = ca[:]
        while PlayerState() == 'InGame':
            RPC.update(
                large_image=ca_,
                large_text=c_,
                details=GameMode(),
                state='In Game',
                small_image='https://freepngimg.com/save/85643-blue-league-legends-icons-of-symbol-garena/1600x1600.png',
                small_text=KDA(),
                start=start_time
            )
    elif PlayerState() == 'InLobby':
        start_time = time.time()
        while PlayerState() == 'InLobby':
            RPC.update(
                large_image='https://freepngimg.com/save/85643-blue-league-legends-icons-of-symbol-garena/1600x1600.png',
                large_text='In Lobby',
                state='In Lobby',
                start=start_time
            )
else:
    print(f'{Colors.red}LeagueOfLegends.exe was terminated. RPC shuting down...'+Colors.reset)
    exit()
