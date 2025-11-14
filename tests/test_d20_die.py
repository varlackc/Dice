import unittest
from dice import D20


class TestD20(unittest.TestCase):
    """
    This class describes the tests for a twenty sided die

    Args:
        unittest (_type_): _description_
    """
    def test_roll(self) -> None:
        # verify an output is present
        self.assertIsNotNone(D20().roll())

    def test_low_bound(self) -> None:
        # verify the output does not exceed lower bound
        self.assertGreater(D20().roll(), 0)

    def test_upper_bound(self) -> None:
        # verify the output does not exceed upper bound
        self.assertLess(D20().roll(), 21)

    def test_shake(self) -> None:
        # verify the shake method does not output
        self.assertIsNone(D20().shake())

    def test_sides(self):
        # verify that the number of sides are correct
        self.assertEqual(D20().side_number, 20)

    def test_die_Type(self):
        # verify that the die type is correct
        self.assertEqual(D20().die_Type, "d20")
