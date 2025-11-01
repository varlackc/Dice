from .die import Die


class D8(Die):
    """
    This class describes the D8 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self) -> None:
        self.die_Type: str = "d8"
        self.face: int = 1
        self.side_number: int = 8
