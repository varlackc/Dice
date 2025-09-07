# unittest library documentation for python version 3.7
# https://docs.python.org/3.7/library/unittest.html
import unittest
from dice import Die


# to test the whole thing python -m unittest
class TestDie(unittest.TestCase):
    """This class describes the tests for a six sided die

    Args:
        unittest (_type_): _description_
    """
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(Die().roll())

    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(Die().roll(), 0)

    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(Die().roll(), 7)

    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(Die().shake())

    def test_sides(self):
        # verify that the number of sides are correct
        self.assertEqual(Die().side_number, 6)

    def test_die_Type(self):
        # verify that the die type is correct
        self.assertEqual(Die().die_Type, "d6")
