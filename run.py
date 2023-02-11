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