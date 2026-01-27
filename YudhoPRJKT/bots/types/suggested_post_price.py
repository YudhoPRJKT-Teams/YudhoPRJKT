from .enable_types import EnableTypes

class SuggestedPostPrice(EnableTypes):
  def __init__(self) -> None:
    self._currency: str
    self._ammount: int
  # currentcy getter
  @property
  def currentcy(self) -> str:
    return str(self._currentcy)
  # currentcy setter
  @currentcy.setter
  def currentcy(self, _):
    self._currentcy = _
  # ammount getter
  @property
  def ammount(self) -> int:
    return int(self._ammount)
  # ammount setter
  @ammount.setter
  def ammount(self, _):
    self._ammount = _