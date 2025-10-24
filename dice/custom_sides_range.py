# use a relative import
from .die import Die


class CustomSidesRange(Die):
    """
    This class describes the Custom Sides Range Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self, lower: int, higher: int) -> None:
        """
        use is instance to verify that the sides is of type integer
        https://docs.python.org/3.7/library/functions.html#isinstance
        """
        if (isinstance(lower, int) and isinstance(higher, int)):
            self.die_Type: str = "custom_sided_range"
            self.face: int = lower
            self.side_number: int = higher - lower
            self.lower: int = lower
            self.higher: int = higher
