import random
# Die supper class
class Die:
    """This class describes the base Die

    Returns:
        _type_: _description_
    """
    # constructor method
    def __init__(self):
        # initialize the attributes
        # set default values for a d6 
        # instead of leaving attributes at None
        self.die_Type = "d6"
        self.face = 1
        self.side_number = 6
        self.other = None
    def roll(self):
        # check if the die is non-numeric
        if(self.die_Type == "non-numeric"):
          self.face = random.choice(self.other)
        # otherwise then change the face number
        else:
          self.face = random.randint(1,self.side_number)
        return self.face
    def shake(self):
        # if the die is non numeric then select from the list in the other attribute
        if(self.die_Type == "non-numeric"):
          self.face = random.choice(self.other)
        else:
          self.face = random.randint(1,self.side_number)
    def get_face(self):
        return self.face
    def get_type(self):
        return self.die_Type
    def set_face(self, value):
        if(value < self.side_number and value > 0):
            self.face = value
class D2(Die):
    """This class describes the D2 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self):
        self.die_Type = "d2"
        self.side_number = 2
class D4(Die):
    def __init__(self):
        self.die_Type = "d4"
        self.side_number = 4
class D6(Die):
    def __init__(self):
        self.die_Type = "d6"
        self.side_number = 6
class D8(Die):
    def __init__(self):
        self.die_Type = "d8"
        self.side_number = 8
class D10(Die):
    def __init__(self):
        self.die_Type = "d10"
        self.side_number = 10
class D12(Die):
    def __init__(self):
        self.die_Type = "d12"
        self.side_number = 12
class D20(Die):
    def __init__(self):
        self.die_Type = "d20"
        self.side_number = 20
class CustomSides(Die):
    def __init__(self,sides):
        if (type(sides) == type(1)):
          self.die_Type = "custom_sided"
          self.side_number = sides
class NonNumeric(Die):
    def __init__(self, side_list):
        self.die_Type = "non-numeric"
        self.face = side_list[0]
        self.side_number = len(side_list)
        self.other = side_list
class CustomSidesRange(Die):
  def __init__(self,lower,higher):
      if(type(lower) == type(1) and type(higher) == type(1)):
        self.die_Type = "custom_sided_range"
        self.side_number = higher - lower