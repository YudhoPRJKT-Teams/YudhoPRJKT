import aiohttp
import asyncio
from .create_log import CreateLog
from dataclasses import dataclass
from typing import Optional

@dataclass
class telegraph_data:
  short_name: Optional[str] = None
  author_name: Optional[str] = None
  author_url: Optional[str] = None
  access_token: Optional[str] = None
  auth_url: Optional[str] = None
  url: Optional[str] = None

class Graph:
  api = 'https://api.telegra.ph'
  @classmethod
  async def createToken(cls, short_name: str, author_name: str):
    """Use this method to create a new Telegraph account. Most users only need one account, but this can be useful for channel administrators who would like to keep individual author names and profile links for each of their channels. On success, returns an [Account](https://telegra.ph/api#Account) object with the regular fields and an additional `access_token` field.

    Args:
        short_name (str): Account name, helps users with several accounts remember which they are currently using. Displayed to the user above the "Edit/Publish" button on Telegra.ph, other users don't see this name.
        author_name (str): Default author name used when creating new articles.
    """
    if short_name is not None and author_name is not None:
      payload = {'short_name': short_name, 'author_name': author_name}
      async with aiohttp.ClientSession() as client:
        async with client.post(f"{cls.api}/createAccount", json=payload) as session:
          raw = await session.json()
          if session.status == 200:
            return telegraph_data(
              raw['result'].get('short_name'),
              raw['result'].get('author_name'),
              raw['result'].get('author_url'),
              raw['result'].get('access_token'),
              raw['result'].get('auth_url')
            )
          else:
            return telegraph_data(
              raw['result'].get('short_name'),
              raw['result'].get('author_name'),
              raw['result'].get('author_url'),
              raw['result'].get('access_token'),
              raw['result'].get('auth_url')
            )
  @classmethod
  async def createPage(cls, title: str, author_name: str, author_url: str, content: str, short_name: str, return_content: Optional[bool] = False):
    if title is not None and author_name is not None and author_url is not None and content is not None and short_name is not None:
      a = await cls.createToken(short_name, author_name)
      payload = {
        'access_token': a.access_token,
        'title': title,
        'author_name': author_name,
        'content': [
          {
            "tag": "p",
            "children": [
              content
            ]
          }
        ],
        'return_content': return_content
      }
      async with aiohttp.ClientSession() as client:
        async with client.post(f"{cls.api}/createPage", json=payload) as session:
          raw = await session.json()
          if session.status == 200:
            return telegraph_data(url=raw['result'].get('url', ''))
          else:
            return telegraph_data(url=raw['result'].get('url', ''))
    else:
      pass