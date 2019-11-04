""""
Game: McGyver maze
Creator: Grégory Le Terte

Class: class_level.py
"""

import  os
from    random  import randint
from    item    import Item

# ===========================
#         Level class
# ===========================
class Level:
    """
    This is to generate the level's maze and items positions
    """

    def __init__(self, file_map, required_name_object):
        self.pathfile = os.getcwd() + "/ressources/maps/" + file_map.get("filemap")

        # Generape map from file
        self.generate_from_file()

        self.items       = {}
        self.nb_sprites = file_map.get("nb_sprites")

        """
        For each item key in required_items,
        set each item in the items dict of the Level class
        by instanciating it with the Item class,
        taking in parameter the random_pos method of the Level class.
        This results in {"item_key": <xxx.Item object at *******>}.
        """
        for item in required_name_object.keys():
            self.items[item] = Item(self.random_pos(self.nb_sprites))


    def generate_from_file(self):
        with open(self.pathfile, "r") as lvl_file:

            structure_level = []
            """
            Nested list comprehension to build a 2D array,
            breaking down the specified lvl_file into rows and cols.
            """

            # On parcourt les lignes du fichier
            for line in lvl_file:
                line_level = []
                # On parcourt les sprites (lettres) contenus dans le fichier
                for sprite in line:
                    # On ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        # On ajoute le sprite à la liste de la ligne
                        line_level.append(sprite)
                # On ajoute la ligne à la liste du niveau
                structure_level.append(line_level)
            # On sauvegarde cette structure
            self.structure = structure_level

    def random_pos(self, nbsprites):
        """
        While self.maze_map[pos_y][pos_x] is not on a free space,
        search for a random position.
        Then set this random position to the *
        This is to avoid items superposition.
        """
        pos_x = 0
        pos_y = 0

        while self.structure[pos_y][pos_x] != "":

            pos_x = randint(1, (int(nbsprites) - 1))
            pos_y = randint(1, (int(nbsprites) - 1))

            if self.structure[pos_y][pos_x] == "F":
                self.structure[pos_y][pos_x] = "O"
                return pos_x, pos_y

