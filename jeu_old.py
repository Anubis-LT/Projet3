import json
import random

# initialisation structure Depart,murs,arrivée,objets
class Structure:
    def __init__(self, position, **structures_attributes):
        self.position = position
        # Affectation des valeurs aux attributs d un objet
        for attr_name, attr_value in structures_attributes.items():
            setattr(self, attr_name, attr_value)


class Position:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

class Map:
    MAPS = []
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    HEIGHT_DEGREES = 1
    WIDTH_DEGREES = 1

    def __init__(self,corner1,corner2):
        self.corner1 = corner1
        self.corner2 = corner2
        self.objectgame = []

    def add_objectgame(self, objectgame):
        self.objectgame.append(objectgame)
        print(objectgame)
    @classmethod
    def _initialize_maps(cls):
        for position_y in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            for position_x in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                bottom_left_corner = Position(position_x, position_y)
                top_right_corner = Position(position_x + cls.WIDTH_DEGREES, position_y + cls.HEIGHT_DEGREES)
                map = Map(bottom_left_corner, top_right_corner)
                cls.MAPS.append(map)
                # print(len(cls.MAPS))

    def contains(self, position):
        return position.position_x >= min(self.corner1.position_x, self.corner2.position_x) and \
               position.position_x < max(self.corner1.position_x, self.corner2.position_x) and \
               position.position_y >= min(self.corner1.position_y, self.corner2.position_y) and \
               position.position_y < max(self.corner1.position_y, self.corner2.position_y)

    @classmethod
    def find_zone_that_contains(cls, position):
        if not cls.MAPS:
            # Initialize zones automatically if necessary
            cls._initialize_maps()

        # Compute the index in the ZONES array that contains the given position
        positionx_index = int((position.position_x - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        positiony_index = int((position.position_y - cls.MIN_LATITUDE_DEGREES) / cls.HEIGHT_DEGREES)
        positionx_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES) # 180-(-180) / 1
        map_index = positiony_index  * positionx_bins + positionx_index

        # Just checking that the index is correct
        map = cls.MAPS[map_index]
        #assert map.contains(position)
        print(cls.MAPS[map_index])

        return map

def main():
    # récupération des données d un fichier json pour la structure du  Depart Murs et arrivée
    for structures_attributes in json.load(open("structure.json")):

        position_x = structures_attributes.pop('position_x')
        position_y = structures_attributes.pop('position_y')
        position = Position(position_x, position_y)

        structures = Structure(position, **structures_attributes)

        map = Map.find_zone_that_contains(position)
        map.add_objectgame(structures)

    # Ajout des 3 objets du jeux dans les emplacements vides
    # on initialise la position des objects au hazard
    # les objets ne doivent pas tomber sur une structure
    # positionimageobject_x = random.sample(range(5, 224), 3)
    # positionimageobject_y = random.sample(range(5, 224), 3)


main()
