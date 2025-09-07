from .die import Die


class D6(Die):
    """This class describes the D6 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self):
        self.die_Type = "d6"
        self.face = 1
        self.side_number = 6
