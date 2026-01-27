import os
from dotenv import load_dotenv, set_key
from ..utils import Log


class Auth:
  def __init__(self) -> None:
    self.envfile = os.path.join(os.getcwd(), '.env')
    load_dotenv(self.envfile)
    self._token = os.getenv('token')
    self._api = os.getenv('api')
    self._gemini_key = os.getenv('gemini_key')
    self._github_pat = os.getenv('github_pat')
    if not self._token:
      Log.Debug('Unable to find env files, creating....').Show().Save()
      self._token = str(input('Input your telegram bot token: '))
      self._api = f'https://api.telegram.org/bot{self._token}'
      with open(self.envfile, 'w') as w:
        w.writelines([
          f'token="{self._token}"\n',
          f'api="{self._api}"\n'
        ])
    else:
      if not self._api:
        self._api = f'https://api.telegram.org/bot{self._token}'

  def UseCustomApi(self, api_url: str):
    """Use Your own api telegram"""
    if not self._token:
      Log.Debug('Token missing. Please initialize first.').Show().Save()
      return
    self._api = f"{api_url.rstrip('/')}/bot{self._token}"
    with open(self.envfile, 'w') as w:
      w.writelines([
        f'token="{self._token}"\n',
        f'api="{self._api}"\n'
      ])
  def AddCredentials(self, keys: str, value: str):
    with open(self.envfile, 'a') as w:
      w.writelines([f'{keys}="{value}"'])
      Log.Info(f'{keys} Added to credentials!').Show().Save()
  @property
  def token(self):
    return self._token
  @property
  def api(self):
    return self._api
  @property
  def gemini_key(self):
    return self._gemini_key
  @property
  def github_pat(self):
    return self._github_pat
  def methods(self, methods_telegram):
    return f'{self._api}/{methods_telegram}'