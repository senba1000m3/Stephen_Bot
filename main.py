import discord,json,os,keep_alive
from discord.ext import commands

intents = discord.Intents.all()

with open("setting.json","r",encoding="utf8") as file:
    data = json.load(file)

bot = commands.Bot(command_prefix='%',intents=intents)
bot.remove_command('help') #移除預設help指令

@bot.event
async def on_ready():
    print("【 Bot is online 】")

@bot.event #指定事件
async def on_member_join(member): #偵測是否有人加入群組
    channel = bot.get_channel(768408387653861379)
    await channel.send(f"歡迎新同學{member}加入201！") #傳送歡迎訊息

@bot.event #指定事件
async def on_member_remove(member): #偵測是否有人離開群組
    channel = bot.get_channel(768408387653861379)
    await channel.send(f"歡送{member}同學離開201！") #傳送送別訊息

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}ms")
  
@bot.command()
async def repeat(ctx,*,msg):
    if ctx.author.id == 486103022221525003:
        await ctx.message.delete()
        await ctx.send(msg)
    else:
        await ctx.send("你沒有使用該指令的權限！")

@bot.command()
async def clear(ctx,n:int):
    if ctx.author.id == 486103022221525003:
        await ctx.channel.purge(limit=n+1)
    else:
        await ctx.send("你沒有使用該指令的權限！")

@bot.command()
async def 神奇海螺(ctx):
    pic = discord.File(data["Stephen"])
    await ctx.send("神奇宗良")
    await ctx.send(file = pic)

for cog_file in os.listdir("./commands"):
    if cog_file.endswith(".py"):
        bot.load_extension(f"commands.{cog_file[:-3]}")
    
if __name__ == "__main__":
    keep_alive.keep_alive() #讓機器人維持運作的命令
    bot.run(data["Token"])

