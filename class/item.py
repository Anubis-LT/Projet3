""""
Game: McGyver maze
Creator: Grégory Le Terte

Class: class_item.py
Item and Inventory

"""


# ===========================
#        Items' class
# ===========================
class Item:
    """Describes an item"""

    def __init__(self, position):
        self.pos_x, self.pos_y = position

    @property
    def case_position(self):
        """
        Case position of the item, to blit the image.
        Can be accessed via instance.case_position
        The case position is equal to the position of
        the item on the map's file times the SPRITE_SIZE.
        """

        self.case_x = self.pos_x
        self.case_y = self.pos_y

        return (self.case_x, self.case_y)


# ===========================
#      Inventory's class
# ===========================
class Inventory:
    """
    Creates an Inventory object.
    It has an _items list used to store items.
    This object is iterable.
    """

    def __init__(self):
        self.items = []
        self.nbItems = 0

    def add_object(self, item):
        # adds an item to the _items list
        self.items.append(item)
        nb_items = Inventory.nb_object(self)
        print("Numbers Items Collected : ", nb_items)

    def nb_object(self):
        # Number Items collected
        nb_items = 0
        for item in self.items:
            nb_items += 1

        return nb_items
