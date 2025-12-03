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
  
async def edit_message_text(chat_id: Union[str, int], message_id: Union[str,int], text: Any, parse_mode: str, reply_markup: Optional[str] = None):
  try:
    payload = {
      'chat_id': chat_id,
      'message_id': message_id,
      'text': text,
      'parse_mode': parse_mode
    }
    if reply_markup is not None:
      payload.update({'reply_markup': reply_markup})
    async with aiohttp.ClientSession() as client:
      async with client.post(f'{AuthManager.ReadConfig().get('api')}/editMessageText', json=payload) as session:
        raw = await session.json()
        if session.status == 200:
          return DataBots(raw,json.dumps(raw, indent=2), session.status, raw['result']['message_id'])
        else:
          return DataBots(raw,json.dumps(raw, indent=2), session.status, raw['result']['message_id'])
  except aiohttp.ClientConnectionError as e:
    CreateLog.Error(f"Error while use methods: editMessageText", str(e))
    return DataBots()