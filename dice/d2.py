# use a relative import
from .die import Die


class D2(Die):
    """
    This class describes the D2 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self) -> None:
        self.die_Type: str = "d2"
        self.face: int = 1
        self.side_number: int = 2
