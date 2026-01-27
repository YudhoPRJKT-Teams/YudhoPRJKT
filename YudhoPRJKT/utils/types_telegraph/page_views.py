from ...bots.types.enable_types import EnableTypes

class PageViews(EnableTypes):
  def __init__(self) -> None:
    self._views: int
  # views getter
  @property
  def views(self) -> int:
    return int(self._views)
  # views setter
  @views.setter
  def views(self, _):
    self._views = _