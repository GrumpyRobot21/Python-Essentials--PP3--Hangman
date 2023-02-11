"""
 Import python modules
"""
import string  # ascii alphabet function
import time  # time sleep function
import random  # random selection module
import pyfiglet  # big letter graphics module
import gspread  # Imports gspread library.
from google.oauth2.service_account import Credentials
# Imports credentials class.


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')


class Colortext:  # pylint: disable=too-few-public-methods
    """adds text color classes for game"""
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    YELLOW = "\033[1;33m"
    BOLD = "\033[1m"

print("\033c", end='')

name = input(Colortext.BLUE + Colortext.BOLD + "What is your name? ")

print("\033c", end='')


def start_intro():
    """
    Generates game options for player: intro to the game, difficulty, rules.
    """
    print(
        Colortext.BOLD
        + Colortext.YELLOW
        + r"""
       ==============================================
       ==============================================
         ||                              \ \     |  |
         ||                               \ \    |  |
        /==\                               \ \   |  |
       |====|                               \ \  |  |
       |====|                                \ \ |  |
        \==/                                  \ \|  |
       //  \\                                  \ |  |
      //    \\                                  \|  |
     //      \\                                  |  |
     \\      //                                  |  |
      \\    //                                   |  |
       \\==//                                    |  |
    """
    )
    print(
        Colortext.BLUE
        + Colortext.BOLD
        + "Welcome " + Colortext.RED
        + Colortext.BOLD
        + name.upper() + Colortext.BLUE
        + Colortext.BOLD + " to ye olde game of HANGMAN!!!!")
    print(
        Colortext.BLUE
        + Colortext.BOLD
        + "\n\nYou must carefully select letters")
    print("in the vain hope of avoiding the gallows")
    print(
        "by guessing the word before it's too late!")
    print("Can you cheat the hangman's noose in time?")
    print(
        Colortext.BLUE
        + Colortext.BOLD
        + "Find out....if you dare!")

    print(
        Colortext.BLUE
        + Colortext.BOLD
        + "\n\nEnter "
        + Colortext.GREEN
        + Colortext.BOLD
        + "'p' "
        + Colortext.BLUE
        + Colortext.BOLD
        + "to continue: "
    )

    run = input("\n")
    if run != "p":
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "WRONG KEY!(I would go for the easy setting if I were you.)")
        time.sleep(3)
        print(
            "\033c", end=""
        )  # clears the console - \033 is the ASCII escape character.
        start_intro()
    else:
        print(Colortext.YELLOW + Colortext.BOLD + "\n\nGOOD LUCK!")
        time.sleep(2)
        print(
            "\033c", end=""
        )  # clears the console - \033 is the ASCII escape character.
        game_rules()