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

client.run('NDU0NzcxMjAxMzM2ODAzMzQw.DfymaQ.6TpgZjXC83d7I0XrCz4sU6LQvTs')
