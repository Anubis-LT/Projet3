#! /usr/bin/env python3
# coding: utf-8
""""
Game: McGyver maze
Creator: Grégory Le Terte

Class: characters.py

"""

from random import sample
import sys

sys.path.append("./")
from src.constants import *

class Macgyver:
    """Class to manage the Macgyver moves and the items picking into the maze"""
    def __init__(self, structure_map):

        #Start position and items counter
        self.structure_map      = structure_map
        self.x                  = structure_map.start_x
        self.y                  = structure_map.start_y
        self.items_collected    = 0

    def move_up(self, structure_map):
        # Check if the hero can move up and if he's on an item square
        if structure_map.map_array[self.y - 1][self.x] != WALL_LETTER:
            structure_map.map_array[self.y][self.x] = FLOOR_LETTER
            self.y -= 1
            structure_map.map_array[self.y][self.x] = MCGYVER_LETTER
            self.collect_items(structure_map)
        return structure_map

    def move_down(self, structure_map):
        # Check if the hero can move down and if he's on an item square
        if structure_map.map_array[self.y + 1][self.x] != WALL_LETTER:
            structure_map.map_array[self.y][self.x] = FLOOR_LETTER
            self.y += 1
            structure_map.map_array[self.y][self.x] = MCGYVER_LETTER
            self.collect_items(structure_map)
        return structure_map

    def move_right(self, structure_map):
        # Check if the hero can move right and if he's on an item square
        if structure_map.map_array[self.y][self.x + 1] != WALL_LETTER:
            structure_map.map_array[self.y][self.x] = FLOOR_LETTER
            self.x += 1
            structure_map.map_array[self.y][self.x] = MCGYVER_LETTER
            self.collect_items(structure_map)
        return map

    def move_left(self, structure_map):
        # Check if the hero can move left and if he's on an item square
        if structure_map.map_array[self.y][self.x - 1] != WALL_LETTER:
            if self.x-1>=0:
                structure_map.map_array[self.y][self.x] = FLOOR_LETTER
                self.x -= 1
                structure_map.map_array[self.y][self.x] = MCGYVER_LETTER
                self.collect_items(structure_map)
        return structure_map

    def collect_items(self, structure_map):
        # Check if the hero position is also an item position, and increments the backpack
        # The item position is moved away to avoid repetitions
        if (self.y, self.x) == structure_map.items[0]:
            self.items_collected += 1
            structure_map.items[0] = (14, 0)
        elif (self.y, self.x) == structure_map.items[1]:
            self.items_collected += 1
            structure_map.items[1] = (14, 1)
        elif (self.y, self.x) == structure_map.items[2]:
            self.items_collected += 1
            structure_map.items[2] = (14, 2)

class Structure_map:
     # Class which reads the map file, extract all the characters and places items randomly

    def __init__(self, filename):
        """Lists of the entire map, the start coordonates
        and of all the available squares to place items"""
        self.filename       = filename
        self.map_array      = []
        self.items          = []
        self.start_x        = []
        self.start_y        = []

        """Method to create positions"""
        self.load_from_file()
        self.extract_positions()

    def load_from_file(self):
        # Loading map to make an array with all the file characters
        try:
            with open(self.filename, "r") as map_file:
                for line in map_file:
                    self.map_array.append(list(line.strip()))
        except FileNotFoundError:
            print("Couldn't open map file \"" + self.filename + "\"")

    def extract_positions(self):
        """Method to extract a start position, every path position into the map_array
        and using the random.sample function to select three items positions"""
        positions   = []
        start       = []

        for x, line in enumerate(self.map_array):
            for y, column in enumerate(line):
                if column == FLOOR_LETTER:
                    positions.append((x, y))
                elif column == MCGYVER_LETTER:
                    start.append((x, y))


        self.items = sample(positions, 3)
        self.map_array[self.items[0][0]][self.items[0][1]] = NEEDLE_LETTER
        self.map_array[self.items[1][0]][self.items[1][1]] = TUBE_LETTER
        self.map_array[self.items[2][0]][self.items[2][1]] = ETHER_LETTER
        self.start_y = start[0][0]
        self.start_x = start[0][1]