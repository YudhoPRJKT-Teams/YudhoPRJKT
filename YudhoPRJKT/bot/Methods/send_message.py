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

async def send_message(chat_id: Union[str,int], text: Any, parse_mode: str, disable_notification: bool = False, protect_content: bool = False, reply_markup: Optional[str] = None, reply_chat: Optional[Union[str, bool]] = True):
  try:
    payload = {
      'chat_id': chat_id,
      'text': text,
      'parse_mode': parse_mode,
      'disable_notification': disable_notification,
      'protect_content': protect_content
    }
    # reply_chat
    if type(reply_chat) is bool and reply_chat is True:
      payload.update({'reply_parameters': {'message_id': int(Message.message_id)}})
    elif type(reply_chat) is int:
      payload.update({'reply_parameters': {'message_id': int(reply_chat)}})
    # reply_markup
    if reply_markup is not None:
      payload.update({'reply_markup': reply_markup})
    async with aiohttp.ClientSession() as client:
      async with client.post(f"{AuthManager.ReadConfig().get('api')}/sendMessage", json=payload) as session:
        raw = await session.json()
        if session.status == 200:
          return DataBots(raw, json.dumps(raw, indent=2), session.status)
        else:
          return DataBots(raw, json.dumps(raw, indent=2), session.status)
  except aiohttp.ClientConnectorError as e:
    CreateLog.Error(f"Error while use methods: sendMessage", str(e))
    return DataBots()