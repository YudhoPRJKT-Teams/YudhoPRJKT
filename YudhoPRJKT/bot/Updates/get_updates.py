import aiohttp
import json
from dataclasses import dataclass
from typing import Optional, Union, Any
from ...configs.config import AuthManager
from ...utils import CreateLog

@dataclass
class DataBots:
  raw_json: Optional[dict] = None
  serialized_json: Optional[str] = None
  status_code: Optional[int] = None

async def get_updates(offset: Optional[int] = None):
  try:
    payload = {'timeout': 0}
    if offset is not None:
      payload.update({'offset': offset})
    async with aiohttp.ClientSession() as client:
      async with client.get(f"{AuthManager.ReadConfig().get('api')}/getUpdates", params=payload) as session:
        raw = await session.json()
        if session.status == 200:
          return DataBots(raw, json.dumps(raw, indent=2), session.status)
        else:
          return DataBots(raw, json.dumps(raw, indent=2), session.status)
  except aiohttp.ClientConnectorError as e:
    CreateLog.Error(f"Error while use methods: getUpdates", str(e))
    return DataBots()