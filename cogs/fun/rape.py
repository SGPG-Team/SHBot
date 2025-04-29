import discord
from discord.ext import commands
from discord import app_commands

from utils import handle_errors

class RapeCommand(commands.Cog):
	@commands.has_permissions(ban_members=True)
	@commands.hybrid_command(
		aliases=["рейп", "рейпнуть"],
		description="**Админская команда.** RAPE MEMBER.",
		usage="`/rape <пользователь>`",
		help="")
	@app_commands.default_permissions(ban_members=True)
	@app_commands.describe(user="RAPE THIS MEMBER")
	
	async def rape(self, ctx, *, user: discord.Member):
		await ctx.channel.send("https://media.discordapp.net/attachments/1154568629959020594/1263614527719870595/right_click.gif?ex=67fa37fc&is=67f8e67c&hm=ef484ad6b5f316c1eeb9c70dba3259123c85c5481e620ab5ba12250b0cc06c66&=")
		if ctx.interaction:
			await ctx.send("_ _", ephemeral=True, delete_after=0)
		else:
			await ctx.message.delete()

	@rape.error
	async def rape_error(self, ctx, error):
		await handle_errors(ctx, error, [
			{
				"exception": commands.MissingRequiredArgument,
				"msg": "Введите пользователя"
			},
			{
				"exception": commands.MissingPermissions,
				"msg": "Недостаточно прав"
			}
		])