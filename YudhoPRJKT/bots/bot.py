from .methods import *
from .polling.handler import Polling
from ..utils import Log,ParseMode, Inline
from .types import Message, LinkPreviewOptions, MessageEntity, SuggestedPostParameters
from typing import Callable, Dict, Awaitable, Any
from functools import wraps

pick_command: Dict[str, Callable[[], Awaitable[Any]]] = {}

class _methods:
  def __init__(self) -> None:
    pass
  def getMe(self) -> get_me:
    """A simple method for testing your bot's authentication token

    Returns:
        str: basic information about the bot in form of a [User](https://core.telegram.org/bots/api#user) object.
    """
    return get_me()
  def logOut(self) -> log_out:
    """Use this method to log out from the cloud Bot API server before launching the bot locally. You must log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns True on success. Requires no parameters."""
    return log_out()
  def close(self) -> Close:
    """Use this method to close the bot instance before moving it from one local server to another. You need to delete the webhook before calling this method to ensure that the bot isn't launched again after server restart. The method will return error 429 in the first 10 minutes after the bot is launched. Returns True on success. Requires no parameters."""
    return Close()
  def getUpdates(self,
    offset: int | None = None,
    limit: int = 100,
    timeout: int = 0,
    allowed_updates: str | None = None
  ) -> get_updates:
    """Use this method to receive incoming updates using long polling ([wiki](https://en.wikipedia.org/wiki/Push_technology#Long_polling)). 

    Args:
        offset (int | None, optional): _description_. Defaults to None.
        limit (int, optional): _description_. Defaults to 100.
        timeout (int, optional): _description_. Defaults to 0.
        allowed_updates (str | None, optional): _description_. Defaults to None.

    Returns:
        get_updates: Returns an Array of Update objects.
    """
    return get_updates(offset, limit, timeout, allowed_updates)
  def sendMessage(self,
    chat_id:  int | str,
    text: str,
    parse_mode: ParseMode,
    # Optional
    business_connection_id: str | None = None,
    message_thread_id: int | None =None,
    direct_messages_topic_id: int | None = None,
    entities: MessageEntity | None = None,
    link_preview_options: LinkPreviewOptions | None =None,
    disable_notification: bool | None = False,
    protect_content: bool | None = False,
    allow_paid_broadcast: bool | None = True,
    message_effect_id: str | None = None,
    suggested_post_parameters: SuggestedPostParameters | None = None
  ):
    """Use this method to send text messages

    Args:
        chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        text (str): Text of the message to be sent, 1-4096 characters after entities parsing
        parse_mode (ParseMode): Mode for parsing entities in the message text
        business_connection_id (str | None, optional): Unique identifier of the business connection on behalf of which the message will be sent. Defaults to None.
        message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only. Defaults to None.
        direct_messages_topic_id (int | None, optional): Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat. Defaults to None.
        entities (MessageEntity | None, optional): A JSON-serialized list of special entities that appear in message text, which can be specified instead of parse_mode. Defaults to None.
        link_preview_options (LinkPreviewOptions | None, optional): Link preview generation options for the message. Defaults to None.
        disable_notification (bool | None, optional): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.. Defaults to False.
        protect_content (bool | None, optional): Protects the contents of the sent message from forwarding and saving. Defaults to False.
        allow_paid_broadcast (bool | None, optional): Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance. Defaults to True.
        message_effect_id (str | None, optional): Unique identifier of the message effect to be added to the message; for private chats only. Defaults to None.
        suggested_post_parameters (SuggestedPostParameters | None, optional): A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined. Defaults to None.

    Returns:
        Message: On success, the sent Message is returned.
    """
    return send_message(chat_id, text, parse_mode, business_connection_id, message_thread_id, direct_messages_topic_id, entities, link_preview_options, disable_notification, protect_content, allow_paid_broadcast, message_effect_id, suggested_post_parameters)

class Bot:
  def __init__(self) -> None:
    self.methods = _methods()
  def command(self, command: str) -> Callable[[Callable[[], Awaitable[Any]]], Callable[[], Awaitable[Any]]]:
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
  async def run(self):
    """Run bot"""
    Log.Info('Bots is Running!').Show().Save()
    await Polling().run()