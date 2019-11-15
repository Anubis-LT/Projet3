"""
Game: McGyver maze
Creator: Grégory Le Terte

File: constants.py

"""

# Init parameters
from configjson import ConfigJson


parameters      = ConfigJson('./resources/config.json')
constants       = ConfigJson.file_map(parameters, "constants")
structure       = ConfigJson.file_map(parameters, "structures")
characters      = ConfigJson.file_map(parameters, "characters")
objects         = ConfigJson.file_map(parameters, "object")

TITLE           = constants.get("title")
FILE_MAP        = constants.get("filemap")
NB_SPRITES      = constants.get("nb_sprites")
SIZE_SPRITES    = constants.get("size_sprites")
LOGO            = constants.get("logo")
ICON            = constants.get("icon")
BACKGROUND_GAME = constants.get("background_game")

wall            = structure["wall"]
floor           = structure["floor"]
mcgyver         = characters["mac_gyver"]
guardian        = characters["guardian"]
needle          = objects["needle"]
tube            = objects["tube"]
ether           = objects["ether"]


WALL_LETTER     = wall["caractere"]
FLOOR_LETTER    = floor["caractere"]
MCGYVER_LETTER  = mcgyver["caractere"]
GUARDIAN_LETTER = guardian["caractere"]
NEEDLE_LETTER   = needle["caractere"]
TUBE_LETTER     = tube["caractere"]
ETHER_LETTER    = ether["caractere"]


WALL_IMG        = wall["file_picture"]
FLOOR_IMG       = floor["file_picture"]
MCGYVER_IMG     = mcgyver["file_picture"]
GUARDIAN_IMG    = guardian["file_picture"]
NEEDLE_IMG      = needle["file_picture"]
TUBE_IMG        = tube["file_picture"]
ETHER_IMG       = ether["file_picture"]



#   Load images Mac Gyver and Guardian from characters config.json





#   Load images Needle,tube,ether from object config.json





