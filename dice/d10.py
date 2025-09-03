from .die import Die
class D10(Die):
    def __init__(self):
        self.die_Type = "d10"
        self.face = 1
        self.side_number = 10