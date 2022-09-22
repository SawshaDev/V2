import io
import logging
import typing
from typing_extensions import Self
import voltage
from voltage.ext import commands
from bot import Aswo
logger = logging.getLogger(__name__)

class a(commands.SubclassedCog):
    def __init__(self, bot: Aswo):
        self.bot = bot
        self.name = "hi"
        
    @commands.command()
    async def profile(self, ctx: commands.CommandContext, member: voltage.Member = None):
        member = member or ctx.author
        profile = await member.fetch_profile()
        em = voltage.SendableEmbed(description=f"Profile Content\n{profile.content}", media=profile.background.url)

        await ctx.send(embed=em)


def setup(bot: Aswo):
    cog = a(bot)

    return cog