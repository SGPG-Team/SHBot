import discord
from discord.ext import commands

from utils import handle_errors

class SGexCommand(commands.Cog):
	@commands.Cog.listener("on_message")
	async def sgex(self, msg):
		if msg.content == "s.gex":
			file = discord.File("assets/saygex.gif")
			await msg.channel.send(file=file)

