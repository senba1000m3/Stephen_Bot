import discord
from discord.ext import commands
from core.cog import cog

class help(cog):
    
    @commands.command() 
    async def help(self,ctx):
        embed=discord.Embed(title="【詳細功能】", color=ctx.author.color, timestamp=ctx.message.created_at)
        embed.add_field(name="早/午/晚安", value="在「早晚安頻道」中輸入早安、午安、晚安\n即可得到答覆。",inline=False)
        embed.add_field(name="嗎/?/？", value="在「抽籤與問題」頻道中句尾加上嗎或?或？\n即可得到相對應的答案。\n（機率為7/15是 7/15否 1/15窩不知道）",inline=False)
        embed.add_field(name="的機率", value="在「抽籤與問題」頻道中句尾加上的機率\n即可得到相對應的機率。\n（機率範圍從0%至100%）",inline=False)
        embed.add_field(name="校園資訊", value="可抓取潮州高中學校官網訊息並於「校園資訊」頻道通知。",inline=False)
        embed.add_field(name="預定行程", value="在「預定行程」頻道中登陸的行程會在前一天及前一小時傳送訊息通知。",inline=False)
        await ctx.send(embed=embed)

        embed=discord.Embed(title="【指令大全】", color=ctx.author.color, timestamp=ctx.message.created_at)
        embed.add_field(name="%help", value="查詢Magic Stephen II可用指令與功能",inline=False)
        embed.add_field(name="%神奇海螺", value="神奇宗良！",inline=False)
        embed.add_field(name="%time", value="查詢本日日期與現在時間",inline=False)
        embed.add_field(name="%抽籤", value="隨機抽取一支籤",inline=False)
        embed.add_field(name="%課表", value="查詢潮州高中二年一班課表",inline=False)
        embed.add_field(name="%下一節課", value="查詢下一節課是什麼（關閉中）",inline=False)
        embed.add_field(name="%input 選項A 選項B 選項C 選項D", value="輸入選項",inline=False)
        embed.add_field(name="%ans", value="隨機輸出選項",inline=False)
        embed.add_field(name="%record 名稱 月 日 時 分", value="登錄預定行程",inline=False)
        embed.add_field(name="%check", value="查詢預定行程",inline=False)
        embed.add_field(name="%cancel 編號", value="取消對應編號行程",inline=False)
        embed.add_field(name="%repeat 訊息", value="讓Magic Stephen II輸入相對應訊息（管理員專用）",inline=False)
        embed.add_field(name="%clear 數量", value="在該頻道清除相對應數量訊息（管理員專用）",inline=False)
        await ctx.send(embed=embed)

       
def setup(bot):
    bot.add_cog(help(bot))
