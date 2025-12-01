# Message.From
class message_from:
  id = '' # Message.From.id
  first_name = '' # Message.From.first_name
  last_name = '' # Message.From.last_name
  username = '' # Message.From.username

# Message.chat
class message_chat:
  id = '' # Message.chat.id
  title = '' # Message.chat.title
  username = '' # Message.chat.username

# Message.reply_to_message.From 
class reply_to_message_from:
  id = '' # Message.reply_to_message.From.id
  is_bot = '' # Message.reply_to_message.From.is_bot
  first_name = '' # Message.reply_to_message.From.first_name
  last_name = '' # Message.reply_to_message.From.last_name
  username = '' # Message.reply_to_message.From.username

# Message.reply_to_message.chat
class reply_to_message_chat:
  id = '' # Message.reply_to_message.chat.id
  title = '' # Message.reply_to_message.chat.title
  username = '' # Message.reply_to_message.chat.username
  type = '' # Message.reply_to_message.chat.type

# Message.photo
class reply_to_message_photo:
  file_id = ''

# Message.reply_to_message
class reply_to_message_ist:
  From = reply_to_message_from # Message.reply_to_message.From
  chat = reply_to_message_chat # Message.reply_to_message.chat
  photo = reply_to_message_photo # Message.reply_to_message.photo
  message_id = '' # Message.reply_to_message.message_id
  text = '' # Message.reply_to_message.text

class Message:
  text = '' # Message.text
  date = '' # Message.date
  message_id = '' # Message.message_id
  From = message_from # Message.From
  chat = message_chat # Message.chat
  reply_to_message = reply_to_message_ist # Message.reply_to_message