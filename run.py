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


def play_game(hang_word, lives):
    """
    Game play function
    """
    player_letters = set(hang_word)  # creates set of random word letters
    characters = set(
        string.ascii_uppercase
    )  # Ascii letters pool for user and word letter choices (in uppercase)
    used = (
        set()
    )  # creates a set of the letters that have been used in the game

    print(
        Colortext.GREEN
        + Colortext.BOLD
        + "Now we get to test your nerve!!!")
    print(
        Colortext.GREEN
        + Colortext.BOLD
        + "Guess the word and escape the noose this day...!")
    print(
        "\nYou have",
        lives,
        "lives left before the big drop...\nDon't lose them all at once!",
    )

    while player_letters and lives > 0:
        # loops user letter guesses
        print(
            Colortext.RED + player_lives(lives)
        )  # Prints player hangman 'life' graphic
        check_list = [
            letter if letter in used else "-" for letter in hang_word
        ]  # Comprehension substitutes dashes for the letters
        # and checks to see if letters have been used.
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "\nYour word to guess for this round is: ",
            " ".join(check_list),
        )  # presents list of dashes for randomly chosen game word
        print(
            "\nYou have already used these letters: ",
            " ".join(used),
        )

        user_guess = input("\nWhat's your best guess? \n").upper()
        if user_guess in characters - used:
            used.add(user_guess)  # when user chooses a letter
            # add it to the used set
            if user_guess in player_letters:
                player_letters.remove(user_guess)
                print(" ")  # For correct user guesses.
                # Adds letter(s) to word template
                print(
                    Colortext.YELLOW
                    + Colortext.BOLD
                    + "Phew! That WAS a lucky guess! It's in there!"
                )
                time.sleep(3)  # 3 second delay
            else:
                lives = lives - 1
                # Incorrect user choice and deducts life from tally
                print(
                    Colortext.YELLOW
                    + Colortext.BOLD
                    + "\nOh dear, oh dear. One step closer to the drop!..\n",
                    user_guess,
                    " 'ain't in the word my friend!",
                )
                time.sleep(4)  # 4 second delay
        elif (
                user_guess in used
        ):  # When user chooses letter already used
            # and identified as being in the used set
            print(
                Colortext.YELLOW
                + Colortext.BOLD
                + "\nTrying to pull a fast one are you?")
            print(
                Colortext.YELLOW
                + Colortext.BOLD
                + "\nYou can't use the same letter twice!")
            time.sleep(3)  # 3 second delay
        else:  # when user chooses non ascii qualified character.
            print(
                Colortext.YELLOW
                + Colortext.BOLD
                + "\nHehehe, Time to make better choices "
                + name.upper() + ".")
            print(
                Colortext.YELLOW
                + Colortext.BOLD
                + "\n\nPreferably one's you haven't made already....")
            time.sleep(4)  # 4 second delay
        print(
            "\033c", end=""
        )  # clears the console - \033 s the ASCII escape character.
    if lives == 0:
        print(Colortext.RED + player_lives(lives))
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "\nOUCH!! I bet that stings a bit " + name.upper() + "!")
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "You didn't beat the hangman this time around,")
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "but in the wonderful realm of the digital world")
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "you may get the chance to play again...")
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "\nif you've the 'neck' for it that is.")
        print("\nBy the way, the word you missed was: "
              + Colortext.YELLOW + hang_word)
        time.sleep(10)  # 12 second delay
    else:
        print(Colortext.RED + player_lives(lives))
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "\nWell done " + name.upper() +
            "!! (You just cost me a fiver though...)")
        print(
            Colortext.GREEN
            + Colortext.BOLD
            + "I'll bet you fancy another try now?")
        time.sleep(6)  # 4 second delay

    print(
        "\033c", end=""
    )  # clears the console - \033 is the ASCII escape character.
    re_run()  # goes to game replay options


