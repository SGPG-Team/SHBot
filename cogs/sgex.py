import discord
from discord.ext import commands

from utils import handle_errors

class SGexCommand(commands.Cog):
	@commands.Cog.listener("on_message")
	async def sgex(self, msg):
		if msg.content == "s.gex":
		    await msg.channel.send("https://cdn.discordapp.com/attachments/1346554594238533652/1376256682220322846/saygex.gif")

