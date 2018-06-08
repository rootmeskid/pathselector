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

bot.run("JQJvczpMDV63nE-8BfWW3bywA091V8Nz")