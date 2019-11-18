"""
Game: McGyver maze
Creator: Grégory Le Terte

Class: display.py

"""

import pygame as pg
import sys

sys.path.append("./")
from resources.filepy.constants import *


class Display:
    # Class only used for displaying the game, by loading images and blitting them on the screen
    def __init__(self):

        self.wall       = pg.image.load(WALL_IMG).convert_alpha()
        self.floor      = pg.image.load(FLOOR_IMG).convert_alpha()
        self.mcgyver    = pg.image.load(MCGYVER_IMG).convert_alpha()
        self.guardian   = pg.image.load(GUARDIAN_IMG).convert_alpha()
        self.tube       = pg.image.load(TUBE_IMG).convert_alpha()
        self.ether      = pg.image.load(ETHER_IMG).convert_alpha()
        self.needle     = pg.image.load(NEEDLE_IMG).convert_alpha()

    def display_map(self, structure_map, screen):
        # Method to analyze the map characters and blit an image on every one of them
        line_number = 0
        for line in structure_map.map_array:
            col_number = 0
            for sprite in line:
                x = col_number * SIZE_SPRITES
                y = line_number * SIZE_SPRITES

                if sprite == WALL_LETTER:
                    screen.blit(self.wall, (x, y))
                elif sprite == GUARDIAN_LETTER:
                    screen.blit(self.floor, (x, y))
                    screen.blit(self.guardian, (x, y))
                elif sprite == FLOOR_LETTER:
                    screen.blit(self.floor, (x, y))
                elif sprite == MCGYVER_LETTER:
                    screen.blit(self.floor, (x, y))
                    screen.blit(self.mcgyver, (x, y))
                elif sprite == NEEDLE_LETTER:
                    screen.blit(self.floor, (x, y))
                    screen.blit(self.needle, (x, y))
                elif sprite == TUBE_LETTER:
                    screen.blit(self.floor, (x, y))
                    screen.blit(self.tube, (x, y))
                elif sprite == ETHER_LETTER:
                    screen.blit(self.floor, (x, y))
                    screen.blit(self.ether, (x, y))
                col_number += 1
            line_number += 1
