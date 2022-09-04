import discord,json,random
from discord.ext import commands
from core.cog import cog

with open("setting.json","r",encoding="utf8") as file:
    data = json.load(file)

channel = 843367061421948958

class kuji(cog):
    
    @commands.command() 
    async def 抽籤(self,ctx):
        if ctx.channel.id == channel:
            random_picture = random.choice(data["Kuji"])
            if random_picture == "https://i.imgur.com/A1JvfIX.png":
                luck = "大吉"
            elif random_picture == "https://i.imgur.com/CaLCRO0.png":
                luck = "吉"
            elif random_picture == "https://i.imgur.com/jESMqFj.png":
                luck = "平"
            elif random_picture == "https://i.imgur.com/bloePTO.png":
               luck = "凶"
            elif random_picture == "https://i.imgur.com/apefclT.png":
               luck = "大凶"
            embed=discord.Embed(title="【抽籤結果】", color=ctx.author.color, timestamp=ctx.message.created_at)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name="你今天的運勢是", value=luck)
            embed.set_image(url = random_picture)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(kuji(bot))