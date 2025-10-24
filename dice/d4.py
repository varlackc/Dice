from .die import Die


class D4(Die):
    """
    This class describes the D4 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self) -> None:
        self.die_Type: str = "d4"
        self.face: int = 1
        self.side_number: int = 4
