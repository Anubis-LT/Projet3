#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Game: McGyver maze
Creator: Grégory Le Terte

The game is all about McGyver struggling to find 3 items,
in order to put a guard to sleep and escape the maze.

main.py

"""


import sys

sys.path.append("./class")

from level import Level
from characters import Character
from characters import Npc
from configjson import ConfigJson
from display import screen


# ===========================
#    Initialize the game
# ===========================
def launch_game():

    print("* McGyver Maze *")
    print("The game is all about McGyver struggling to find 3 items")
    print("in order to put a guard to sleep and escape the maze.")

    # ===========================
    #       Instantiations
    # ===========================

    # Instantiations 'parameters' from config.json
    parameters = ConfigJson('./ressources/config.json')

    # Instantiations 'map' from config.json
    file_map = ConfigJson.file_map(parameters, "constants")

    # Instantiations 'object' from config.json
    name_object = ConfigJson.file_map(parameters, "object")

    # Instantiations 'mac_gyver_maze' from 'file_map' and 'name_object' for ramdom
    mac_gyver_maze = Level(file_map, name_object)

    """
    Instantiations character, Npc from config.json
    """
    character   = ConfigJson.file_map(parameters, "characters")
    mcgyver     = Character(mac_gyver_maze)
    Npc(mac_gyver_maze, character["guardian"])

    # Display screen
    screen(mcgyver.lvl.structure)

    # Play game
    game = True

    while game:

        touch_user = input("Move Mac Gyver (U'UP' D'Down' L'left' R'Right' Q'Quit')  ?") \
            .strip() \
            .upper()

        stouch = "UDLRQ"

        if touch_user in stouch:
            if touch_user == "R":
                mcgyver.move("right")
                game = True
            if touch_user == "L":
                mcgyver.move("left")
                game = True
            if touch_user == "U":
                mcgyver.move("up")
                game = True
            if touch_user == "D":
                mcgyver.move("down")
                game = True
            if touch_user == "Q":
                response = input("Do you want to leave the game ? [Y/N] : ")
                response = response.upper()
                if response == "Y":
                    game = False

        if game:

            """ Until Mac Gyver did not retrieve the 3 objects"""
            if mcgyver.continue_game:

                # Display screen
                screen(mcgyver.lvl.structure)

            else:
                response = input("Do you want to play again ? [Y/N] : ")
                response = response.upper()
                if response == "Y":
                    launch_game()

    # End of game
    print("Good Bye, see you soon")

if __name__ == "__main__":
    launch_game()
