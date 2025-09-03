from .die import Die
class NonNumeric(Die):
    def __init__(self, side_list):
        self.die_Type = "non-numeric"
        self.face = side_list[0]
        self.side_number = len(side_list)
        self.other = side_list
    def set_face(self, value:str) -> None:
        self.face = value