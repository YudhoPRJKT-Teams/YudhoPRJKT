from dataclasses import dataclass, field
from ...client.connector import BaseConnector
from ...configs.handlers import Config

conf = Config()

@dataclass
class BotsData:
  raw: dict = field(default_factory=dict)
  serialized_json: str = field(default_factory=str)
  status_code: int = field(default_factory=int)
  
class get_me:
  def __init__(self):
    self.methods = 'getMe'
  async def _exc(self) -> BotsData:
    async with BaseConnector.get(f'{conf.api}/{self.methods}') as client:
      return BotsData(client.raw, client.serilized_json, client.status_code)
  def __await__(self):
    return self._exc().__await__()