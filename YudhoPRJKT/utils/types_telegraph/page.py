from ...bots.types.enable_types import EnableTypes

class Page(EnableTypes):
  def __init__(self) -> None:
    self._path: str
    self._url: str
    self._title: str
    self._description: str
    self._author_name: str
    self._author_url: str
    self._image_url: str
    self._content: list
    self._views: int
    self._can_edit: bool
  # path getter
  @property
  def path(self) -> str:
    return str(self._path)
  # path setter
  @path.setter
  def path(self, _):
    self._path = _
  # url getter
  @property
  def url(self) -> str:
    return str(self._url)
  # url setter
  @url.setter
  def url(self, _):
    self._url = _
  # title getter
  @property
  def title(self) -> str:
    return str(self._title)
  # title setter
  @title.setter
  def title(self, _):
    self._title = _
  # description getter
  @property
  def description(self) -> str:
    return str(self._description)
  # description setter
  @description.setter
  def description(self, _):
    self._description = _
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
  # image_url getter
  @property
  def image_url(self) -> str:
    return str(self._image_url)
  # image_url setter
  @image_url.setter
  def image_url(self, _):
    self._image_url = _
  # content getter
  @property
  def content(self) -> list:
    return list(self._content)
  # content setter
  @content.setter
  def content(self, _):
    self._content = _
  # views getter
  @property
  def views(self) -> int:
    return int(self._views)
  # views setter
  @views.setter
  def views(self, _):
    self._views = _
  # can_edit getter
  @property
  def can_edit(self) -> bool:
    return bool(self._can_edit)
  # can_edit setter
  @can_edit.setter
  def can_edit(self, _):
    self._can_edit = _
  