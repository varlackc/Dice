# use a relative import
from .die import Die
class D2(Die):
    """This class describes the D2 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self):
        self.die_Type = "d2"
        self.side_number = 2