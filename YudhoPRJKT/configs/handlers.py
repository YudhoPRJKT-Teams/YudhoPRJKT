from dotenv import load_dotenv
import os


class Config:
  def __init__(self) -> None:
    self.envfile = f'{os.getcwd()}/.env'
    load_dotenv(self.envfile)

    # Telegram bot properties
    self._token = os.environ.get('token')
    self._api = f'https://api.telegram.org/bot{self._token}'
    if not self._token:
      self._token = str(input('Input your telegram bot token: '))
    if not os.path.exists(self.envfile):
      with open(self.envfile, 'w') as w:
        if open(self.envfile, 'r').read() == '':
          w.write(f"token='{self._token}'\napi='{self._api}'\n")
    if self._token != '' and self._api  != '':
      self._token = os.environ.get('token', self._token)
      self._api = os.environ.get('api', self._api)
  
  def UseCustomApi(self, custom_api: str):
    self.api = f'{custom_api}/bot{self._token}'
    return self
  
  # Api
  @property
  def api(self):
    return self._api
  
  @api.setter
  def api(self, api):
    self._api = api
  
  # Token
  @property
  def token(self):
    return self._token
  
  @token.setter
  def token(self, token):
    self._token = token