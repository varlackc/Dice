import unittest
from dice import CustomSides

class TestCustomSides(unittest.TestCase):
    """This class describes the tests for a custom sided die

    Args:
        unittest (_type_): _description_
    """
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(CustomSides(100).roll())
    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(CustomSides(100).roll(),0)
    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(CustomSides(100).roll(),101)
    def test_string_error(self):
        # verify that given a string the dice races and error
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
        with self.assertRaises(TypeError):
            CustomSides("A").roll()
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(CustomSides(100).shake())
    def test_sides(self):
        self.assertEqual(CustomSides(100).side_number, 100)
    def test_die_Type(self):
        self.assertEqual(CustomSides(100).die_Type, "custom_sided")
