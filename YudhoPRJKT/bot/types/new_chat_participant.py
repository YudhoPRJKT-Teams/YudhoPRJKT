# new_chat_participant.message.chat
class message_chat:
  id = '' # new_chat_participant.message.chatid
  title = '' # new_chat_participant.message.chat.title
  username = '' # new_chat_participant.message.chat.username
  type = '' # new_chat_participant.message.chat.type
# new_chat_participant.message.From
class message_from:
  id = '' # new_chat_participant.From.id
  is_bot = '' # new_chat_participant.From.is_bot
  first_name = '' # new_chat_participant.From.first_name
  last_name = '' # new_chat_participant.From.last_name
  username = '' # new_chat_participant.From.username
  language_code = '' # new_chat_participant.From.language_code
  
# new_chat_participant.message
class message_ist:
  message_id = '' # new_chat_participant.message.message_id
  chat = message_chat # new_chat_participant.message.chat
  From = message_from # new_chat_participant.message.From
  
class new_chat_participant:
  message = message_ist # new_chat_participant.message
  id = '' # new_chat_participant.id
  is_bot = '' # new_chat_participant.is_bot
  first_name = '' # new_chat_participant.first_name
  last_name = '' # new_chat_participant.last_name
  username = '' # new_chat_participant.username
  language_code = '' # new_chat_participant.language_code