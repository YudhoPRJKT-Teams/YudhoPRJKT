from .enable_types import EnableTypes
from .suggested_post_price import SuggestedPostPrice

class SuggestedPostParameters(EnableTypes):
  def __init__(self) -> None:
    self.price = SuggestedPostPrice()
    self._send_date: int
  # send_date getter
  @property
  def send_date(self) -> int:
    return int(self._send_date)
  # send_date setter
  @send_date.setter
  def send_date(self, _):
    self._send_date = _
  