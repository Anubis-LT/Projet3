import json
import random

# initialisation structure Depart,murs,arrivée
class Structure:
    def __init__(self, position, **structures_attributes):
        self.position = position
        # Affectation des valeurs aux attributs d un objet
        for attr_name, attr_value in structures_attributes.items():
            setattr(self, attr_name, attr_value)

    def Object(self):
        pass

class Position:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y


def main():
    # récupération des données d un fichier json pour la struture du  Depart Murs et arrivée
    for structures_attributes in json.load(open("structure.json")):
        position_x = structures_attributes.pop('position_x')
        position_y = structures_attributes.pop('position_y')
        position = Position(position_x, position_y)

        structures = Structure(position, **structures_attributes)

    # Ajout des 3 objets du jeux
    # on initialise la position des objects au hazard
    # les objets ne doivent pas tomber sur une structure
    # positionimageobject_x = random.sample(range(5, 224), 3)
    # positionimageobject_y = random.sample(range(5, 224), 3)




main()
