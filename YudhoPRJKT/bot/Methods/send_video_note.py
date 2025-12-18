from aiohttp.client import ClientSession
from aiohttp.client_exceptions import ClientConnectionError
from aiohttp.formdata import FormData
from dataclasses import dataclass, field
from ...utils.create_log import CreateLog
from ..types.message import Message
from ...configs.config import AuthManager
import json

@dataclass
class DataBots:
  raw_json: dict = field(default_factory=dict)
  seriliazed_json: str = field(default_factory=str)
  status_code: int = field(default_factory=int)
  message_id: int = field(default_factory=int)
  
async def send_video_note(
  chat_id: int | str, 
  video_note: str, 
  business_connection_id: str | None = None, 
  message_thread_id: int | None = None, 
  direct_messages_topic_id: int | None = None, 
  duration: int | None = None,
  length: int | None = None,
  thumbnail: str | None = None,
  message_effect_id: str | None = None,
  suggested_post_parameters: str | None = None,
  disable_notification: bool = False,
  protect_content: bool = False,
  allow_paid_broadcast: bool = True,
  reply_chat: bool | str = False,
  reply_markup: str | None = None
) -> DataBots:
  try:
    f = FormData()
    f.add_field('chat_id', str(chat_id))
    
    # Check input video note
    if video_note.startswith(('http://', 'https://')):
      f.add_field('video_note', str(video_note))
    if video_note.endswith(('.mp4')):
      f.add_field('video_note', open(video_note, 'rb').read(), filename=video_note)
    if not video_note.endswith(('.mp4')):
      CreateLog.Error('To send a video note the file you must use .mpeg4 filename!')
    if disable_notification is True:
      f.add_field('disable_notification', str(True).lower())
    if protect_content is True:
      f.add_field('protect_content', str(True).lower())
    if allow_paid_broadcast is False:
      f.add_field('allow_paid_broadcast', str(False).lower())
    if type(reply_chat) is str:
      f.add_field('reply_parameters', json.dumps({'message_id', int(reply_chat)}))
    if type(reply_chat) is bool and reply_chat is True:
      f.add_field('reply_parameters', json.dumps({
        'message_id': int(Message.message_id)
      }))
    if reply_markup is not None:
      f.add_field('reply_markup', reply_markup)
    if (business_connection_id is not None or
      message_thread_id is not None or
      direct_messages_topic_id is not None or
      duration is not None or
      length is not None or
      thumbnail is not None or
      message_effect_id is not None or
      suggested_post_parameters is not None
    ):
      f.add_field('business_connection_id', business_connection_id)
      f.add_field('message_thread_id', message_thread_id)
      f.add_field('direct_messages_topic_id', direct_messages_topic_id)
      f.add_field('duration', duration)
      f.add_field('length', length)
      f.add_field('thumbnail', thumbnail)
      f.add_field('message_thread_id', message_thread_id)
      f.add_field('message_effect_id', message_effect_id)
      f.add_field('suggested_post_parameters', suggested_post_parameters)
    async with ClientSession() as client:
      async with client.post(f'{AuthManager.ReadConfig().get('api')}/sendVideoNote', data=f) as session:
        raw = await session.json()
        if session.status == 200:
          return DataBots(raw, json.dumps(raw, indent=2), session.status)
        else:
          return DataBots(raw, json.dumps(raw, indent=2), session.status)
  except ClientConnectionError as e:
    CreateLog.Error(f"Error while use methods: sendVideoNote", str(e))
    return DataBots()