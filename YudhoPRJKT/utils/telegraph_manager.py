import aiohttp
import markdown
from .create_log import CreateLog
from dataclasses import dataclass
from typing import Optional
from bs4 import BeautifulSoup


ALLOWED_TAGS = {
  "p", "h3", "h4", "strong", "em", "a", 
  "ul", "ol", "li",
  "img",
  "pre", "code",
  "blockquote",
  "figure", "figcaption"
}

@dataclass
class telegraph_data:
  short_name: Optional[str] = None
  author_name: Optional[str] = None
  author_url: Optional[str] = None
  access_token: Optional[str] = None
  auth_url: Optional[str] = None
  url: Optional[str] = None

def conv(html: str):
  soup = BeautifulSoup(html, "html.parser")
  return parse_children(soup)

def parse_children(element):
  result = []

  TAG_REPLACE = {
    "b": "strong",
    "i": "em",
    "h1": "h3",
    "h2": "h3",
    "h5": "h4",
    "h6": "h4",
    "div": "p",
    "span": "p",
  }

  for child in element.children:
    if child.name is None:
      text = (child.string or "").strip()
      if text:
        result.append(text)
      continue

    tag = child.name.lower()

    if tag not in ALLOWED_TAGS:
      if tag in TAG_REPLACE:
        tag = TAG_REPLACE[tag]
      else:
        tag = "p"

    if tag == "pre":
      code_child = child.find("code")
      text = code_child.get_text() if code_child else child.get_text()
      result.append({"tag": "pre", "children": [text]})
      continue

    node = {"tag": tag}

    if tag == "a" and child.get("href"):
      node["attrs"] = {"href": child["href"]}
    if tag == "img" and child.get("src"):
      node["attrs"] = {"src": child["src"]}

    children = parse_children(child)
    if children:
      node["children"] = children

    result.append(node)

  return result

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
        'content': conv(markdown.markdown(content)),
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
