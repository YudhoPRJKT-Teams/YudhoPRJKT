from ...connector.client import TelegramMethods
from ...bots.types import User

class get_me(TelegramMethods):
  def __init__(self):
    super().__init__('getMe', 'GET')
    self.user = User()
  async def parse_updater(self):
    if self.status_code == 200:
      updater = self.raw['result']
      self.user.id = updater.get('id', 'no-id')
      self.user.is_bot = updater.get('is_bot', 'no-is_bot')
      self.user.first_name = updater.get('first_name',  'no-first_name')
      self.user.username = f"@{updater.get('username', 'no-username')}"
      self.user.can_join_groups = updater.get('can_join_groups', 'no-can_join_groups')
      self.user.can_read_all_group_messages = updater.get('can_read_all_group_messages', 'no-can_read_all_group_messages')
      self.user.supports_inline_queries = updater.get('supports_inline_queries', 'no-supports_inline_queries')
      self.user.can_connect_to_business = updater.get('can_connect_to_business', 'no-can_connect_to_business')
      self.user.has_main_web_app = updater.get('has_main_web_app', 'no-has_main_web_app')
    return self
  def __str__(self) -> str:
    return self.serialized_json