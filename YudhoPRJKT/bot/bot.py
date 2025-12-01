from typing import Callable, Awaitable, Any, Optional, Union, Dict
from functools import wraps
# Methods
from .Methods.get_me import get_me
from .Methods.log_out import log_out
from .Methods.close import close
from .Methods.send_message import send_message
# Updates
from .Updates.get_updates import get_updates
# types.message
from .types.message import Message

# Pick command
pick_command: Dict[str, Callable[[], Awaitable[Any]]] = {}

class _methods:
  @classmethod
  async def getMe(cls):
    """A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a [User](https://core.telegram.org/bots/api#user) object."""
    return await get_me()
  @classmethod
  async def logOut(cls):
    """Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters."""
    return await log_out()
  @classmethod
  async def close(cls):
    """Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters."""
    return await close()
  @classmethod
  async def sendMessage(cls,chat_id: Union[str,int], text: Any, parse_mode: str, disable_notification: bool = False, protect_content: bool = False, reply_markup: Optional[str] = None, reply_chat: Optional[Union[str, bool]] = Message.message_id):
    """Use this method to send text messages. On success, the sent [Message](https://core.telegram.org/bots/api#message) is returned.

    Args:
        chat_id (Union[str,int]): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        text (Any): Text of the message to be sent, 1-4096 characters after entities parsing
        parse_mode (str): Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details.
        disable_notification (bool, optional): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. Defaults to False.
        protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving. Defaults to False.
        reply_markup (Optional[str], optional): Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove a reply keyboard or to force a reply from the user. Defaults to None.
        reply_chat (Optional[Union[str, bool]], optional): Description of the message to reply to. Defaults to Message.message_id.
    """
    return await send_message(chat_id, text, parse_mode, disable_notification, protect_content, reply_markup, reply_chat)
  
class _update:
  @classmethod
  async def getUpdates(cls, offset: Optional[int] = None):
    """Use this method to receive incoming updates using long polling (wiki). Returns an Array of Update objects.

    Args:
        offset (int): Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will be forgotten.
    """
    return await get_updates(offset)

class bot:
  methods = _methods
  updates = _update  
  
  @classmethod
  def command(cls, command: str) -> Callable[[Callable[[], Awaitable[Any]]], Callable[[], Awaitable[Any]]]:
    """Use this decorator to register a command in the bot.

    Args:
        command (str): Your command name. Example: /start, /help, etc.
    """
    def decorator(func: Callable[[], Awaitable[Any]]) -> Callable[[], Awaitable[Any]]:
        @wraps(func)
        async def wrapper() -> Any:
            return await func()
        pick_command[command] = wrapper
        return wrapper
    return decorator