#pathselector by lain
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = discord.Client()

bot = commands.bot(command_prefix='.')

@client.event
async def on_ready():
print('The Cannons Are Ready To Fire!!')
print('Not Yet Megaman 11')

@client.command(pass_context=True)
async def purge(context, number : int):	
"""Clear a specified number of messages in the chat"""	
deleted = await bot.purge_from(context.message.channel, limit=number)	
await bot.send_message(context.message.channel, 'Deleted {} message(s)'.format(len(deleted)))

client.run("NDU0NzcxMjAxMzM2ODAzMzQw.DfymaQ.6TpgZjXC83d7I0XrCz4sU6LQvTs")
