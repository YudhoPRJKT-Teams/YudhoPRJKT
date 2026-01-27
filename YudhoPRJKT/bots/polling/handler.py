from ...connector.client import TelegramMethods
from ...utils.log import Log
from ..methods.get_updates import get_updates
from ..types.message import Message
import asyncio
import json

class clear_polling(TelegramMethods):
  def __init__(self):
    super().__init__('getUpdates', 'GET')
  async def parse_updater(self):
    if self.raw['result']:
      offset = max(updater["update_id"] for updater in self.raw["result"]) + 1
      payload = {'offset': offset}
      async with TelegramMethods('getUpdates', 'GET', params=payload) as client:
        await client.read()
    else:
      pass
    return self
class long_polling:
  def __init__(self):
    pass
  async def __aiter__(self):
    await clear_polling()
    offset = None
    while True:
      fr = await get_updates(offset)
      if fr.raw and 'result' in fr.raw:
        for updater in fr.raw['result']:
          offset = updater.get('update_id', 'no-update_id') + 1
          yield updater
        await asyncio.sleep(0.1)
class Polling:
  def __init__(self) -> None:
    self.message = Message()
  async def _exc(self):
    try:
      async for updater in long_polling():
        if 'message' in updater:
          msg = updater.get('message')
          self.message.message_id = msg.get('message_id', 'no-message_id')
          self.message.text = msg.get('text', 'no-text')
          self.message.date = msg.get('date', 'no-date')
          # message.from
          if 'from' in msg:
            fr = msg['from']
            self.message.From.id = fr.get('id', 'no-id')
            self.message.From.is_bot = fr.get('is_bot', 'no-is_bot')
            self.message.From.first_name = fr.get('first_name', 'no-first_name')
            self.message.From.last_name = fr.get('last_name', 'no-last_name')
            self.message.From.username = f"@{fr.get('username', 'no-username')}"
            self.message.From.language_code = fr.get('language_code', 'no-language_code')
          # message.from
          if 'chat' in msg:
            ch = msg['chat']
            self.message.chat.id = ch.get('id', 'no-id')
            self.message.chat.title = ch.get('title', 'no-title')
            self.message.chat.username = f"@{ch.get('username', 'no-username')}"
            self.message.chat.type = ch.get('type', 'no-type')
        # Distpatcher
        await Distpatch().Command(self.message)
        await asyncio.sleep(0.1)
    except KeyError as e:
      Log.Error(e.__str__())
  async def run(self):
    await asyncio.create_task(self._exc())
    await asyncio.sleep(0.1)

class Distpatch:
  def __init__(self) -> None:
    pass
  async def Command(self, message):
    from ..bot import pick_command
    msg = message
    if msg.text:
      command = msg.text.split()[0]
      if command in pick_command:
        await pick_command[command]()
