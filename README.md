![Logo](https://github.com/daglaroglou/league-rpc-linux/blob/main/assets/league-rpc.png)

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Python](https://img.shields.io/badge/Python-FCC624?style=for-the-badge&logo=python&logoColor=blue)

League of Legends Discord Rich Presence for Linux (WINE / Lutris)

## Installation
1. Download the source code  (You can clone it if you have git installed and know how to use it)
2. Extract the .zip (If using git just do `cd league-rpc-linux`)
3. Install dependencies using `pip3 install -r requirements.txt` or `python3 setup.py`
4. Run `python3 main.py`

## Using with lutris
To use this code with Lutris you need to install it (no need for step 4 tho)
Then
1. Open lutris
2. Right click on League of Legends and hit configure
3. Go in the System Options tab
4. Enable Advanced (Top roght toggle)
5. Scroll down to pre-launch script
6. Click browse and select the main.py file
(Make sure that the file is executable, if it isn't open a terminal and type `chmod +x /path/to/league-rpc-linux/main.py` changing the path according to your file structure

## VERY IMPORTANT: Issues with locales
While testing on Italian game language the script would crash when playing Nunu but not some other champs like Mordekaiser
Turns out the issue is the script expects "Nunu & Willump" to convert it to "Nunu" but not "Nunu e Willump" which is the italian version
A fix for this has already been implemented but many more could come up, and therefore i ask of anyone who encounters such bugs to report it in the issues tab, and the issue will be fixed right away (as it's just adding more to the if statements, easy stuff)
Also you should probably keep the script up to date if any new fixes roll out

## FAQ
- Is this gonna ban my account?
> No. This uses the local Riot's API which runs at `127.0.0.1:2999` at your computer. Besides that, you are resoinsible for using it.
- Is it legal?
> By no means is this affiliated or supported by Riot Games. This means im the only maintainer and owner.
- Does it support TFT?
> No. At least for now.
- Is this working on Windows?
> It could probably run as expected there as well (probably some minor adjustments needed) but Windows already have native Rich Presence support for the game.
- I got a question
> Feel free to contact me on socials or open an issue here!
