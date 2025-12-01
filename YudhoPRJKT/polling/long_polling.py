from ..bot.bot import bot
from.clear_polling import clear_polling
import asyncio

async def long_polling():
  offset = None
  await clear_polling()
  while True:
    a = await bot.updates.getUpdates(offset)
    if a.raw_json and 'result' in a.raw_json:
      for out_polling in a.raw_json['result']:
        offset = out_polling['update_id'] + 1
        return out_polling
      await asyncio.sleep(1)