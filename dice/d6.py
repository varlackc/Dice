from .die import Die


class D6(Die):
    """
    This class describes the D6 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self) -> None:
        self.die_Type: str = "d6"
        self.face: int = 1
        self.side_number: int = 6
