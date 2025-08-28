import unittest
from src import *

class TestDiceHand(unittest.TestCase):
    def test_add_die(self):
        # verify that a die can be added
        d1 = Die()
        set_d1 = DiceHand()
        set_d1.add_die(d1)
        self.assertGreater(len(set_d1.die_set),0)
    def test_get_faces(self):
        # verify that the faces can be shown
        d1 = Die()
        d2 = Die()
        set_d1 = DiceHand()
        set_d1.add_die(d1)
        set_d1.add_die(d2)
        self.assertIsNotNone(set_d1.get_faces())
    def test_shake_dice(self):
        # verify that the faces can be shaken without
        # showing the numbers
        d1 = Die()
        d2 = Die()
        set_d1 = DiceHand()
        set_d1.add_die(d1)
        set_d1.add_die(d2)
        self.assertIsNone(set_d1.shake_dice())
    def test_roll_dice(self):
        # verify that the dice can be rolled
        d1 = D6()
        d2 = D6()
        set_d1 = DiceHand()
        set_d1.add_die(d1)
        set_d1.add_die(d2)
        self.assertIsNotNone(set_d1.roll_dice())
    def test_get_total(self):
        # verify that the dice total can be aquired
        d1 = D6()
        d2 = D6()
        set_d1 = DiceHand()
        set_d1.add_die(d1)
        set_d1.add_die(d2)
        self.assertIsNotNone(set_d1.get_total())