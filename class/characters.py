""""
Game: McGyver maze
Creator: Grégory Le Terte

Class: class_characters.py


"""

from item import Inventory
from random import randint
from config_json import Config_Json

# ============================
#  Base class of all personas
# ============================
class GamePersona():
    """
    Base class for all personas (Chars, NPC...) in the game
    """

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        parameters = Config_Json('./ressources/config.json')
        config_file=Config_Json.filemap(parameters, "constants")
        size_sprite = config_file.get("size_sprites")

        self.case_x = self.pos_x * size_sprite
        self.case_y = self.pos_y * size_sprite

    def case_position(self, lvl):
        """
        Returns the position of the persona
        """
        return (self.case_x, self.case_y)


# ===========================
#         NPCS' class
# ===========================
class NPC(GamePersona):
    """
    Class to create NPCS.
    """

    def __init__(self, lvl, name):
        self.name = name

        super().__init__()
        self.pos_x, self.pos_y = self.random_npc_position(lvl,name)

    def random_npc_position(self, lvl,name):
        parameters = Config_Json('./ressources/config.json')
        config_file = Config_Json.filemap(parameters, "constants")
        size_sprite = config_file.get("size_sprites")
        nb_sprite = config_file.get("nb_sprites")

        # load
        structure = Config_Json.filemap(parameters, "structures")
        floor = structure["floor"]
        floor_caractere = floor["caractere"]

        """
        Returns a random position for each instance of NPC
        """
        while lvl.maze_map[self.pos_y][self.pos_x] != floor_caractere:
            self.pos_x = randint(10, (nb_sprite - 1))
            self.pos_y = randint(10, (nb_sprite - 1))
        self.case_x = self.pos_x * size_sprite
        self.case_y = self.pos_y * size_sprite

        # set the case name as NPCS' initial
        lvl.maze_map[self.pos_y][self.pos_x] = name["caractere"]
        return self.case_x, self.case_y


# ===========================
#     Characters' class
# ===========================
class Character(GamePersona):
    """
    Class to create playable characters.
    """

    def __init__(self, lvl):
        self.lvl = lvl
        self.inventory = Inventory()
        super().__init__()