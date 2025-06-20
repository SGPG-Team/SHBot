from discord.ext import commands
from discord import app_commands

class ZaebalCommand(commands.Cog):
	@commands.hybrid_command(
		aliases=["заебал", "❌"],
		description="ЗАЕБАЛ.",
		usage="`/zaebal`",
		help="")
	
	async def zaebal(self, ctx):
		await ctx.channel.send("https://media.discordapp.net/attachments/1226597207948398752/1383405092530684095/converted.gif?ex=6855ec24&is=68549aa4&hm=b6294902646b4b37a1852248d441dde07e97f161aece63b4be4e9b1a46c185fd&=")
		if ctx.interaction:
			await ctx.send("_ _", ephemeral=True, delete_after=0)
		else:
			await ctx.message.delete()
