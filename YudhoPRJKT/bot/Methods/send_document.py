from ...configs.config import AuthManager
from ...utils import ParseMode, CreateLog,  Inline
from ..types import Message
from  typing import Optional, Union, Any
from dataclasses import dataclass, field
from aiohttp.client import ClientSession
from aiohttp.client_exceptions import ClientConnectionError
from aiohttp.formdata import FormData
import json

@dataclass
class DataBots:
  raw_json: dict = field(default_factory=dict)
  serialized_json: str = field(default_factory=str)
  status_code: int = field(default_factory=int)
  message_id: str = field(default_factory=str)

async def send_document(chat_id: Union[str, int], document: str, caption: str, parse_mode: str, disable_notification: Optional[bool] = False, protect_content: Optional[bool] = False, reply_chat: Optional[Union[bool, str]] = True, reply_markup: Optional[str] = None) -> DataBots:
  try:
    f = FormData()
    f.add_field('chat_id',str(chat_id))
    f.add_field('caption', str(caption))
    f.add_field('parse_mode', str(parse_mode))
    f.add_field('disable_notification', str(disable_notification).lower())
    f.add_field('protect_content', str(protect_content).lower())
    # Check Input document
    if document.startswith('http://') or document.startswith('https://'):
      f.add_field('document', document)
    else:
      f.add_field('document', open(document, 'rb').read(), filename=document)
    if type(reply_chat) is bool and reply_chat is True:
      f.add_field('reply_parameters', json.dumps({
        'message_id': int(Message.message_id)
      }))
    elif type(reply_chat) is str:
      f.add_field('reply_parameters', json.dumps({
        'message_id': int(reply_chat)
      }))
    if reply_markup is not None:
      f.add_field('reply_markup', reply_markup)      
    async with ClientSession() as client:
      async with client.post(f"{AuthManager.ReadConfig().get('api')}/sendDocument", data=f) as session:
        raw = await session.json()
        if session.status == 200:
          return DataBots(raw, json.dumps(raw, indent=2), session.status, raw['result'].get('message_id', 'no_message-id'))
        else:
          return DataBots(raw, json.dumps(raw, indent=2), session.status, raw['result'].get('message_id', 'no_message-id'))
  except ClientConnectionError as e:
    CreateLog.Error(f"Error while use methods: sendDocument", str(e))
    return DataBots()