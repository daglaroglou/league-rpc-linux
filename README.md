![Logo](https://github.com/daglaroglou/league-rpc-linux/blob/main/assets/league-rpc.png)

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Python](https://img.shields.io/badge/Python-FCC624?style=for-the-badge&logo=python&logoColor=blue)

League of Legends Discord Rich Presence for Linux (WINE / Lutris)

## Installation
1. Download the source code  (You can clone it if you have git installed and know how to use it)
2. Extract the .zip (If using git just do `cd league-rpc-linux`)
3. Install dependencies using `pip3 install -r requirements.txt` or `python3 setup.py`
4. Run `python3 main.py`

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

## This is a fork from [daglaroglou/league-rpc-linux](https://github.com/daglaroglou/league-rpc-linux)
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=daglaroglou&repo=league-rpc-linux)](https://github.com/daglaroglou/league-rpc-linux)

I'm planning to add more features and maybe make the RPC more similar to that of the official client, but considering other things going on in my life it might take a while
