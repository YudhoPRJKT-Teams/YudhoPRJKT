import aiohttp
import httpx
import json
from .exceptions import ConnectionError

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
  ):
    self.url = url
    self.methods = methods
    self.params = params
    self.data = data
    self.json_data = json_data
    self.headers = headers
    
  def _prepare_data(self):
    if self.data is None:
      return None
    
    if isinstance(self.data, dict):
      form = aiohttp.FormData()
      for keys, value in self.data.items():
        if isinstance(value, (bytes, bytearray)):
          form.add_field(name=keys, value=value, filename=keys, content_type="application/octet-stream")
        else:
          form.add_field(name=keys, value=str(value))
      return form
    return self.data
  
  async def __aenter__(self):
    try:
      self._session = aiohttp.ClientSession()
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
      return self
    except aiohttp.ClientConnectionError as e:
      await self._session.close()
      raise ConnectionError(f'Got Error!', str(e), 400)
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
  def serilized_json(self):
    return json.dumps(self.raw_cache, indent=2)
  async def text(self):
    return await self._res.text()
  
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
  

class ConnectorSync:
  def __init__(self, url, methods, *, params=None, data=None, json_data=None, headers=None):
    self.url = url
    self.methods = methods
    self.params = params
    self.data = data
    self.json_data = json_data
    self.headers = headers
    self._client = None
    self._res = None
    self._raw_cache = None
    
    
  def __enter__(self):
    try:
      self._cl = httpx.Client()
      self._res = self._cl.request(
        method=self.methods,
        url=self.url,
        params=self.params,
        data=self.data,
        json=self.json_data,
        headers=self.headers,
      )
      try:
        self._raw_cache = self._res.json()
      except ValueError:
        self._raw_cache = self._res.text
      return self
    except httpx.HTTPError as e:
      if self._client:
        self._client.close()
      raise ConnectionError("Got Error!", str(e), 400)

  def __exit__(self, exc_type, exc, tb):
    if self._client:
      self._client.close()
    return False
  @property
  def status_code(self):
    return self._res.status_code if self._res else None

  @property
  def raw(self):
    return self._raw_cache

  @property
  def serilized_json(self):
    if isinstance(self._raw_cache, (dict, list)):
      return json.dumps(self._raw_cache, indent=2)
    return self._raw_cache

  def text(self):
    if self._res is None:
      raise RuntimeError("Connection not initialized. Use 'with ConnectorSync(...)'")
    return self._res.text
  @classmethod
  def get(cls, url: str, **kwargs):
    return cls(url, "GET", **kwargs)

  @classmethod
  def post(cls, url: str, **kwargs):
    return cls(url, "POST", **kwargs)

  @classmethod
  def put(cls, url: str, **kwargs):
    return cls(url, "PUT", **kwargs)

  @classmethod
  def delete(cls, url: str, **kwargs):
    return cls(url, "DELETE", **kwargs)
