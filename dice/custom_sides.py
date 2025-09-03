# use a relative import
from .die import Die
class CustomSides(Die):
    def __init__(self,sides):
        if (type(sides) == type(1)):
          self.die_Type = "custom_sided"
          self.face = 1
          self.side_number = sides