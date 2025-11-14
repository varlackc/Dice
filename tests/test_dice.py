import unittest
from dice import Die, D4, D6, D8, DiceHand


class TestDiceHand(unittest.TestCase):
    """
    This class describes the tests for a dice hand

    Args:
        unittest (_type_): _description_
    """
    def test_add_die(self) -> None:
        # verify that a die can be added
        d1 = Die()
        set_d1 = DiceHand()
        set_d1.add_die(d1)
        self.assertGreater(len(set_d1.die_set), 0)

    def test_get_faces(self):
        # verify that the faces can be shown
        d1, d2 = Die(), Die()
        set_d1 = DiceHand()
        set_d1.add_die(d1)
        set_d1.add_die(d2)
        self.assertIsNotNone(set_d1.get_faces())

    def test_shake_dice(self):
        # verify that the faces can be shaken without
        # showing the numbers
        d1, d2 = Die(), Die()
        set_d1 = DiceHand()
        set_d1.add_die(d1)
        set_d1.add_die(d2)
        self.assertIsNone(set_d1.shake_dice())

    def test_roll_dice(self):
        # verify that the dice can be rolled
        d1, d2 = D6(), D6()
        set_d1 = DiceHand()
        set_d1.add_die(d1)
        set_d1.add_die(d2)
        self.assertIsNotNone(set_d1.roll_dice())

    def test_get_total(self):
        # verify that the dice total can be aquired
        d1, d2 = D6(), D6()
        set_d1 = DiceHand()
        set_d1.add_die(d1)
        set_d1.add_die(d2)
        self.assertIsNotNone(set_d1.get_total())

    def test_add_dice(self):
        """
        verify that a list of dice can be added
        all at once to the dice hand
        """
        d1, d2, d3 = D4(), D6(), D8()
        set_d1 = DiceHand()
        set_d1.add_dice([d1, d2, d3])
        self.assertIsNotNone(set_d1.die_set)

    def test_set_faces(self):
        # verify that the faces in the different dice could be set
        d1, d2, d3 = D6(), D6(), D6()
        set_d1 = DiceHand()
        set_d1.add_dice([d1, d2, d3])
        initial = set_d1.get_faces()
        new_values = []
        # numeric cases
        for item in initial:
            if (item < 6):
                new_values.append(item + 1)
            else:
                new_values.append(item - 1)
        set_d1.set_faces(new_values)
        result = (initial == set_d1.get_faces())
        self.assertFalse(result)

    def test_set_faces_same(self):
        # verify that dices could be skipped when setting dice faces
        d1, d2, d3 = D6(), D6(), D6()
        set_d1 = DiceHand()
        set_d1.add_dice([d1, d2, d3])
        initial = set_d1.get_faces()
        # try by using the set faces method without modifying the dice
        set_d1.set_faces([None, None, None])
        result = (initial == set_d1.get_faces())
        self.assertTrue(result)
