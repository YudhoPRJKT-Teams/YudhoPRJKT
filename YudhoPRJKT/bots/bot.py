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
  def forwardMessage(self,
    chat_id: int | str,
    from_chat_id: int | str,
    message_id: int,
    # Optional
    message_thread_id: int | None = None,
    direct_messages_topic_id: int | None = None,
    video_start_timestamp: int | None = None,
    disable_notification: bool = False,
    protect_content: bool = False,
    message_effect_id: str | None = None,
    suggested_post_parameters: SuggestedPostParameters | None = None,
  ):
    """Use this method to forward messages of any kind. Service messages and messages with protected content can't be forwarded.

    Args:
        chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        from_chat_id (int | str): Unique identifier for the chat where the original message was sent (or channel username in the format `@channelusername`)
        message_id (int): Message identifier in the chat specified in from_chat_id
        message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only. Defaults to None.
        direct_messages_topic_id (int | None, optional): Identifier of the direct messages topic to which the message will be forwarded; required if the message is forwarded to a direct messages chat. Defaults to None.
        video_start_timestamp (int | None, optional): New start timestamp for the forwarded video in the message. Defaults to None.
        disable_notification (bool, optional): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.. Defaults to False.
        protect_content (bool, optional): Protects the contents of the forwarded message from forwarding and saving. Defaults to False.
        message_effect_id (str | None, optional): Unique identifier of the message effect to be added to the message only available when forwarding to private chats. Defaults to None.
        suggested_post_parameters (SuggestedPostParameters): A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats onlyDefaults to None.
    Returns:
        Message: On success, the sent [Message](https://core.telegram.org/bots/api#message) is returned.
    """
    return forward_message(chat_id, from_chat_id, message_id, message_thread_id, direct_messages_topic_id, video_start_timestamp, disable_notification, protect_content, message_effect_id, suggested_post_parameters)
  def forwardMessages(self,
    chat_id: int | str,
    from_chat_id: int | str,
    message_ids: list,
    disable_notification: bool = False,
    protect_content: bool = False,
    # Optional
    message_thread_id: int | None = None,
    direct_messages_topic_id: int | None = None
  ):
    """Use this method to forward multiple messages of any kind. If some of the specified messages can't be found or forwarded, they are skipped. Service messages and messages with protected content can't be forwarded. Album grouping is kept for forwarded messages.

    Args:
        chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        from_chat_id (int | str): Unique identifier for the chat where the original messages were sent (or channel username in the format `@channelusername`)
        message_ids (list): A JSON-serialized list of 1-100 identifiers of messages in the chat from_chat_id to forward. The identifiers must be specified in a strictly increasing order.
        disable_notification (bool, optional): Sends the messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.. Defaults to False.
        protect_content (bool, optional): Protects the contents of the forwarded messages from forwarding and saving. Defaults to False.
        message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only. Defaults to None.
        direct_messages_topic_id (int | None, optional): Identifier of the direct messages topic to which the messages will be forwarded; required if the messages are forwarded to a direct messages chat. Defaults to None.

    Returns:
        MessageId: On success, an array of MessageId of the sent messages is returned.
    """
    return forward_messages(chat_id, from_chat_id, message_ids, disable_notification, protect_content, message_thread_id, direct_messages_topic_id)
  def copyMessage(self,
    chat_id: int | str,
    from_chat_id: int | str,
    message_id: int,
    show_caption_above_media: bool = True,
    disable_notification: bool = False,
    protect_content: bool = False,
    allow_paid_broadcast: bool = True,
    # Optional
    message_thread_id: int | None = None,
    direct_messages_topic_id: int | None = None,
    video_start_timestamp: int | None = None,
    caption: str | None = None,
    parse_mode: ParseMode | None = None,
    caption_entities: MessageEntity | None = None,
    message_effect_id: str | None = None,
    suggested_post_parameters: SuggestedPostParameters | None = None,
  ):
    """Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz [poll](https://core.telegram.org/bots/api#poll) can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method [forwardMessages](https://core.telegram.org/bots/api#forwardmessages), but the copied messages don't have a link to the original message. Album grouping is kept for copied messages. 

    Args:
        chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        from_chat_id (int | str): Unique identifier for the chat where the original messages were sent (or channel username in the format `@channelusername`)
        message_id (int): A JSON-serialized list of 1-100 identifiers of messages in the chat from_chat_id to copy. The identifiers must be specified in a strictly increasing order.
        show_caption_above_media (bool, optional): Pass True, if the caption must be shown above the message media. Ignored if a new caption isn't specified.. Defaults to True.
        disable_notification (bool, optional): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. Defaults to False.
        protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving. Defaults to False.
        allow_paid_broadcast (bool, optional): Pass True to allow up to 1000 messages per second, ignoring [broadcasting limits](https://core.telegram.org/bots/faq#how-can-i-message-all-of-my-bot-39s-subscribers-at-once) for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance. Defaults to True.
        message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only. Defaults to None.
        direct_messages_topic_id (int | None, optional): Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat. Defaults to None.
        video_start_timestamp (int | None, optional): New start timestamp for the copied video in the message. Defaults to None.
        caption (str | None, optional): New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept. Defaults to None.
        parse_mode (ParseMode | None, optional): Mode for parsing entities in the new caption. . Defaults to None.
        caption_entities (MessageEntity | None, optional): A JSON-serialized list of special entities that appear in the new caption, which can be specified instead of parse_mode. Defaults to None.
        message_effect_id (str | None, optional): Unique identifier of the message effect to be added to the message; only available when copying to private chats. Defaults to None.
        suggested_post_parameters (SuggestedPostParameters | None, optional): A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.. Defaults to None.

    Returns:
        MessageId: On success, an array of MessageId of the sent messages is returned.
    """
    return copy_message(chat_id, from_chat_id, message_id, show_caption_above_media, disable_notification, protect_content, allow_paid_broadcast, message_thread_id, direct_messages_topic_id, video_start_timestamp, caption, parse_mode, caption_entities, message_effect_id, suggested_post_parameters)
  def copyMessages(self,
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
    """Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz [poll](https://core.telegram.org/bots/api#poll) can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method [forwardMessages](https://core.telegram.org/bots/api#forwardmessages), but the copied messages don't have a link to the original message. Album grouping is kept for copied messages

    Args:
        chat_id (int | str): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        from_chat_id (int | str): Unique identifier for the chat where the original messages were sent (or channel username in the format `@channelusername`)
        message_ids (list): A JSON-serialized list of 1-100 identifiers of messages in the chat from_chat_id to copy. The identifiers must be specified in a strictly increasing order.
        disable_notification (bool, optional): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. Defaults to False.
        protect_content (bool, optional): Protects the contents of the sent message from forwarding and saving. Defaults to False.        protect_content (bool, optional): _description_. Defaults to False.
        remove_caption (bool, optional): Pass True to copy the messages without their captions. Defaults to False.
        message_thread_id (int | None, optional): Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only. Defaults to None.
        direct_messages_topic_id (int | None, optional): Identifier of the direct messages topic to which the messages will be sent; required if the messages are sent to a direct messages chat. Defaults to None.

    Returns:
        MessageId: On success, an array of [MessageId](https://core.telegram.org/bots/api#messageid) of the sent messages is returned.
    """
    return copy_messages(chat_id, from_chat_id, message_ids, disable_notification, protect_content, remove_caption, message_thread_id, direct_messages_topic_id)
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