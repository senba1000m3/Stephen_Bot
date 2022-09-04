import discord,random,datetime
from datetime import date,datetime,timezone,timedelta
from discord.ext import commands
from core.cog import cog

tz = timezone(timedelta(hours=+8,minutes=+0,seconds=+0))

class dt(cog):

    @commands.command()
    async def time(self,ctx):
        today = date.today()
        nowtime = datetime.now(tz).strftime("現在是%H點%M分%S秒")
        nowday = today.strftime("今天是%Y年%m月%d日")
        week = today.weekday()
        if week == 0:
            await ctx.channel.send(f"{nowday} 星期一\n{nowtime}")
        elif week == 1:
            await ctx.channel.send(f"{nowday} 星期二\n{nowtime}")
        elif week == 2:
            await ctx.channel.send(f"{nowday} 星期三\n{nowtime}")
        elif week == 3:
            await ctx.channel.send(f"{nowday} 星期四\n{nowtime}")
        elif week == 4:
            await ctx.channel.send(f"{nowday} 星期五\n{nowtime}")
        elif week == 5:
            await ctx.channel.send(f"{nowday} 星期六\n{nowtime}")
        elif week == 6:
            await ctx.channel.send(f"{nowday} 星期日\n{nowtime}")

def setup(bot):
    bot.add_cog(dt(bot))