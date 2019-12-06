#! /usr/bin/env python3
# coding: utf-8

"""
Game    : McGyver maze
file    : constants.py
Creator : Grégory Le Terte
Info    : Constant of game
"""

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
WINNER_NAME     = constants.get("winner_name")
WINNER_TIME     = constants.get("winner_time")
WINNER_DATE     = constants.get("winner_date")

SOUND_MCGYVER   = constants.get("sound_mcgyver")
SOUND_LEVEL1    = constants.get("sound_level1")
SOUND_LEVEL2    = constants.get("sound_level2")
SOUND_LEVEL3    = constants.get("sound_level3")
SOUND_LEVEL4    = constants.get("sound_level4")
SOUND_LEVEL5    = constants.get("sound_level5")

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
WALLGOLD_IMG    = wall["file_picture1"]
FLOOR_IMG       = floor["file_picture"]
MCGYVER_IMG     = mcgyver["file_picture"]
GUARDIAN_IMG    = guardian["file_picture"]
NEEDLE_IMG      = needle["file_picture"]
TUBE_IMG        = tube["file_picture"]
ETHER_IMG       = ether["file_picture"]




