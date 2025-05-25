import discord
from discord.ext import commands
import config

from cogs import *

cogs = [SayCommand, LinkCommand, RapeCommand, DebugCommand, FAQs, BotPing, SGexCommand]

class SLBot(commands.Bot):
    def __init__(self, *, intents: discord.Intents, command_prefix: str):
        super().__init__(intents=intents, command_prefix=command_prefix, case_insensitive = True)
    
    async def setup_hook(self):
        for cog in cogs:
            await self.add_cog(cog(self))
        self.add_view(BotPingView())

        await self.tree.sync()

        print(f"User: {bot.user} (ID: {bot.user.id})")

intents = discord.Intents.all()
bot = SLBot(command_prefix=commands.when_mentioned_or("$sudo ", "!"), intents=intents)

bot.run(config.DISCORD_API_TOKEN)
