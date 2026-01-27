from .enable_types import EnableTypes

class LinkPreviewOptions(EnableTypes):
  def __init__(self) -> None:
    self._is_disabled: bool
    self._url: str
    self._prefer_small_media: bool
    self._prefer_large_media: bool
    self._show_above_text: bool
  # is_disabled getter
  @property
  def is_disabled(self) -> bool:
    return bool(self._is_disabled)
  # is_disabled setter
  @is_disabled.setter
  def is_disabled(self, _):
    self._is_disabled = _
  # url getter
  @property
  def url(self) -> str:
    return str(self._url)
  # url setter
  @url.setter
  def url(self, _):
    self._url = _
  # prefer_small_media getter
  @property
  def prefer_small_media(self) -> bool:
    return bool(self._prefer_small_media)
  # prefer_small_media setter
  @prefer_small_media.setter
  def prefer_small_media(self, _):
    self._prefer_small_media = _
  # prefer_large_media getter
  @property
  def prefer_large_media(self) -> bool:
    return bool(self._prefer_large_media)
  # prefer_large_media setter
  @prefer_large_media.setter
  def prefer_large_media(self, _):
    self._prefer_large_media = _
  # show_above_text getter
  @property
  def show_above_text(self) -> bool:
    return bool(self._show_above_text)
  # show_above_text setter
  @show_above_text.setter
  def show_above_text(self, _):
    self._show_above_text = _