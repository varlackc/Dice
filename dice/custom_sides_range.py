# use a relative import
from .die import Die


class CustomSidesRange(Die):
    """This class describes the Custom Sides Range Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self, lower: int, higher: int):
        # use is instance to verify that the sides is of type integer
        # https://docs.python.org/3.7/library/functions.html#isinstance
        if (isinstance(lower, int) and isinstance(higher, int)):
            self.die_Type = "custom_sided_range"
            self.face = lower
            self.side_number = higher - lower
            self.lower = lower
            self.higher = higher
