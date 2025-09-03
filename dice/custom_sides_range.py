# use a relative import
from .die import Die
class CustomSidesRange(Die):
  def __init__(self,lower:int,higher:int):
    if(type(lower) == type(1) and type(higher) == type(1)):
      self.die_Type = "custom_sided_range"
      self.face = lower
      self.side_number = higher - lower
      self.lower = lower
      self.higher = higher