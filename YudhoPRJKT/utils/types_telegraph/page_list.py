from ...bots.types.enable_types import EnableTypes

class PageList(EnableTypes):
  def __init__(self) -> None:
    self._total_count: int
    self._pages: list
  # total_count getter
  @property
  def total_count(self) -> int:
    return int(self._total_count)
  # total_count setter
  @total_count.setter
  def total_count(self, _):
    self._total_count = _
  # pages getter
  @property
  def pages(self) -> list:
    return list(self._pages)
  # pages setter
  @pages.setter
  def pages(self, _):
    self._pages = _