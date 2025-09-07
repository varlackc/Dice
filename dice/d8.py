from .die import Die


class D8(Die):
    """This class describes the D8 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self):
        self.die_Type = "d8"
        self.face = 1
        self.side_number = 8
