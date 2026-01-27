from .enable_types import EnableTypes

class User(EnableTypes):
  def __init__(self):
    self._id: int
    self._is_bot: bool
    self._first_name: str
    self._last_name: str
    self._username: str
    self._language_code: str
    self._is_premium: bool
    self._added_to_attachment_menu: bool
    self._can_join_groups: bool
    self._can_read_all_group_messages: bool
    self._supports_inline_queries: bool
    self._can_connect_to_business: bool
    self._has_main_web_app: bool
    self._has_topics_enabled: bool

  # id getter
  @property
  def id(self) -> int:
    return int(self._id)
  # id setter
  @id.setter
  def id(self, _):
    self._id = _
  # is_bot getter
  @property
  def is_bot(self) -> bool:
    return bool(self._is_bot)
  # is_bot setter
  @is_bot.setter
  def is_bot(self, _):
    self._is_bot = _
  # first_name getter
  @property
  def first_name(self) -> str:
    return str(self._first_name)
  # first_name setter
  @first_name.setter
  def first_name(self, _):
    self._first_name = _
  # last_name getter
  @property
  def last_name(self) -> str:
    return str(self._last_name)
  # last_name setter
  @last_name.setter
  def last_name(self, _):
    self._last_name = _
  # username getter
  @property
  def username(self) -> str:
    return str(self._username)
  # username setter
  @username.setter
  def username(self, _):
    self._username = _
  # language_code getter
  @property
  def language_code(self) -> str:
    return str(self._language_code)
  # language_code setter
  @language_code.setter
  def language_code(self, _):
    self._language_code = _
  # is_premium getter
  @property
  def is_premium(self) -> bool:
    return bool(self._is_premium)
  # is_premium setter
  @is_premium.setter
  def is_premium(self, _):
    self._is_premium = _
  # added_to_attachment_menu getter
  @property
  def added_to_attachment_menu(self) -> bool:
    return bool(self._added_to_attachment_menu)
  # added_to_attachment_menu setter
  @added_to_attachment_menu.setter
  def added_to_attachment_menu(self, _):
    self._added_to_attachment_menu = _
  # can_join_groups getter
  @property
  def can_join_groups(self) -> bool:
    return bool(self._can_join_groups)
  # can_join_groups setter
  @can_join_groups.setter
  def can_join_groups(self, _):
    self._can_join_groups = _
  # can_read_all_group_messages getter
  @property
  def can_read_all_group_messages(self) -> bool:
    return bool(self._can_read_all_group_messages)
  # can_read_all_group_messages setter
  @can_read_all_group_messages.setter
  def can_read_all_group_messages(self, _):
    self._can_read_all_group_messages = _
  # supports_inline_queries getter
  @property
  def supports_inline_queries(self) -> bool:
    return bool(self._supports_inline_queries)
  # supports_inline_queries setter
  @supports_inline_queries.setter
  def supports_inline_queries(self, _):
    self._supports_inline_queries = _
  # can_connect_to_business getter
  @property
  def can_connect_to_business(self) -> bool:
    return bool(self._can_connect_to_business)
  # can_connect_to_business setter
  @can_connect_to_business.setter
  def can_connect_to_business(self, _):
    self._can_connect_to_business = _
  # has_main_web_app getter
  @property
  def has_main_web_app(self) -> bool:
    return bool(self._has_main_web_app)
  # has_main_web_app setter
  @has_main_web_app.setter
  def has_main_web_app(self, _):
    self._has_main_web_app = _
  # has_topics_enabled getter
  @property
  def has_topics_enabled(self) -> bool:
    return bool(self._has_topics_enabled)
  # has_topics_enabled setter
  @has_topics_enabled.setter
  def has_topics_enabled(self, _):
    self._has_topics_enabled = _