from ...configs.config import AuthManager
from ...utils import ParseMode, CreateLog,  Inline
from ..types import Message
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

async def send_animation(chat_id: int | str, animation: str, duration: int | None = None, width: int | None = None, height: int | None = None, thumbnail: str | None = None, caption: str | None = None, parse_mode: str | None = None, show_caption_above_media: bool = True, has_spoiler: bool = False, disable_notification: bool = False, protect_content: bool = False, reply_chat: bool | str = False, reply_markup: str | None = None) -> DataBots:
  try:
    f = FormData()
    # Check animation links or not
    f.add_field('chat_id', str(chat_id))
    # payload
    if animation.startswith('http://') or animation.startswith('https://'):
      f.add_field('animation', animation)
    if not animation.endswith('.gif'):
      CreateLog.Error('Filenames for animation to send must .gif filetype')
    if animation.endswith('.gif'):
      f.add_field('animation', open(animation, 'rb').read(), filename=animation)
    if duration is not None:
      f.add_field('duration', duration)
    if width is not None:
      f.add_field('width', width)
    if height is not None:
      f.add_field('height', height)
    if thumbnail is not None and thumbnail.startswith('https://') or thumbnail is not None and thumbnail.startswith('https://'):
      f.add_field('thumbnail', thumbnail)
    if thumbnail is not None and not thumbnail.endswith('.png') or thumbnail is not None and not thumbnail.endswith('.jpg'):
      CreateLog.Error('Filenames for thumbnail to send must .png or .jpg filetype')
    if caption is not None:
      f.add_field('caption', str(caption))
    if parse_mode is not None:
      f.add_field('parse_mode', str(parse_mode))
    if show_caption_above_media is False:
      f.add_field('show_caption_above_media', str(show_caption_above_media).lower())
    if protect_content is True:
      f.add_field('protect_content', str(protect_content).lower())
    if disable_notification is True:
      f.add_field('disable_notification', str(disable_notification).lower())
    if reply_chat is True:
      f.add_field('reply_parameters', json.dumps({'message_id': int(Message.message_id)}))
    if type(reply_chat) is str:
      f.add_field('reply_parameters', json.dumps({'message_id': int(reply_chat)}))
    if reply_markup is not None:
      f.add_field('reply_markup', reply_markup)
    async with ClientSession() as client:
      async with client.post(f'{AuthManager.ReadConfig().get('api')}/sendAnimation', data=f) as session:
        raw = await session.json()
        if session.status == 200:
          return DataBots(raw, json.dumps(raw, indent=2), session.status, raw['result'].get('message_id', 'no_message-id'))
        else:
          return DataBots(raw, json.dumps(raw, indent=2), session.status, raw['result'].get('message_id', 'no_message-id'))
  except ClientConnectionError as e:
    CreateLog.Error(f"Error while use methods: sendAnimation", str(e))
    return DataBots()