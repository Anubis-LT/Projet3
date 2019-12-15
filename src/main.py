#!/usr/bin/python3
# coding: Utf-8

"""
Game    : McGyver maze
File    : main.py
Creator : Grégory Le Terte
Info    : The game is all about McGyver struggling to find 3 items,
          to put a guard to sleep and escape the maze. In addition a time
          management and 5 levels.
"""

from game import Game


def main():
    """ Game Launch """
    load_game = True
    number_level = 0
    time_game = 0

    # Loop while the player is in the levels or press to close the window
    while load_game:
        # Display the menu or loading a level
        game = Game(number_level, time_game)

        # Start the game
        game.start()

        # keeps in mind the level and time of the player
        number_level = game.level_number
        time_game = game.time_game


if __name__ == "__main__":
    # game launch
    main()
