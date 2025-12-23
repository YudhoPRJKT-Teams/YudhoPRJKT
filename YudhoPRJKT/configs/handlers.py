from dotenv import load_dotenv
import os

class Config:
  def __init__(self) -> None:
    self.envfile = f'{os.getcwd()}/.env'
    # Telegram bot credetials
    self._api = None
    if not os.path.exists(self.envfile):
      token = str(input('Input your telegram bot api: '))
      self._token = token
      with open(self.envfile, 'w') as w:
        w.write(f"token='{token}'")
        if self._api == '':
          self._api = f'https://api.telegram.org/bot{token}'
        else:
          pass
        load_dotenv(self.envfile)
    else:
      load_dotenv(self.envfile)
      self._token = os.environ.get('token')
      self._api = os.environ.get('api')
  def UseCustomApi(self, custom_api):
    """Custom Api Wrapper

    Args:
        custom_api (str): Your Custom API
    """
    self._api = f'{custom_api}/bot{self._token}'
    with open(self.envfile, 'w') as w:
      w.write(f"token='{self._token}'\napi='{self._api}'")
    return self
  
  @property
  def token(self):
    return self._token
  @token.setter
  def token(self, token):
    self._token = token
  
  @property
  def api(self):
    return self._api
  @api.setter
  def api(self, api):
    self._api = api