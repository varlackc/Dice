from .die import Die
class D6(Die):
    def __init__(self):
        self.die_Type = "d6"
        self.face = 1
        self.side_number = 6