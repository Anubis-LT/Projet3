"""
Game: McGyver maze
Creator: Grégory Le Terte

Class: class_config_json.py

"""

import json
import sys
from datetime import date
sys.path.append("./")

class ConfigJson:
    # This is to load items of file json
    def __init__(self, file):
        self.file = file
        with open(self.file, "r") as config_json:
            self.parametersConfig = json.load(config_json)

    def file_map(self, name):
        return self.parametersConfig[name]

    def write_winner(self,time):
        today = date.today()
        winner_time = str(time)
        winner_date = str(today.day)+"/"+str(today.month)+"/"+str(today.year)
        self.parametersConfig["constants"]["winner_time"] = winner_time
        self.parametersConfig["constants"]["winner_date"] = winner_date

        with open(self.file, "w") as config_json:
            json.dump(self.parametersConfig,config_json,indent = 4)