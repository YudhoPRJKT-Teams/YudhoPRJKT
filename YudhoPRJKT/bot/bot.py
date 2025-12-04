from typing import Callable, Awaitable, Any, Optional, Union, Dict
from functools import wraps
# Methods
from .Methods import (
  get_me,
  log_out,
  close,
  send_message,
  forward_message,
  edit_message_text,
  copy_message,
  send_photo,
  send_audio,
  send_document,
  send_video
)
# Updates
from .Updates import (
  get_updates
)
# types.message
from .types.message import Message
# Utils
from ..utils import ParseMode, Inline
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
  async def sendMessage(cls,chat_id: Union[str,int], text: Any, parse_mode: str, disable_notification: bool = False, protect_content: bool = False, reply_markup: Optional[str] = None, reply_chat: Optional[Union[str, bool]] = False):
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
  @classmethod
  async def forwardMessage(cls, chat_id: Union[str, int], from_chat_id: Union[str, int] = Message.chat.id, disable_notification: Optional[bool] = False, protect_content: Optional[bool] = False, *, message_id: Union[str,int]):
    """Use this method to forward messages of any kind. Service messages and messages with protected content can't be forwarded. On success, the sent [Message](https://core.telegram.org/bots/api#message) is returned.

    Args:
        chat_id (Union[str, int]): Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        from_chat_id (Union[str, int], optional): Unique identifier for the chat where the original message was sent (or channel username in the format @channelusername). Defaults to Message.chat.id.
        disable_notification (Optional[bool], optional): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. Defaults to False.
        protect_content (Optional[bool], optional): Protects the contents of the forwarded message from forwarding and saving. Defaults to False.
        message_id (Union[str,int]): Message identifier in the chat specified in from_chat_id
    """
    return await forward_message(chat_id, from_chat_id, disable_notification, protect_content, message_id)
  @classmethod
  async def editMessageText(cls, chat_id: Union[str, int], message_id: Union[str, int], text: Any, parse_mode: str, reply_markup: Optional[str] = None):
    """Use this method to edit text and [game](https://core.telegram.org/bots/api#games) messages. On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api#message) is returned, otherwise True is returned. Note that business messages that were not sent by the bot and do not contain an inline keyboard can only be edited within 48 hours from the time they were sent.

    Args:
        chat_id (Union[str, int]): Required if inline_message_id is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        message_id (Union[str, int]): Required if inline_message_id is not specified. Identifier of the message to edit
        text (Any): New text of the message, 1-4096 characters after entities parsing
        parse_mode (str): Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details.
        reply_markup (Optional[str]): A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards). Default is None
      """
    return await edit_message_text(chat_id, message_id, text, parse_mode, reply_markup)
  @classmethod
  async def copyMessage(cls, chat_id: Union[str, int], from_chat_id: Union[str, int], message_id: Union[str, int], caption: Any, parse_mode: str, disable_notification: Optional[bool] = False, protect_content: Optional[bool] = False, reply_chat: Optional[Union[bool, str]] = False, reply_markup: Optional[str] = None):
    """Use this method to copy messages of any kind. If some of the specified messages can't be found or copied, they are skipped. Service messages, paid media messages, giveaway messages, giveaway winners messages, and invoice messages can't be copied. A quiz [poll](https://core.telegram.org/bots/api#poll) can be copied only if the value of the field correct_option_id is known to the bot. The method is analogous to the method [forwardMessages](https://core.telegram.org/bots/api#forwardmessages), but the copied messages don't have a link to the original message. Album grouping is kept for copied messages. On success, an array of [MessageId](https://core.telegram.org/bots/api#messageid) of the sent messages is returned.

    Args:
        chat_id (Union[str, int]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        from_chat_id (Union[str, int]): Unique identifier for the chat where the original messages were sent (or channel username in the format `@channelusername`)
        message_id (Union[str, int]): Message identifier in the chat specified in from_chat_id
        caption (Any): New caption for media, 0-1024 characters after entities parsing. If not specified, the original caption is kept
        parse_mode (str): Mode for parsing entities in the new caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details.
        disable_notification (Optional[bool], optional): Sends the message [silently](Sends the message silently. Users will receive a notification with no sound.). Users will receive a notification with no sound.. Defaults to False.
        protect_content (Optional[bool], optional): Protects the contents of the sent message from forwarding and saving. Defaults to False.
        reply_chat (Optional[Union[bool, str]], optional): Description of the message to reply to. Defaults to False.
        reply_markup (Optional[str], optional): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user. Defaults to None.
    """
    return await copy_message(chat_id, from_chat_id, message_id, caption, parse_mode, disable_notification, protect_content, reply_chat, reply_markup)
  @classmethod
  async def sendPhoto(cls, chat_id: Union[str, int], photo: str, caption: str, parse_mode: str, show_caption_above_media: Optional[bool] = False, has_spoiler: Optional[bool] = False, disable_notification: Optional[bool] = False, protect_content: Optional[bool] = False, reply_chat: Optional[Union[bool, str]] = True, reply_markup: Optional[str] = None):
    """Use this method to send photos. On success, the sent [Message](https://core.telegram.org/bots/api#message) is returned.

    Args:
        chat_id (Union[str, int]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        photo (str): Photo to send. Pass a file_id as String to send a photo that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a photo from the Internet, or upload a new photo using multipart/form-data. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20
        caption (str): Photo caption (may also be used when resending photos by file_id), 0-1024 characters after entities parsing
        parse_mode (str): Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details.
        show_caption_above_media (Optional[bool], optional): Pass True, if the caption must be shown above the message media. Defaults to False.
        has_spoiler (Optional[bool], optional): Pass True if the photo needs to be covered with a spoiler animation. Defaults to False.
        disable_notification (Optional[bool], optional): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. Defaults to False.
        protect_content (Optional[bool], optional): Protects the contents of the sent message from forwarding and saving. Defaults to False.
        reply_chat (Optional[Union[bool, str]], optional): Description of the message to reply to. Defaults to True.
        reply_markup (Optional[Inline], optional): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user. Defaults to None.
    """
    return await send_photo(chat_id, photo, caption, parse_mode, show_caption_above_media, has_spoiler, disable_notification, protect_content, reply_chat, reply_markup)
  @classmethod
  async def sendAudio(cls, chat_id: Union[str, int], audio: str, caption: str, parse_mode: str, duration: Optional[int] = None, performer: Optional[str] = None, title: Optional[str] = None, disable_notification: Optional[bool] = False, protect_content: Optional[bool] = False,  reply_chat: Optional[Union[bool, str]] = True, reply_markup: Optional[str] = None):
    """Use this method to send audio files, if you want Telegram clients to display them in the music player. Your audio must be in the .MP3 or .M4A format. On success, the sent [Message](https://core.telegram.org/bots/api#message) is returned. Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.

    For sending voice messages, use the [sendVoice](https://core.telegram.org/bots/api#sendvoice) method instead.

    Args:
        chat_id (Union[str, int]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        audio (str): 	Audio file to send. Pass a file_id as String to send an audio file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get an audio file from the Internet
        caption (str): Audio caption, 0-1024 characters after entities parsing
        parse_mode (str): Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details.
        duration (Optional[int], optional): Duration of the audio in seconds. Defaults to None.
        performer (Optional[str], optional): Performer. Defaults to None.
        title (Optional[str], optional): Track name. Defaults to None.
        disable_notification (Optional[bool], optional): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. Defaults to False.
        protect_content (Optional[bool], optional): _description_. Defaults to False.
        reply_chat (Optional[Union[bool, str]], optional): Description of the message to reply to. Defaults to True.
        reply_markup (Optional[Inline], optional): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user. Defaults to None.
    """
    return await send_audio(chat_id, audio, caption, parse_mode, duration, performer, title, disable_notification, protect_content, reply_chat, reply_markup)
  @classmethod
  async def sendDocument(cls, chat_id: Union[str, int], document: str, caption: str, parse_mode: str, disable_notification: Optional[bool] = False, protect_content: Optional[bool] = False, reply_chat: Optional[Union[bool, str]] = True, reply_markup: Optional[str] = None):
    """Use this method to send general files. On success, the sent [Message](https://core.telegram.org/bots/api#message) is returned. Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

    Args:
        chat_id (Union[str, int]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        document (str): 	File to send. Pass a file_id as String to send a file that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a file from the Internet, 
        caption (str): Audio caption, 0-1024 characters after entities parsing
        parse_mode (str): Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details.
        disable_notification (Optional[bool], optional): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. Defaults to False.
        protect_content (Optional[bool], optional): Protects the contents of the sent message from forwarding and saving. Defaults to False.
        reply_chat (Optional[Union[bool, str]], optional): Description of the message to reply to. Defaults to True.
        reply_markup (Optional[Inline], optional): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user. Defaults to None.
    """
    return await send_document(chat_id, document, caption, parse_mode, disable_notification, protect_content, reply_chat, reply_markup)
  @classmethod
  async def sendVideo(cls, chat_id: Union[str, int], video: str, caption: str, parse_mode: str, show_caption_above_media: Optional[bool] = False, has_spoiler: Optional[bool] = False, support_streaming: Optional[bool] = True, disable_notification: Optional[bool] = False, protect_content: Optional[bool] = False, reply_chat: Optional[Union[bool, str]] = True, reply_markup: Optional[str] = None):
    """Use this method to send video files, Telegram clients support MPEG4 videos (other formats may be sent as [Document](https://core.telegram.org/bots/api#document)). On success, the sent [Message](https://core.telegram.org/bots/api#message) is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

    Args:
        chat_id (Union[str, int]): Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
        video (str): 	Yes	Video to send. Pass a file_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet,
        caption (str): Audio caption, 0-1024 characters after entities parsing
        parse_mode (str): Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api#formatting-options) for more details.
        show_caption_above_media (Optional[bool], optional): Pass True, if the caption must be shown above the message media. Defaults to False.
        has_spoiler (Optional[bool], optional): Pass True if the photo needs to be covered with a spoiler animation. Defaults to False.
        support_streaming (Optional[bool], optional): Pass True if the uploaded video is suitable for streaming. Defaults to True.
        disable_notification (Optional[bool], optional): Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound. Defaults to False.
        protect_content (Optional[bool], optional): Protects the contents of the sent message from forwarding and saving. Defaults to False.
        reply_chat (Optional[Union[bool, str]], optional): Description of the message to reply to. Defaults to True.
        reply_markup (Optional[Inline], optional): Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots/features#inline-keyboards), [custom reply keyboard](https://core.telegram.org/bots/features#keyboards), instructions to remove a reply keyboard or to force a reply from the user. Defaults to None.
    """
    return await send_video(chat_id, video, caption, parse_mode, show_caption_above_media, has_spoiler, support_streaming, disable_notification, protect_content, reply_chat, reply_markup)
class _update:
  @classmethod
  async def getUpdates(cls, offset: Optional[int] = None):
    """Use this method to receive incoming updates using long polling (wiki). Returns an Array of Update objects.

    Args:
        offset (int): Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will be forgotten.
    """
    return await get_updates(offset)
  
# class Event
class Event:
  handlers_user_join = []
  handlers_joined_user = []
  handlers_user_left = []
  handlers_filter = []
  
  # User Request Join
  @classmethod
  def UserRequest(cls):
    def decorator(func):
      cls.handlers_user_join.append(func)
      return func
    return decorator
  
  # New User Joined
  @classmethod
  def NewUser(cls):
    def decorator(func):
      cls.handlers_joined_user.append(func)
      return func
    return decorator
  
  # User Left
  @classmethod
  def UserLeft(cls):
    def decorator(func):
      cls.handlers_user_left.append(func)
      return func
    return decorator


class bot:
  methods = _methods
  updates = _update
  event = Event
  
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