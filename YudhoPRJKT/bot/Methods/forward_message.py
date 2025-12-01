import aiohttp
import json
from dataclasses import dataclass
from typing import Optional, Union, Any
from ...configs.config import AuthManager
from ...utils import CreateLog
from ..types.message import Message

@dataclass
class DataBots:
  raw_json: Optional[dict] = None
  serialized_json: Optional[str] = None
  status_code: Optional[int] = None
  message_id: Optional[int] = None
  
  
async def forward_message(chat_id: Union[str, int], from_chat_id: Union[str, int] = Message.chat.id, disable_notification: Optional[bool] = False, protect_content: Optional[bool] = False, message_id: Union[str,int] = Message.message_id):
  try:
    payload = {
      'chat_id': chat_id,
      'from_chat_id': from_chat_id,
      'disable_notification': disable_notification,
      'protect_content': protect_content,
      'message_id': message_id
    }
    async with aiohttp.ClientSession() as client:
      async with client.post(f"{AuthManager.ReadConfig().get('api')}/forwardMessage", json=payload) as session:
        raw = await session.json()
        if session.status == 200:
          return DataBots(raw,json.dumps(raw, indent=2), session.status, raw['result']['message_id'])
        else:
          return DataBots()
  except aiohttp.ClientConnectionError as e:
    CreateLog.Error(f"Error while use methods: forwardMessage", str(e))
    return DataBots()