def re_run():
    """
    Option to replay game function
    """
    again = pyfiglet.figlet_format("Try Again! \n" + name.upper() + "")
    print(Colortext.RED + Colortext.BOLD + again)
    print(
        Colortext.GREEN
        + Colortext.BOLD
        + "\n\n(Well, we had to include the statutory "
        + Colortext.YELLOW
        + Colortext.BOLD
        + "'BIG LETTERS'"
        + Colortext.GREEN
        + Colortext.BOLD
        + " at some point..)"
        + "\n\nNow, to give this fabulously designed game another shot"
        + "\n\nEnter "
        + Colortext.YELLOW
        + Colortext.BOLD
        + "'y'"
        + Colortext.GREEN
        + Colortext.BOLD
        + " for 'Lets do this!' or..\n\nEnter "
        + Colortext.YELLOW
        + Colortext.BOLD
        + "'n'"
        + Colortext.GREEN
        + Colortext.BOLD
        + " for 'I'm a big Jessie'"
    )

    choice = input("\n")

    if choice == "y":  # Player elects to play again.
        print(
            Colortext.RED
            + Colortext.BOLD
            + "\n\nIf at first you don't succeed blah blah etc.\n\n")
        print("At least I get a chance to place another little bet!")

        time.sleep(6)  # 4 second delay
        print(
            "\033c", end=""
        )  # clears the console - \033 is the ASCII escape character.
        game_rules()
    elif choice == "n":  # Player selects difficult challenge setting.
        print(
            Colortext.RED
            + Colortext.BOLD
            + "\n\nNever mind " + name.upper() + ", I understand.")
        print(
            Colortext.RED
            + Colortext.BOLD
            + "Once bitten, twice shy.")
        print(
            Colortext.RED
            + Colortext.BOLD
            + "\n\nIt takes a strong backbone to play ")
        print(
            Colortext.RED
            + Colortext.BOLD
            + "this game more than once.")
        print(
            Colortext.RED
            + Colortext.BOLD
            + "\n\nThat's ok if you don't have what it takes....")
        time.sleep(6)  # 6 second delay
        print(
            "\033c", end=""
        )  # clears the console - \033 is the ASCII escape character.
        main()
    else:  # Error message for incorrect choice.
        print(
            Colortext.BLUE
            + Colortext.BOLD
            + "\n\nSTILL not getting the 'hang' of this are you"
            + name.upper() + "?")
        print(
            Colortext.BLUE
            + Colortext.BOLD
            + "\n\nLet's give this one more go shall we?")
        time.sleep(4)  # 4 second delay
        print(
            "\033c", end=""
        )  # clears the console - \033 s the ASCII escape character.
        re_run()


def player_lives(lives):
    """
    Remaining player lives with hangman game graphic
    """

    player_live = [
        """
    ______________
    ||  /        |
    || /         0
    ||/         /|\\
    ||           |
    ||         _/ \\
    ||
    ||
    ||
    ||____________
    """,
        """
    ______________
    ||  /        |
    || /         0
    ||/         /|\\
    ||           |
    ||         _/ \\
    ||
    ||
    ||
    ||____________

    """,
        """
    ______________
    ||  /        |
    || /         0
    ||/         /|\\
    ||           |
    ||         _/
    ||
    ||
    ||
    ||____________

    """,
        """
    ______________
    ||  /        |
    || /         0
    ||/         /|\\
    ||           |
    ||          /
    ||
    ||
    ||
    ||____________

    """,
        """
    ______________
    ||  /        |
    || /         0
    ||/         /|\\
    ||           |
    ||
    ||
    ||
    ||
    ||____________

    """,
        """
    ______________
    ||  /        |
    || /         0
    ||/         /|\\
    ||
    ||
    ||
    ||
    ||
    ||____________
    """,
        """
    ______________
    ||  /        |
    || /         0
    ||/         /|
    ||
    ||
    ||
    ||
    ||
    ||____________
    """,
        """
    ______________
    ||  /        |
    || /         0
    ||/          |
    ||
    ||
    ||
    ||
    ||
    ||____________

    """,
        """
    ______________
    ||  /        |
    || /         0
    ||/
    ||
    ||
    ||
    ||
    ||____________

    """,
        """
    ______________
    ||  /        |
    || /
    ||/
    ||
    ||
    ||
    ||
    ||
    ||____________

    """,
        """
    ______________
    ||  /
    || /
    ||/
    ||
    ||
    ||
    ||
    ||
    ||____________
    """,
    ]
    return player_live[lives]


def main():
    """
       Game starts
       """
    start_intro()


main()
