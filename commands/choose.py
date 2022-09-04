from discord.ext import commands
from core.cog import cog
import json,random

with open("setting.json","r",encoding="utf8") as file:
    data = json.load(file)

class choice(cog):
    @commands.command()
    async def input(self,ctx,a:str,b:str,c:str,d:str):
      if ctx.channel.id == 843086390262759464 or ctx.channel.id == 843367061421948958:
        with open("setting.json","w",encoding="utf8") as file:
          data["choose"] = [a,b,c,d]
          await ctx.channel.send("A:"+a+"\nB:"+b+"\nC:"+c+"\nD:"+d+"\n輸入%ans以隨機選取答案！")
          json.dump(data, file)

class choiceout(cog):
    @commands.command()
    async def ans(self,ctx):
      if ctx.channel.id == 843086390262759464 or ctx.channel.id == 843367061421948958:
        await ctx.channel.send(random.choice(data["choose"]))

def setup(bot):
    bot.add_cog(choice(bot))
    bot.add_cog(choiceout(bot))