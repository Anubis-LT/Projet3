"""
Game: McGyver maze
Creator: Grégory Le Terte

Class: class_images.py


"""
from configjson import Config_Json

class Images:
    """
    Load images from different sources.
    """

    def __init__(self,parameters,required_items):
        """
            Load images Wall and Floor from stucture config.json
        """
        structure = Config_Json.filemap(parameters,"structures")
        self.wall = structure["wall"]
        self.wall_img = self.wall["file_picture"]

        self.floor = structure["floor"]
        self.floor_img = self.load_image(self.floor["file_picture"])

        """
           Load images Mac Gyver and Guardian from characters config.json
        """
        characters = Config_Json.filemap(parameters,"characters")
        self.mcgyver = characters["mac_gyver"]
        self.mcgyver_img = self.load_image(self.mcgyver["file_picture"])

        self.guardian = characters["guardian"]
        self.guardian_img = self.load_image(self.guardian["file_picture"])

        """
           Load images Needle,tube,ether from object config.json
        """
        objects = Config_Json.filemap(parameters, "object")
        self.needle = objects["needle"]
        self.needle_img = self.load_image(self.needle["file_picture"])

        self.tube = objects["tube"]
        self.tube_img = self.load_image(self.tube["file_picture"])

        self.ether = objects["ether"]
        self.ether_img = self.load_image(self.ether["file_picture"])


    def load_image(self, filename):

        """
               Calls pygame to load image for the given filename
               and convert alpha zones in transparent
               """
        try:
            with open(filename):
                return filename
        except FileNotFoundError as fnferr:
            print("Image {} could not be opened. \
                      Here is the original message: {}".format(filename, fnferr))
            exit()
