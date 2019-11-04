""""
Game: McGyver maze
Creator: Grégory Le Terte

Class: class_characters.py


"""

from random import randint
from configjson import ConfigJson
from item import Inventory


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

        parameters = ConfigJson('./ressources/config.json')
        config_file = ConfigJson.file_map(parameters, "constants")

        self.size_sprite = config_file.get("size_sprites")
        self.nb_sprite = config_file.get("nb_sprites")

        structure = ConfigJson.file_map(parameters, "structures")
        wall = structure["wall"]
        self.wall_letter = wall["caractere"]

        floor = structure["floor"]
        self.floor_letter = floor["caractere"]

        characters = ConfigJson.file_map(parameters, "characters")
        mcgyver = characters["mac_gyver"]
        self.mcgyver_letter = mcgyver["caractere"]

        self.case_x = self.pos_x * self.size_sprite
        self.case_y = self.pos_y * self.size_sprite


# ===========================
#         NPCS' class
# ===========================
class Npc(GamePersona):
    """
    Class to create NPCS.
    """

    def __init__(self, lvl, name):
        self.name = name
        if name["caractere"] != "M":
            super().__init__()
            self.pos_x, self.pos_y = self.random_npc_position(lvl, name)

    def random_npc_position(self, lvl, name):

        parameters = ConfigJson('./ressources/config.json')
        config_file = ConfigJson.file_map(parameters, "constants")
        size_sprite = config_file.get("size_sprites")
        nb_sprite = config_file.get("nb_sprites")

        """
        Returns a random position for each instance of NPC
        """
        while lvl.structure[self.pos_y][self.pos_x] != self.floor_letter:
            self.pos_x = randint(10, (int(nb_sprite) - 1))
            self.pos_y = randint(10, (int(nb_sprite) - 1))

        self.case_x = self.pos_x * int(size_sprite)
        self.case_y = self.pos_y * int(size_sprite)

        # set the case name as NPCS' initial
        lvl.structure[self.pos_y][self.pos_x] = name["caractere"]
        return self.case_x, self.case_y


## ===========================
#     Characters' class
# ===========================
class Character(GamePersona):
    """
    Class to create playable characters.
    """

    def __init__(self, lvl):
        self.lvl = lvl
        super().__init__()
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.nbObjectInventory = 0
        self.inventory = Inventory()
        self.continue_game = True

    def move(self, direction):
        """
        Defines the movement of the hero.
        Gets the direction specified in type(str),
        and gets the hero on the case if it's not a wall.
        """
        if direction == "right":
            # to not get out of the screen
            # NB_SPRITES - 1:
            # because there are 15 sprites,
            # but we start counting from 0
            # so it's 0 to 14 (15 sprites)
            if self.pos_x < (self.nb_sprite - 1):
                # check if the case is not a wall
                if self.lvl.structure[self.pos_y][self.pos_x + 1] \
                        not in self.wall_letter:
                    # if it is not, go by one case
                    self.pos_x += 1
                    # move the hero sprite on the case
                    self.case_x = self.pos_x * self.size_sprite

                    Character.control_game(self)

                    self.lvl.structure[self.pos_y][self.pos_x] = self.mcgyver_letter
                    self.lvl.structure[self.pos_y][self.pos_x - 1] = self.floor_letter

        if direction == "left":
            if self.pos_x > 0:
                if self.lvl.structure[self.pos_y][self.pos_x - 1] \
                        not in self.wall_letter:
                    self.pos_x -= 1
                    self.case_x = self.pos_x * self.size_sprite

                    Character.control_game(self)

                    self.lvl.structure[self.pos_y][self.pos_x] = self.mcgyver_letter
                    self.lvl.structure[self.pos_y][self.pos_x + 1] = self.floor_letter

        if direction == "up":
            if self.pos_y > 0:
                if self.lvl.structure[self.pos_y - 1][self.pos_x] \
                        not in self.wall_letter:
                    self.pos_y -= 1
                    self.case_y = self.pos_y * self.size_sprite

                    Character.control_game(self)

                    self.lvl.structure[self.pos_y][self.pos_x] = self.mcgyver_letter
                    self.lvl.structure[self.pos_y + 1][self.pos_x] = self.floor_letter

        if direction == "down":
            if self.pos_y < (self.nb_sprite - 1):
                if self.lvl.structure[self.pos_y + 1][self.pos_x] \
                        not in self.wall_letter:
                    self.pos_y += 1
                    self.case_y = self.pos_y * self.size_sprite

                    Character.control_game(self)

                    self.lvl.structure[self.pos_y][self.pos_x] = self.mcgyver_letter
                    self.lvl.structure[self.pos_y - 1][self.pos_x] = self.floor_letter

    def control_game(self):

        if self.lvl.structure[self.pos_y][self.pos_x] == "O":
            self.inventory.add_object(self.lvl.structure[self.pos_y][self.pos_x])
        else:
            if self.lvl.structure[self.pos_y][self.pos_x] == "G":
                print("")
                print("")
                if self.inventory.nb_object() == 3:
                    print("***************************")
                    print("**     You are Winner    **")
                    print("***************************")

                else:
                    print("-------  You Lost ! -------")

                print("")
                print("")

                self.continue_game = False
