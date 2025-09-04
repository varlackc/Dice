import unittest
from dice import D4

class TestD4Die(unittest.TestCase):
    """This class describes the tests for a four sided die

    Args:
        unittest (_type_): _description_
    """
    def test_d4_roll(self):
        # verify an output is present
        self.assertIsNotNone(D4().roll())
    def test_d4_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(D4().roll(),0)
    def test_d4_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(D4().roll(),5)
    def test_d4_shake(self):
        # verify the shake method does not output
        self.assertIsNone(D4().shake())
    def test_d4_sides(self):
        # verify the number of sides is correct
        self.assertEqual(D4().side_number, 4)
    def test_d4_type(self):
        # verify the die type is correct
        self.assertEqual(D4().die_Type, "d4")