import random
# Die supper class
class Die:
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
    def __init__(self):
        super().d2()
class D4(Die):
    def __init__(self):
        super().d4()
class D6(Die):
    def __init__(self):
        super().__init__()
class D8(Die):
    def __init__(self):
        super().d8()
class D10(Die):
    def __init__(self):
        super().d10()
class D12(Die):
    def __init__(self):
        super().d12()
class D20(Die):
    def __init__(self):
        super().d20()
class CustomSides(Die):
    def __init__(self,sides):
        if (type(sides) == type(1)):
          self.die_Type = "custom_sided"
          self.side_number = sides
