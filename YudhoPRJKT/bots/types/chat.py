from .enable_types import EnableTypes

class Chat(EnableTypes):
  def __init__(self) -> None:
    self._id: int 
    self._type: str
    self._title: str
    self._username: str
    self._first_name: str
    self._last_name: str
    self._is_forum: bool
    self._is_direct_messages: bool 
  # id getter
  @property
  def id(self) -> int:
    return int(self._id)
  # id setter
  @id.setter
  def id(self, _):
    self._id = _
  # type getter
  @property
  def type(self) -> str:
    return str(self._type)
  # type setter
  @type.setter
  def type(self, _):
    self._type = _
  # title getter
  @property
  def title(self) -> str:
    return str(self._title)
  # title setter
  @title.setter
  def title(self, _):
    self._title = _
  # username getter
  @property
  def username(self) -> str:
    return str(self._username)
  # username setter
  @username.setter
  def username(self, _):
    self._username = _
  # first_name getter
  @property
  def first_name(self) -> str:
    return str(self._first_name)
  # first_name setter
  @first_name.setter
  def first_name(self, _):
    self._first_name = _
  # last_name getter
  @property
  def last_name(self) -> str:
    return str(self._last_name)
  # last_name setter
  @last_name.setter
  def last_name(self, _):
    self._last_name = _
  # is_forum getter
  @property
  def is_forum(self) -> bool:
    return bool(self._is_forum)
  # is_forum setter
  @is_forum.setter
  def is_forum(self, _):
    self._is_forum = _
  # is_direct_messages getter
  @property
  def is_direct_messages(self) -> bool:
    return bool(self._is_direct_messages)
  # is_direct_messages setter
  @is_direct_messages.setter
  def is_direct_messages(self, _):
    self._is_direct_messages = _
  