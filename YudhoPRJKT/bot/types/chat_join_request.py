# chat_join_request.chat
class chat_join_request_chat:
  id = '' # chat_join_request.chat.id
  title = '' # chat_join_request.chat.title
  username = '' # chat_join_request.chat.username
  type = '' # chat_join_request.chat.type

# chat_join_request.From
class chat_join_request_from:
  id = '' # chat_join_request.From.id
  is_bot = '' # chat_join_request.From.is_bot
  first_name = '' # chat_join_request.From.first_name
  last_name = '' # chat_join_request.From.last_name
  username = '' # chat_join_request.From.username
  language_code = '' # chat_join_request.From.language_code


# chat_join_request
class chat_join_request:
  chat = chat_join_request_chat # chat_join_request.chat
  From = chat_join_request_from # chat_join_request.From
  update_id = '' # chat_join_request.update_id
  user_chat_id = '' # chat_join_request.user_chat_id
  date = '' # chat_join_request.date
  