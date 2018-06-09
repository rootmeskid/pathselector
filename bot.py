#pathselector by lain
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = discord.Client()

client = commands.Bot(command_prefix='.')

@commands.command()
async def test(ctx, arg):
   await ctx.send(arg)

@client.event
async def on_ready():
print("i am ready")

client.run('NDU0NzcxMjAxMzM2ODAzMzQw.DfzVcg.BuwT4txMrokDL_vrKFLfeTMYrXU')
