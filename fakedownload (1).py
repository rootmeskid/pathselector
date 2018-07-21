import discord
import time
import requests
import json
import random
import asyncio
from PythonGists import PythonGists
from discord.ext import commands
from cogs.utils.checks import *

'''FakeDownload'''

class FakeDownload:
	def __init__(self, bot):
		self.bot = bot
		config = load_config()
		self.bot_prefix = config["bot_identifier"]
	
	@commands.command(pass_context=True)
	async def download(self, ctx,*filename):
		"""downloads specified file(s) from db
		"""
		file = (' '.join(list(filename)))
		await ctx.message.channel.send('Downloading ' + '`' + file + '`' + ' to `Downloads/`...')
		await asyncio.sleep(10 + (random.random() * 10))
		await ctx.message.channel.send('Finished downloading ' + '`' + file + '`' + '!')
		


def setup(bot):
	bot.add_cog(FakeDownload(bot))
	print('thank you for downloading SUPER DUPER ULTRA COG !! ')
	print('for one time donation of $5.66 you could make man wallet better :) thank again for downnload SUPER COG')
	