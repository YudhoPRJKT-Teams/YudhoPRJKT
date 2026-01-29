from ...connector.client import TelegramMethods
from ..types import MessageId

class copy_messages(TelegramMethods):
  def __init__(self,
    chat_id: int | str,
    from_chat_id: int | str,
    message_ids: list,
    disable_notification: bool = False,
    protect_content: bool = False,
    remove_caption: bool = False,
    # Optional
    message_thread_id: int | None = None,
    direct_messages_topic_id: int | None = None,
  ):
    payload: dict = {
      'chat_id': chat_id,
      'from_chat_id': from_chat_id,
      'message_ids': message_ids,
      'disable_notification': disable_notification,
      'protect_content': protect_content,
      'remove_caption': remove_caption
    }
    if message_thread_id is not None:
      payload.update({'message_thread_id': message_thread_id})
    if direct_messages_topic_id is not None:
      payload.update({'direct_messages_topic_id': direct_messages_topic_id})
    super().__init__('copyMessages', 'POST', data=payload)
  async def parse_updater(self):
    self.msgID = MessageId()
    slices = []
    if self.status_code == 200:
      raw = self.raw.get('result', [])
      for updater in raw:
        msg_id = updater.get('message_id', 'no-message_id')
        slices.append(msg_id)
      for updatable_ids in slices:
        self.msgID.message_id = updatable_ids
    return self
  def __str__(self) -> str:
    return self.serialized_json