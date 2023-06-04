import subprocess
import os
import pystyle

from commands import *

from colorama import Fore

class createTerminal:
    """
    Create the index CLI interface for Angel
    allowing for a user to run pre-programmed
    commands in the terminal (CMD).
    """
    def __init__(self):
        global inputCommand
        os.system("cls")
        os.system("title Angel")
        pystyle.Write.Print(pystyle.Center.XCenter("""
    ___                     __
   /   |  ____  ____ ____  / /
  / /| | / __ \/ __ `/ _ \/ / 
 / ___ |/ / / / /_/ /  __/ /  
/_/  |_/_/ /_/\__, /\___/_/   
             /____/           
        """) , pystyle.Colors.white_to_blue , interval = 0)
        pystyle.Write.Print(pystyle.Center.XCenter("\n\n>> Created by Coded#0001 on Discord") , pystyle.Colors.white_to_blue , interval = 0)
        while True:
            inputCommand = pystyle.Write.Input(pystyle.Center.XCenter("\n\nInput your command >> ") , pystyle.Colors.white , interval = 0).lower()
            if inputCommand in command_dictionary:
                command_dictionary[inputCommand]()

if __name__ == "__main__":
    createTerminal()