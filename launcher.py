import asyncio
import aiohttp
from bot import Aswo
import os

async def main():
    async with aiohttp.ClientSession() as session:
        bot = Aswo(session=session) 
        exts = [
            f"cogs.{ext if not ext.endswith('.py') else ext[:-3]}"
            for ext in os.listdir("cogs")
            if not ext.startswith("_")
        ]
        for ext in exts:
            bot.add_extension(ext)
        await bot.start("", banner=True)


asyncio.run(main())