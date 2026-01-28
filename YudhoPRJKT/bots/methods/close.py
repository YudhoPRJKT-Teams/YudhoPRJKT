from ...connector.client import TelegramMethods

class Close(TelegramMethods):
  def __init__(self):
    super().__init__('close', 'GET')
  def __str__(self) -> str:
    return self.serialized_json