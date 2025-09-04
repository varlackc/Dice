# use a relative import
from .die import Die
class CustomSides(Die):
    """This class describes the Custom Sides Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self,sides):
        if (type(sides) == type(1)):
          self.die_Type = "custom_sided"
          self.face = 1
          self.side_number = sides
        else:
          raise TypeError("The custom sided die must take an interger as an input")