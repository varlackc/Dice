# import typing to allow for the use of List parameters of objects
from typing import List, Any


class DiceHand:
    """
    This class describes the Dice Hand
    It allows to work with multiple die
    """
    def __init__(self) -> None:
        self.die_set: list = []
        self.die_faces: list = []
        self.count_total: int = 0

    def add_die(self, die) -> None:
        """
        This method adds a dice to the dice hand
        """
        self.die_set.append(die)

    def add_dice(self, dice: List[Any]) -> None:
        # add multiple dice at once
        for i in range(len(dice)):
            self.die_set.append(dice[i])

    def get_faces(self) -> int:
        # reset the die faces
        self.die_faces: list = []
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

    def set_faces(self, faces: List[Any]) -> None:
        # set values to the dice
        for i in range(len(faces)):
            if (isinstance(faces[i], type(self.die_set[i].face))):
                self.die_set[i].face = faces[i]
