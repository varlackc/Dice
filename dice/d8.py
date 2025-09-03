from .die import Die
class D8(Die):
    def __init__(self):
        self.die_Type = "d8"
        self.face = 1
        self.side_number = 8