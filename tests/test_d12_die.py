import unittest
from dice import D12


class TestD12(unittest.TestCase):
    """
    This class describes the tests for a twelve sided die

    Args:
        unittest (_type_): _description_
    """
    def test_roll(self) -> None:
        # verify an output is present
        self.assertIsNotNone(D12().roll())

    def test_low_bound(self) -> None:
        # verify the output does not exceed lower bound
        self.assertGreater(D12().roll(), 0)

    def test_upper_bound(self) -> None:
        # verify the output does not exceed upper bound
        self.assertLess(D12().roll(), 13)

    def test_shake(self) -> None:
        # verify the shake method does not output
        self.assertIsNone(D12().shake())

    def test_sides(self):
        # verify that the number of sides are correct
        self.assertEqual(D12().side_number, 12)

    def test_die_Type(self):
        # verify that the die type is correct
        self.assertEqual(D12().die_Type, "d12")
