import aiohttp
import asyncio
from ..configs.config import AuthManager
from ..utils.create_log import CreateLog


async def clear_polling():
  async with aiohttp.ClientSession() as client:
    async with client.get(f"{AuthManager.ReadConfig().get('api')}/getUpdates") as srv:
      raw = await srv.json()
      if raw['result']:
        offset = max(u["update_id"] for u in raw["result"]) + 1
        payload = {'offset': offset}
        async with client.get(f"{AuthManager.ReadConfig().get('api')}/getUpdates", params=payload) as client:
          await client.read()
      else:
        pass