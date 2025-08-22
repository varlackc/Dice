# unittest library documentation for python version 3.7
# https://docs.python.org/3.7/library/unittest.html
import unittest
from die import *

# to test the whole thing python -m unittest
class TestD2(unittest.TestCase):
    """This class describes the tests for a two sided die

    Args:
        unittest (_type_): _description_
    """
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(D2().roll())
    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(D2().roll(),0)
    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(D2().roll(),3)
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(D2().shake())
    def test_sides(self):
        self.assertEqual(D2().side_number, 2)
    def test_die_Type(self):
        self.assertEqual(D2().die_Type, "d2")
class TestD4(unittest.TestCase):
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(D4().roll())
    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(D4().roll(),0)
    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(D4().roll(),5)
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(D4().shake())
    def test_sides(self):
        self.assertEqual(D4().side_number, 4)
    def test_die_Type(self):
        self.assertEqual(D4().die_Type, "d4")
class TestD6(unittest.TestCase):
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(D6().roll())
    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(D6().roll(),0)
    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(D6().roll(),7)
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(D6().shake())
    def test_sides(self):
        self.assertEqual(D6().side_number, 6)
    def test_die_Type(self):
        self.assertEqual(D6().die_Type, "d6")
class TestD8(unittest.TestCase):
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
class TestD10(unittest.TestCase):
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(D10().roll())
    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(D10().roll(),0)
    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(D10().roll(),11)
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(D10().shake())
    def test_sides(self):
        self.assertEqual(D10().side_number, 10)
    def test_die_Type(self):
        self.assertEqual(D10().die_Type, "d10")
class TestD12(unittest.TestCase):
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(D12().roll())
    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(D12().roll(),0)
    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(D12().roll(),13)
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(D12().shake())
    def test_sides(self):
        self.assertEqual(D12().side_number, 12)
    def test_die_Type(self):
        self.assertEqual(D12().die_Type, "d12")
class TestD20(unittest.TestCase):
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(D20().roll())
    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(D20().roll(),0)
    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(D20().roll(),21)
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(D20().shake())
    def test_sides(self):
        self.assertEqual(D20().side_number, 20)
    def test_die_Type(self):
        self.assertEqual(D20().die_Type, "d20")
class TestCustomSides(unittest.TestCase):
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(CustomSides(100).roll())
    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(CustomSides(100).roll(),0)
    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(CustomSides(100).roll(),101)
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(CustomSides(100).shake())
    def test_sides(self):
        self.assertEqual(CustomSides(100).side_number, 100)
    def test_die_Type(self):
        self.assertEqual(CustomSides(100).die_Type, "custom_sided")
class TestNonNumeric(unittest.TestCase):
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(NonNumeric(["A","B","C","D","E","F"]).roll())
    def test_string_output(self):
        # verify the output is a string
        self.assertEqual(type(NonNumeric(["A","B","C","D","E","F"]).roll()),type("A"))
        # verify the output is an element in the list of sides
        self.assertIn(NonNumeric(["A","B","C","D","E","F"]).roll(), ["A","B","C","D","E","F"])
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(NonNumeric(["A","B","C","D","E","F"]).shake())
    def test_sides(self):
        self.assertEqual(NonNumeric(["A","B","C","D","E","F"]).side_number, len(["A","B","C","D","E","F"]))
    def test_die_Type(self):
        self.assertEqual(NonNumeric(["A","B","C","D","E","F"]).die_Type, "non-numeric")
class TestCustomSidesRange(unittest.TestCase):
    def test_roll(self):
        # verify an output is present
        self.assertIsNotNone(CustomSidesRange(5,100).roll())
    def test_low_bound(self):
        # verify the output does not exceed lower bound
        self.assertGreater(CustomSidesRange(5,100).roll(),4)
    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(CustomSidesRange(5,100).roll(),101)
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(CustomSidesRange(5,100).shake())
    def test_sides(self):
        self.assertEqual(CustomSidesRange(5,100).side_number, 95)
    def test_die_Type(self):
        self.assertEqual(CustomSidesRange(5,100).die_Type, "custom_sided_range")