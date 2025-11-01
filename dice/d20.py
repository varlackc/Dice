from .die import Die


class D20(Die):
    """
    This class describes the D20 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self) -> None:
        self.die_Type: str = "d20"
        self.face: int = 1
        self.side_number: int = 20
