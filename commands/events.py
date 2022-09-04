import discord,random,datetime,json,asyncio
from datetime import date,datetime,timezone,timedelta
from discord.ext import commands
from core.cog import cog

with open("record.json","r",encoding="utf8") as file:
    record = json.load(file)

tz = timezone(timedelta(hours=+8,minutes=+0,seconds=+0))

class loadevent(cog):
    @commands.command()
    async def record(self,ctx,a:str,b:int,c:int,d:int,e:int):
      if ctx.channel.id == 843086390262759464:
        with open("record.json","w",encoding="utf8") as file:
          record["times"] = record["times"]+1 
          record[record["times"]] = [a,b,c,d,e]
          await ctx.channel.send("該事項已儲存！\n項目編號："+str(record["times"])+"\n項目內容："+a+"\n日期："+str(b)+"月"+str(c)+"日\n時間："+str(d)+"點"+str(e)+"分 （24小時制）")
          json.dump(record, file, ensure_ascii=False)
        
class notice(cog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def notice():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(843086390262759464)
            #self.channel2 = self.bot.get_channel(843086390262759464)
            while not self.bot.is_closed():
                with open("record.json","r",encoding="utf8") as file:
                    record = json.load(file)
                for x in range(1,record["times"]+1):
                  #await self.channel.send(record[str(x)][1])
                  today = date.today()
                  month = today.strftime("%m")
                  dates = today.strftime("%d")
                  hour = datetime.now(tz).strftime("%H")
                  minute = datetime.now(tz).strftime("%M")
                  if str(record[str(x)]) != "0":
                    if record[str(x)][1] < 10:
                      x1 = ("0"+str(record[str(x)][1]))
                      x1_2 = ("0"+str(record[str(x)][1]))
                    else:
                      x1 = str(record[str(x)][1])
                      x1_2 = str(record[str(x)][1])
                    if record[str(x)][2] < 10:
                      x2 = ("0"+str(record[str(x)][2]))
                    else:
                      x2 = str(record[str(x)][2])
                    if record[str(x)][2]-1 == 0:
                      if record[str(x)][1]-1 < 10:
                        x1_2 = ("0"+str(record[str(x)][1]-1))
                      else:
                        x1_2 = str(record[str(x)][1]-1)
                    elif record[str(x)][2]-1 < 10:
                      x2_2 = ("0"+str(record[str(x)][2]-1))
                    else:
                      x2_2 = str(record[str(x)][2]-1)
                    if record[str(x)][3] < 10:
                      x3 = ("0"+str(record[str(x)][3]))
                    else:
                      x3 = str(record[str(x)][3])
                    if record[str(x)][3]-1 < 10:
                      x3_2 = ("0"+str(record[str(x)][3]-1))
                    else:
                      x3_2 = str(record[str(x)][3]-1)
                    if record[str(x)][4] < 10:
                      x4 = ("0"+str(record[str(x)][4]))
                    else:
                      x4 = str(record[str(x)][4])
                      
                    if x1_2 == month and x2_2 == dates and x3 == hour and x4 == minute:
                      await self.channel.send("——————————————————————————\n【通知】\n明天有一項預定行程：\n**"+record[str(x)][0]+"**\n\n日期："+x1+"月"+x2+"日\n時間："+x3+"點"+x4+"分\n——————————————————————————") 
                    if x1 == month and x2 == dates and x3_2 == hour and x4 == minute:
                      await self.channel.send("——————————————————————————\n【通知】\n一小時後有一項預定行程：\n**"+record[str(x)][0]+"**\n\n日期："+x1+"月"+x2+"日\n時間："+x3+"點"+x4+"分\n——————————————————————————") 
                    if x1 == month and x2 == dates and x3 == hour and x4 == minute:
                      await self.channel.send("——————————————————————————\n【通知】\n現在有一項預定行程：\n**"+record[str(x)][0]+"**\n\n日期："+x1+"月"+x2+"日\n時間："+x3+"點"+x4+"分\n——————————————————————————") 
                      with open("record.json","w",encoding="utf8") as file:
                          record[str(x)] = 0
                          json.dump(record, file, ensure_ascii=False)
                    with open("record.json","r",encoding="utf8") as file:
                        record = json.load(file)
                await asyncio.sleep(60)
        
        self.bg_task = self.bot.loop.create_task(notice())

class checkevent(cog):
    @commands.command()
    async def check(self,ctx):
        if ctx.channel.id == 843086390262759464:
            with open("record.json","r",encoding="utf8") as file:
                record = json.load(file)
            embed=discord.Embed(title="【預定事項】", color=0x9c59b6, timestamp=ctx.message.created_at)
            #embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            for c in range(1, record["times"]+1):
                if record[str(c)] != 0:
                    embed.add_field(name=record[str(c)][0], value=("項目編號："+str(c)+"\n日期："+str(record[str(c)][1])+"月"+str(record[str(c)][2])+"日\n時間："+str(record[str(c)][3])+"點"+str(record[str(c)][4])+"分"),inline=False)
            await ctx.send(embed=embed)

class deleteevent(cog):
    @commands.command()
    async def cancel(self,ctx,a:int):
        if ctx.channel.id == 843086390262759464:
            with open("record.json","r",encoding="utf8") as file:
                    record = json.load(file)
            with open("record.json","w",encoding="utf8") as file:
                await ctx.send("項目編號"+str(a)+"（"+record[str(a)][0]+"）已刪除！")
                record[str(a)] = 0
                json.dump(record, file, ensure_ascii=False)
            with open("record.json","r",encoding="utf8") as file:
                record = json.load(file)


def setup(bot):
    bot.add_cog(loadevent(bot))
    bot.add_cog(notice(bot))
    bot.add_cog(checkevent(bot))
    bot.add_cog(deleteevent(bot))