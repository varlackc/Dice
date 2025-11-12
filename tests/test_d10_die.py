import unittest
from dice import D10


class TestD10(unittest.TestCase):
    """
    This class describes the tests for a ten sided die

    Args:
        unittest (_type_): _description_
    """
    def test_roll(self) -> None:
        # verify an output is present
        self.assertIsNotNone(D10().roll())

    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(D10().roll(), 0)

    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(D10().roll(), 11)

    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(D10().shake())

    def test_sides(self):
        # verify that the number of sides are correct
        self.assertEqual(D10().side_number, 10)

    def test_die_Type(self):
        # verify that the die type is correct
        self.assertEqual(D10().die_Type, "d10")
