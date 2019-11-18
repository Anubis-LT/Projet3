#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Game: McGyver maze
Creator: Grégory Le Terte

The game is all about McGyver struggling to find 3 items,
in order to put a guard to sleep and escape the maze.

main.py
"""

"""Only import the Game to lauch the program"""
import sys
sys.path.append("./resources/filepy")
from game import Game


def main():
    # Lauch the program, by calling the start method of the Game in folder resources/filepy
    # Instancie game
    load_game       = True
    number_level    = 0

    while load_game:

        game = Game(number_level)

        # start the game
        game.start()

        number_level = game.levelnumber

if __name__ == "__main__":
    main()
