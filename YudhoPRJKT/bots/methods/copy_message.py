from typing import Any
from ...connector.client import TelegramMethods
from ..types import MessageId, MessageEntity, SuggestedPostParameters, Message
from ...utils import ParseMode, Inline

class copy_message(TelegramMethods):
  def __init__(self,
    chat_id: int | str,
    from_chat_id: int | str,
    message_id: int,
    show_caption_above_media: bool = True,
    disable_notification: bool = False,
    protect_content: bool = False,
    allow_paid_broadcast: bool = True,
    # Optional
    message_thread_id: int | None = None,
    direct_messages_topic_id: int | None = None,
    video_start_timestamp: int | None = None,
    caption: str | None = None,
    parse_mode: ParseMode | None = None,
    caption_entities: MessageEntity | None = None,
    message_effect_id: str | None = None,
    suggested_post_parameters: SuggestedPostParameters | None = None,
  ):
    self.message = Message()
    self.payload: dict = {
      'chat_id': chat_id,
      'from_chat_id': from_chat_id,
      'message_id': message_id,
      'show_caption_above_media': show_caption_above_media,
      'disable_notification': disable_notification,
      'protect_content': protect_content,
      'allow_paid_broadcast': allow_paid_broadcast
    }
    if message_thread_id is not None:
      self.payload.update({'message_thread_id': message_thread_id})
    if direct_messages_topic_id is not None:
      self.payload.update({'direct_messages_topic_id': direct_messages_topic_id})
    if video_start_timestamp is not None:
      self.payload.update({'video_start_timestamp': video_start_timestamp})
    if caption is not None:
      self.payload.update({'caption': caption})
    if parse_mode is not None:
      self.payload.update({'parse_mode': parse_mode})
    if caption_entities is not None:
      self.payload.update({'caption_entities': caption_entities})
    if message_effect_id is not None:
      self.payload.update({'message_effect_id': message_effect_id})
    if suggested_post_parameters is not None:
      self.payload.update({'suggested_post_parameters': suggested_post_parameters})
    super().__init__('copyMessage', 'POST', data=self.payload)
  def reply(self):
    """Reply Message"""
    self.message_id: int
    self.chat_id: int
    if self.message.message_id:
      self.message_id = self.message.message_id
      self.chat_id = self.message.chat.id
    self.payload.update(
      {
        'reply_parameters': {
          'chat_id': self.chat_id,
          'message_id': self.message_id
        }
      }
    )
    return self
  def inline(self, inline: Inline):
    self.payload.update({'reply_markup': inline})
    return self
  async def parse_updater(self) -> Any:
    if self.status_code == 200:
      updater = self.raw['result']
      MessageId().message_id = updater.get('message_id', 'no-message_id')
      return MessageId()
  def __str__(self) -> str:
    return self.serialized_json