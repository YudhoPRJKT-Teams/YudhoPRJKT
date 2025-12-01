from ..bot.types.message import Message
from .long_polling import long_polling
from ..utils.create_log import CreateLog
from ..bot.bot import pick_command
import asyncio

# Distpatch
class Distpatch:
  # dispatch command
  @classmethod
  async def Command(cls):
    if Message.text:
      command = Message.text.split()[0]
      if command in pick_command:
        await pick_command[command]()

class Telegram:
  @classmethod
  async def Polling(cls):
    while True:
      try:
        cls.out = await long_polling()
        if 'message' in cls.out:
          msg_key = cls.out['message']
          
          # Message
          Message.text = msg_key.get("text", "")
          Message.message_id = msg_key.get("message_id", "")
          Message.date = msg_key.get("date", "")
          
          # message.chat
          Message.chat.id = msg_key["chat"].get("id", "")
          Message.chat.title = msg_key["chat"].get("title", "")
          Message.chat.username = f"@{msg_key['chat'].get('username', '')}"

          # mmessage.chat.from
          Message.From.id = msg_key["from"].get("id", "")
          Message.From.first_name = msg_key["from"].get("first_name", "")
          Message.From.last_name = msg_key["from"].get("last_name", "")
          Message.From.username = f"@{msg_key['from'].get('username', '')}"
          
          if "reply_to_message" in msg_key:
            reply_key = msg_key["reply_to_message"]
            # message.reply_to_message
            Message.reply_to_message.message_id = reply_key.get("message_id", "")
            Message.reply_to_message.text = reply_key.get("text", "")
            
            # message.reply_to_message.From
            Message.reply_to_message.From.id = reply_key["from"].get("id", "")
            Message.reply_to_message.From.first_name = reply_key["from"].get("first_name", "")
            Message.reply_to_message.From.last_name = reply_key["from"].get("last_name", "")
            Message.reply_to_message.From.username = f"@{reply_key['from'].get('username', '')}"

            # message.reply_to_message.chat
            Message.reply_to_message.chat.id = reply_key["chat"].get("id", "")
            Message.reply_to_message.chat.title = reply_key["chat"].get("title", "")
            Message.reply_to_message.chat.username = f"@{reply_key['chat'].get('username', '')}"
            Message.reply_to_message.chat.type = reply_key["chat"].get("type", "")
            Message.reply_to_message.chat.type = reply_key["chat"].get("type", "")
            
            # message.reply_to_message.photo
            if "photo" in reply_key and len(reply_key["photo"]) > 0:
                if reply_key["photo"][0]:
                    Message.reply_to_message.photo.file_id = reply_key["photo"][0].get("file_id", "")
                if len(reply_key["photo"]) > 1 and reply_key["photo"][1]:
                    Message.reply_to_message.photo.file_id = reply_key["photo"][1].get("file_id", "")
          await Distpatch.Command()
          await asyncio.sleep(1)
          return cls
      except KeyError as e:
        CreateLog.Error("Unable to find key for polling", str(e))
        
  class bot:
    @classmethod
    async def run(cls):
      """Run the telegram bots"""
      CreateLog.Info('Bot is running!')
      while True:
        await Telegram.Polling()
