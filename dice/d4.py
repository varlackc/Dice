from .die import Die


class D4(Die):
    """
    This class describes the D4 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self):
        self.die_Type = "d4"
        self.face = 1
        self.side_number = 4
