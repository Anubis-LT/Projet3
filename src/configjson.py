"""
Game: McGyver maze
Creator: Grégory Le Terte

Class: class_config_json.py

"""

import json

class ConfigJson:
    # This is to load items of file json
    def __init__(self, file):
        with open(file, "r") as config_json:
            self.parametersConfig = json.load(config_json)

    def file_map(self, name):
        return self.parametersConfig[name]
