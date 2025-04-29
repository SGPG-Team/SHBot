import discord
from discord.ext import commands
import config

from cogs.admin import SayCommand, DebugCommand
from cogs.help import LinkCommand
from cogs.fun import RapeCommand
from cogs.faqs import FAQs

cogs = [SayCommand, LinkCommand, RapeCommand, DebugCommand, FAQs]

class SLBot(commands.Bot):
    def __init__(self, *, intents: discord.Intents, command_prefix:str):
        super().__init__(intents=intents, command_prefix=commands.when_mentioned_or(command_prefix), case_insensitive = True)
    
    async def setup_hook(self):
        for cog in cogs:
            await self.add_cog(cog(self))

        await self.tree.sync()

        print(f"User: {bot.user} (ID: {bot.user.id})")

intents = discord.Intents.all()
bot = SLBot(command_prefix="$sudo ", intents=intents)

bot.run(config.DISCORD_API_TOKEN)
