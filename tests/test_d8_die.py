import unittest
from src import *

class TestD8(unittest.TestCase):
    """This class describes the tests for an eight sided die

    Args:
        unittest (_type_): _description_
    """
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(D8().roll())
    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(D8().roll(),0)
    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(D8().roll(),9)
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(D8().shake())
    def test_sides(self):
        self.assertEqual(D8().side_number, 8)
    def test_die_Type(self):
        self.assertEqual(D8().die_Type, "d8")