# import typing to allow for the use of List parameters of objects
from typing import List, Any
from . import *

class DiceHand:
    """This class describes the Dice Hand
       It allows to work with multiple die
    """
    def __init__(self):
        self.die_set = []
        self.die_faces = []
        self.count_total = 0
    def add_die(self, die) -> None:
        self.die_set.append(die)
    def add_dice(self, dice: List[Any]) -> None:
        # add multiple dice at once
        for i in range(len(dice)):
            self.die_set.append(dice[i])
    def get_faces(self) -> int:
        # reset the die faces
        self.die_faces = []
        for i in range(len(self.die_set)):
            self.die_faces.append(self.die_set[i].get_face())
        return self.die_faces
    def shake_dice(self) -> None:
        # shake the dice
        for i in range(len(self.die_set)):
            self.die_set[i].shake()
    def roll_dice(self) -> int:
        # roll the dice
        result = []
        for i in range(len(self.die_set)):
            result.append(self.die_set[i].roll())
        return result
    def get_total(self) -> int:
        # get the dice count total
        result = 0
        for i in range(len(self.die_set)):
            result += self.die_set[i].get_face()
        return result