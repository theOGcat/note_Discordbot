import discord
from discord.ext import commands
from discord.ext.commands.core import command


class fun(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('fun is On')

    @commands.command(aliases=['小橘猫'])
    async def repeatWord(self, ctx, *, question):
        await ctx.send(f'{question[1:]}')


def setup(bot):
    bot.add_cog(fun(bot))
