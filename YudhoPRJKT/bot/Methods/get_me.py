import aiohttp
import json
from dataclasses import dataclass, field
from typing import Optional, Union, Any
from ...configs.config import AuthManager
from ...utils import CreateLog

@dataclass
class DataBots:
  raw_json: dict = field(default_factory=dict)
  serialized_json: str = field(default_factory=str)
  status_code: int = field(default_factory=int)
  message_id: str = field(default_factory=str)

async def get_me() -> DataBots:
  try:
    async with aiohttp.ClientSession() as client:
      async with client.get(f"{AuthManager.ReadConfig().get('api')}/getMe") as session:
        raw = await session.json()
        if session.status == 200:
          return DataBots(raw, json.dumps(raw, indent=2), session.status)
        else:
          return DataBots(raw, json.dumps(raw, indent=2), session.status)
  except aiohttp.ClientConnectorError as e:
    CreateLog.Error(f"Error while use methods: getMe", str(e))
    return DataBots()