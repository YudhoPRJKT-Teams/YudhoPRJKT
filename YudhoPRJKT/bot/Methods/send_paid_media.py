from aiohttp.client import ClientSession
from aiohttp.client_exceptions import ClientConnectionError
from aiohttp.formdata import FormData
from dataclasses import dataclass, field
from ...utils.create_log import CreateLog
from ..types.message import Message
from ...configs.config import AuthManager
import json
import re
import os

@dataclass
class DataBots:
  raw_json: dict = field(default_factory=dict)
  seriliazed_json: str = field(default_factory=str)
  status_code: int = field(default_factory=int)
  message_id: int = field(default_factory=int)
  
async def send_paid_media(
  chat_id: int | str,
  star_count: int,
  media: str,
  # business_connection_id: str | None = None,
  # message_thread_id: int | None = None,
  # direct_messages_topic_id: int | None = None,
  # payload: str | None = None,
  # caption: str | None = None,
  # parse_mode: str | None = None,
  # caption_entities: str | None = None,
  # show_caption_above_media: bool | None = True,
  # disable_notification: bool | None = False,
  # protect_content: bool | None = False,
  # allow_paid_broadcast: bool | None = None,
  # suggested_post_parameters: bool | None = None,
  # reply_chat: str | bool = False,
  # reply_markup: str | None = None
) -> DataBots:
  try:
    f = FormData()
    f.add_field('chat_id', str(chat_id))
    f.add_field('star_count', str(star_count))
    cut_filetype = os.path.splitext(media)
    # Send as photo
    if media.endswith(('.jpg', '.jpeg', '.png', '.webp')):
      f.add_field('media', json.dumps(
        [
          {
            'type': 'photo',
            'media': f'attach://{cut_filetype}',
          }
        ]
      ))
    f.add_field(f'{cut_filetype}', open(media, 'rb').read(), filename=media)
    async with ClientSession() as client:
      async with client.post(f'{AuthManager.ReadConfig().get('api')}/sendPaidMedia', data=f) as session:
        raw = await session.json()
        if session.status == 200:
          return DataBots(raw, json.dumps(raw, indent=2), session.status, raw['result'].get('message_id', 'no_message_id'))
        else:
          return DataBots(raw, json.dumps(raw, indent=2), session.status, raw['result'].get('message_id', 'no_message_id'))
  except ClientConnectionError as e:
    CreateLog.Error(f'Got Error in methods sendPaidMedia', str(e))
    return DataBots()