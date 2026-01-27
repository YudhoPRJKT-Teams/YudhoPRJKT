from .enable_types import EnableTypes
from .user import User

class MessageEntity(EnableTypes):
  def __init__(self) -> None:
    self._type: str
    self._offset: int
    self._length: int
    self._url: str
    self.user: User
    self._language: str
    self._custom_emoji_set: str
  # type getter
  @property
  def type(self) -> str:
    return str(self._type)
  # type setter
  @type.setter
  def type(self, _):
    self._type = _
  # offset getter
  @property
  def offset(self) -> int:
    return int(self._offset)
  # offset setter
  @offset.setter
  def offset(self, _):
    self._offset = _
  # length getter
  @property
  def length(self) -> int:
    return int(self._length)
  # length setter
  @length.setter
  def length(self, _):
    self._length = _
  # url getter
  @property
  def url(self) -> str:
    return str(self._url)
  # url setter
  @url.setter
  def url(self, _):
    self._url = _
  # language getter
  @property
  def language(self) -> str:
    return str(self._language)
  # language setter
  @language.setter
  def language(self, _):
    self._language = _
  # custom_emoji_set getter
  @property
  def custom_emoji_set(self) -> str:
    return str(self._custom_emoji_set)
  # custom_emoji_set setter
  @custom_emoji_set.setter
  def custom_emoji_set(self, _):
    self._custom_emoji_set = _