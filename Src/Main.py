import discord
import asyncio
from discord.ext import commands

from func import get_token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
discord.utils.setup_logging() #Starts logging

async def main():
    async with bot:
        await bot.load_extension('commands')
        await bot.start(get_token())

asyncio.run(main())