#!/usr/bin/env python3
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
import argparse
import logging
import time

# 3rd party
import psutil
from pypresence import Presence

# Locals
from src.champion import ChampionAsset, ChampionName
from src.gamemode import GameMode
from src.kda import KDA
from src.username import SummonerName


def process_exists(processName: str) -> bool:
    logging.info(f"Starting process checking iteration, Looking for {processName}")
    for proc in psutil.process_iter():
        logging.debug(f"Checking process {proc}")
        try:
            if processName.lower() in proc.name().lower():
                logging.info(f"Found process {proc} matching required name ({processName})")
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            logging.warning(f"Process {proc} returned 'NoSuchProcess', 'AccesDenied' or 'ZombieProcess'")
            pass
    logging.warning(f"Did not find process matching required name ({processName})")
    return False

def PlayerState() -> str:
    logging.info("Checking PlayerState")
    if process_exists('LeagueClient.exe') or process_exists('LeagueClientUx.exe'):
        if process_exists('League of Legends.exe'): 
            logging.debug("Current player state: InGame")
            return 'InGame'
        else:
            logging.debug("Current player state: InLobby")
            return 'InLobby'
    else:
        logging.warning("Current player state: NotLaunched")
        return 'NotLaunched'

def in_game_handler_fetch_data() -> tuple[str, str, str]:
    logging.info("Fetching champion and champion art data")
    start_time = time.time()
    logging.debug(f"Start time: {start_time}")
    username = SummonerName()
    logging.debug(f"Summoner Name: {username}")
    while username == False:
        logging.warning("Username is not found, trying again")
        username = SummonerName()
        logging.debug(f"Summoner Name: {username}")
        time.sleep(1)
    champion_name = ChampionName(Name=username)
    logging.debug(f"Champion Name: {champion_name}")
    champion_art = ChampionAsset(Champion=champion_name)
    logging.debug(f"Champion Asset: {champion_art}")

    return champion_name, champion_art, start_time

def scan_for_required_processes(end_after_n_attempts = 15) -> None:
    logging.info("Checking if discord and league of legends are both on")
    # System state variables
    scanning = True
    discord_on = False
    league_on = False
    attempts = 0
    while scanning:
        attempts += 1
        logging.debug(f"Scanning. Attempt number: {attempts}")
        # Checking discord
        if process_exists('Discord') or process_exists('DiscordPTB') or process_exists('DiscordCanary'):
            discord_on = True

        # Checking League
        if process_exists('LeagueClient.exe') or process_exists('LeagueClientUx.exe'):
            league_on = True

        # TODO: configurable
        if attempts >= end_after_n_attempts:
            logging.error(f"Scanning attempts exceeded maximum ({end_after_n_attempts}): Exiting")
            exit()

        # scanning = False if both discord and league were found to be active
        scanning = not ((discord_on == True) and (league_on == True))
        if not scanning:
            break
        logging.warning(f"Couldn't find required processes (Discord: {'found' if discord_on else 'not found'}; League of Legends: {'found' if league_on else 'not found'})")
        time.sleep(5)

def main() -> None:

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="enable debug logging", action="store_true")
    parser.add_argument("-i", "--info", help="enable info logging", action="store_true")
    parser.add_argument("-w", "--warning", help="enable warning logging", action="store_true")
    parser.add_argument("-e", "--error", help="enable error logging", action="store_true")
    args = parser.parse_args()

    # Configure logging based on command-line arguments
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    elif args.info:
        logging.basicConfig(level=logging.INFO)
    elif args.warning:
        logging.basicConfig(level=logging.WARNING)
    elif args.error:
        logging.basicConfig(level=logging.ERROR)
    else:
        logging.basicConfig(level=logging.ERROR)

    attempts_to_quit = 0
    logging.info("Starting LoL RPC for Linux")
    # Scanning
    scan_for_required_processes()

    logging.debug("Attempting RPC connection with discord client")
    RPC = Presence("863018853482889236")
    RPC.connect()
    logging.info("RPC Connection succesfull")

    player_state = PlayerState()
    restart_loop = False
    while True:
        if player_state != 'NotLaunched':
            if player_state == 'InGame':
                champion_name, champion_art, start_time = in_game_handler_fetch_data()
                while player_state == 'InGame':
                    gamemode = GameMode()
                    logging.debug(f"Updating RPC: Champion {champion_name} ChampionArt: {champion_art} Gamemode:{gamemode} StartTime: {start_time}")
                    print(champion_art + "\n" + champion_name)   
                    RPC.update(
                        large_image=champion_art,
                        large_text=champion_name,
                        details=gamemode,
                        state='In Game',
                        small_image='https://freepngimg.com/save/85643-blue-league-legends-icons-of-symbol-garena/1600x1600.png',
                        small_text=KDA(),
                        start=start_time
                    )
                    logging.debug("Updating succesfull")
                    # We check the player state again to make sure we're still in game
                    player_state = PlayerState()
            elif player_state == 'InLobby':
                start_time = time.time()
                while player_state == 'InLobby':
                    logging.debug(f"Updating RPC: StartTime: {start_time}")
                    RPC.update(
                        large_image='https://freepngimg.com/save/85643-blue-league-legends-icons-of-symbol-garena/1600x1600.png',
                        large_text='In Lobby',
                        state='In Lobby',
                        start=start_time
                    )
                    logging.debug("Updating succesfull")
                    # We check the player state again to make sure we're still in lobby
                    player_state = PlayerState()
            continue
        else:
            logging.warning("Player state: NotLaunched. Seems like league processes stopped or are invisible. Waiting 5s")
            time.sleep(5)
            player_state = PlayerState()
            if player_state == "NotLaunched":
                logging.error("Player state is still NotLaunched: meaning either League of Legends is closed or something wrong happened. If League was closed while running the script this error can be ignored")
                exit()

if __name__ == "__main__":
    main()
