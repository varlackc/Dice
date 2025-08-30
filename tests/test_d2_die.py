import unittest
from src import *

class TestD2Die(unittest.TestCase):
    """This class describes the tests for a two sided die

    Args:
        unittest (_type_): _description_
    """
    def test_d2_roll(self):
        # verify an output is present
        self.assertIsNotNone(D2().roll())
    def test_d2_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(D2().roll(),0)
    def test_d2_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(D2().roll(),3)
    def test_d2_shake(self):
        # verify the shake method does not output
        self.assertIsNone(D2().shake())
    def test_d2_sides(self):
        self.assertEqual(D2().side_number, 2)
    def test_d2_Type(self):
        self.assertEqual(D2().die_Type, "d2")
