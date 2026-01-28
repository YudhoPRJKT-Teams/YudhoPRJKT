from typing import Any
from ...connector.client import TelegramMethods
from ..types import SuggestedPostParameters, Message

class forward_message(TelegramMethods):
  def __init__(self,
    chat_id: int | str,
    from_chat_id: int | str,
    message_id: int,
    # Optional
    message_thread_id: int | None = None,
    direct_messages_topic_id: int | None = None,
    video_start_timestamp: int | None = None,
    disable_notification: bool = False,
    protect_content: bool = False,
    message_effect_id: str | None = None,
    suggested_post_parameters: SuggestedPostParameters | None = None,
  ):
    self.payload: dict = {
      'chat_id': chat_id,
      'from_chat_id': from_chat_id,
      'message_id': message_id,
      'disable_notification': disable_notification,
      'protect_content': protect_content
    }
    if message_thread_id is not None:
      self.payload.update({'message_thread_id': message_thread_id})
    if direct_messages_topic_id is not None:
      self.payload.update({'direct_messages_topic_id': direct_messages_topic_id})
    if video_start_timestamp is not None:
      self.payload.update({'video_start_timestamp': video_start_timestamp})
    if message_effect_id is not None:
      self.payload.update({'message_effect_id': message_effect_id})
    if suggested_post_parameters is not None:
      self.payload.update({'suggested_post_parameters': suggested_post_parameters})
    super().__init__('forwardMessage', 'POST', data=self.payload)
  # async def parse_updater(self) -> Message:
  def __str__(self) -> str:
    return self.serialized_json