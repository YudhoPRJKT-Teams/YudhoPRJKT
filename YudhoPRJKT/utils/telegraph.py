from ..connector.client import BaseConnector
from .types_telegraph.account import Account
from html.parser import HTMLParser
from .types_telegraph import Page
from ..bots.types.message import Message
from .log import Log
import json
import re

class TelegraphContentParser(HTMLParser):
  def __init__(self):
    super().__init__()
    self.stack = [{"tag": "root", "children": []}]
    self.in_pre = False
    self.supported_tags = [
      'a', 'aside', 'b', 'blockquote', 'br', 'code', 'em', 
      'figcaption', 'figure', 'h3', 'h4', 'hr', 'i', 'iframe', 
      'img', 'li', 'ol', 'p', 'pre', 's', 'strong', 'u', 'ul'
    ]
    self.tag_mapping = {
      'div': 'p', 'section': 'p', 'article': 'p',
      'h1': 'h3', 'h2': 'h3', 'h5': 'h4', 'h6': 'h4',
      'span': 'em', 'del': 's', 'center': 'p'
    }
  def handle_starttag(self, tag, attrs):
    target_tag = self.tag_mapping.get(tag, tag)
    if target_tag == 'pre':
        self.in_pre = True
    if target_tag not in self.supported_tags:
      self.stack.append({"tag": "fragment", "children": []})
      return
    node = {"tag": target_tag, "children": []}
    if attrs:
      valid_attrs = {k: v for k, v in attrs if k in ['href', 'src']}
      if valid_attrs:
        node["attrs"] = valid_attrs
    self.stack[-1]["children"].append(node)
    self.stack.append(node)
  def handle_endtag(self, tag):
    target_tag = self.tag_mapping.get(tag, tag)
    if target_tag == 'pre':
      self.in_pre = False
    if len(self.stack) > 1:
      if self.stack[-1]["tag"] == "fragment":
        content = self.stack.pop()["children"]
        self.stack[-1]["children"].extend(content)
      elif self.stack[-1]["tag"] == target_tag:
        self.stack.pop()
  def handle_data(self, data):
    if self.in_pre:
      self.stack[-1]["children"].append(data)
    else:
      if data.strip() or data == " ":
        self.stack[-1]["children"].append(data)
  def get_nodes(self):
    return self.stack[0]["children"]

class TelegraphInit:
  def __init__(self):
    self.connector = BaseConnector
    self.account = Account()
    self.page = Page()
  def Methods(self, methods: str) -> str:
    return f'https://api.telegra.ph/{methods}'.__str__()
  def convert_to_node(self, value):
    if isinstance(value, list):
      return value
    parser = TelegraphContentParser()
    parser.feed(str(value))
    return parser.get_nodes()  
  async def make_account(self, short_name: str, author_name: str, author_url: str):
    """Use this method to create a new Telegraph account. Most users only need one account, but this can be useful for channel administrators who would like to keep individual author names and profile links for each of their channels

    Args:
        short_name (str): Account name, helps users with several accounts remember which they are currently using. Displayed to the user above the "Edit/Publish" button on Telegra.ph, other users don't see this name.
        author_name (str): Default author name used when creating new articles.
        author_url (str): Default profile link, opened when users click on the author's name below the title. Can be any link, not necessarily to a Telegram profile or channel.


    Returns:
        Account: returns an Account object with the regular fields and an additional access_token field.
    """
    payload: dict = {
      'short_name': short_name,
      'author_name': author_name,
      'author_url': author_url
    }
    async with self.connector.post(self.Methods('createAccount'), data=payload ) as client:
      if 'result' in client.raw:
        updater = client.raw['result']
        self.account.short_name = updater.get('short_name', 'no-short_name')
        self.account.author_name = updater.get('author_name', 'no-author_name')
        self.account.auth_url = updater.get('author_url', 'no-author_url')
        self.account.access_token = updater.get('access_token', 'no-access_token')
        self.account.auth_url = updater.get('auth_url', 'no-auth_url')
      return self

class Telegraph(TelegraphInit):
  def __init__(self):
    super().__init__()
    self.msg = Message()
  async def createPage(self, title: str, content: list | str) -> Page:
    """Use this method to create a new Telegraph page. 

    Args:
        title (str): Page title.
        author_name (str): Author name, displayed below the article's title.
        author_url (str): Profile link, opened when users click on the author's name below the title. Can be any link, not necessarily to a Telegram profile or channel.
        content (list|str): _description_
        return_content (bool | None, optional): _description_. Defaults to False.

    Returns:
        Page: On success, returns a Page object.
    """
    remove_username_at = re.sub('@', '', self.msg.From.username)
    my_account = await self.make_account(
      remove_username_at,
      f'{self.msg.From.first_name} {self.msg.From.last_name}',
      f'https://t.me/{remove_username_at}'
    )
    payload: dict = {
      'access_token': my_account.account.access_token,
      'title': title,
      'author_name': my_account.account.author_name,
      'author_url': f'https://t.me/{remove_username_at}',
      'content': self.convert_to_node(content),
      'return_content': True
    }
    async with self.connector.post(self.Methods('createPage'), data=payload) as client:
      raw = client.raw
      if client.status_code != 200:
        error_msg: str = raw['error']
        Log.Error('Failed to create page', error_msg).Show().Save()
      else:
        if 'result' in raw:
          updater = raw['result']
          Page().path = updater.get('path', 'no-path')
          Page().url = updater.get('url', 'no-url')
          Page().title = updater.get('title', 'no-title')
          Page().description = updater.get('description', 'no-description')
          Page().author_name = updater.get('author_name', 'no-author_name')
          Page().author_url = updater.get('author_url', 'no-author_url')
          Page().content = updater.get('content', 'no-content')
      return Page()
  def __str__(self) -> str:
    return self.connector.serialized_json.__str__()