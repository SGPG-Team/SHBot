from discord.ext import commands

from importlib import reload

from utils.general import handle_errors
from utils.shortcuts import no_ping
import temp


class DebugCommand(commands.Cog):
	@commands.has_permissions(ban_members=True)
	@commands.command(aliases=["d"])

	async def debug(self, ctx, *, text: str):
		if ctx.author.id == 685091615991136290 or ctx.author.id == 567014541507035148 or ctx.author.id == 544544013710000149:
			with open("temp.py", "w", encoding="utf-8") as code:
				code.write(f"import discord\nfrom discord.ext import commands\nasync def debug_func(ctx):\n {text.replace("\n", "\n ")}")
			reload(temp)
			await temp.debug_func(ctx)
		else:
			await ctx.reply("Ты не мой разраб 😈", allowed_mentions=no_ping)

	@debug.error
	async def say_error(self, ctx, error):
		await handle_errors(ctx, error, [
			{
				"exception": commands.MissingRequiredArgument,
				"msg": f"Введите текст, который хотите сказать от моего имени"
			},
			{
				"exception": commands.MissingPermissions,
				"msg": f"Недостаточно прав"
			}
		])