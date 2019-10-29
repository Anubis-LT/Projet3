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

        # turn to false when char position == item position
        self.displaying = True

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
        self._items = []

    def __iter__(self):
        for item in self._items:
            yield item

    def add_object(self, item):
        # adds an item to the _items list
        self._items.append(item)
