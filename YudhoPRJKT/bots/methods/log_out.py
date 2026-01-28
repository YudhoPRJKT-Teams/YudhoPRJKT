from ...connector.client import TelegramMethods

class log_out(TelegramMethods):
  def __init__(self):
    super().__init__('logOut', 'GET')
  def __str__(self) -> str:
    return self.serialized_json