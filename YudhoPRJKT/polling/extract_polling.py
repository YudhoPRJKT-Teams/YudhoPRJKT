from ..bot.types.message import Message
from ..bot.types.chat_join_request import chat_join_request
from ..bot.types.new_chat_participant import new_chat_participant
from ..bot.types.left_chat_participant import left_chat_participant
from .long_polling import long_polling
from ..utils.create_log import CreateLog
from ..bot.bot import pick_command, bot
import asyncio
import json

# Distpatch
class Distpatch:
  # dispatch command
  @classmethod
  async def Command(cls):
    if Message.text:
      command = Message.text.split()[0]
      if command in pick_command:
        await pick_command[command]()
  @classmethod      
  async def ChatJoinRequest(cls):
    for handlers in bot.event.handlers_user_join:
      await handlers()
      
  # new chat member
  @classmethod
  async def NewChatMember(cls):
    for handlers in bot.event.handlers_joined_user:
      await handlers()
      
  # user left member
  @classmethod
  async def UserChatLeft(cls):
    for handlers in bot.event.handlers_user_left:
      await handlers()
      
  @classmethod
  async def Filter(cls):
    for handlers in bot.event.handlers_filter:
      await handlers(Message)

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
        if 'chat_join_request' in cls.out:
          keys_chat_join_request = cls.out['chat_join_request']
          # chat_join_request.chat
          chat_join_request.chat.id = keys_chat_join_request['chat'].get('id', '')
          chat_join_request.chat.title = keys_chat_join_request['chat'].get('title', '')
          chat_join_request.chat.username = f"@{keys_chat_join_request['chat'].get('username', 'no_username')}"
          chat_join_request.chat.type = keys_chat_join_request['chat'].get('type', '')
          # chat_join_request.From
          chat_join_request.From.id = keys_chat_join_request['from'].get('id', '')
          chat_join_request.From.is_bot = keys_chat_join_request['from'].get('is_bot', '')
          chat_join_request.From.first_name = keys_chat_join_request['from'].get('first_name', '')
          chat_join_request.From.last_name = keys_chat_join_request['from'].get('last_name', '')
          chat_join_request.From.username = f"@{keys_chat_join_request['from'].get('username', 'no_username')}"
          chat_join_request.From.language_code = keys_chat_join_request['from'].get('language_code', '')
          # chat_join_request.update_id
          chat_join_request.update_id = cls.out['update_id']
          # chat_join_request.user_chat_id
          chat_join_request.user_chat_id = keys_chat_join_request['user_chat_id']
          # chat_join_request.date
          chat_join_request.date = keys_chat_join_request['date']
          # Distpatch
          await Distpatch.ChatJoinRequest()
        if 'new_chat_participant' in cls.out['message']:
          CreateLog.Debug("User New")
          keys_new_chat_participant = cls.out['message']
          # new_chat_participant.message_id
          new_chat_participant.message.message_id = keys_new_chat_participant['message_id']
          # new_chat_participant.From
          new_chat_participant.message.From.id = keys_new_chat_participant['from'].get('id', '')
          new_chat_participant.message.From.is_bot = keys_new_chat_participant['from'].get('is_bot', '')
          new_chat_participant.message.From.first_name = keys_new_chat_participant['from'].get('first_name', '')
          new_chat_participant.message.From.last_name = keys_new_chat_participant['from'].get('last_name', 'no_last_name')
          new_chat_participant.message.From.username = f'@{keys_new_chat_participant['from'].get('username', 'no_username')}'
          new_chat_participant.message.From.language_code = keys_new_chat_participant['from'].get('language_code', '')
          # new_chat_participant.chat
          new_chat_participant.message.chat.id = keys_new_chat_participant['chat'].get('id', '')
          new_chat_participant.message.chat.title = keys_new_chat_participant['chat'].get('title', '')
          new_chat_participant.message.chat.username = f'@{keys_new_chat_participant['chat'].get('username', 'no_username')}'
          new_chat_participant.message.chat.type = keys_new_chat_participant['chat'].get('type', '')
          # new_chat_participant.
          new_chat_participant.id = keys_new_chat_participant['new_chat_participant'].get('id', '')
          new_chat_participant.is_bot = keys_new_chat_participant['new_chat_participant'].get('is_bot', '')
          new_chat_participant.first_name = keys_new_chat_participant['new_chat_participant'].get('first_name', '')
          new_chat_participant.last_name = keys_new_chat_participant['new_chat_participant'].get('last_name', 'no_last_name')
          new_chat_participant.username = f'@{keys_new_chat_participant['new_chat_participant'].get('username', 'no_username')}'
          new_chat_participant.language_code = keys_new_chat_participant['new_chat_participant'].get('language_code', '')
          await Distpatch.NewChatMember()
        if 'left_chat_participant' in cls.out['message']:
          keys_left_chat_participant = cls.out['message']
          # new_chat_participant.message_id
          left_chat_participant.message.message_id = keys_left_chat_participant['message_id']
          # new_chat_participant.From
          left_chat_participant.message.From.id = keys_left_chat_participant['from'].get('id', '')
          left_chat_participant.message.From.is_bot = keys_left_chat_participant['from'].get('is_bot', '')
          left_chat_participant.message.From.first_name = keys_left_chat_participant['from'].get('first_name', '')
          left_chat_participant.message.From.last_name = keys_left_chat_participant['from'].get('last_name', 'no_last_name')
          left_chat_participant.message.From.username = f'@{keys_left_chat_participant['from'].get('username', 'no_username')}'
          left_chat_participant.message.From.language_code = keys_left_chat_participant['from'].get('language_code', '')
          # new_chat_participant.chat
          left_chat_participant.message.chat.id = keys_left_chat_participant['chat'].get('id', '')
          left_chat_participant.message.chat.title = keys_left_chat_participant['chat'].get('title', '')
          left_chat_participant.message.chat.username = f'@{keys_left_chat_participant['chat'].get('username', 'no_username')}'
          left_chat_participant.message.chat.type = keys_left_chat_participant['chat'].get('type', '')
          # new_chat_participant.
          left_chat_participant.id = keys_left_chat_participant['left_chat_participant'].get('id', '')
          left_chat_participant.is_bot = keys_left_chat_participant['left_chat_participant'].get('is_bot', '')
          left_chat_participant.first_name = keys_left_chat_participant['left_chat_participant'].get('first_name', '')
          left_chat_participant.last_name = keys_left_chat_participant['left_chat_participant'].get('last_name', 'no_last_name')
          left_chat_participant.username = f'@{keys_left_chat_participant['left_chat_participant'].get('username', 'no_username')}'
          left_chat_participant.language_code = keys_left_chat_participant['left_chat_participant'].get('language_code', '')
          await Distpatch.UserChatLeft()
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
