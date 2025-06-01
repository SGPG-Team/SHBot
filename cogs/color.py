import discord
from discord.ext import commands
from discord import app_commands

from utils import handle_errors
from re import compile

hex_re = compile("#?[\da-fA-F]{6}")


class ColorCommand(commands.Cog):
	@commands.hybrid_command(
		aliases=["колор", "цвет"],
		description="Изменяет цвет ника",
		usage="`/color <#цвет>",
		help="")
	@app_commands.describe(color="Цвет в формате (h)gex")
	
	async def color(self, ctx: commands.Context, color: str):
		if not hex_re.match(color):
			raise ValueError("Wrong color")
		roles = ctx.author.roles
		for role in roles:
			if hex_re.match(role.name):
				color_role = role
				break
		else:
			color_role = await ctx.guild.create_role()
			await ctx.author.add_roles(color_role)
		await color_role.edit(
			color=int(color.replace("#", ""), 16),
			name=color
		)
		await ctx.send("Цвет вскибижден")
	
	@color.error
	async def color_error(self, ctx, error):
		await handle_errors(ctx, error, [
			{
				"exception": ValueError,
				"msg": "Для кого написано в гекс формате воодить"
			}
		])
