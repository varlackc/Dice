from . import *

class DiceHand:
    def __init__(self):
        self.die_set = []
        self.count_total = 0
    def add_die(self, die):
        self.die_set.append(die)