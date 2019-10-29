"""
Game: McGyver maze
Creator: Grégory Le Terte

The game is all about McGyver struggling to find 3 items,
in order to put a guard to sleep and escape the maze.

Python scripts used:
main.py

Class:
Class_load_config.py
class_level.py

Others  folders,files :
config.json
map.txt
/picture/*.png

"""

# from class_level import *
import sys
sys.path.append("./class")

from level import Level
from characters import Character
from characters import Npc
from images import Images
from configjson import Config_Json

# ===========================
#    Initialize the game
# ===========================
def launch_game():
    # ===========================
    #       Instantiations
    # ===========================

    # Instantiations 'parameters' from config.json
    parameters = Config_Json('./ressources/config.json')

    # Instantiations 'map' from config.json
    map = Config_Json.filemap(parameters,"constants")

    # Instantiations 'object' from config.json
    object = Config_Json.filemap(parameters,"object")

    # Instantiations 'guardians' from config.json
    guardians = Config_Json.filemap(parameters, "characters")

    # Instantiations 'mcgyver_maze' from 'map' and 'object'
    mcgyver_maze = Level(map, object)

    # creating character, NPC and images instances
    mcgyver = Character(mcgyver_maze)
    guardian = Npc(mcgyver_maze, guardians["guardian"])
    images = Images(parameters,object)



if __name__ == "__main__":
    launch_game()
