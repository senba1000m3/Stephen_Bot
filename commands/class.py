import discord,json
from discord.ext import commands
from core.cog import cog

with open("setting.json","r",encoding="utf8") as file:
    data = json.load(file)

class classlist(cog):

    @commands.command()
    async def 課表(self,ctx):
        if ctx.channel.id == 843367061421948958:
            pic = discord.File("./picture/課表.png")
            await ctx.send(file = pic)

def setup(bot):
    bot.add_cog(classlist(bot))