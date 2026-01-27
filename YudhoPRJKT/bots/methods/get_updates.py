from ...connector.client import TelegramMethods

class get_updates(TelegramMethods):
  def __init__(self,
    offset: int | None = None,
    limit: int = 100,
    timeout: int = 0,
    allowed_updates: str | None = None
  ):
    payload: dict = {
      'limit': limit,
      'timeout': timeout
    }
    if offset is not None:
      payload.update({'offset': offset})
    if allowed_updates is not None:
      payload.update({'allowed_updates': allowed_updates})
    super().__init__('getUpdates', 'GET', params=payload)
  def __str__(self) -> str:
    return self.raw.__str__()