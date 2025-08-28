from . import *

class DiceHand:
    def __init__(self):
        self.die_set = []
        self.die_faces = []
        self.count_total = 0
    def add_die(self, die):
        self.die_set.append(die)
    def get_faces(self):
        # reset the die faces
        self.die_faces = []
        for i in range(len(self.die_set)):
            self.die_faces.append(self.die_set[i].get_face())
        return self.die_faces
    def shake_dice(self):
        # shake the dice
        for i in range(len(self.die_set)):
            self.die_set[i].shake()
    def roll_dice(self):
        # roll the dice
        result = []
        for i in range(len(self.die_set)):
            result.append(self.die_set[i].roll())
        return result