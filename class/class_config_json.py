"""
Game: McGyver maze
Creator: Grégory Le Terte

Class: class_config_json.py

"""

# ===========================
#         Config json class
# ===========================

import json

class Config_Json:
    """
    This is to load items of file json
    """

    def __init__(self,file):
        with open(file, "r") as config_json:
            Config_Json.parametresConfig = json.load(config_json)


    def filemap(self,name):
        return((self.parametresConfig[name]))

