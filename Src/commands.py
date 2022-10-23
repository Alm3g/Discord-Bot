from ast import operator
from discord.ext import commands
import requests
import random
import operator
from func import get_api_key

    
class commands(commands.Cog):
    def init(self, bot):
        self.bot = bot
        
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hi there!')

    @commands.command()
    async def gif(self, ctx):
        result = requests.get("https://api.giphy.com/v1/gifs/random", params={"api_key": get_api_key()}).json()
        await ctx.send(result["data"]["url"])
        
    @commands.command()
    async def FreeNitro(self, ctx):
        await ctx.send('https://media.tenor.com/pO54yeWaIJUAAAAd/nitro-rick-roll.gif')
        
        
        
async def setup(bot):
    await bot.add_cog(commands(bot))
    