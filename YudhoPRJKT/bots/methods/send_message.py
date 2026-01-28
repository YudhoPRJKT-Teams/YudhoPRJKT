from ...connector.client import TelegramMethods
from ...utils import ParseMode, Inline
from ..types import Message, LinkPreviewOptions, MessageEntity, SuggestedPostParameters
import json

class send_message(TelegramMethods):
  def __init__(self,
    chat_id:  int | str,
    text: str,
    parse_mode: ParseMode,
    # Optional
    business_connection_id: str | None = None,
    message_thread_id: int | None =None,
    direct_messages_topic_id: int | None = None,
    entities: MessageEntity | None = None,
    link_preview_options: LinkPreviewOptions | None =None,
    disable_notification: bool | None = False,
    protect_content: bool | None = False,
    allow_paid_broadcast: bool | None = True,
    message_effect_id: str | None = None,
    suggested_post_parameters: SuggestedPostParameters | None = None
  ):
    self.message = Message()
    self.payload: dict = {
      'chat_id': chat_id,
      'text': text,
      'parse_mode': parse_mode,
      'disable_notification': disable_notification,
      'protect_content': protect_content
    }
    if business_connection_id is not None:
      self.payload.update({'business_connection_id': business_connection_id})
    if message_thread_id is not None:
      self.payload.update({'message_thread_id': message_thread_id})
    if entities is not None:
      self.payload.update({'entities': json.dumps(entities)})
    if direct_messages_topic_id is not None:
      self.payload.update({'direct_messages_topic_id': direct_messages_topic_id})
    if link_preview_options is not None:
      self.payload.update({'link_preview_options': link_preview_options})
    if allow_paid_broadcast is not None:
      self.payload.update({'allow_paid_broadcast': allow_paid_broadcast})
    if message_effect_id is not None:
      self.payload.update({'message_effect_id': message_effect_id})
    if suggested_post_parameters is not None:
      self.payload.update({'suggested_post_parameters': suggested_post_parameters})
    super().__init__('sendMessage', 'POST', json=self.payload)
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
  def __str__(self) -> str:
    return self.serialized_json