from .methods import get_me

# Methods class
class _methods:
  @classmethod
  async def getMe(cls):
    """A simple method for testing your bot's authentication token. Requires no parameters. Returns .
    
    Returns:
        User: basic information about the bot in form of a User object
    """
    return await get_me()


class bot:
  methods = _methods()