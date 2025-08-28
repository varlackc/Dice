from .die import Die
class D20(Die):
    def __init__(self):
        self.die_Type = "d20"
        self.face = 1
        self.side_number = 20