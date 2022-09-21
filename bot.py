import asyncio
import aiohttp
import voltage
from voltage.ext import commands
from discord import utils

utils.setup_logging()

class Aswo(commands.CommandsClient):
    def __init__(self, *, session: aiohttp.ClientSession):
        self.session = session
        super().__init__("!!")
    