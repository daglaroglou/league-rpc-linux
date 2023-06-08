#############################################################
#  _                                   _____  _____   _____ #
# | |                                 |  __ \|  __ \ / ____|#
# | |     ___  __ _  __ _ _   _  ___  | |__) | |__) | |     #
# | |    / _ \/ _` |/ _` | | | |/ _ \ |  _  /|  ___/| |     #
# | |___|  __/ (_| | (_| | |_| |  __/ | | \ \| |    | |____ #
# |______\___|\__,_|\__, |\__,_|\___| |_|  \_\_|     \_____|#
#                    __/ |                                  #
#                   |___/                                   #             
#############################################################
# ZeroKun265/league-rpc-linux - forked from daglaroglou/league-rpc-linux

# Built ins
import logging
import os
import time

# 3rd party
import psutil
from pypresence import Presence

# Locals
from src.champion import ChampionAsset, ChampionName
from src.gamemode import GameMode
from src.kda import KDA
from src.username import SummonerName

def get_client_id():
    with open("client_id.txt", "r") as f:
        return f.read()

def process_exists(processName: str) -> bool:
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def PlayerState() -> str:
    if process_exists('LeagueClient.exe') or process_exists('LeagueClientUx.exe'):
        if process_exists('League of Legends.exe'): 
            return 'InGame'
        else:
            return 'InLobby'
    else:
        return 'NotLaunched'

def in_game_handler_fetch_data() -> tuple[str, str, str]:
    print(f"State: In Game\n") # TODO: logger
    start_time = time.time()
    username = SummonerName()
    while username == False:
        username = SummonerName()
        time.sleep(1)
    champion_name = ChampionName(Name=username)
    champion_asset = ChampionAsset(Champion=ChampionName(Name=SummonerName()))

    return champion_name, champion_asset, start_time

def scan_for_required_processes() -> None:
    while scanning:
        attempts += 1
        # Checking discord
        if process_exists('Discord') or process_exists('DiscordPTB') or process_exists('DiscordCanary') == True:
            discord_on = True
        else:
            pass

        # Checking League
        if process_exists('LeagueClient.exe') or process_exists('LeagueClientUx.exe') == True:
            league_on = True
        else:
            pass

        # TODO: configurable
        if attempts >= 10:
            # TODO: logger
            exit()

        # scanning = False if both discord and league were found to be active
        scanning = not ((discord_on == True) and (league_on == True))
        print("Not everything is on, waiting and trying again") # TODO: logger
        time.sleep(5)

def main() -> None:
    # System state variables
    scanning = True
    discord_on = False
    league_on = False
    attempts = 0
    # Scanning
    scan_for_required_processes()

    print("all good") # TODO: logger

    while player_state != 'NotLaunched':
        if player_state == 'InGame':
            champion_name, champion_art, start_time = in_game_handler_fetch_data()
            while player_state == 'InGame':
                RPC.update(
                    large_image=champion_art,
                    large_text=champion_name,
                    details=GameMode(),
                    state='In Game',
                    small_image='https://freepngimg.com/save/85643-blue-league-legends-icons-of-symbol-garena/1600x1600.png',
                    small_text=KDA(),
                    start=start_time
                )
                # We check the player state again to make sure we're still in game
                player_state = PlayerState()
        elif player_state == 'InLobby':
            print(f"State: In Lobby\n") #TODO: logger
            start_time = time.time()
            while player_state == 'InLobby':
                RPC.update(
                    large_image='https://freepngimg.com/save/85643-blue-league-legends-icons-of-symbol-garena/1600x1600.png',
                    large_text='In Lobby',
                    state='In Lobby',
                    start=start_time
                )
                # We check the player state again to make sure we're still in lobby
                player_state = PlayerState()
    else:
        print("seems like League is disconnected, trying again and quitting if not found") #TODO: actually implement this

if __name__ == "__main__":
    main()