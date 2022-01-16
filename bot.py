import discord
import random
import os
from dotenv import load_dotenv
from discord import activity
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv("CLIENT_TOKEN")
client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('被大哥调试'))
    print('Hello world, My name is LittleOrangeCat')


@client.command()
async def loadcog(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} was loaded')


@client.command()
async def unloadcog(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} was unloaded')


@client.command()
async def reloadcog(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} was reloaded')


for fileName in os.listdir('./cogs'):
    if fileName.endswith('.py'):
        client.load_extension(f'cogs.{fileName[:-3]}')


client.run(TOKEN)
