import os
import time

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
time.sleep(1.5)

print(f'{Colors.dmagenta}Installing dependencies...{Colors.reset}')

os.system('pip3 install pypresence requests psutil')
