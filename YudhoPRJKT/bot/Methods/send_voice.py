from aiohttp.client import ClientSession
from aiohttp.client_exceptions import ClientConnectionError
from aiohttp.formdata import FormData
from dataclasses import dataclass, field
from ...utils.create_log import CreateLog
from ...configs.config import AuthManager
from ..types.message import Message
import json

@dataclass
class BotsData:
  raw_json: dict = field(default_factory=dict)
  seriliazed_json: str = field(default_factory=str)
  status_code: int | None = field(default_factory=int)
  message_id: int | None = field(default_factory=int)
  
async def send_voice(chat_id: int | str, voice: str, caption: str | None = None, parse_mode: str | None = None, duration: int | None = None, disable_notification: bool = False, protect_content: bool = False, reply_chat: bool | str = False, reply_markup: str | None = None, business_connection_id: str | None = None, message_thread_id: int | str | None = None, direct_messages_topic_id: int | str | None = None, caption_entities: list | None = None, allow_paid_broadcast: bool = True, message_effect_id: str | None = None, suggested_post_parameters: str  | None = None) -> BotsData:
  try:
    forms = FormData()
    forms.add_field('chat_id', str(chat_id))
    if voice.startswith('http://') or voice.startswith('https://'):
      forms.add_field('voice', str(voice))
    if voice.endswith('.ogg') or voice.endswith('.opus') or voice.endswith('.mp3') or voice.endswith('.m4a'):
      forms.add_field('voice', open(voice, 'rb').read(), filename=voice)
    if not voice.endswith('.ogg') or not voice.endswith('.opus') or not voice.endswith('.mp3') or not voice.endswith('.m4a'):
      CreateLog.Error('Please use filename .ogg/.opus/.mp3/.m4a')
    if caption is not None:
      forms.add_field('caption', str(caption))
    if parse_mode is not None:
      forms.add_field('parse_mode', str(parse_mode))
    if duration is not None:
      forms.add_field('duration', str(duration))
    if disable_notification is True:
      forms.add_field('disable_notification', str(disable_notification).lower())
    if protect_content is True:
      forms.add_field('protect_content', str(protect_content).lower())
    if reply_markup is not None:
      forms.add_field('reply_markup', reply_markup)
    if business_connection_id is not None:
      forms.add_field('business_connection_id', str(business_connection_id))
    if message_thread_id is not None:
      forms.add_field('message_thread_id', str(message_thread_id))
    if direct_messages_topic_id is not None:
      forms.add_field('direct_messages_topic_id', str(direct_messages_topic_id))
    if caption_entities is not None:
      forms.add_field('caption_entities', str(caption_entities))
    if type(allow_paid_broadcast) is bool:
      forms.add_field('allow_paid_broadcast', str(allow_paid_broadcast).lower())
    if message_effect_id is not None:
      forms.add_field('message_effect_id', str(caption_entities))
    if suggested_post_parameters is not None:
      forms.add_field('suggested_post_parameters', str(suggested_post_parameters))
    # Reply chat
    if type(reply_chat) is str:
      forms.add_field('reply_parameters', json.dumps({'message_id': int(reply_chat)}))
    if type(reply_chat) is bool and reply_chat is True:
      forms.add_field('reply_parameters', json.dumps({'message_id': int(Message.message_id)}))
    async with ClientSession() as client:
      async with client.post(f'{AuthManager.ReadConfig().get('api')}/sendVoice', data=forms) as session:
        raw = await session.json()
        if session.status == 200:
          return BotsData(raw, json.dumps(raw, indent=2), int(session.status))
        else:
          return BotsData(raw, json.dumps(raw, indent=2), int(session.status))
  except ClientConnectionError as e:
    CreateLog.Error(f'Got error! on methods sendVoice', str(e))
    return BotsData()
