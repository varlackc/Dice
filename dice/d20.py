from .die import Die


class D20(Die):
    """
    This class describes the D20 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self):
        self.die_Type = "d20"
        self.face = 1
        self.side_number = 20
