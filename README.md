<h2 align='center'>YudhoPRJKT<h2>

<h3>YudhoPRJKT is a Python library for creating Telegram Bots using your custom api</h3>

## Installation
Use Package Manager/PIP
```bash
pip install YudhoPRJKT
```
or building from sources
```bash
git clone https://github.com/YudhoPRJKT-Teams/YudhoPRJKT
cd YudhoPRJKT
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Authentication
Make Credentials First (After this complete you can remove this code)
```python
from YudhoPRJKT.auth import Auth

my_auth = Auth()
my_auth.UseCustomApi('http://api.myproject.com')
```
### Usage
```python 
from YudhoPRJKT.bots import Bots
from YudhoPRJKT.bots.types import Message
from YudhoPRJKT.utils import ParseMode
import asyncio

bot = Bots()

@bot.command('/start')
async def command_start(m=Message()):
  await bot.methods.sendMessage(
    m.chat.id,
    "*Hi i'm bots from YudhoPRJKT*",
    ParseMode.MarkdownV2()
  ).reply

if __name__ == '__main__':
  asyncio.run(bot.run())
```
### Documentation
Will Posted Soon

## Contact Me
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/960px-Telegram_logo.svg.png" alt="Contact me on telegram" style="display: block; margin: 0 auto; width: 10%;">
<a href="https://t.me/YudhoPatrianto" style='display: block; text-align:center; font-family: Arial;'>Contact me on telegram</p>
