# use a relative import
from .die import Die
class D12(Die):
    def __init__(self):
        self.die_Type = "d12"
        self.face = 1
        self.side_number = 12