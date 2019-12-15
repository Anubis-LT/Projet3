#! /usr/bin/env python3
# coding: utf-8

"""
Game    : McGyver maze
File    : configjson.py
Creator : Grégory Le Terte
Info    : This program allows you to work with a json file
"""

import json
import sys
from datetime import date

sys.path.append("./")


class ConfigJson:

    def __init__(self, file):
        """ This is to load items of file json
            Args:
                file :  file .json ( ./resources/config.json)
        """
        self.file = file
        with open(self.file, "r") as config_json:
            self.parametersConfig = json.load(config_json)

    def file_map(self, name):
        """ Return value of keys
            Args:
                name :  name of Keys
        """
        return self.parametersConfig[name]

    def write_winner(self, time):
        """ Format dat time of winner
            Args:
                time :  time to be saved by the player (Game.endings())
        """

        today = date.today()
        winner_time = str(time)
        winner_date = str(today.day) + "/" + str(today.month) + "/" + \
                      str(today.year)

        # Assignment
        self.parametersConfig["constants"]["winner_time"] = winner_time
        self.parametersConfig["constants"]["winner_date"] = winner_date

        # Save file json
        with open(self.file, "w") as config_json:
            json.dump(self.parametersConfig, config_json, indent=4)
