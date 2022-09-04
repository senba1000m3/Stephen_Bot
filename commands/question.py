import discord,json,random
from discord.ext import commands
from core.cog import cog

with open("setting.json","r",encoding="utf8") as file:
    data = json.load(file)

channel = 843367061421948958

class questions(cog):
    
    @commands.Cog.listener() 
    async def on_message(self,msg):
        if msg.channel.id == channel:
            if msg.content.endswith("嗎") or msg.content.endswith("?") or msg.content.endswith("？"):
                YorN = random.choice(data["A"])
                message = msg.content
                await msg.channel.send(message+"\n → "+YorN)

class percent(cog):
  
    @commands.Cog.listener() 
    async def on_message(self,msg):
        if msg.channel.id == channel:
            if msg.content.endswith("的機率"):
                Per = random.uniform(0,100)
                message = msg.content
                await msg.channel.send(message+"\n → "+f"{round(Per)}%")

def setup(bot):
    bot.add_cog(questions(bot))
    bot.add_cog(percent(bot))