import unittest
from dice import *

class TestCustomSidesRange(unittest.TestCase):
    """This class describes the tests for the custom sided range die

    Args:
        unittest (_type_): _description_
    """
    def test_custom_roll(self):
        # verify an output is present
        self.assertIsNotNone(CustomSidesRange(5,100).roll())
    def test_custom_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(CustomSidesRange(5,100).roll(),4)
    def test_custom_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(CustomSidesRange(5,100).roll(),101)
    def test_custom_shake(self):
        # verify the shake method does not output
        self.assertIsNone(CustomSidesRange(5,100).shake())
    def test_custom_sides(self):
        self.assertEqual(CustomSidesRange(5,100).side_number, 95)
    def test_custom_negative(self):
        self.assertLess(CustomSidesRange(-5,-1).roll(),0)
    def test_custom_die_Type(self):
        self.assertEqual(CustomSidesRange(5,100).die_Type, "custom_sided_range")