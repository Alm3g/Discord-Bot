import requests
import discord
from discord.ext import commands

from func import get_token, get_api_key

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send('Hi there!')

@bot.command()
async def gif(ctx):
    result = requests.get("https://api.giphy.com/v1/gifs/random", params={"api_key": get_api_key()}).json()
    await ctx.send(result["data"]["url"])
    
@bot.command()
async def FreeNitro(ctx):
    await ctx.send('https://media.tenor.com/pO54yeWaIJUAAAAd/nitro-rick-roll.gif')
      
bot.run(get_token())