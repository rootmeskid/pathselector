#pathselector by lain
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.bot(command_prefix='.')
@bot.event
async def on_ready():
print("The Cannons Are Ready To Fire!!")
print("Not Yet Megaman 11")

@bot.command(pass_context=True)
async def clr(context, number : int):	
"""Clear a specified number of messages in the chat"""	
deleted = await bot.purge_from(context.message.channel, limit=number)	
await bot.send_message(context.message.channel, 'Deleted {} message(s)'.format(len(deleted)))

bot.run("NDU0NzcxMjAxMzM2ODAzMzQw.DfyipA.O3jDDK_FJEKszzWEmSvJgNOeVNE")