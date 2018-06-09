#pathselector by lain
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

client = discord.Client()

bot = commands.bot(command_prefix='.')

@bot.command()
async def test(ctx):
   await ctx.send(arg)
 
@client.event
async def on_ready():
print('The Cannons Are Ready To Fire!!')
print('Not Yet Megaman 11')

bot.add_command(test)
client.run('NDU0NzcxMjAxMzM2ODAzMzQw.DfymaQ.6TpgZjXC83d7I0XrCz4sU6LQvTs')
