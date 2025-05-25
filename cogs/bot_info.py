import discord
from discord.ext import commands

from utils.shortcuts import no_ping, no_color
from utils.msg_utils import Emojis

class BotPing(commands.Cog):
	def __init__(self, bot):
		self.bot: commands.Bot = bot
	
	@commands.Cog.listener("on_message")
	async def main(self, msg):
		if msg.author == self.bot.user:
			return
		if msg.content.strip() == ("<@1360341683014729979>"):
			embed = discord.Embed(
				description=f"Привет! Я многофункциональный дискорд бот, созданный <@685091615991136290> и <@567014541507035148> и предназначенный чисто для этого сервера SGPG Team. Моя главная цель — помочь вам в изучении команд, датапаков и ресурспаков, но я также имею и другие интересные функции", 
				color=no_color)
			#embed.set_author(name="AntBot", icon_url=self.bot.user.avatar.url)
			embed.set_thumbnail(url=self.bot.user.avatar.url)
			await msg.reply(embed=embed, view=BotPingView(), allowed_mentions=no_ping)

class BotPingView(discord.ui.View):
	def __init__(self):
		super().__init__(timeout=None)
		self.add_item(discord.ui.Button(
			label="Исходный код",
			emoji=f"{Emojis.github}",
			url="https://github.com/SGPG-Team/SHBot"
		))
		self.add_item(discord.ui.Button(
			label="Предложить идею/зарепортить баг",
			emoji="🔗",
			url="https://discord.com/channels/1343257023432626268/1360526871669772341"
		))
	