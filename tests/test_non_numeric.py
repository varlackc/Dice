import unittest
from dice import NonNumeric


class TestNonNumeric(unittest.TestCase):
    """
    This class describes the tests for non numeric die

    Args:
        unittest (_type_): _description_
    """
    def test_roll(self) -> None:
        # verify an output is present
        self.assertIsNotNone(NonNumeric(["A", "B", "C", "D", "E", "F"]).roll())

    def test_string_output(self) -> None:
        # verify the output is a string
        self.assertEqual(type(NonNumeric(["A", "B", "C", "D", "E", "F"]
                                         ).roll()), type("A"))
        # verify the output is an element in the list of sides
        self.assertIn(NonNumeric(["A", "B", "C", "D", "E", "F"]).roll(),
                      ["A", "B", "C", "D", "E", "F"])

    def test_string_and_int(self) -> None:
        # verify that both integers and strings are used
        self.assertIsNotNone(NonNumeric(["A", 1, "B", 2, "C", 3]))

    def test_int(self) -> None:
        # verify that the integers can be added
        self.assertIsNotNone(NonNumeric([1, 2, 3]))

    def test_shake(self) -> None:
        # verify the shake method does not output
        self.assertIsNone(NonNumeric(["A", "B", "C", "D", "E", "F"]
                                     ).shake())

    def test_sides(self) -> None:
        # verify that the number of sides on the die is correct
        self.assertEqual(NonNumeric(["A", "B", "C", "D", "E", "F"]
                                    ).side_number,
                         len(["A", "B", "C", "D", "E", "F"]))

    def test_die_Type(self) -> None:
        self.assertEqual(NonNumeric(["A", "B", "C", "D", "E", "F"]
                                    ).die_Type, "non-numeric")
