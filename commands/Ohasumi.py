import discord
from discord.ext import commands
from core.cog import cog

channel = 770644976782671922

class oha(cog):
    
    @commands.Cog.listener() 
    async def on_message(self,msg):
        if msg.channel.id == channel:
            if (msg.content.endswith("早安") or msg.content.endswith("早")) and msg.author != self.bot.user:
                await msg.channel.send("同學早安")

class sumi(cog):
    
    @commands.Cog.listener() 
    async def on_message(self,msg):
        if msg.channel.id == channel:
           if msg.content.endswith("晚安") and msg.author != self.bot.user:
                await msg.channel.send("同學晚安")

class hiru(cog):
    
    @commands.Cog.listener() 
    async def on_message(self,msg):
        if msg.channel.id == channel:
            if msg.content.endswith("午安") and msg.author != self.bot.user:
                await msg.channel.send("同學午安")
            
def setup(bot):
    bot.add_cog(oha(bot))
    bot.add_cog(sumi(bot))
    bot.add_cog(hiru(bot))