""""
Game: McGyver maze
Creator: Grégory Le Terte

Class: class_level.py


"""
import os
from random import randint
from item import Item

# ===========================
#         Level class
# ===========================
class Level:
    """
    This is to generate the level's maze and items positions
    """

    def __init__(self, lvl_file, required_items):
        self.pathfile = os.getcwd()+"/ressources/maps/"+lvl_file.get("filemap")
        self.items = {}
        self.generate_from_file()

        #
        self.nbsprites = lvl_file.get("nb_sprites")

        """
        For each item key in required_items,
        set each item in the items dict of the Level class
        by instanciating it with the Item class,
        taking in parameter the random_pos method of the Level class.
        This results in {"item_key": <xxx.Item object at *******>}.
        """
        for item in required_items.keys():
            self.items[item] = Item(self.random_pos(self.nbsprites))
        """
        Generates a 2D array to iterate on,
        to display the lvl in the display_lvl method.
        """

    def generate_from_file(self):
        with open(self.pathfile, "r") as lvl_file:
            """
            Nested list comprehension to build a 2D array,
            breaking down the specified lvl_file into rows and cols.
            """
            self.maze_map = [
                [sprite for sprite in line if sprite != "\n"]
                for line in lvl_file
            ]

    def random_pos(self,nbsprites):
        """
        While self.maze_map[pos_y][pos_x] is not on a free space,
        search for a random position.
        Then set this random position to the *
        This is to avoid items superposition.
        """
        pos_x = 0
        pos_y = 0

        while self.maze_map[pos_y][pos_x] != "":
            pos_x = randint(1, (int(nbsprites) - 1))
            pos_y = randint(1, (int(nbsprites) - 1))
            self.maze_map[pos_y][pos_x] = "*"
            return pos_x, pos_y