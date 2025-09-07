from .die import Die


class D10(Die):
    """This class describes the D10 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self):
        self.die_Type = "d10"
        self.face = 1
        self.side_number = 10
