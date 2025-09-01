# unittest library documentation for python version 3.7
# https://docs.python.org/3.7/library/unittest.html
import unittest
#from src.die import Die
#from src.d2 import D2
from src import *
#from src.d4 import D4
#from src.d6 import D6
#from src.d8 import D8
#from src.d10 import D10
#from src.d12 import D12
#from src.d20 import D20
#from src.non_numeric import NonNumeric
#from src.custom_sides import CustomSides
#from src.custom_sides_range import CustomSidesRange

#from src.d4 import D4

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
        self.assertGreater(Die().roll(),0)
    def test_upper_bound(self):
        # verify the output does not exceed upper bound
        self.assertLess(Die().roll(),7)
    def test_shake(self):
        # verify the shake method does not output
        self.assertIsNone(Die().shake())
    def test_sides(self):
        self.assertEqual(Die().side_number, 6)
    def test_die_Type(self):
        self.assertEqual(Die().die_Type, "d6")