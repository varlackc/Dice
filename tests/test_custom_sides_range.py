import unittest
from dice import CustomSidesRange


class TestCustomSidesRange(unittest.TestCase):
    """
    This class describes the tests for the custom sided range die

    Args:
        unittest (_type_): _description_
    """
    def test_custom_roll(self) -> None:
        # verify an output is present
        self.assertIsNotNone(CustomSidesRange(5, 100).roll())

    def test_custom_low_bound(self) -> None:
        # verify the output does not exceed lower bound
        self.assertGreater(CustomSidesRange(5, 100).roll(), 4)

    def test_custom_upper_bound(self) -> None:
        # verify the output does not exceed upper bound
        self.assertLess(CustomSidesRange(5, 100).roll(), 101)

    def test_custom_shake(self):
        # verify the shake method does not output
        self.assertIsNone(CustomSidesRange(5, 100).shake())

    def test_custom_sides(self):
        # verify that the number of sides is equal to the expected value
        self.assertEqual(CustomSidesRange(5, 100).side_number, 95)

    def test_custom_negative(self):
        # verify that it is possible to assign negative values
        self.assertLess(CustomSidesRange(-5, -1).roll(), 0)

    def test_custom_no_input(self):
        # verify that an exception is raced if no input is given
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
        with self.assertRaises(TypeError):
            CustomSidesRange()

    def test_custom_excess_input(self):
        # verify that an error occur if two many parameters are used
        with self.assertRaises(TypeError):
            CustomSidesRange(5, 10, 20)

    def test_custom_die_Type(self):
        # verify that the type of die is correct.
        self.assertEqual(CustomSidesRange(5, 100).die_Type,
                         "custom_sided_range")
