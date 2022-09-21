import io
import typing
import voltage
from voltage.ext import commands
from bot import Aswo

class a(commands.SubclassedCog):
    def __init__(self, bot: Aswo):
        self.bot = bot
        self.name = "hi"


    @commands.command()
    async def ui(self, ctx: commands.CommandContext, member: voltage.Member = None):
        member = member or ctx.author
        avatar = await (await ctx.client.session.get(member.avatar.url)).read()
        roles = ', '.join(role.name for role in member.roles) if member.roles else "No Roles"

        await ctx.send(f"Name: {member.name}\nNickname: {member.nickname}\nRoles: {roles}", attachment=voltage.File(f=avatar, filename=ctx.author.name))

    @commands.command()
    async def botinfo(self, ctx: commands.CommandContext):
        await ctx.send(f"{ctx.client}")


def setup(bot: Aswo):
    return a(bot)