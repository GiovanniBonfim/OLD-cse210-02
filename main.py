"""
Author: Team E - 7am
Version: 1.0.0
Date: Jan 24th, 2022

Problem Statement:
Apply abtraction and using classes
through the Hilo game
using python

"""

# Plugins or Utils obtain OS utils
import shutil
import os
from director import Director


# Obtain number of column of the shell
terminalSize = shutil.get_terminal_size().columns
tittle = 'Hilo'


def clear_console():
    """ Clear the console accorging the the OS
    Returns: nothing
    """
    if os.name in ('nt', 'dos'):
        os.system('cls')
    else:
        os.system('clear')


# Print title center based on the size of their shell
def title_print(my_tittle):
    """Print a center title in console
    Parameters:
        my_tittle: String of the tittle
    Returns: nothing
    """
    tittle = f'{my_tittle}  - \U0001f601  \n'
    print(tittle.center(terminalSize))


def main():
    clear_console()
    title_print(tittle)
    director = Director()
    director.start_game()


if __name__ == "__main__":
    main()
