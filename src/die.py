import random

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
    def roll(self) -> int:
        # check if the die is non-numeric
        if(self.die_Type == "non-numeric"):
          self.face = random.choice(self.other)
        # if the value has a range then roll withing the range
        elif(self.die_Type == "custom_sided_range"):
            self.face = random.randrange(self.lower,(self.higher + 1))
        # otherwise then change the face number
        else:
          self.face = random.randint(1,self.side_number)
        return self.face
    def shake(self) -> None:
        # if the die is non numeric then select from the list in the other attribute
        if(self.die_Type == "non-numeric"):
          self.face = random.choice(self.other)
        elif(self.die_Type == "custom_sided_range"):
          self.face = random.randrange(self.lower, (self.higher + 1))
        else:
          self.face = random.randint(1,self.side_number)
    def get_face(self) -> int:
        return self.face
    def get_type(self) -> str:
        return self.die_Type
    def set_face(self, value:int) -> None:
        if(value < self.side_number and value > 0):
            self.face = value