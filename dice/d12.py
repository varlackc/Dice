# use a relative import
from .die import Die
class D12(Die):
    """This class describes the D12 Die

    Args:
        Die (_type_): _description_
    """
    def __init__(self):
        self.die_Type = "d12"
        self.face = 1
        self.side_number = 12