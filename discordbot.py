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

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

async def happybirthday(message):
    reply01 = f'{message.author.mention} 誕生日おめでとう'
    await message.channel.send(reply01)

async def tanqyoutube(message):
    reply02 = f'{message.author.mention} https://www.youtube.com/channel/UCEK-5vX5I8rf1Bfcn_QCL4w'
    await message.channel.send(reply02)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    if message.content == '/inu':
        await message.channel.send('ワン')

    if client.user in message.mentions: # 話しかけられたかの判定
        contentWithoutMention = message.content[23:]
        if "誕生日祝って" in contentWithoutMention:
            await happybirthday(message)
        elif "探究学舎のYoutube" in contentWithoutMention:
            await tanqyoutube(message)
        else:
            await reply(message) # 返信する非同期関数を実行
    
    
bot.run(token)
