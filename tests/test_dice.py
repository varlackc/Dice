import unittest
from src import *

class TestDiceHand(unittest.TestCase):
    def test_add_die(self):
        # verify that a die can be added
        d1 = die
        set_d1 = DiceHand()
        set_d1.add_die(d1)
        self.assertGreater(len(set_d1.die_set),0)