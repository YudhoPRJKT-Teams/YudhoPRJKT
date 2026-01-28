import aiohttp
import json
from .exceptions import ClientExceptions
from ..auth.credentials import Auth
import socket
import asyncio
from typing import AsyncGenerator, Any, Union, Self

class BaseConnector:
  """BaseConnector"""
  def __init__(self,
    url,
    methods,
    *,
    params=None,
    data=None,
    json_data=None,
    headers=None,
    raw_cache=None
  ):
    self.url = url
    self.methods = methods
    self.params = params
    self.data = data
    self.json_data = json_data
    self.headers = headers
    self.raw_cache: dict[str, Any] = {}
  def _prepare_data(self):
    if self.data is None:
      return None
    
    if isinstance(self.data, dict):
      form = aiohttp.FormData()
      for key, value in self.data.items():
        if isinstance(value, (bytes, bytearray)):
          form.add_field(name=key, value=value, filename=key, content_type="application/octet-stream")
        elif isinstance(value, (dict, list)):
          form.add_field(name=key, value=json.dumps(value))
        else:
          form.add_field(name=key, value=str(value))
      return form
    return self.data
  
  async def __aenter__(self) -> Self:
    try:
      resolv = aiohttp.ThreadedResolver()
      self._session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False, use_dns_cache=True, family=socket.AF_INET, resolver=resolv))
      payload = self._prepare_data()
      self._res = await self._session.request(
        method=self.methods,
        url=self.url,
        params=self.params,
        data=payload,
        json=self.json_data,
        headers=self.headers
      )
      self.raw_cache = await self._res.json()
    except (aiohttp.ClientConnectionError, asyncio.CancelledError):
      if not self._session.closed:
        await self._session.close()
      raise
    except Exception as e:
      if not self._session.closed:
        if hasattr(self, "_res"):
          await self._res.release()
        if not self._session.closed:
          await self._session.close()
        raise ClientExceptions.ConnectionError('Got Error!', f'{e}', 400)
    return self
  async def __aexit__(self, exc_type, exc, tb):
    if self._res:
      await self._res.release()
    if self._session:
      await self._session.close()
  @property
  def status_code(self):
    return self._res.status
  @property
  def raw(self):
    return self.raw_cache
  @property
  def serialized_json(self):
    return json.dumps(self.raw_cache, indent=2)
  async def text(self):
    return await self._res.text()
  def read(self):
    return self._res.read()
  async def close(self):
    self._res.close()
  @classmethod
  def get(cls, url: str, **kwargs):
    """Methods get 

    Args:
        url (str): your target links
    """
    return cls(url, "GET", **kwargs)
  @classmethod
  def post(cls, url: str, **kwargs):
    """Methods post 

    Args:
        url (str): your target links
    """
    return cls(url, "POST", **kwargs)

class TelegramMethods(BaseConnector):
  def __init__(self, bot_methods: str, request_type: str = 'GET', data: dict | None = None, json: dict | None = None, params: dict | None = None):
    """Telegram methods connector utils

    Args:
        bot_methods (str): Telegram bot methods
        request_type (str, optional): Request connection type. Defaults to 'GET'.
        data (dict | None, optional): Request Data Headers
        json (dict | None, optional): Request Json Headers
        params (dict | None, optional): Request Params Headers
    """
    super().__init__(url=Auth().methods(bot_methods), methods=request_type, data=data, json_data=json, params=params)
  async def _exc(self):
    async with self as cl:
      await self.parse_updater()
      return self
  def __await__(self):
    return self._exc().__await__()
  def __str__(self) -> str:
    if hasattr(self, "raw_cache"):
      return json.dumps(self.raw_cache, indent=2)
    return "{}"
  async def parse_updater(self) -> Any:
    return self
  @property
  def serialized_json(self):
    if hasattr(self, 'raw_cache') and self.raw_cache is not None:
      return super().serialized_json
    return "{}"
  @property
  def raw(self):
    return getattr(self, 'raw_cache', {})