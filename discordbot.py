from discord.ext import commands
import os
import traceback


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
   
@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')
    
@bot.command()
async def 入部(ctx):
    await ctx.send('''部活にはいる方法はこちら
    https://youtu.be/wq21u3RrS9M''')

@bot.command()
async def 部活リスト(ctx):
    await ctx.send('''【部活リスト】
●ふくいズンバクラブ
●朝会企画部
●ラジオ勢
●アニメ・マンガ部 
●マイクラ部
●歴史部
●読書部
●音楽部
●いきもの部
●鉄道部
●料理部
●ポケモン部
●あつもり部
●Fortnite部
●スプラ部
●ボードゲーム部
●クイズ部 
●ヨガ部
●サッカー部 
【保護者の部活】
●保護者部
●運動愛好会''')

@bot.command()
async def Youtubeにアップしたい(ctx):
    await ctx.send('''youtubeへ動画をアップロードする方法は？
    https://youtu.be/8Par0yc3ZXA''')

ROLE_BASIC_ID = 714716828961603645

@bot.command()
@commands.has_permissions(administrator=True)
async def set_members(ctx):
    海洋生物編 = ctx.guild.get_role(ROLE_BASIC_ID)
    for member in ctx.guild.members:
        if not member.bot:
            await member.add_roles(海洋生物編)

bot.run(token)
