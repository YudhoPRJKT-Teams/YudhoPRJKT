from ...bots.types.enable_types import EnableTypes

class Account(EnableTypes):
  def __init__(self) -> None:
    self._short_name: str
    self._author_name: str
    self._author_url: str
    self._access_token: str
    self._auth_url: str
    self._page_count: int
  # short_name getter
  @property
  def short_name(self) -> str:
    return str(self._short_name)
  # short_name setter
  @short_name.setter
  def short_name(self, _):
    self._short_name = _
  # author_name getter
  @property
  def author_name(self) -> str:
    return str(self._author_name)
  # author_name setter
  @author_name.setter
  def author_name(self, _):
    self._author_name = _
  # author_url getter
  @property
  def author_url(self) -> str:
    return str(self._author_url)
  # author_url setter
  @author_url.setter
  def author_url(self, _):
    self._author_url = _
  # access_token getter
  @property
  def access_token(self) -> str:
    return str(self._access_token)
  # access_token setter
  @access_token.setter
  def access_token(self, _):
    self._access_token = _
  # auth_url getter
  @property
  def auth_url(self) -> str:
    return str(self._auth_url)
  # auth_url setter
  @auth_url.setter
  def auth_url(self, _):
    self._auth_url = _
  # page_count getter
  @property
  def page_count(self) -> int:
    return int(self._page_count)
  # page_count setter
  @page_count.setter
  def page_count(self, _):
    self._page_count = _