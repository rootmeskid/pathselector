#pathselector by lain
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = discord.Client()

client = commands.bot(command_prefix='.')

@bot.command()
async def test(ctx):
   await ctx.send(arg)
 
@client.event
async def on_ready():
  print('i am ready')

bot.add_command(test)
client.run('NDU0NzcxMjAxMzM2ODAzMzQw.DfymaQ.6TpgZjXC83d7I0XrCz4sU6LQvTs')