from .die import Die


class D10(Die):
    """
    This class describes the D10 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self) -> None:
        self.die_Type: str = "d10"
        self.face: int = 1
        self.side_number: int = 10
