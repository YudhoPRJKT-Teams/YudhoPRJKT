from .enable_types import EnableTypes

class MessageId(EnableTypes):
  def __init__(self) -> None:
    self._message_id: int
  # message_id getter
  @property
  def message_id(self) -> int:
    return int(self._message_id)
  # message_id setter
  @message_id.setter
  def message_id(self, _):
    self._message_id = _