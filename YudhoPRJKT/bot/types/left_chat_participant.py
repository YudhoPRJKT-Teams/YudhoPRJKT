# left_chat_participant.message.chat
class message_chat:
  id = '' # left_chat_participant.message.chatid
  title = '' # left_chat_participant.message.chat.title
  username = '' # left_chat_participant.message.chat.username
  type = '' # left_chat_participant.message.chat.type

class message_from:
  id = '' # left_chat_participant.From.id
  is_bot = '' # left_chat_participant.From.is_bot
  first_name = '' # left_chat_participant.From.first_name
  last_name = '' # left_chat_participant.From.last_name
  username = '' # left_chat_participant.From.username
  language_code = '' # left_chat_participant.From.language_code
  
# left_chat_participant.message
class message_ist:
  message_id = '' # left_chat_participant.message.message_id
  chat = message_chat # left_chat_participant.message.chat
  From = message_from # left_chat_participant.message.From

class left_chat_participant:
  message = message_ist # left_chat_participant.message
  id = '' # left_chat_participant.id
  is_bot = '' # left_chat_participant.is_bot
  first_name = '' # left_chat_participant.first_name
  last_name = '' # left_chat_participant.last_name
  username = '' # left_chat_participant.username
  language_code = '' # left_chat_participant.language_code