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

def game_rules():
    """
    Rules for gameplay and player difficulty selection
    """
    print(
        Colortext.RED
        + Colortext.BOLD
        + "Select your difficulty level from the choices below")
    print(
        Colortext.RED
        + Colortext.BOLD
        + "and the challenge will begin.")
    print(
        Colortext.RED
        + Colortext.BOLD
        + "See you at the end .......of the rope!")
    print("\nEnter"
          + Colortext.BLUE
          + Colortext.BOLD
          + " '1' "
          + Colortext.RED
          + Colortext.BOLD
          + "for difficulty level - "
          + Colortext.YELLOW
          + "'Lemon Squeezy' "
          + Colortext.RED
          + Colortext.BOLD
          + "\nalso known as: "
          + Colortext.YELLOW
          + "'I can see the pub from up here!' \n\n"
          + Colortext.RED
          + Colortext.BOLD
          + "Enter"
          + Colortext.BLUE
          + Colortext.BOLD
          + " '2' "
          + Colortext.RED
          + Colortext.BOLD
          + "for difficulty level - "
          + Colortext.YELLOW
          + "'King of the Swingers!' "
          + Colortext.RED
          + Colortext.BOLD
          + "\nalso known as:"
          + Colortext.YELLOW
          + " 'That's a smidge on the tight side, cough cough!'")

    choose = input("\n")

    if choose == "1":  # Player selects the easiest challenge setting.
        lives = 10  # given 10 lives to start game with

        def hang_word_easy():
            """
            retrieves randonly chosen word from the easyword google sheet
            """
            easywords = SHEET.worksheet('easywords')
            easychoice = easywords.get_all_values()
            easy = random.choice(easychoice)
            choice1 = str(easy)[2:-2]  # removes brackets & quote marks
            return choice1.upper()  # returns random game word in upper case

        hang_word = hang_word_easy()
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "\n\nPlaying it safe eh " + name.upper() +
            "? or maybe prolonging the agony.....")
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "They do say that waiting is the worst!!")
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "\n\n All that nervous anticipation.....! ")
        time.sleep(5)  # 5 second delay
        print(
            "\033c", end=""
        )  # clears the console - \033 is the ASCII escape character.
        play_game(hang_word, lives)
    elif choose == "2":  # Player selects difficult challenge setting.
        lives = 5  # only given 5 lives to start game with

        def hang_word_hard():
            """
            retrieves randonly chosen word from the hardword google sheet
            """
            hardwords = SHEET.worksheet('hardwords')
            hardchoice = hardwords.get_all_values()
            hard = random.choice(hardchoice)
            choice2 = str(hard)[2:-2]
            return choice2.upper()

        hang_word = hang_word_hard()
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "\n\nOoh " + name.upper() + ", you're feeling brave aren't you!")
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "\n\nThis won't take long!")
        time.sleep(5)  # 5 second delay
        print(
            "\033c", end=""
        )  # clears the console - \033 is the ASCII escape character.
        play_game(hang_word, lives)
    else:  # Error message for incorrect choice.
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "\n\nNot getting the 'hang' of this are you " + name.upper() +
            "?")
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "(do you see what I did there?).")
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "\n\nLet's try this again...")
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "\n\nChoose either 1 or 2 to get this show on the road!")
        time.sleep(5)  # 5 second delay
        print(
            "\033c", end=""
        )  # clears the console - \033 s the ASCII escape character.
        game_rules()        