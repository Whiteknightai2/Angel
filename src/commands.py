import pystyle
import os
import discord
import yaml

from dpyConsole import Console
from discord.ext import commands

with open("configs\\angel.yaml") as configFile:
    yaml.safe_load(configFile)
    discordToken = configFile["Angel_Configs"]["Discord"]["Token"]
def help_command():
    pystyle.Write.Print(pystyle.Center.XCenter(
        """
        \nHelp - The command you ran...
        \nExit - Exit the program | Usage: exit
        \nTarget - This will run a full search on a target (passwords included) | Usage: Target {user} {link}
        \nDiscord - Scrape information about a Discord user. | Usage: discord {userID}
        \nFacebook - Scrape information about a Facebook user | Usage: Facebook {user}
        \nGithub - Scrape information about a Github user | Usage: Github {user}
        \nGuilded - Scrape information about a Guilded user | Usage: Guilded {user}
        \nInstagram - Scrape information about an Instagram user | Usage: Instagram {user}
        \nLinkedin - Scrape information about a Linkedin user | Usage: Linkedin {user}
        \nNintendo - Scrape information about a Nintendo user | Usage: Nintendo {user}
        \nPlaystation - Scrape information about a Playstation user | Usage: Playstation {user}
        \nReddit - Scrape information about a Reddit user | Usage: Reddit {user}
        \nSnapchat - Scrape information about a Snapchat | Usage: Snapchat {user}
        \nSpotify - Scrape information about a Spotify user | Usage: Spotify {user}
        \nSteam - Scrape information about a Steam user | Usage: Steam {user}
        \nTelegram - Scrape information about a Telegram user | Usage: Telegram {user}
        \nTwitter - Scrape information about a Twitter user | Usage: Twitter {user}
        \nWhatsapp - Scrape information about a Whatsapp user | Usage: Whatsapp {user}
        \nXbox - Scrape information about a Xbox user | Usage: Xbox {user}
        \nYoutube - Scrape information about a Youtube user | Usage: Youtube {user}
        """
        ) , pystyle.Colors.blue , interval = 0)
    
def exit_command():
    os.system("cls")
    os._exit(0)

def discord_command():
    Angel = commands.Bot(command_prefix = "c!" , intents = discord.Intents().all() , help_command = False)
    my_console = Console(Angel)
    @my_console.command()
    async def getTargetInfo(target: int) -> str:
        ## PUBLIC FLAGS ##
        publicFlags = []
        if target.public_flag.staff == True:
            publicFlags.append("Stafff")
        if target.public_flag.partner == True:
            publicFlags.append("Partner")
    Angel.run(discordToken)

command_dictionary = {"help" : help_command,
                      "exit" : exit_command}