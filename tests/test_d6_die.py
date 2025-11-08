import unittest
from dice import D6


class TestD6Die(unittest.TestCase):
    """
    This class describes the tests for the six sided die

    Args:
        unittest (_type_): _description_
    """
    def test_roll(self) -> None:
        # verify an output is present
        self.assertIsNotNone(D6().roll())

    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(D6().roll(), 0)

    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(D6().roll(), 7)

    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(D6().shake())

    def test_sides(self):
        # verify that the number of sides are correct
        self.assertEqual(D6().side_number, 6)

    def test_die_Type(self):
        # verify that the die type is correct
        self.assertEqual(D6().die_Type, "d6")
