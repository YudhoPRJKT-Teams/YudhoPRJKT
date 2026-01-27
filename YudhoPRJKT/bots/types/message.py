from .enable_types import EnableTypes
from .user import User
from .chat import Chat

class Message(EnableTypes):
  def __init__(self):
    self._message_id: int
    self._text: str
    self._date: str
    self.From = User()
    self.chat = Chat()
  # message_id getter
  @property
  def message_id(self) -> int:
    return int(self._message_id)
  # message_id setter
  @message_id.setter
  def message_id(self, _):
    self._message_id = _
  # text getter
  @property
  def text(self) -> str:
    return str(self._text)
  # text setter
  @text.setter
  def text(self, _):
    self._text = _
  # date getter
  @property
  def date(self) -> str:
    return str(self._date)
  # date setter
  @date.setter
  def date(self, _):
    self._date = _