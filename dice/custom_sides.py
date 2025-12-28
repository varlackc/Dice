# use a relative import
from .die import Die


class CustomSides(Die):
    """
    This class describes the Custom Sides Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self, sides: any) -> None:
        """
        use is instance to verify that the sides is of type integer
        https://docs.python.org/3.7/library/functions.html#isinstance
        """
        if (isinstance(sides, int)):
            self.die_Type: str = "custom_sided"
            self.face: int = 1
            self.side_number: int = sides
        else:
            raise TypeError(
              "The custom sided die must take an interger as an input"
              )
