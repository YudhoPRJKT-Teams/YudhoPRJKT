from ...bots.types.enable_types import EnableTypes

class NodeElement(EnableTypes):
  def __init__(self) -> None:
    self._tag: str
    self._attrs: str
    self._children: list
  # tag getter
  @property
  def tag(self) -> str:
    return str(self._tag)
  # tag setter
  @tag.setter
  def tag(self, _):
    self._tag = _
  # attrs getter
  @property
  def attrs(self) -> str:
    return str(self._attrs)
  # attrs setter
  @attrs.setter
  def attrs(self, _):
    self._attrs = _
  