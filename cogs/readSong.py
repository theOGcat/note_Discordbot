import discord
import os
from discord.ext import commands
from discord.ext.commands.core import command


class readSong(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('readSongs is On')

    @commands.command(aliases=['爷要听周杰伦'])
    async def readSongJay(self, ctx):
        for songName in os.listdir('./songName'):
            if songName.endswith('.txt'):
                f = open("./songName/jayChou.txt", "r")
                await ctx.send(f'好的大哥\n'+f.read())
                f.close()
                break

    @commands.command(aliases=['爷要听林宥嘉'])
    async def readSongYoga(self, ctx):
        for songName in os.listdir('./songName'):
            if songName.endswith('.txt'):
                f = open("./songName/yoga.txt", "r")
                await ctx.send(f'好的大哥\n'+f.read())
                f.close()
                break

    @commands.command(aliases=['爷要听周兴哲'])
    async def readSongEric(self, ctx):
        for songName in os.listdir('./songName'):
            if songName.endswith('.txt'):
                f = open("./songName/ericZhou.txt", "r")
                await ctx.send(f'好的大哥\n'+f.read())
                f.close()
                break

    @commands.command(aliases=['爷要听颜人中'])
    async def readSongYan(self, ctx):
        for songName in os.listdir('./songName'):
            if songName.endswith('.txt'):
                f = open("./songName/yanrenZhong.txt", "r")
                await ctx.send(f'好的大哥\n'+f.read())
                f.close()
                break

    @commands.command(aliases=['爷要听我的歌单'])
    async def readSongMyplay(self, ctx):
        for songName in os.listdir('./songName'):
            if songName.endswith('.txt'):
                f = open("./songName/myPlayList.txt", "r")
                await ctx.send(f'好的大哥\n'+f.read())
                f.close()
                break


def setup(bot):
    bot.add_cog(readSong(bot))
