import urllib.request as req #import連結網站的模組
import bs4 #import解析HTML的模組
from discord.ext import commands
from core.cog import cog
import json,asyncio

with open("setting.json","r",encoding="utf8") as file:
    data = json.load(file)

class news(cog):
    @commands.command()
    async def news(self,ctx):
        if ctx.channel.id == 926411520961806356 or ctx.channel.id == 926703770090504233:
            await ctx.channel.purge(limit=1)

            url = "https://www.ccsh.ptc.edu.tw/" #潮州高中校網連結
            with req.urlopen(url) as response: #打開此連結
                data = response.read().decode("utf-8") #讀取連結並印出

            root = bs4.BeautifulSoup(data, "html.parser") #以HTML解析data內資料
            title = root.find("div", class_="index_honor_div") #從root從尋找class為index_honor_div的div階層
            news = title.find_all("td") #從title（class為index_honor_div的div階層）尋找所有td階層

            await ctx.channel.send("——————————————————————————")
            await ctx.channel.send("最新校園新聞：")
            count = 0
            for new in news:
                count+=1 #內容區分技術
                if count%5 == 1: #排除不必要輸出
                    continue
                elif count%5 == 0: #排除不必要輸出
                    await ctx.channel.send("——————————————————————————")
                    continue
                elif count == 17:
                    break
                await ctx.channel.send(new.string) #輸出所需數值（時間、處室、名稱）
                if new.a != None: #偵測內部階層a是否為None 是--->跳過 否--->get階層a的所屬href（對應網址）並印出
                    if new.select_one("a").get("href").startswith("data"): #判斷是否為學校網址 是--->補上校網前綴後印出
                        await ctx.channel.send("https://www.ccsh.ptc.edu.tw/"+new.select_one("a").get("href"))
                    else: #判斷是否為學校網址 否--->直接印出
                        await ctx.channel.send(new.select_one("a").get("href"))

class renews(cog):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def renew():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(926703770090504233)
            self.channel2 = self.bot.get_channel(926411520961806356)
            while not self.bot.is_closed():
                url = "https://www.ccsh.ptc.edu.tw/" #潮州高中校網連結
                with req.urlopen(url) as response: #打開此連結
                    tdata = response.read().decode("utf-8") #讀取連結並印出

                root = bs4.BeautifulSoup(tdata, "html.parser") #以HTML解析data內資料
                title = root.find("div", class_="index_honor_div") #從root從尋找class為index_honor_div的div階 層
                news = title.find_all("td") #從title（class為index_honor_div的div階層）尋找所有td階層

                count = 0
                for new2 in news:
                    count+=1 
                    if count == 6:
                        break
                    if new2.a != None:
                        if new2.select_one("a").get("href").startswith("data"):
                           id = str(new2.select_one("a").get("href"))
                           if id != data["id"]:
                              with open("setting.json","w",encoding="utf8") as file:
                                  data["id"] = id
                                  json.dump(data, file)
                              count2 = 0
                              for new3 in news:
                                  count2+=1 #內容區分技術
                                  if count2 == 1: #排除不必要輸出
                                      await self.channel.send("最新校園新聞：")
                                      await self.channel.send("——————————————————————————")
                                      await self.channel2.send("最新校園新聞：")
                                      await self.channel2.send("——————————————————————————")
                                      continue
                                  elif count2%5 == 0: #排除不必要輸出
                                      await self.channel.send("——————————————————————————")
                                      await self.channel2.send("——————————————————————————")
                                      continue
                                  elif count2 == 6:
                                      break
                                  await self.channel.send(new3.string)
                                  await self.channel2.send(new3.string)
                                  if new3.a != None: 
                                      if new2.select_one("a").get("href").startswith("data"): #判斷是否為學校網址 是--->補上校網前綴後印出
                                          await self.channel.send("https://www.ccsh.ptc.edu.tw/"+new2.select_one("a").get("href"))
                                          await self.channel2.send("https://www.ccsh.ptc.edu.tw/"+new2.select_one("a").get("href"))
                                      else: #判斷是否為學校網址 否--->直接印出
                                          await self.channel.send(new2.select_one("a").get("href"))
                                          await self.channel2.send(new2.select_one("a").get("href"))
                #await self.channel.send("hi")
                await asyncio.sleep(600)
        
        self.bg_task = self.bot.loop.create_task(renew())
    
class renews_2(cog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def renew_2():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(926703770090504233)
            self.channel2 = self.bot.get_channel(926411520961806356)
            while not self.bot.is_closed():
                url = "https://www.ccsh.ptc.edu.tw/" #潮州高中校網連結
                with req.urlopen(url) as response: #打開此連結
                    tdata = response.read().decode("utf-8") #讀取連結並印出

                root_2 = bs4.BeautifulSoup(tdata, "html.parser") #以HTML解析data內資料
                title_2 = root_2.find("div", class_="index_news6_div") #從root從尋找class為index_honor_div的div階 層
                news_2 = title_2.find_all("td")

                count_2 = 0
                for new2_2 in news_2:
                    count_2+=1 
                    if count_2 == 6:
                        break
                    if new2_2.a != None:
                        if new2_2.select_one("a").get("href").startswith("data"):
                           id_2 = str(new2_2.select_one("a").get("href"))
                           if id_2 != data["id_2"]:
                              with open("setting.json","w",encoding="utf8") as file:
                                  data["id_2"] = id_2
                                  json.dump(data, file)
                              count2_2 = 0
                              for new3_2 in news_2:
                                  count2_2+=1 #內容區分技術
                                  if count2_2 == 1: #排除不必要輸出
                                      await self.channel.send("最新學生課外活動：")
                                      await self.channel.send("——————————————————————————")
                                      await self.channel2.send("最新學生課外活動：")
                                      await self.channel2.send("——————————————————————————")
                                      continue
                                  elif count2_2%5 == 0: #排除不必要輸出
                                      await self.channel.send("——————————————————————————")
                                      await self.channel2.send("——————————————————————————")
                                      continue
                                  elif count2_2 == 6:
                                      break
                                  await self.channel.send(new3_2.string)
                                  await self.channel2.send(new3_2.string)
                                  if new3_2.a != None: 
                                      if new2_2.select_one("a").get("href").startswith("data"): #判斷是否為學校網址 是--->補上校網前綴後印出
                                          await self.channel.send("https://www.ccsh.ptc.edu.tw/"+new2_2.select_one("a").get("href"))
                                          await self.channel2.send("https://www.ccsh.ptc.edu.tw/"+new2_2.select_one("a").get("href"))
                                      else: #判斷是否為學校網址 否--->直接印出
                                          await self.channel.send(new2_2.select_one("a").get("href"))
                                          await self.channel2.send(new2_2.select_one("a").get("href"))
                #await self.channel.send("hi")
                await asyncio.sleep(600)
        
        self.bg_task = self.bot.loop.create_task(renew_2())
    
class renews_3(cog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def renew_3():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(926703770090504233)
            self.channel2 = self.bot.get_channel(926411520961806356)
            while not self.bot.is_closed():
                url = "https://www.ccsh.ptc.edu.tw/" #潮州高中校網連結
                with req.urlopen(url) as response: #打開此連結
                    tdata = response.read().decode("utf-8") #讀取連結並印出

                root_3 = bs4.BeautifulSoup(tdata, "html.parser") #以HTML解析data內資料
                title_3 = root_3.find("div", class_="index_news3_div") #從root從尋找class為index_honor_div的div階 層
                news_3 = title_3.find_all("td")

                count_3 = 0
                for new2_3 in news_3:
                    count_3+=1 
                    if count_3 == 6:
                        break
                    if new2_3.a != None:
                        if new2_3.select_one("a").get("href").startswith("data"):
                           id_3 = str(new2_3.select_one("a").get("href"))
                           if id_3 != data["id_3"]:
                              with open("setting.json","w",encoding="utf8") as file:
                                  data["id_3"] = id_3
                                  json.dump(data, file)
                              count2_3 = 0
                              for new3_3 in news_3:
                                  count2_3+=1 #內容區分技術
                                  if count2_3 == 1: #排除不必要輸出
                                      await self.channel.send("最新獎助學金：")
                                      await self.channel.send("——————————————————————————")
                                      await self.channel2.send("最新獎助學金：")
                                      await self.channel2.send("——————————————————————————")
                                      continue
                                  elif count2_3%5 == 0: #排除不必要輸出
                                      await self.channel.send("——————————————————————————")
                                      await self.channel2.send("——————————————————————————")
                                      continue
                                  elif count2_3 == 6:
                                      break
                                  await self.channel.send(new3_3.string)
                                  await self.channel2.send(new3_3.string)
                                  if new3_3.a != None: 
                                      if new2_3.select_one("a").get("href").startswith("data"): #判斷是否為學校網址 是--->補上校網前綴後印出
                                          await self.channel.send("https://www.ccsh.ptc.edu.tw/"+new2_3.select_one("a").get("href"))
                                          await self.channel2.send("https://www.ccsh.ptc.edu.tw/"+new2_3.select_one("a").get("href"))
                                      else: #判斷是否為學校網址 否--->直接印出
                                          await self.channel.send(new2_3.select_one("a").get("href"))
                                          await self.channel2.send(new2_3.select_one("a").get("href"))
                #await self.channel.send("hi")
                await asyncio.sleep(600)
        
        self.bg_task = self.bot.loop.create_task(renew_3())

def setup(bot):
    bot.add_cog(news(bot))
    bot.add_cog(renews(bot))
    bot.add_cog(renews_2(bot))
    bot.add_cog(renews_3(bot))