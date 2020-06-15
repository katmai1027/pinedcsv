import discord
import random
import os
import re
import requests
import linecache
import tweepy
import json
from discord.ext import commands
import math

bot = commands.Bot(command_prefix='$')

TOKEN = 'NzA4ODYxOTYzMjE1Njk5OTg4.Xrdhig.d2znvPl9wMhogr1Logsb6BBH0SQ'
pad = 0
client = discord.Client()
id_list = []


@bot.event
async def on_ready():
    
    print('ログインしました')






    
@bot.event

async def on_message(message):
    if message.author.bot:
        return
    au = message.author
    na = message.channel
    co = message.content
    
    #print(au,":",co,"at",na)

    #if '@' in message.content:
     #   if message.content.startswith('>'):
      #      pass
#
 #       else:
            #await message.delete()
            #await message.channel.send('引用以外のメンションは禁止されています。')
            #return
  #          pass


# ===ここから会話===

    if '$' not in message.content:
        if '706481838553825280'in message.content:
            await message.channel.send('?')
            return
        if 'おはまんこ'in message.content or '🤔'in message.content or 'おふぱこ'in message.content:      
            await message.add_reaction('🤔')
            return
        
        if 'botの説明書' in message.content:
            await message.channel.send('-<<鯖ァーンwww bot 説明書>>-\n\n反応するワード(一部)\nおはよ/おやすみ/あ/しねかぶった/ぶっ壊す/f**k/買った/ァーン/ンーァ/ぴえん/びえん/ひえん/ヴィーン/クソ/うるせぇ/ェーン/うっきー/ゴルァ\n\nコマンド\n$CPU型番を書く/$S-specを書く/$poop モノor人/$god モノor人/$custom モノor人 任意の言葉 $tweet ツイート内容/$reply')
        
            return


        if 'よっしゃ' in message.content or 'わーい' in message.content or 'やったぁ' in message.content or '嬉しい' in message.content:   
            num = random.randint(0, 2)
            if num == 0:
                await message.channel.send('おおおおおお！')
            elif num == 1:
                await message.channel.send('おめでと！！')
            else:
                await message.channel.send('いいねぇ')
            return
        if '喜' in message.content or '楽し' in message.content or 'よろこ' in message.content or 'うれし' in message.content:
            num = random.randint(0, 2)
            if num == 0:
                await message.channel.send('ひゃっはぁー！')
            elif num == 1:
                await message.channel.send('そりゃいいなぁ')
            else:
                await message.channel.send(file=discord.File('(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)イヒーwwwwwwwwwwwイヒヒヒヒヒヒヒヒヒヒヒwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'))
            return
        if 'たのし' in message.content or 'ハッピー' in message.content or 'happy' in message.content or 'glad' in message.content:
            num = random.randint(0, 2)
            if num == 0:
                await message.channel.send('フーンよかったじゃん（←むかつくやつ）')
            elif num == 1:
                await message.channel.send('おめでとさん！！')
            else:
                await message.channel.send('(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)イヒーwwwwwwwwwwwイヒヒヒヒヒヒヒヒヒヒヒwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
            return

        if '完成' in message.content or 'ひゃっは' in message.content or '勝った' in message.content or 'いえーい' in message.content:
            num = random.randint(0, 2)
            if num == 0:
                await message.channel.send('わーお')
            elif num == 1:
                await message.channel.send('すっげぇや')
            else:
                await message.channel.send('(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)(՞ةڼ◔)イヒーwwwwwwwwwwwイヒヒヒヒヒヒヒヒヒヒヒwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
            return

        if '買った' in message.content or '購入' in message.content or '買いました' in message.content or '買ってきた' in message.content:  
            num = random.randint(0, 2)
            if num == 0:
                await message.channel.send('ちゃりーん！散財完了！')
            elif num == 1:
                await message.channel.send('おーええやん')
            else:
                await message.channel.send('それを買う金をワシによこせ')
            return
    




        if '鯖ァーン' in message.content:
            await message.channel.send('鯖ァーンｗｗｗ')
            return
        if 'ァーン' in message.content:
            await message.channel.send('喘ぐな気持ち悪い')
            return
        if 'ぴえん' in message.content or 'ピエン' in message.content or 'ぴゑん' in message.content or 'ピヱン' in message.content:
            await message.channel.send(':pleading_face:')
            return
        if 'びえん' in message.content or 'ビエン' in message.content or '鼻炎' in message.content or 'びゑん' in message.content or 'ビヱン' in message.content:
             
            await message.channel.send(':sneeze:')
            return
    
        if 'ンーァ' in message.content:
            await message.channel.send('ァーンァーンｗｗｗ')
            return
        if 'おはよ' in message.content:
            await message.channel.send('やぁ、おはよう！')
            return
        if 'ヴィーン' in message.content:
            await message.channel.send('ヴィーンヴィーンｗｗｗ')
            return
        if 'ぶっ壊す' in message.content or 'ぶっこわす' in message.content or 'ぶっこわ～す' in message.content:
            await message.channel.send('ぶっ壊す？今からお前んち焼きにいくわ')
            return

        
        if 'クソ' in message.content or 'くそ' in message.content or '糞' in message.content or 'poop' in message.content or 'うんち' in message.content or 'うんこ' in message.content or 'んんこ' in message.content or 'ウンチ' in message.content or 'ゆゆうた' in message.content or 'ウンコ' in message.content or '💩' in message.content:
            await message.channel.send("（っ’-‘)╮ =͟͟͞:poop:ﾌﾞｫﾝ")
        
        if 'ｸｿ' in message.content or 'ぅんち' in message.content or 'ぅんこ' in message.content or 'ｳﾝﾁ' in message.content or 'ｳﾝｺ' in message.content or 'うンこ' in message.content or 'ウんこ'  in message.content or 'ウんち' in message.content or 'Poop' in message.content or 'POOP' in message.content or '唐沢貴洋' in message.content:
            await message.channel.send("（っ’-‘)╮ =͟͟͞:poop:ﾌﾞｫﾝ")
        
        if 'うるせ' in message.content or 'うるさい' in message.content or '黙れ' in message.content or 'だまれ' in message.content:
            await message.channel.send("お前のほうがうるさい！")
            return
        if 'ェーン' in message.content:
            await message.channel.send('やーい泣き虫！')
            return
        if 'F***' in message.content or 'f***' in message.content or 'FUCK' in message.content or 'fuck' in message.content or 'Fuck' in message.content:
            await message.channel.send('Fuck you motherfucker!')
            return
        if 'F**k' in message.content or 'F**K' in message.content or 'f**k' in message.content or 'fuc*' in message.content or 'Fuc*' in message.content:
            await message.channel.send('Fuck you!')
            return
        if '倒すぞ' in message.content or '殺すぞ' in message.content:
            await message.channel.send('負ける気がしまへんがな')
            return
        if '喧嘩売って' in message.content or 'けんか売って' in message.content or 'けんかうって' in message.content:
            await message.channel.send('やんのかゴラァ')
            return
        if 'ゴラァ' in message.content or 'ゴルァ' in message.content:
            await message.channel.send('あ？負ける気しないぞ？おい？かかってこいや')
            return
        if ('暇' in message.content or 'ヒマ' in message.content or 'ひま' in message.content)and not ('ない' in message.content or 'ません' in message.content):
            await message.channel.send('勉強したらどうだ？')
            return
        if 'Botに死はない' in message.content or '不死身のBot' in message.content:
            await message.channel.send('（正論）')
            return
        if 'そうだよ' in message.content or 'そーだよ' in message.content:
            await message.channel.send('ソーダよ（瓶状）')
            return
        if 'うっき' in message.content or 'うきゃ' in message.content or 'ウッキ' in message.content or 'ウキャ' in message.content or 'ウキー' in message.content or 'うきー' in message.content:
            await message.channel.send('しねサル')
            return
        if 'ｲｷｷｲｲｲｲ' in message.content or 'ﾋﾞﾊﾞﾋﾊｧｲｸｩ' in message.content:
            await message.channel.send('ｲｷｷｲｲｲｲｲｲｲwwwwｲｯﾋﾋﾋﾋﾋﾊﾊﾞﾋﾞﾊﾞﾋﾊｧｲｸｩ!!!!wwwwwwww')
            return
        if 'ひえん' in message.content or 'ヒエン' in message.content:
            await message.channel.send(':hot_face:')
            return
        if '喘ぐな気持ち悪い' in message.content:
            await message.channel.send('俺のセリフ真似してんじゃねぇよゴルァ')
            return
        if '草' in message.content and '余談' not in message.content and 'めんど'not in message.content and 'たくさん'not in message.content or 'くさ' in message.content and '余談' not in message.content and 'めんど'not in message.content and 'たくさん'not in message.content or 'ｸｯｻ' in message.content and '余談' not in message.content and 'めんど'not in message.content and 'たくさん'not in message.content or 'kusa' in message.content and '余談' not in message.content and 'めんど'not in message.content and 'たくさん'not in message.content or 'ｸｻ' in message.content and '余談' not in message.content and 'めんど'not in message.content and 'たくさん'not in message.content:
            await message.channel.send('~~ 草 ~~ \n余談ですが草を生やしたように面白うございますので草を生やさせていただきます候')
            return
        if '勉強' in message.content:
            await message.channel.send('勉強？！俺、大っ嫌い！！')
            return
        if 'おやすみ' in message.content or '寝る' in message.content or '寝ます' in message.content:
            num = random.randint(0, 2)
            if num == 0:
                await message.channel.send('おやすみぃ！おねしょすんなよ？')
            elif num == 1:
                await message.channel.send('ナニィ？お化けが怖くて寝れないのか？')
            else:
                await message.channel.send('まだだ。まだ甘い。寝てはいけない。')
            return
        





        
        if message.content == "thinkpad" or message.content == "Thinkpad" or message.content == "ThinkPad" or message.content == "thinkPad":
            pad = random.randint(0, 2)
            if pad == 0:
                await message.channel.send(file=discord.File('pic/think.png'))
            elif pad == 1:
                await message.channel.send(file=discord.File('pic/thick.png'))
            else:
                await message.channel.send(file=discord.File('pic/thin.png'))
        if message.content == "PentiumIII" or message.content == "pentium3" or message.content == "pentiumIII" or message.content == "pen3" or message.content == "Pentium3":
            await message.channel.send(file=discord.File('pic/katmai.png'))
        if message.content == "よし" or message.content == "ヨシ" or message.content == "よし！" or message.content == "ヨシ！" or message.content == "よしっ" or message.content == "ヨシッ":
            await message.channel.send(file=discord.File('pic/yoshi.jpg'))
        if message.content == "1+1=" or message.content == "1+1" or message.content == "１＋１" or message.content == "１＋１＝" or message.content == "１+１=":
            pad = random.randint(0, 2)
            if pad == 0:
                await message.channel.send(file=discord.File('pic/win.png'))
            elif pad == 1:
                await message.channel.send(file=discord.File('pic/tanbo1.jpg'))
            else:
                await message.channel.send('２に決まってんだろ！botをなめてんのか？（マジレス）')
    #if "さなだむし"  in message.content or "サナダムシ" in message.content:
     #   await message.channel.send(file=discord.File('pic/sanada.png'))    

##################################################################################
        if '1000円' in message.content or '1k' in message.content:
            await message.channel.send(file=discord.File('pic/bird/illuminatiparrot.gif'))
            return
        if 'bird' in message.content or '鳥' in message.content or 'TINTIN' in message.content.upper() or 'OPPAI' in message.content.upper() or 'ちんちん' in message.content or 'おっぱい' in message.content or 'とり' in message.content or 'トリ' in message.content or '🐦' in message.content or '🦢' in message.content or '🐓' in message.content or '🐤' in message.content or '🐣' in message.content or '🐥' in message.content or '🦆' in message.content or '🦅' in message.content or '🦉' in message.content or '🐔' in message.content or '🐧' in message.content or '🦇' in message.content:
            
            s = message.content.upper()
            bird00=(s.count('鳥'))
            bird01=(s.count('とり'))
            bird02=(s.count('トリ'))
            bird03=(s.count('BIRD'))
            bird04=(s.count('TINTIN'))
            bird05=(s.count('OPPAI'))
            bird06=(s.count('ちんちん'))
            bird07=(s.count('おっぱい'))
            bird08=(s.count('🐦'))
            bird09=(s.count('🦢'))
            bird10=(s.count('🐓'))

            bird11=(s.count('🐤'))
            bird12=(s.count('🐣'))
            bird13=(s.count('🐥'))
            bird14=(s.count('🦆'))
            bird15=(s.count('🦅'))
            bird16=(s.count('🦉'))
            bird17=(s.count('🐔'))
            bird18=(s.count('🐧'))
            bird19=(s.count('🦇'))



            birdcount=(bird00+bird01+bird02+bird03+bird04+bird05+bird06+bird07+bird08+bird09+bird10+bird11+bird12+bird13+bird14+bird15+bird16+bird17+bird18+bird19)


            if birdcount > 5:
                birdcount = 5

            for i in range(birdcount):

                numb = random.randint(0, 19)
                birdfile = 'pic/bird/%s.gif'% (numb)
                await message.channel.send(file=discord.File(birdfile))
    
##################################################################################

        
        if message.content == "あ":
            await message.channel.send('い\nう\nえ\nお')
        if message.content == "しねかぶった":
            await message.channel.send('ころす')
        if message.content == "デジャヴ":
            await message.channel.send('ここまでがテンプレ')
    
# === ここからコマンド ===
        



    







    if message.content.startswith('$'):


        if 'NEHALEM' in message.content.upper():
            if 'I7' in message.content.upper():      
                await message.channel.send('860-SLBJJ(LGA1156,4c8t,2.8-3.46GHz) \n860S-SLBLG(LGA1156,4c4\8t,2.53-3.46GHz) \n870-SLBJG(LGA1156,4c8t,2.93-3.6GHz) \n870S-SLBQ7(LGA1156,4c8t,2.66-3.6GHz)\n875K-SLBS2(LGA1156,4c8t,2.93-3.6GHz)\n880-SLBPS(LGA1156,4c8t,3.06-3.73GHz)\n920-SLBCH/SLBEJ(LGA1366,4c8t,2.66-2.93GHz)\n930-SLBKP(LGA1366,4c8t,2.7-3.06GHz)\n940-SLBCK(LGA1366,4c8t,2.93-3.2GHz)\n950-SLBEN(LGA1366,4c8t,3.06-3.33GHz)\n960-SLBEU(LGA1366,4c8t,3.2-3.46GHz)')
            elif 'I5' in message.content.upper():      
                await message.channel.send('760-SLBRP(LGA1156,4c4t,2.8-3.33GHz) \n750-SLBLC(LGA1156,4c4t,2.66-3.2GHz) \n750S-SLBLH(LGA1156,4c4t,2.4-3.2GHz)')
            elif 'I3' in message.content.upper():      
                await message.channel.send('560-SLBY2(LGA1156,2c4t,3.33GHz) \n550-SLBUD(LGA1156,2c4t,3.2GHz) \n540-SLBTD(LGA1156,2c4t,3.06GHz) \n530-SLBX7(LGA1156,2c4t,2.93GHz)')
            elif 'PENTIUM' in message.content.upper():      
                await message.channel.send('未実装です。')
            elif 'CELERON' in message.content.upper():      
                await message.channel.send('未実装です。')
            else:
                pass
                #全て表示

            
            return








        if 'tanium' in message.content and '733' in message.content or 'SL4LT' in message.content or 'SL5VS' in message.content or 'SL4LS' in message.content or 'SL5VT' in message.content:
            await message.channel.send('名称:Itanium 733MHz   \nマイクロアーキテクチャ:Itanium \nソケット名:PAC418  \nコア数/スレッド数:1/1  \nベース:733MHz')
            return
        if 'tanium' in message.content and '800' in message.content or 'SL4LR' in message.content or 'SL5VU' in message.content or 'SL4LQ' in message.content or 'SL5VW' in message.content:
            await message.channel.send('名称:Itanium 800MHz   \nマイクロアーキテクチャ:Itanium \nソケット名:PAC418  \nコア数/スレッド数:1/1  \nベース:800MHz')
            return
        

        
        if '.' in message.content:
            if '860.' in message.content or 'SLBJJ' in message.content.upper():
                await message.channel.send('名称:Core i7-860   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1156  \nコア数/スレッド数:4/8  \nベース:2.8GHz\nTB時:3.46GHz')
                return
            if '860S.' in message.content.upper() or 'SLBLG' in message.content.upper():
                await message.channel.send('名称:Core i7-860S   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1156  \nコア数/スレッド数:4/8  \nベース:2.53GHz\nTB時:3.46GHz')
                return
            if '870.' in message.content or 'SLBJG' in message.content.upper():
                await message.channel.send('名称:Core i7-870   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1156  \nコア数/スレッド数:4/8  \nベース:2.93GHz\nTB時:3.6GHz')
                return
            if '870S.' in message.content.upper() or 'SLBQ7' in message.content.upper():
                await message.channel.send('名称:Core i7-870S   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1156  \nコア数/スレッド数:4/8  \nベース:2.66GHz\nTB時:3.6GHz')
                return
            if '875K.' in message.content.upper() or 'SLBS2' in message.content.upper():
                await message.channel.send('名称:Core i7-875K   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1156  \nコア数/スレッド数:4/8  \nベース:2.93GHz\nTB時:3.6GHz')
                return
            if '880.' in message.content or 'SLBPS' in message.content.upper():
                await message.channel.send('名称:Core i7-880   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1156  \nコア数/スレッド数:4/8  \nベース:3.06GHz\nTB時:3.73GHz')
                return



            if '920.' in message.content or 'SLBCH' in message.content.upper() or 'SLBEJ' in message.content.upper():
                await message.channel.send('名称:Core i7-920   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1366  \nコア数/スレッド数:4/8  \nベース:2.66GHz\nTB時:2.93GHz')
                return
            if '930.' in message.content or 'SLBKP' in message.content.upper():
                await message.channel.send('名称:Core i7-930   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1366  \nコア数/スレッド数:4/8  \nベース:2.7GHz\nTB時:3.06GHz')
                return
            if '940.' in message.content or 'SLBCK' in message.content.upper():
                await message.channel.send('名称:Core i7-940   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1366  \nコア数/スレッド数:4/8  \nベース:2.93GHz\nTB時:3.2GHz')
                return
            if '950.' in message.content or 'SLBEN' in message.content.upper():
                await message.channel.send('名称:Core i7-950   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1366  \nコア数/スレッド数:4/8  \nベース:3.06GHz\nTB時:3.33GHz')
                return
            if '960.' in message.content or 'SLBEU' in message.content.upper():
                await message.channel.send('名称:Core i7-960   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1366  \nコア数/スレッド数:4/8  \nベース:3.2GHz\nTB時:3.46GHz')
                return
            if '970.' in message.content or 'SLBVF' in message.content.upper():
                await message.channel.send('名称:Core i7-970   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1366  \nコア数/スレッド数:6/12  \nベース:3.2GHz\nTB時:3.46GHz')
                return
            if '980.' in message.content or 'SLBEU' in message.content.upper():
                await message.channel.send('名称:Core i7-980   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1366  \nコア数/スレッド数:6/12  \nベース:3.33GHz\nTB時:3.6GHz')
                return
            if '980X.' in message.content.upper() or 'SLBUZ' in message.content.upper():
                await message.channel.send('名称:Core i7-980X   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1366  \nコア数/スレッド数:6/12  \nベース:3.33GHz\nTB時:3.6GHz')
                return
            if '990X.' in message.content.upper() or 'SLBVZ' in message.content.upper():
                await message.channel.send('名称:Core i7-990X   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1366  \nコア数/スレッド数:6/12  \nベース:3.46GHz\nTB時:3.73GHz')
                return
            if '965.' in message.content or 'SLBCJ' in message.content.upper():
                await message.channel.send('名称:Core i7-965   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1366  \nコア数/スレッド数:4/8  \nベース:3.2GHz\nTB時:3.46GHz')
                return
            if '975.' in message.content or 'SLBEQ' in message.content.upper():
                await message.channel.send('名称:Core i7-975   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1366  \nコア数/スレッド数:4/8  \nベース:3.33GHz\nTB時:3.6GHz')
                return





            
            if '2600.' in message.content or 'SR00B' in message.content.upper():
                await message.channel.send('名称:Core i7-2600   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/8  \nベース:3.4GHz\nTB時:3.8GHz')
                return
            if '2600K.' in message.content.upper() or 'SR00C' in message.content.upper():
                await message.channel.send('名称:Core i7-2600K   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/8  \nベース:3.4GHz\nTB時:3.8GHz')
                return
            if '2600S.' in message.content.upper() or 'SR00E' in message.content.upper():
                await message.channel.send('名称:Core i7-2600S   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/8  \nベース:2.8GHz\nTB時:3.8GHz')
                return
            if '2700K.' in message.content.upper() or 'SR0DG' in message.content.upper():
                await message.channel.send('名称:Core i7-2700K   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/8  \nベース:3.5GHz\nTB時:3.9GHz')
                return
            if '3820.' in message.content or 'SR0LD' in message.content.upper():
                await message.channel.send('名称:Core i7-3820   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA2011  \nコア数/スレッド数:4/8  \nベース:3.6GHz\nTB時:3.8GHz')
                return
            if '3770.' in message.content or 'SR0PK' in message.content.upper():
                await message.channel.send('名称:Core i7-3770   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/8  \nベース:3.4GHz\nTB時:3.9GHz')
                return
            if '3770K.' in message.content.upper() or 'SR0PL' in message.content.upper():
                await message.channel.send('名称:Core i7-3770K   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/8  \nベース:3.5GHz\nTB時:3.9GHz')
                return
            if '3770S.' in message.content.upper() or 'SR0PN' in message.content.upper():
                await message.channel.send('名称:Core i7-3770S   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/8  \nベース:3.1GHz\nTB時:3.9GHz')
                return
            if '3770T.' in message.content.upper() or 'SR0PQ' in message.content.upper():
                await message.channel.send('名称:Core i7-3770T   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/8  \nベース:2.5GHz\nTB時:3.7GHz')
                return
            if '3930K.' in message.content.upper() or 'SR0H9' in message.content.upper() or 'SR0KY' in message.content.upper():
                await message.channel.send('名称:Core i7-3930K   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA2011  \nコア数/スレッド数:4/8  \nベース:3.2GHz\nTB時:3.8GHz')
                return
            if '3960X.' in message.content.upper() or 'SR0KF' in message.content.upper() or 'SR0KY' in message.content.upper():
                await message.channel.send('名称:Core i7-3960X   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA2011  \nコア数/スレッド数:6/12  \nベース:3.3GHz\nTB時:3.9GHz')
                return
            if '3970X.' in message.content.upper() or 'SR0WR' in message.content.upper() or 'SR0KY' in message.content.upper():
                await message.channel.send('名称:Core i7-3970X   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA2011  \nコア数/スレッド数:6/12  \nベース:3.5GHz\nTB時:4GHz')
                return


            if '4765T.' in message.content.upper() or 'SR14Q' in message.content.upper():
                await message.channel.send('名称:i7-4765T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:2GHz\nTB時:3GHz')
                return
            if '4770.' in message.content.upper() or 'SR149' in message.content.upper():
                await message.channel.send('名称:i7-4770   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:3.4GHz\nTB時:3.9GHz')
                return
            if '4770K.' in message.content.upper() or 'SR147' in message.content.upper():
                await message.channel.send('名称:i7-4770K   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:3.5GHz\nTB時:3.9GHz')
                return
            if '4770R.' in message.content.upper() or 'SR18K' in message.content.upper():
                await message.channel.send('名称:i7-4770R   \nマイクロアーキテクチャ:Haswell \nソケット名:BGA1364  \nコア数/スレッド数:4/8  \nベース:3.2GHz\nTB時:3.9GHz')
                return
            if '4770S.' in message.content.upper() or 'SR14H' in message.content.upper():
                await message.channel.send('名称:i7-4770S   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:3.1GHz\nTB時:3.9GHz')
                return
            if '4770T.' in message.content.upper() or 'SR14N' in message.content.upper():
                await message.channel.send('名称:i7-4770T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:2.5GHz\nTB時:3.7GHz')
                return
            if '4770TE.' in message.content.upper() or 'SR183' in message.content.upper():
                await message.channel.send('名称:i7-4770TE   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:2.3GHz\nTB時:3.3GHz')
                return
            if '4771.' in message.content.upper() or 'SR1BW' in message.content.upper():
                await message.channel.send('名称:i7-4771   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:3.5GHz\nTB時:3.9GHz')
                return
            if '4785T.' in message.content.upper() or 'SR1QU' in message.content.upper():
                await message.channel.send('名称: i7-4785T  \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:2.2GHz\nTB時:3.2GHz')
                return
            if '4790.' in message.content.upper() or 'SR1QF' in message.content.upper():
                await message.channel.send('名称:i7-4790   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:3.6GHz\nTB時:4GHz')
                return
            if '4790K.' in message.content.upper() or 'SR219' in message.content.upper():
                await message.channel.send('名称:i7-4790K   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:4GHz\nTB時:4.4GHz')
                return
            if '4790S.' in message.content.upper() or 'SR1QM' in message.content.upper():
                await message.channel.send('名称:i7-4790S   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:3.2GHz\nTB時:4GHz')
                return
            if '4790T.' in message.content.upper() or 'SR1QS' in message.content.upper():
                await message.channel.send('名称:i7-4790T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:2.7GHz\nTB時:3.9GHz')
                return
            if '4820K.' in message.content.upper() or 'SR1AU' in message.content.upper():
                await message.channel.send('名称:i7-4820K   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA2011  \nコア数/スレッド数:4/8  \nベース:3.7GHz\nTB時:3.9GHz')
                return
            if '4930K.' in message.content.upper() or 'SR1AT' in message.content.upper():
                await message.channel.send('名称:i7-4930K   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA2011  \nコア数/スレッド数:6/12  \nベース:3.4GHz\nTB時:3.9GHz')
                return
            if '4960X.' in message.content.upper() or 'SR1AS' in message.content.upper():
                await message.channel.send('名称:i7-4960X   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA2011  \nコア数/スレッド数:6/12  \nベース:3.6GHz\nTB時:4GHz')
                return

    
            if '5775C.' in message.content.upper() or 'SR2AG' in message.content.upper():
                await message.channel.send('名称:i7-5775C   \nマイクロアーキテクチャ:Broadwell \nソケット名:LGA1150  \nコア数/スレッド数:4/8  \nベース:3.3GHz\nTB時:3.7GHz')
                return
            if '5775R.' in message.content.upper() or 'SR2AL' in message.content.upper():
                await message.channel.send('名称:i7-5775R   \nマイクロアーキテクチャ:Broadwell \nソケット名:BGA1364  \nコア数/スレッド数:4/8  \nベース:3.7GHz\nTB時:3.8GHz')
                return
            if '5820K.' in message.content.upper() or 'SR20S' in message.content.upper():
                await message.channel.send('名称:i7-5820K   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA2011-3  \nコア数/スレッド数:6/12  \nベース:3.3GHz\nTB時:3.6GHz')
                return
            if '5930K.' in message.content.upper() or 'SR20R' in message.content.upper():
                await message.channel.send('名称:i7-5930K   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA2011-3  \nコア数/スレッド数:6/12  \nベース:3.5GHz\nTB時:3.7GHz')
                return
            if '5760X.' in message.content.upper() or 'SR20Q' in message.content.upper():
                await message.channel.send('名称:i7-5760X   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA2011-3  \nコア数/スレッド数:8/16  \nベース:3GHz\nTB時:3.5GHz')
                return


            if '6700.' in message.content.upper() or 'SR2L2' in message.content.upper() or 'SR2BT' in message.content.upper():
                await message.channel.send('名称:i7-6700   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/8  \nベース:3.4GHz\nTB時:4GHz')
                return
            if '6700K.' in message.content.upper() or 'SR2BR' in message.content.upper() or 'SR2L0' in message.content.upper():
                await message.channel.send('名称:i7-6700K  \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/8  \nベース:4GHz\nTB時:4.2GHz')
                return
            if '6700T.' in message.content.upper() or 'SL2BU' in message.content.upper() or 'SR2L3' in message.content.upper():
                await message.channel.send('名称:i7-6700T   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/8  \nベース:2.8GHz\nTB時:3.6GHz')
                return
            if '6700TE.' in message.content.upper() or 'SR2LP' in message.content.upper():
                await message.channel.send('名称:i7-6700TE   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/8  \nベース:2.4GHz\nTB時:3.4GHz')
                return
            if '6785R.' in message.content.upper() or 'SR2U0' in message.content.upper():
                await message.channel.send('名称:i7-6785R   \nマイクロアーキテクチャ:Skylake \nソケット名:BGA1440  \nコア数/スレッド数:4/8  \nベース:3.3GHz\nTB時:3.9GHz')
                return
            if '6800K.' in message.content.upper() or 'SR2PD' in message.content.upper():
                await message.channel.send('名称:i7-6800K   \nマイクロアーキテクチャ:Broadwell \nソケット名:LGA2011-3  \nコア数/スレッド数:6/12  \nベース:3.4GHz\nTB時:3.6GHz')
                return
            if '6850K.' in message.content.upper() or 'SR2PC' in message.content.upper():
                await message.channel.send('名称:i7-6850K   \nマイクロアーキテクチャ:Broadwell \nソケット名:LGA2011-3  \nコア数/スレッド数:6/12  \nベース:3.6GHz\nTB時:3.8GHz')
                return
            if '6900K.' in message.content.upper() or 'SR2PB' in message.content.upper():
                await message.channel.send('名称:i7-6900K   \nマイクロアーキテクチャ:Broadwell \nソケット名:LGA2011-3  \nコア数/スレッド数:8/16  \nベース:3.2GHz\nTB時:3.7GHz')
                return
            if '6950X.' in message.content.upper() or 'SR2PA' in message.content.upper():
                await message.channel.send('名称:i7-6950X   \nマイクロアーキテクチャ:Broadwell \nソケット名:LGA2011-3  \nコア数/スレッド数:10/20  \nベース:3GHz\nTB時:4GHz')
                return


            if '7700.' in message.content.upper() or 'SR338' in message.content.upper():
                await message.channel.send('名称:i7-7700   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:4/8  \nベース:G3.6Hz\nTB時:4.2GHz')
                return
            if '7700K.' in message.content.upper() or 'SR33A' in message.content.upper():
                await message.channel.send('名称:i7-7700K   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:4/8  \nベース:4.2GHz\nTB時:4.GHz')
                return
            if '7700T.' in message.content.upper() or 'SR339' in message.content.upper():
                await message.channel.send('名称:i7-7700T   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:4/8  \nベース:2.9GHz\nTB時:3.8GHz')
                return
            if '7740X.' in message.content.upper() or 'SR3FP' in message.content.upper():
                await message.channel.send('名称:i7-7740X   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA2066  \nコア数/スレッド数:4/8  \nベース:4.3GHz\nTB時:4.5GHz')
                return
            if '7800X.' in message.content.upper() or 'SR3L4' in message.content.upper():
                await message.channel.send('名称:i7-7800X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:6/12  \nベース:3.5GHz\nTB時:4GHz')
                return
            if '7820X.' in message.content.upper() or 'SR3L5' in message.content.upper():
                await message.channel.send('名称:i7-7820X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数8/16:  \nベース:3.6GHz\nTB時:4.3GHz')
                return

            
            if '8700K.' in message.content.upper() or 'SR3QR' in message.content.upper():
                await message.channel.send('名称:i7-8700K   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/12  \nベース:3.7GHz\nTB時:4.7GHz')
                return
            if '8700.' in message.content.upper() or 'SR3QS' in message.content.upper():
                await message.channel.send('名称:i7-8700   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/12  \nベース:3.2GHz\nTB時:4.6GHz')
                return
            if '8700T.' in message.content.upper() or 'SR3WX' in message.content.upper():
                await message.channel.send('名称:i7-8700T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/12  \nベース:2.4GHz\nTB時:4GHz')
                return
            if '8086K.' in message.content.upper() or 'SRCX5' in message.content.upper():
                await message.channel.send('名称:i7-8086K   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/12  \nベース:4GHz\nTB時:5GHz')
                return

            
            if '9700.' in message.content.upper() or 'SRG13' in message.content.upper():
                await message.channel.send('名称:i7-9700   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/8  \nベース:3GHz\nTB時:4.7GHz')
                return
            if '9700E.' in message.content.upper() or 'SRGDX' in message.content.upper():
                await message.channel.send('名称:i7-9700E   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/8  \nベース:2.6GHz\nTB時:4.4GHz')
                return
            if '9700F.' in message.content.upper() or 'SRG14' in message.content.upper():
                await message.channel.send('名称:i7-9700F   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/8  \nベース:3GHz\nTB時:4.7GHz')
                return
            if '9700KF.' in message.content.upper() or 'SRFAC' in message.content.upper() or 'SRG16' in message.content.upper():
                await message.channel.send('名称:i7-9700KF   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/8  \nベース:3.6GHz\nTB時:4.9GHz')
                return
            if '9700K.' in message.content.upper() or 'SRELT' in message.content.upper() or 'SRG15' in message.content.upper():
                await message.channel.send('名称:i7-9700K   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/8  \nベース:3.6GHz\nTB時:4.9GHz')
                return
            if '9700T.' in message.content.upper() or 'SRG17' in message.content :
                await message.channel.send('名称:i7-9700T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/8  \nベース:2GHz\nTB時:4.3GHz')
                return
            if '9700TE.' in message.content.upper() or 'SRGE3' in message.content:
                await message.channel.send('名称:i7-9700TE   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/8  \nベース:1.8GHz\nTB時:3.8GHz')
                return
            if '9800X.' in message.content.upper() or 'SREZ9' in message.content:
                await message.channel.send('名称:i7-9800X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:8/16  \nベース:3.8GHz\nTB時:4.4GHz')
                return


            if '10700.' in message.content.upper() or 'unknown' in message.content:
                await message.channel.send('名称:i7-10700   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:8/16  \nベース:2.9GHz\nTB時:4.8GHz')
                return
            if '10700E.' in message.content.upper() or 'unknown' in message.content:
                await message.channel.send('名称:i7-10700E   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:8/16  \nベース:2.9GHz\nTB時:4.5GHz')
                return
            if '10700F.' in message.content.upper() or 'unknown' in message.content:
                await message.channel.send('名称:i7-10700F   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:8/16  \nベース:2.9GHz\nTB時:4.8GHz')
                return
            if '10700K.' in message.content.upper() or 'unknown' in message.content:
                await message.channel.send('名称:i7-10700K   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:8/16  \nベース:3.8GHz\nTB時:5.1GHz')
                return
            if '10700KF.' in message.content.upper() or 'unknown' in message.content:
                await message.channel.send('名称:i7-10700KF   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:8/16  \nベース:3.8GHz\nTB時:5.1GHz')
                return
            if '10700T.' in message.content.upper() or 'unknown' in message.content:
                await message.channel.send('名称:i7-10700T   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:8/16  \nベース:2GHz\nTB時:4.5GHz')
                return
            if '10700TE.' in message.content.upper() or 'unknown' in message.content:
                await message.channel.send('名称:i7-10700TE   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:8/16  \nベース:2GHz\nTB時:4.4GHz')
                return
###########ここからi5です#############


            if 'i5' in message.content and '760.' in message.content or 'SLBRP' in message.content:
                await message.channel.send('名称:Core i5-760   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1156  \nコア数/スレッド数:4/4  \nベース:2.8GHz\nTB時:3.33GHz') 
                return
            if 'i5' in message.content and '750.' in message.content or 'SLBLC' in message.content:
                await message.channel.send('名称:Core i5-750   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1156  \nコア数/スレッド数:4/4  \nベース:2.66GHz\nTB時:3.2GHz') 
                return
            if 'i5' in message.content and '750S.' in message.content or 'SLBLH' in message.content:
                await message.channel.send('名称:Core i5-750S   \nマイクロアーキテクチャ:Nehalem \nソケット名:LGA1156  \nコア数/スレッド数:4/4  \nベース:2.4GHz\nTB時:3.2GHz') 
                return
            if 'i5' in message.content and '680.' in message.content or 'SLBTM' in message.content:
                await message.channel.send('名称:Core i5-680   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1156  \nコア数/スレッド数:2/4  \nベース:3.6GHz\nTB時:3.86GHz') 
                return
            if 'i5' in message.content and'670.' in message.content or 'SLBLT' in message.content or 'SLBTL' in message.content:
                await message.channel.send('名称:Core i5-670   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1156  \nコア数/スレッド数:2/4  \nベース:3.46GHz\nTB時:3.73GHz') 
                return
            if 'i5' in message.content and'661.' in message.content or 'SLBNE' in message.content or 'SLBTB' in message.content:
                await message.channel.send('名称:Core i5-661   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1156  \nコア数/スレッド数:2/4  \nベース:3.33GHz\nTB時:3.6GHz') 
                return
            if 'i5' in message.content and'660.' in message.content or 'SLBLV' in message.content or 'SLBTK' in message.content:
                await message.channel.send('名称:Core i5-660   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1156  \nコア数/スレッド数:2/4  \nベース:3.33GHz\nTB時:3.6GHz') 
                return
            if 'i5' in message.content and'670.' in message.content or 'SLBLT' in message.content or 'SLBTL' in message.content:
                await message.channel.send('名称:Core i5-670   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1156  \nコア数/スレッド数:2/4  \nベース:3.46GHz\nTB時:3.73GHz') 
                return
            if 'i5' in message.content and '655K.' in message.content or 'SLBXL' in message.content:
                await message.channel.send('名称:Core i5-655K   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1156  \nコア数/スレッド数:2/4  \nベース:3.2GHz\nTB時:3.46GHz')
                return
            if 'i5' in message.content and'650.' in message.content or 'SLBLK' in message.content or 'SLBTJ' in message.content:
                await message.channel.send('名称:Core i5-650   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1156  \nコア数/スレッド数:2/4  \nベース:3.2GHz\nTB時:3.46GHz') 
                return

            

            if 'i5' in message.content and '2550K.' in message.content or 'SR0QH' in message.content:
                await message.channel.send('名称:Core i5-2550K   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.4GHz\nTB時:3.8GHz') 
                return
            if 'i5' in message.content and '2500K.' in message.content or 'SR008' in message.content:
                await message.channel.send('名称:Core i5-2500K   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.3GHz\nTB時:3.7GHz') 
                return
            if 'i5' in message.content and '2500.' in message.content or 'SR00T' in message.content:
                await message.channel.send('名称:Core i5-2500   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.3GHz\nTB時:3.7GHz') 
                return
            if 'i5' in message.content and '2500S.' in message.content or 'SR009' in message.content:
                await message.channel.send('名称:Core i5-2500S   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.7GHz\nTB時:3.3GHz')
                return
            if 'i5' in message.content and '2500T.' in message.content or 'SR00A' in message.content:
                await message.channel.send('名称:Core i5-2500T   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.3GHz\nTB時:3.7GHz') 
                return
            if 'i5' in message.content and '2450P.' in message.content or 'SR0G1' in message.content:
                await message.channel.send('名称:Core i5-2450P   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.2GHz\nTB時:3.5GHz')  
                return
            if 'i5' in message.content and '2400.' in message.content or 'SR00Q' in message.content:
                await message.channel.send('名称:Core i5-2400   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.1GHz\nTB時:3.4GHz') 
                return
            if 'i5' in message.content and '2380P.' in message.content or 'SR0G2' in message.content:
                await message.channel.send('名称:Core i5-2380P   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.1GHz\nTB時:3.4GHz') 
                return
            if 'i5' in message.content and '2405S.' in message.content or 'SR0BB' in message.content:
                await message.channel.send('名称:Core i5-2405S   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.5GHz\nTB時:3.3GHz') 
                return
            if 'i5' in message.content and '2400S.' in message.content or 'SR00S' in message.content:
                await message.channel.send('名称:Core i5-2400S   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.5GHz\nTB時:3.3GHz') 
                return
            if 'i5' in message.content and '2320.' in message.content or 'SR02L' in message.content:
                await message.channel.send('名称:Core i5-2320   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.0GHz\nTB時:3.3GHz') 
                return
            if 'i5' in message.content and '2310.' in message.content or 'SR02K' in message.content:
                await message.channel.send('名称:Core i5-2310   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.9GHz\nTB時:3.2GHz') 
                return
            if 'i5' in message.content and '2300.' in message.content or 'SR00D' in message.content:
                await message.channel.send('名称:Core i5-2300   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.8GHz\nTB時:3.1GHz') 
                return
            if 'i5' in message.content and '2390T.' in message.content or 'SR065' in message.content:
                await message.channel.send('名称:Core i5-2390T   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:2.7GHz\nTB時:3.5GHz') 
                return





            if 'i5' in message.content and '3570K.' in message.content or 'SR0PM' in message.content:
                await message.channel.send('名称:Core i5-3570K   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.4GHz\nTB時:3.8GHz')
                return
            if 'i5' in message.content and '3570.' in message.content or 'SR0T7' in message.content:
                await message.channel.send('名称:Core i5-3570   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.4GHz\nTB時:3.8GHz')
                return
            if 'i5' in message.content and '3570S.' in message.content or 'SR0T9' in message.content:
                await message.channel.send('名称:Core i5-3570S   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.1GHz\nTB時:3.8GHz')
                return
            if 'i5' in message.content and '3570T.' in message.content or 'SR0P1' in message.content:
                await message.channel.send('名称:Core i5-3570T   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.3GHz\nTB時:3.3GHz')
                return
            if 'i5' in message.content and '3550.' in message.content or 'SR0P0' in message.content:
                await message.channel.send('名称:Core i5-3550   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.3GHz\nTB時:3.7GHz')
                return
            if 'i5' in message.content and '3550S.' in message.content or 'SR0T7' in message.content:
                await message.channel.send('名称:Core i5-3570   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.9GHz\nTB時:3.6GHz')
                return
            if 'i5' in message.content and '3475S.' in message.content or 'SR0PP' in message.content:
                await message.channel.send('名称:Core i5-3475S   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.9GHz\nTB時:3.6GHz')
                return
            if 'i5' in message.content and '3470.' in message.content or 'SR0T8' in message.content:
                await message.channel.send('名称:Core i5-3470   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.2GHz\nTB時:3.6GHz')
                return
            if 'i5' in message.content and '3470.' in message.content or 'SR0TA' in message.content:
                await message.channel.send('名称:Core i5-3470S   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.9GHz\nTB時:3.6GHz')
                return
            if 'i5' in message.content and '3470T.' in message.content or 'SR0RJ' in message.content:
                await message.channel.send('名称:Core i5-3570T   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:2.9GHz\nTB時:3.6GHz')
                return
            if 'i5' in message.content and '3450.' in message.content or 'SR0PE' in message.content:
                await message.channel.send('名称:Core i5-3450   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.1GHz\nTB時:3.5GHz')
                return
            if 'i5' in message.content and '3450S.' in message.content or 'SR0P2' in message.content:
                await message.channel.send('名称:Core i5-3450S   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.8GHz\nTB時:3.8GHz')
                return
            if 'i5' in message.content and '3350P.' in message.content or 'SR0WS' in message.content:
                await message.channel.send('名称:Core i5-3350P   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.1GHz\nTB時:3.3GHz')
                return
            if 'i5' in message.content and '3340.' in message.content or 'SR0T7' in message.content:
                await message.channel.send('名称:Core i5-3340   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.4GHz\nTB時:3.8GHz')
                return
            if 'i5' in message.content and '3340S.' in message.content or 'SR0YH' in message.content:
                await message.channel.send('名称:Core i5-3340S   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.8GHz\nTB時:3.3GHz')
                return
            if 'i5' in message.content and '3335S.' in message.content or 'SR0TJ' in message.content:
                await message.channel.send('名称:Core i5-3335S   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.7GHz\nTB時:3.2GHz')
                return
            if 'i5' in message.content and '3330S.' in message.content or 'SR0RR' in message.content:
                await message.channel.send('名称:Core i5-3330S   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:2.7GHz\nTB時:3.2GHz')
                return
            if 'i5' in message.content and '3330.' in message.content or 'SR0RQ' in message.content:
                await message.channel.send('名称:Core i5-3330   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:4/4  \nベース:3.0GHz\nTB時:3.2GHz')
                return



            if 'i5' in message.content and '5675C.' in message.content or 'SR2FX' in message.content:
                await message.channel.send('名称:Core i5-5675C   \nマイクロアーキテクチャ:Broadwell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.1GHz\nTB時:3.6GHz')
                return
            if 'i5' in message.content and '5675R.' in message.content or 'SR2AJ' in message.content:
                await message.channel.send('名称:Core i5-5675R   \nマイクロアーキテクチャ:Broadwell \nソケット名:BGA1364  \nコア数/スレッド数:4/4  \nベース:3.1GHz\nTB時:3.6GHz')  
                return
            if 'i5' in message.content and '5575R.' in message.content or 'SR2AK' in message.content:
                await message.channel.send('名称:Core i5-5575R   \nマイクロアーキテクチャ:Broadwell \nソケット名:BGA1364  \nコア数/スレッド数:4/4  \nベース:2.8GHz\nTB時:3.3GHz')
                return




            if 'i5' in message.content and '4690K.' in message.content or 'SR21A' in message.content:
                await message.channel.send('名称:Core i5-4690K   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.5GHz\nTB時:3.9GHz') 
                return
            if 'i5' in message.content and '4690.' in message.content or 'SR19H' in message.content:
                await message.channel.send('名称:Core i5-4690   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.5GHz\nTB時:3.9GHz') 
                return
            if 'i5' in message.content and '4690S.' in message.content or 'SR1QP' in message.content:
                await message.channel.send('名称:Core i5-4690S   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.2GHz\nTB時:3.9GHz') 
                return
            if 'i5' in message.content and '4690T.' in message.content or 'SR1QT' in message.content:
                await message.channel.send('名称:Core i5-4690T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:2.5GHz\nTB時:3.5GHz') 
                return
            if 'i5' in message.content and '4670K.' in message.content or 'SR14A' in message.content:
                await message.channel.send('名称:Core i5-4670K   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.4GHz\nTB時:3.8GHz') 
                return
            if 'i5' in message.content and '4670.' in message.content or 'SR14D' in message.content:
                await message.channel.send('名称:Core i5-4670   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.4GHz\nTB時:3.8GHz') 
                return
            if 'i5' in message.content and '4670S.' in message.content or 'SR14K' in message.content:
                await message.channel.send('名称:Core i5-4670S   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.4GHz\nTB時:3.8GHz') 
                return
            if 'i5' in message.content and '4670R.' in message.content or 'SR18M' in message.content:
                await message.channel.send('名称:Core i5-4670R   \nマイクロアーキテクチャ:Haswell \nソケット名:BGA1364  \nコア数/スレッド数:4/4  \nベース:3.0GHz\nTB時:3.7GHz') 
                return
            if 'i5' in message.content and '4670T.' in message.content or 'SR14P' in message.content:
                await message.channel.send('名称:Core i5-4670T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:2.3GHz\nTB時:3.3GHz') 
                return
            if 'i5' in message.content and '4590.' in message.content or 'SR1QJ' in message.content:
                await message.channel.send('名称:Core i5-4590   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.3GHz\nTB時:3.7GHz') 
                return
            if 'i5' in message.content and '4590S.' in message.content or 'SR1QN' in message.content:
                await message.channel.send('名称:Core i5-4590S   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.0GHz\nTB時:3.7GHz') 
                return
            if 'i5' in message.content and '4590T.' in message.content or 'SR1S6' in message.content:
                await message.channel.send('名称:Core i5-4590T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:2.0GHz\nTB時:3.0GHz')
                return
            if 'i5' in message.content and '4570.' in message.content or 'SR14E' in message.content:
                await message.channel.send('名称:Core i5-4570   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.4GHz\nTB時:3.8GHz') 
                return
            if 'i5' in message.content and '4570S.' in message.content or 'SR14J' in message.content:
                await message.channel.send('名称:Core i5-4570S   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:2.9GHz\nTB時:3.6GHz')  
                return
            if 'i5' in message.content and '4570R.' in message.content or 'SR18P' in message.content:
                await message.channel.send('名称:Core i5-4570R   \nマイクロアーキテクチャ:Haswell \nソケット名:BGA1364  \nコア数/スレッド数:4/4  \nベース:2.7GHz\nTB時:3.2GHz') 
                return
            if 'i5' in message.content and '4570T.' in message.content or 'SR1CA' in message.content:
                await message.channel.send('名称:Core i5-4570T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:2.9GHz\nTB時:3.6GHz') 
                return
            if 'i5' in message.content and '4570TE.' in message.content or 'SR17Z' in message.content:
                await message.channel.send('名称:Core i5-4570TE   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:2.7GHz\nTB時:3.3GHz') 
                return
            if 'i5' in message.content and '4460.' in message.content or 'SR1QK' in message.content:
                await message.channel.send('名称:Core i5-4460   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.2GHz\nTB時:3.4GHz')  
                return
            if 'i5' in message.content and '4460S.' in message.content or 'SR1QQ' in message.content:
                await message.channel.send('名称:Core i5-4460S   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:2.9GHz\nTB時:3.4GHz')  
                return
            if 'i5' in message.content and '4460T.' in message.content or 'SR1S7' in message.content:
                await message.channel.send('名称:Core i5-4460T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:1.9GHz\nTB時:2.7GHz')  
                return
            if 'i5' in message.content and '4440.' in message.content or 'SR14F' in message.content:
                await message.channel.send('名称:Core i5-4440   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.1GHz\nTB時:3.3GHz') 
                return
            if 'i5' in message.content and '4440S.' in message.content or 'SR14L' in message.content:
                await message.channel.send('名称:Core i5-4440S   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:2.8GHz\nTB時:3.3GHz')  
                return
            if 'i5' in message.content and '4430.' in message.content or 'SR14G' in message.content:
                await message.channel.send('名称:Core i5-4430   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:3.0GHz\nTB時:3.2GHz') 
                return
            if 'i5' in message.content and '4430S.' in message.content or 'SR14M' in message.content:
                await message.channel.send('名称:Core i5-4430S   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:4/4  \nベース:2.7GHz\nTB時:3.2GHz')
                return




            if 'i5' in message.content and '7640X.' in message.content or 'SR3FR' in message.content:
                await message.channel.send('名称:Core i5-7640X   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA2066  \nコア数/スレッド数:4/4  \nベース:4.0GHz\nTB時:4.2GHz') 
                return


            if 'i5' in message.content and '10600K.' in message.content or 'SRH6R' in message.content:
                await message.channel.send('名称:Core i5-10600K   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:6/12  \nベース:4.1GHz\nTB時:4.8GHz') 
                return
            if 'i5' in message.content and '10600KF.' in message.content or 'SRH6S' in message.content:
                await message.channel.send('名称:Core i5-10600KF   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:6/12  \nベース:4.1GHz\nTB時:4.8GHz') 
                return
            if 'i5' in message.content and '10600.' in message.content or 'SRH37' in message.content:
                await message.channel.send('名称:Core i5-10600   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:6/12  \nベース:3.3GHz\nTB時:4.8GHz') 
                return
            if 'i5' in message.content and '10600T.' in message.content or 'SRH39' in message.content:
                await message.channel.send('名称:Core i5-10600T   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:6/12  \nベース:2.4GHz\nTB時:4.0GHz') 
                return
            if 'i5' in message.content and '10500.' in message.content or 'SRH3A' in message.content:
                await message.channel.send('名称:Core i5-10500   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:6/12  \nベース:3.1GHz\nTB時:4.5GHz') 
                return
            if 'i5' in message.content and '10500T.' in message.content or 'SRH3B' in message.content:
                await message.channel.send('名称:Core i5-10500T   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:6/12  \nベース:2.3GHz\nTB時:3.8GHz') 
                return
            if 'i5' in message.content and '10400.' in message.content or 'SRH3C' in message.content:
                await message.channel.send('名称:Core i5-10400   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:6/12  \nベース:2.9GHz\nTB時:4.3GHz') 
                return
            if 'i5' in message.content and '10400F.' in message.content or 'SRH3D' in message.content:
                await message.channel.send('名称:Core i5-10400F   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:6/12  \nベース:2.9GHz\nTB時:4.3GHz') 
                return
            if 'i5' in message.content and '10400T.' in message.content or 'SRH3F' in message.content:
                await message.channel.send('名称:Core i5-10400T   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:6/12  \nベース:2.0GHz\nTB時:3.6GHz') 
                return

            if 'i5' in message.content and '9600K.' in message.content or 'SRELU' in message.content:
                await message.channel.send('名称:Core i5-9600K   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:3.7GHz\nTB時:4.6GHz') 
                return
            if 'i5' in message.content and '9600KF.' in message.content or 'SRFAD' in message.content:
                await message.channel.send('名称:Core i5-9600KF   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:3.7GHz\nTB時:4.6GHz') 
                return
            if 'i5' in message.content and '9600.' in message.content or 'SRF4H' in message.content:
                await message.channel.send('名称:Core i5-9600   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:3.1GHz\nTB時:4.6GHz') 
                return
            if 'i5' in message.content and '9600T.' in message.content or 'SRF4F' in message.content:
                await message.channel.send('名称:Core i5-9600T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:2.3GHz\nTB時:3.9GHz') 
                return
            if 'i5' in message.content and '9500.' in message.content or 'SRF4B' in message.content:
                await message.channel.send('名称:Core i5-9500   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:3.7GHz\nTB時:4.6GHz') 
                return
            if 'i5' in message.content and '9500F.' in message.content or 'SRF6Q' in message.content:
                await message.channel.send('名称:Core i5-9500F   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:3.0GHz\nTB時:4.4GHz') 
                return
            if 'i5' in message.content and '9500T.' in message.content or 'SRF4D' in message.content:
                await message.channel.send('名称:Core i5-9500T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:2.2GHz\nTB時:3.7GHz') 
                return
            if 'i5' in message.content and '9500TE.' in message.content or 'SRF4B' in message.content:
                await message.channel.send('名称:Core i5-9500TE   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:2.2GHz\nTB時:3.6GHz') 
                return
            if 'i5' in message.content and '9400.' in message.content or 'SR3X5' in message.content:
                await message.channel.send('名称:Core i5-9400   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:2.9GHz\nTB時:4.1GHz') 
                return
            if 'i5' in message.content and '9400F.' in message.content or 'SRF6M' in message.content:
                await message.channel.send('名称:Core i5-9400F   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:2.9GHz\nTB時:4.1GHz') 
                return
            if 'i5' in message.content and '9400T.' in message.content or 'SR3X8' in message.content:
                await message.channel.send('名称:Core i5-9400T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:1.8GHz\nTB時:3.4GHz') 
                return

            if 'i5' in message.content and '8600K.' in message.content or 'SR3QU' in message.content:
                await message.channel.send('名称:Core i5-8600K   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:3.6GHz\nTB時:4.3GHz') 
                return
            if 'i5' in message.content and '8600.' in message.content or 'SR3X0' in message.content:
                await message.channel.send('名称:Core i5-8600   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:3.1GHz\nTB時:4.3GHz') 
                return
            if 'i5' in message.content and '8600T.' in message.content or 'SR3X3' in message.content:
                await message.channel.send('名称:Core i5-8600T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:2.3GHz\nTB時:3.7GHz') 
                return
            if 'i5' in message.content and '8500.' in message.content or 'SR3XE' in message.content:
                await message.channel.send('名称:Core i5-8500   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:3.0GHz\nTB時:4.1GHz') 
                return
            if 'i5' in message.content and '8500T.' in message.content or 'SR3XD' in message.content:
                await message.channel.send('名称:Core i5-8500T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:2.1GHz\nTB時:3.5GHz') 
                return
            if 'i5' in message.content and '8400.' in message.content or 'SR3QT' in message.content:
                await message.channel.send('名称:Core i5-8400   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:2.8GHz\nTB時:4.0GHz') 
                return
            if 'i5' in message.content and '8400T.' in message.content or 'SR3X6' in message.content:
                await message.channel.send('名称:Core i5-8400T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:6/6  \nベース:1.7GHz\nTB時:3.3GHz') 
                return

            if 'i5' in message.content and '7600K.' in message.content or 'SR32V' in message.content:
                await message.channel.send('名称:Core i5-7600K   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:3.8GHz\nTB時:4.2GHz') 
                return
            if 'i5' in message.content and '7600.' in message.content or 'SR334' in message.content:
                await message.channel.send('名称:Core i5-7600   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:3.5GHz\nTB時:4.1GHz') 
                return
            if 'i5' in message.content and '7600T.' in message.content or 'SR336' in message.content:
                await message.channel.send('名称:Core i5-7600T   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:2.8GHz\nTB時:3.7GHz') 
                return
            if 'i5' in message.content and '7500.' in message.content or 'SR335' in message.content:
                await message.channel.send('名称:Core i5-7500   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:3.4GHz\nTB時:3.8GHz') 
                return
            if 'i5' in message.content and '7500T.' in message.content or 'SR337' in message.content:
                await message.channel.send('名称:Core i5-7500T   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:2.7GHz\nTB時:3.3GHz') 
                return
            if 'i5' in message.content and '7400.' in message.content or 'SR332' in message.content:
                await message.channel.send('名称:Core i5-7400   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:3.0GHz\nTB時:3.5GHz') 
                return
            if 'i5' in message.content and '7400T.' in message.content or 'SR332' in message.content:
                await message.channel.send('名称:Core i5-7400T   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:2.4GHz\nTB時:3.0GHz') 
                return

            if 'i5' in message.content and '6600K.' in message.content or 'SR2L4' in message.content:
                await message.channel.send('名称:Core i5-6600K   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:3.5GHz\nTB時:3.9GHz')
                return
            if 'i5' in message.content and '6600.' in message.content or 'SR2AJ' in message.content:
                await message.channel.send('名称:Core i5-6600   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:3.3GHz\nTB時:3.9GHz')
                return
            if 'i5' in message.content and '6600T.' in message.content or 'SR2L9' in message.content:
                await message.channel.send('名称:Core i5-6600T   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:2.7GHz\nTB時:3.5GHz')
                return
            if 'i5' in message.content and '6500.' in message.content or 'SR2L6' in message.content:
                await message.channel.send('名称:Core i5-6500   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:3.2GHz\nTB時:3.6GHz')
                return
            if 'i5' in message.content and '6500T.' in message.content or 'SR2L8' in message.content:
                await message.channel.send('名称:Core i5-6500T   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:\2.5GHz\nTB時:3.1GHz')
                return
            if 'i5' in message.content and '6402P.' in message.content or 'SR2NJ' in message.content:
                await message.channel.send('名称:Core i5-6402P   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:2.8GHz\nTB時:3.4GHz')
                return
            if 'i5' in message.content and '6400.' in message.content or 'SR2L7' in message.content:
                await message.channel.send('名称:Core i5-6400   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:2.7GHz\nTB時:3.3GHz')
                return
            if 'i5' in message.content and '6400T.' in message.content or 'SR2L1' in message.content:
                await message.channel.send('名称:Core i5-6400T   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:4/4  \nベース:2.2GHz\nTB時:2.8GHz')
                return
##############################


            if 'i3' in message.content and '560.' in message.content or 'SLBY2' in message.content:
                await message.channel.send('名称:Core i3-560   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1156  \nコア数/スレッド数:2/4  \nベース:3.33GHz') 
                return
            if 'i3' in message.content and '550.' in message.content or 'SLBUD' in message.content:
                await message.channel.send('名称:Core i3-550   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1156  \nコア数/スレッド数:2/4  \nベース:3.2GHz') 
                return
            if 'i3' in message.content and '540.' in message.content or 'SLBTD' in message.content:
                await message.channel.send('名称:Core i3-540   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1156  \nコア数/スレッド数:2/4  \nベース:3.06GHz') 
                return
            if 'i3' in message.content and '530.' in message.content or 'SLBX7' in message.content:
                await message.channel.send('名称:Core i3-530   \nマイクロアーキテクチャ:Westmere \nソケット名:LGA1156  \nコア数/スレッド数:2/4  \nベース:2.93GHz') 
                return

            if 'i3' in message.content and '2130.' in message.content or 'SR05W' in message.content:
                await message.channel.send('名称:Core i3-2130   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.4GHz') 
                return
            if 'i3' in message.content and '2125.' in message.content or 'SR0AY' in message.content:
                await message.channel.send('名称:Core i3-2125   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.3GHz') 
                return
            if 'i3' in message.content and '2120T.' in message.content or 'SR060' in message.content:
                await message.channel.send('名称:Core i3-2120T   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:2.6GHz') 
                return
            if 'i3' in message.content and '2120.' in message.content or 'SR05Y' in message.content:
                await message.channel.send('名称:Core i3-2120   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.3GHz') 
                return
            if 'i3' in message.content and '2105.' in message.content or 'SR0AY' in message.content:
                await message.channel.send('名称:Core i3-2105   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.3GHz') 
                return
            if 'i3' in message.content and '2102.' in message.content or 'SR05D' in message.content:
                await message.channel.send('名称:Core i3-2102   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.1GHz') 
                return
            if 'i3' in message.content and '2100T.' in message.content or 'SR052' in message.content:
                await message.channel.send('名称:Core i3-2100T   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:2.5GHz') 
                return
            if 'i3' in message.content and '2100.' in message.content or 'SR05C' in message.content:
                await message.channel.send('名称:Core i3-2100   \nマイクロアーキテクチャ:Sandy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.1GHz') 
                return

            if 'i3' in message.content and '3250T.' in message.content or 'SR0YW' in message.content:
                await message.channel.send('名称:Core i3-3250T   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.0GHz')
                return
            if 'i3' in message.content and '3250.' in message.content or 'SR0YX' in message.content:
                await message.channel.send('名称:Core i3-3250   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.5GHz')
                return
            if 'i3' in message.content and '3245.' in message.content or 'SR0YL' in message.content:
                await message.channel.send('名称:Core i3-3245   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.4GHz')
                return
            if 'i3' in message.content and '3240T.' in message.content or 'SR0RK' in message.content:
                await message.channel.send('名称:Core i3-3240T   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:2.9GHz')
                return
            if 'i3' in message.content and '3240.' in message.content or 'SR0RH' in message.content:
                await message.channel.send('名称:Core i3-3240   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.4GHz')
                return
            if 'i3' in message.content and '3225.' in message.content or 'SR0RF' in message.content:
                await message.channel.send('名称:Core i3-3225   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.3GHz')
                return
            if 'i3' in message.content and '3220T.' in message.content or 'SR0RE' in message.content:
                await message.channel.send('名称:Core i3-3220T   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:2.8GHz')
                return
            if 'i3' in message.content and '3220.' in message.content or 'SR0RG' in message.content:
                await message.channel.send('名称:Core i3-3220   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.3GHz')
                return
            if 'i3' in message.content and '3210.' in message.content or 'SR0YY' in message.content:
                await message.channel.send('名称:Core i3-3210   \nマイクロアーキテクチャ:Ivy Bridge \nソケット名:LGA1155  \nコア数/スレッド数:2/4  \nベース:3.2GHz')
                return


            if 'i3' in message.content and '4330.' in message.content or 'SR1NM' in message.content:
               await message.channel.send('名称:Core i3-4330   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.5GHz')
               return
            if 'i3' in message.content and '4330T.' in message.content or 'SR1NK' in message.content:
               await message.channel.send('名称:Core i3-4330T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.0GHz')
               return
            if 'i3' in message.content and '4340.' in message.content or 'SR1NL' in message.content:
               await message.channel.send('名称:Core i3-4340   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.6GHz')
               return
            if 'i3' in message.content and '4350.' in message.content or 'SR1PF' in message.content:
               await message.channel.send('名称:Core i3-4350   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.6GHz')
               return
            if 'i3' in message.content and '4350T.' in message.content or 'SR1PA' in message.content:
               await message.channel.send('名称:Core i3-4350T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.5GHz')
               return
            if 'i3' in message.content and '4360.' in message.content or 'SR1PC' in message.content:
               await message.channel.send('名称:Core i3-4360   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.7GHz')
               return
            if 'i3' in message.content and '4360T.' in message.content or 'SR1PB' in message.content:
               await message.channel.send('名称:Core i3-4360T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.2GHz')
               return
            if 'i3' in message.content and '4370.' in message.content or 'SR1PD' in message.content:
               await message.channel.send('名称:Core i3-4370   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.8GHz')
               return
            if 'i3' in message.content and '4370T.' in message.content or 'SR1TB' in message.content:
               await message.channel.send('名称:Core i3-4370T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.3GHz')
               return
            if 'i3' in message.content and '4170T.' in message.content or 'SR1TC' in message.content:
               await message.channel.send('名称:Core i3-4170T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.2GHz')
               return
            if 'i3' in message.content and '4170.' in message.content or 'SR1PL' in message.content:
               await message.channel.send('名称:Core i3-4170   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.7GHz')
               return
            if 'i3' in message.content and '4160T.' in message.content or 'SR1PH' in message.content:
               await message.channel.send('名称:Core i3-4160T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.1GHz')
               return
            if 'i3' in message.content and '4160.' in message.content or 'SR1PK' in message.content:
               await message.channel.send('名称:Core i3-4160   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.6GHz')
               return
            if 'i3' in message.content and '4150T.' in message.content or 'SR1PG' in message.content:
               await message.channel.send('名称:Core i3-4150T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.0GHz')
               return
            if 'i3' in message.content and '4150.' in message.content or 'SR1PJ' in message.content:
               await message.channel.send('名称:Core i3-4150   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.5GHz')
               return
            if 'i3' in message.content and '4130T.' in message.content or 'SR1NN' in message.content:
               await message.channel.send('名称:Core i3-4130T   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.5GHz')
               return
            if 'i3' in message.content and '4130.' in message.content or 'SR1NP' in message.content:
               await message.channel.send('名称:Core i3-4130   \nマイクロアーキテクチャ:Haswell \nソケット名:LGA1150  \nコア数/スレッド数:2/4  \nベース:3.4GHz')
               return


            if 'i3' in message.content and '6300.' in message.content or 'SR2HA' in message.content:
               await message.channel.send('名称:Core i3-6300   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:3.8GHz')
               return
            if 'i3' in message.content and '6300T.' in message.content or 'SR2HD' in message.content:
               await message.channel.send('名称:Core i3-6300T   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:3.3GHz')
               return
            if 'i3' in message.content and '6320.' in message.content or 'SR2H9' in message.content:
               await message.channel.send('名称:Core i3-6320   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:3.9GHz')
               return
            if 'i3' in message.content and '6100.' in message.content or 'SR2HG' in message.content:
               await message.channel.send('名称:Core i3-6100   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:3.7GHz')
               return
            if 'i3' in message.content and '6100T.' in message.content or 'SR2HE' in message.content:
               await message.channel.send('名称:Core i3-6100T   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:3.2GHz')
               return
            if 'i3' in message.content and '6098P.' in message.content or 'SR2NN' in message.content:
               await message.channel.send('名称:Core i3-6098P   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:3.6GHz')
               return 


            if 'i3' in message.content and '7350K.' in message.content or 'SR35B' in message.content:
                await message.channel.send('名称:Core i3-7350K   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:4.2GHz') 
                return
            if 'i3' in message.content and '7320.' in message.content or 'SR358' in message.content:
                await message.channel.send('名称:Core i3-7320   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:4.1GHz') 
                return
            if 'i3' in message.content and '7300.' in message.content or 'SR359' in message.content:
                await message.channel.send('名称:Core i3-7300   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:4.0GHz') 
                return
            if 'i3' in message.content and '7300T.' in message.content or 'SR35M' in message.content:
                await message.channel.send('名称:Core i3-7300T   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:3.5GHz') 
                return
            if 'i3' in message.content and '7101E.' in message.content or 'SR32Z' in message.content:
                await message.channel.send('名称:Core i3-7101E   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:3.9GHz') 
                return
            if 'i3' in message.content and '7101TE.' in message.content or 'SR374' in message.content:
                await message.channel.send('名称:Core i3-7101TE   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:3.4GHz') 
                return
            if 'i3' in message.content and '7100T.' in message.content or 'SR35P' in message.content:
                await message.channel.send('名称:Core i3-7100T   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:3.4GHz') 
                return
            if 'i3' in message.content and '7100.' in message.content or 'SR35C' in message.content:
                await message.channel.send('名称:Core i3-7100   \nマイクロアーキテクチャ:Kaby Lake \nソケット名:LGA1151  \nコア数/スレッド数:2/4  \nベース:3.9GHz') 
                return



            if 'i3' in message.content and '8350K.' in message.content or 'SR3N4' in message.content:
                await message.channel.send('名称:Core i3-8350K   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:4.0GHz') 
                return
            if 'i3' in message.content and '8300.' in message.content or 'SR3XY' in message.content:
                await message.channel.send('名称:Core i3-8300   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:3.7GHz') 
                return
            if 'i3' in message.content and '8300T.' in message.content or 'SR3Y1' in message.content:
                await message.channel.send('名称:Core i3-8300T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:3.2GHz') 
                return
            if 'i3' in message.content and '8100.' in message.content or 'SR3N5' in message.content:
                await message.channel.send('名称:Core i3-8100   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:3.6GHz') 
                return
            if 'i3' in message.content and '8100T.' in message.content or 'SR3Y8' in message.content:
                await message.channel.send('名称:Core i3-8100T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:3.1GHz') 
                return



            if 'i3' in message.content and '9350K.' in message.content or 'SRCZT' in message.content:
                await message.channel.send('名称:Core i3-9350K   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:4.0GHz\nTB時:4.6GHz') 
                return
            if 'i3' in message.content and '9350KF.' in message.content or 'SRF7V' in message.content:
                await message.channel.send('名称:Core i3-9350KF   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:4.0GHz\nTB時:4.6GHz') 
                return
            if 'i3' in message.content and '9300.' in message.content or 'SRCZU' in message.content:
                await message.channel.send('名称:Core i3-9300   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:3.7GHz\nTB時:4.3GHz') 
                return
            if 'i3' in message.content and '9300T.' in message.content or 'SRCZW' in message.content:
                await message.channel.send('名称:Core i3-9300T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:3.7GHz\nTB時:4.3GHz') 
                return
            if 'i3' in message.content and '9320.' in message.content or 'SRF7X' in message.content:
                await message.channel.send('名称:Core i3-9320   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:4.0GHz\nTB時:4.6GHz') 
                return
            if 'i3' in message.content and '9100F.' in message.content or 'SRF7W' in message.content:
                await message.channel.send('名称:Core i3-9100F   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:3.7GHz\nTB時:4.2GHz') 
                return
            if 'i3' in message.content and '9100T.' in message.content or 'SRCZX' in message.content:
                await message.channel.send('名称:Core i3-9100T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:3.1GHz\nTB時:3.7GHz') 
                return
            if 'i3' in message.content and '9100.' in message.content or 'SRCZV' in message.content:
                await message.channel.send('名称:Core i3-9100   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:4/4  \nベース:3.6GHz\nTB時:4.2GHz') 
                return

            if 'i3' in message.content and '10320.' in message.content or 'SRH3G' in message.content:
                await message.channel.send('名称:Core i3-10320   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:4/8  \nベース:3.8GHz\nTB時:4.6GHz') 
                return
            if 'i3' in message.content and '10300T.' in message.content or 'SRH3L' in message.content:
                await message.channel.send('名称:Core i3-10300T   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:4/8  \nベース:3.0GHz\nTB時:3.9GHz') 
                return
            if 'i3' in message.content and '10300.' in message.content or 'SRH3J' in message.content:
                await message.channel.send('名称:Core i3-10300   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:4/8  \nベース:3.7GHz\nTB時:4.4GHz') 
                return
            if 'i3' in message.content and '10100T.' in message.content or 'SRH3Q' in message.content:
                await message.channel.send('名称:Core i3-10100T   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:4/8  \nベース:3.0GHz\nTB時:3.8GHz') 
                return
            if 'i3' in message.content and '10100.' in message.content or 'SRH3N' in message.content:
                await message.channel.send('名称:Core i3-10100   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:4/8  \nベース:3.6GHz\nTB時:4.3GHz') 
                return



#######################################


            if 'I9' in message.content.upper() and '7980XE.' in message.content.upper() or 'SR3RS' in message.content.upper():
                await message.channel.send('名称:Core i9-7980XE   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:18/36  \nベース:2.6GHz\nTB時:4.2GHz')
                return
            if 'I9' in message.content.upper() and '7960X.' in message.content.upper() or 'SR3RR' in message.content.upper():
                await message.channel.send('名称:Core i9-7960X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:16/32  \nベース:2.8GHz\nTB時:4.2GHz')
                return
            if 'I9' in message.content.upper() and '7940X.' in message.content.upper() or 'SR3RQ' in message.content.upper():
                await message.channel.send('名称:Core i9-7940X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:14/28  \nベース:3.1GHz\nTB時:4.3GHz')
                return
            if 'I9' in message.content.upper() and '7920X.' in message.content.upper() or 'SR3NG' in message.content.upper():
                await message.channel.send('名称:Core i9-7920X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:12/24  \nベース:2.9GHz\nTB時:4.3GHz')
                return
            if 'I9' in message.content.upper() and '7900X.' in message.content.upper() or 'SR3L2' in message.content.upper():
                await message.channel.send('名称:Core i9-7900X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:10/20  \nベース:3.3GHz\nTB時:4.3GHz')
                return


            if 'I9' in message.content.upper() and '9820X.' in message.content.upper() or 'SREZ8' in message.content.upper():
                await message.channel.send('名称:Core i9-9820X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:10/20  \nベース:3.3GHz\nTB時:4.4GHz')
                return
            if 'I9' in message.content.upper() and '9900X.' in message.content.upper() or 'SREZ7' in message.content.upper():
                await message.channel.send('名称:Core i9-9900X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:10/20  \nベース:3.5GHz\nTB時:4.4GHz')
                return
            if 'I9' in message.content.upper() and '9920X.' in message.content.upper() or 'SREZ6' in message.content.upper():
                await message.channel.send('名称:Core i9-9920X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:12/24  \nベース:3.5GHz\nTB時:4.4GHz')
                return
            if 'I9' in message.content.upper() and '9940X.' in message.content.upper() or 'SREZ5' in message.content.upper():
                await message.channel.send('名称:Core i9-9940X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:14/28  \nベース:3.3GHz\nTB時:4.4GHz')
                return
            if 'I9' in message.content.upper() and '9960X.' in message.content.upper() or 'SREZ4' in message.content.upper():
                await message.channel.send('名称:Core i9-9960X   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:16/32  \nベース:3.1GHz\nTB時:4.4GHz')
                return
            if 'I9' in message.content.upper() and '9980XE.' in message.content.upper() or 'SREZ3' in message.content.upper():
                await message.channel.send('名称:Core i9-9980XE   \nマイクロアーキテクチャ:Skylake \nソケット名:LGA2066  \nコア数/スレッド数:18/36  \nベース:3GHz\nTB時:4.1GHz')
                return
        
            if 'I9' in message.content.upper() and '9900K.' in message.content.upper() or 'SRELS' in message.content.upper() or 'サッカーボール' in message.content:
                await message.channel.send('名称:Core i9-9900K   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/16  \nベース:3.6GHz\nTB時:5GHz')
                return
            if 'I9' in message.content.upper() and '9900KF.' in message.content.upper() or 'SRFAA' in message.content.upper():
                await message.channel.send('名称:Core i9-9900KF   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/16  \nベース:3.6GHz\nTB時:5GHz')
                return
            if 'I9' in message.content.upper() and '9900KS.' in message.content.upper() or 'SRG1Q' in message.content.upper() or 'カス' in message.content:
                await message.channel.send('名称:Core i9-9900KS   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/16  \nベース:4GHz\nTB時:5GHz')
                return
            if 'I9' in message.content.upper() and '9900.' in message.content.upper() or 'SRG18' in message.content.upper() or 'アイマス' in message.content:
                await message.channel.send('名称:Core i9-9900   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/16  \nベース:3.1GHz\nTB時:5GHz')
                return
            if 'I9' in message.content.upper() and '9900T.' in message.content.upper() or 'SRG1B' in message.content.upper():
                await message.channel.send('名称:Core i9-9900T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:8/16  \nベース:2.1GHz\nTB時:4.4GHz')
                return


            if 'I9' in message.content.upper() and '10900X.' in message.content.upper() or 'SRGV7' in message.content.upper():
                await message.channel.send('名称:Core i9-10900X   \nマイクロアーキテクチャ:Cascade Lake \nソケット名:LGA2066  \nコア数/スレッド数:10/20  \nベース:3.7GHz\nTB時:4.5GHz')
                return
            if 'I9' in message.content.upper() and '10920X.' in message.content.upper() or 'SRGSJ' in message.content.upper():
                await message.channel.send('名称:Core i9-10920X   \nマイクロアーキテクチャ:Cascade Lake \nソケット名:LGA2066  \nコア数/スレッド数:12/24  \nベース:3.5GHz\nTB時:4.6GHz')
                return
            if 'I9' in message.content.upper() and '10940X.' in message.content.upper() or 'SRGSH' in message.content.upper():
                await message.channel.send('名称:Core i9-10940X   \nマイクロアーキテクチャ:Cascade Lake \nソケット名:LGA2066  \nコア数/スレッド数:14/28  \nベース:3.3GHz\nTB時:4.6GHz')
                return
            if 'I9' in message.content.upper() and '10980XE.' in message.content.upper() or 'SRGSG' in message.content.upper():
                await message.channel.send('名称:Core i9-10980XE   \nマイクロアーキテクチャ:Cascade Lake \nソケット名:LGA2066  \nコア数/スレッド数:18/36  \nベース:3GHz\nTB時:4.6GHz')
                return


            if 'I9' in message.content.upper() and '10900T.' in message.content.upper() or 'SRH8Y' in message.content.upper():
                await message.channel.send('名称:Core i9-10900T   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:10/20  \nベース:1.9GHz\nTB時:4.6GHz')
                return
            if 'I9' in message.content.upper() and '10900KF.' in message.content.upper() or 'SRH92' in message.content.upper():
                await message.channel.send('名称:Core i9-10900KF   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:10/20  \nベース:3.7GHz\nTB時:5.3GHz')
                return
            if 'I9' in message.content.upper() and '10900K.' in message.content.upper() or 'SRH91' in message.content.upper():
                await message.channel.send('名称:Core i9-10900K   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:10/20  \nベース:3.7GHz\nTB時:5.3GHz')
                return
            if 'I9' in message.content.upper() and '10900F.' in message.content.upper() or 'SRH90' in message.content.upper():
                await message.channel.send('名称:Core i9-10900F   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:10/20  \nベース:2.8GHz\nTB時:5.2GHz')
                return
            if 'I9' in message.content.upper() and '10900.' in message.content.upper() or 'SRH8Z' in message.content.upper():
                await message.channel.send('名称:Core i9-10900   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:10/20  \nベース:2.8GHz\nTB時:5.2GHz')
                return
            if 'I9' in message.content.upper() and '10900TE.' in message.content.upper() or 'SRJFC' in message.content.upper():
                await message.channel.send('名称:Core i9-10900TE   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:10/20  \nベース:1.8GHz\nTB時:4.5GHz')
                return
            if 'I9' in message.content.upper() and '10900E.' in message.content.upper() or 'unknown' in message.content.upper():
                await message.channel.send('名称:Core i9-10900E   \nマイクロアーキテクチャ:Comet Lake \nソケット名:LGA1200  \nコア数/スレッド数:10/20  \nベース:2.8GHz\nTB時:4.7GHz')
                return

            if 'I9' in message.content.upper() and '10885H.' in message.content.upper() or 'SRJ8J' in message.content.upper():
                await message.channel.send('名称:Core i9-10885H   \nマイクロアーキテクチャ:Comet Lake \nソケット名:BGA1440  \nコア数/スレッド数:8/16  \nベース:2.4GHz\nTB時:5.3GHz')
                return
            if 'I9' in message.content.upper() and '10980HK.' in message.content.upper() or 'SRH8T' in message.content.upper():
                await message.channel.send('名称:Core i9-10980HK   \nマイクロアーキテクチャ:Comet Lake \nソケット名:BGA1440  \nコア数/スレッド数:8/16  \nベース:2.4GHz\nTB時:5.1GHz')
                return


            if 'I9' in message.content.upper() and '9880H.' in message.content.upper() or 'SRFD1' in message.content.upper():
                await message.channel.send('名称:Core i9-9880H   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:BGA1440  \nコア数/スレッド数:8/16  \nベース:2.3GHz\nTB時:4.8GHz')
                return
            if 'I9' in message.content.upper() and '9980HK.' in message.content.upper() or 'SRFD0' in message.content.upper():
                await message.channel.send('名称:Core i9-9980HK \nマイクロアーキテクチャ:Coffee Lake \nソケット名:BGA1440  \nコア数/スレッド数:8/16  \nベース:2.4GHz\nTB時:5GHz')
                return


            
            if 'I9' in message.content.upper() and '8950HK.' in message.content.upper() or 'SRCKN' in message.content.upper():
                await message.channel.send('名称:Core i9-8950HK   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:BGA1440  \nコア数/スレッド数:8/16  \nベース:2.9GHz\nTB時:4.8GHz')
                return






#############################
        if '$' in message.content:
            

            if 'eleron' in message.content and '266.' in message.content or 'SL2QG' in message.content or 'SL2YN' in message.content:
                await message.channel.send('名称:Celeron 266MHz   \nマイクロアーキテクチャ:P6(covington) \nソケット名:slot1  \nコア数/スレッド数:1/1  \nベース:266MHz')
                return
            if 'eleron' in message.content and '300.' in message.content or 'SL27Z' in message.content or 'SL2Z7' in message.content or 'SL2Y2' in message.content:
                await message.channel.send('名称:Celeron 300MHz   \nマイクロアーキテクチャ:P6(covington) \nソケット名:slot1  \nコア数/スレッド数:1/1  \nベース:300MHz')
                return








            if 'eleron' in message.content and '333.' in message.content:
                await message.channel.send('名称:Celeron 333MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370/slot1  \nコア数/スレッド数:1/1  \nベース:333MHz')
                return
            if 'eleron' in message.content and '366.' in message.content:
                await message.channel.send('名称:Celeron 366MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370/slot1  \nコア数/スレッド数:1/1  \nベース:366MHz')
                return

            if 'eleron' in message.content and '400.' in message.content:
                await message.channel.send('名称:Celeron 400MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370/slot1  \nコア数/スレッド数:1/1  \nベース:400MHz')
                return
            if 'eleron' in message.content and '433.' in message.content:
                await message.channel.send('名称:Celeron 433MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370/slot1  \nコア数/スレッド数:1/1  \nベース:433MHz')
                return





            if 'eleron' in message.content and '300.' in message.content or 'SL35Q' in message.content or 'SL36A' in message.content:
                await message.channel.send('名称:Celeron 300MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:300MHz')
                return
            if 'SL35R' in message.content or 'SL36B' in message.content:
                await message.channel.send('名称:Celeron 333MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:333MHz')
                return
            if 'eleron' in message.content and '300A.' in message.content or 'SL2WM' in message.content or 'SL32A' in message.content:
                await message.channel.send('名称:Celeron 300AMHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:slot1  \nコア数/スレッド数:1/1  \nベース:300MHz')
                return
            if 'SL2WN' in message.content or 'SL32B' in message.content:
                await message.channel.send('名称:Celeron 333MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:slot1  \nコア数/スレッド数:1/1  \nベース:333MHz')
                return
            if 'SL35S' in message.content or 'SL36C' in message.content:
                await message.channel.send('名称:Celeron 366MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:366MHz')
                return
            if 'SL376' in message.content or 'SL37Q' in message.content:
                await message.channel.send('名称:Celeron 366MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:slot1  \nコア数/スレッド数:1/1  \nベース:366MHz')
                return
            if 'SL37X' in message.content or 'SL3A2' in message.content:
                await message.channel.send('名称:Celeron 400MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:400MHz')
                return
            if 'SL37V' in message.content or 'SL39Z' in message.content:
                await message.channel.send('名称:Celeron 400MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:slot1  \nコア数/スレッド数:1/1  \nベース:400MHz')
                return
            if 'SL3BS' in message.content or 'SL3BA' in message.content:
                await message.channel.send('名称:Celeron 433MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:433MHz')
                return
            if 'SL3BC' in message.content:
                await message.channel.send('名称:Celeron 433MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:slot1  \nコア数/スレッド数:1/1  \nベース:433MHz')
                return
            if 'eleron' in message.content and '350.' in message.content or 'Q867' in message.content:
                await message.channel.send('名称:Celeron 350MHz ※見つけたら買え  \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:350MHz')
                return
            if 'eleron' in message.content and '466.' in message.content or 'SL3FL' in message.content or 'SL3EH' in message.content:
                await message.channel.send('名称:Celeron 466MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:466MHz')
                return
            if 'eleron' in message.content and '500.' in message.content or 'SL3LQ' in message.content or 'SL3FY' in message.content:
                await message.channel.send('名称:Celeron 500MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370 \nコア数/スレッド数:1/1  \nベース:500MHz')
                return
            if 'eleron' in message.content and '533.' in message.content or 'SL3PZ' in message.content or 'SL3FZ' in message.content:
                await message.channel.send('名称:Celeron 533MHz   \nマイクロアーキテクチャ:P6(Mendocino) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:533MHz')
                return




            if 'eleron' in message.content and '533A.' in message.content or 'SL3W6' in message.content or 'SL46S' in message.content or 'SL4PD' in message.content:
                await message.channel.send('名称:Celeron 533AMHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:533AMHz')
                return
            if 'eleron' in message.content and '566.' in message.content or 'SL3W7' in message.content or 'SL46T' in message.content or 'SL4PC' in message.content or 'SL5L5' in message.content or 'SL4NW' in message.content:
                await message.channel.send('名称:Celeron 566MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:566MHz')
                return
            if 'eleron' in message.content and '600.' in message.content or 'SL3W8' in message.content or 'SL46U' in message.content or 'SL4NX' in message.content or 'SL4PB' in message.content:
                await message.channel.send('名称:Celeron 600MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:600MHz')
                return
            if 'eleron' in message.content and '633.' in message.content or 'SL3VS' in message.content or 'SL3W9' in message.content or 'SL4NY' in message.content or 'SL4PA' in message.content:
                await message.channel.send('名称:Celeron 633MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:633MHz')
                return
            if 'eleron' in message.content and '667.' in message.content or 'SL48E' in message.content or 'SL4AB' in message.content or 'SL4NZ' in message.content or 'SL4P9' in message.content or 'SL532' in message.content:
                await message.channel.send('名称:Celeron 667MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:667MHz')
                return


            if 'eleron' in message.content and '700.' in message.content or 'SL48F' in message.content or 'SL4E6' in message.content or 'SL4EG' in message.content or 'SL4P2' in message.content or 'SL4P8' in message.content or 'SL52Z' in message.content or 'SL5E6' in message.content:
                await message.channel.send('名称:Celeron 700MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:700MHz')
                return
            if 'eleron' in message.content and '733.' in message.content or 'SL4P3' in message.content or 'SL4P7' in message.content or 'SL52Y' in message.content or 'SL5E9' in message.content:
                await message.channel.send('名称:Celeron 733MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:733MHz')
                return
            if 'eleron' in message.content and '766.' in message.content or 'SL4P6' in message.content or 'SL52X' in message.content or 'SL5EA' in message.content or 'SL4QF' in message.content:
                await message.channel.send('名称:Celeron 766MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:766MHz')
                return
            if 'eleron' in message.content and '800.' in message.content or 'SL4TF' in message.content or 'SL55R' in message.content or 'SL5EB' in message.content or 'SL5WC' in message.content or 'SL5WW' in message.content:
                await message.channel.send('名称:Celeron 800MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:800MHz')
                return
            if 'eleron' in message.content and '850.' in message.content or 'SL54Q' in message.content or 'SL5EC' in message.content or 'SL5GA' in message.content or 'SL5GB' in message.content or 'SL5WB' in message.content or 'SL5WX' in message.content:
                await message.channel.send('名称:Celeron 850MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:850MHz')
                return

            if 'eleron' in message.content and '900.' in message.content:
                await message.channel.send('名称:Celeron 900MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370 ※SL633のみsocket370-2  \nコア数/スレッド数:1/1  \nベース:900MHz')
                return
            if 'eleron' in message.content and '950.' in message.content:
                await message.channel.send('名称:Celeron 950MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370 ※SL634のみsocket370-2  \nコア数/スレッド数:1/1  \nベース:950MHz')
                return



            if 'SL5LX' in message.content or 'SL5MQ' in message.content or 'SL5WA' in message.content or 'SL5WY' in message.content:  
                await message.channel.send('名称:Celeron 900MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370 \nコア数/スレッド数:1/1  \nベース:900MHz') #かっぱの900
                return
            if 'SL5UZ' in message.content or 'SL5V2' in message.content:
                await message.channel.send('名称:Celeron 950MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370 \nコア数/スレッド数:1/1  \nベース:950MHz') #かっぱの950
                return
            if 'SL633' in message.content:  
                await message.channel.send('名称:Celeron 900MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370-2 \nコア数/スレッド数:1/1  \nベース:900MHz') #370-2の900
                return
            if 'SL634' in message.content:
                await message.channel.send('名称:Celeron 950MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370-2 \nコア数/スレッド数:1/1  \nベース:950MHz') #370-2の950
                return


            if 'eleron' in message.content and '1000.' in message.content or 'eleron' in message.content and '1.0.' in message.content or 'SL5XQ' in message.content or 'SL5XT' in message.content:
                await message.channel.send('名称:Celeron 1000MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:1000MHz') #かっぱの1GHz
                return
            if 'eleron' in message.content and '1100.' in message.content or 'eleron' in message.content and '1.1.' in message.content or 'SL5XR' in message.content or 'SL5XU' in message.content:
                await message.channel.send('名称:Celeron 1100MHz   \nマイクロアーキテクチャ:P6(Coppermine-128) \nソケット名:socket370  \nコア数/スレッド数:1/1  \nベース:1100MHz') #かっぱの1.1GHz
                return


            if 'eleron' in message.content and '1.0A.' in message.content or 'eleron' in message.content and '1000A.' in message.content or 'SL5ZF' in message.content or 'unknown' in message.content:
                await message.channel.send('名称:Celeron 1.0AGHz   \nマイクロアーキテクチャ:P6(Tualatin-256) \nソケット名:socket370-2  \nコア数/スレッド数:1/1  \nベース:1GHz')
                return
            if 'eleron' in message.content and '1.1A.' in message.content or 'eleron' in message.content and '1100A.' in message.content or 'SL5VQ' in message.content or 'SL5ZE' in message.content or 'SL6CA' in message.content or 'SL6JR' in message.content:
                await message.channel.send('名称:Celeron 1.1AGHz   \nマイクロアーキテクチャ:P6(Tualatin-256) \nソケット名:socket370-2  \nコア数/スレッド数:1/1  \nベース:1.1GHz')
                return
            if 'eleron' in message.content and '1.2.' in message.content or 'eleron' in message.content and '1200.' in message.content or 'SL5XS' in message.content or 'SL5Y5' in message.content or 'SL656' in message.content or 'SL68P' in message.content or 'SL6C8' in message.content or 'SL6JS' in message.content:
                await message.channel.send('名称:Celeron 1.2GHz   \nマイクロアーキテクチャ:P6(Tualatin-256) \nソケット名:socket370-2  \nコア数/スレッド数:1/1  \nベース:1.2GHz')
                return
            if 'eleron' in message.content and '1.3.' in message.content or 'eleron' in message.content and '1300.' in message.content or 'SL5VR' in message.content or 'SL5ZJ' in message.content or 'SL6C7' in message.content or 'SL6JT' in message.content:
                await message.channel.send('名称:Celeron 1.3GHz   \nマイクロアーキテクチャ:P6(Tualatin-256) \nソケット名:socket370-2  \nコア数/スレッド数:1/1  \nベース:1.3GHz')
                return
            if 'eleron' in message.content and '1.4.' in message.content or 'eleron' in message.content and '1400.' in message.content or 'SL64V' in message.content or 'SL68G' in message.content or 'SL6C6' in message.content or 'SL6JU' in message.content:
                await message.channel.send('名称:Celeron 1.4GHz   \nマイクロアーキテクチャ:P6(Tualatin-256) \nソケット名:socket370-2  \nコア数/スレッド数:1/1  \nベース:1.4GHz')
                return
            if 'eleron' in message.content and '1.5.' in message.content or 'eleron' in message.content and '1500.' in message.content or 'SL6C5' in message.content or 'SL6JV' in message.content:
                await message.channel.send('名称:Celeron 1.5GHz   \nマイクロアーキテクチャ:P6(Tualatin-256) \nソケット名:socket370-2  \nコア数/スレッド数:1/1  \nベース:1.5GHz')
                return

            

#　tualatinのせれろんまで終わりました。

            
            if 'eleron' in message.content and '1.8.' in message.content:
                await message.channel.send('名称:Celeron 1.8GHz   \nマイクロアーキテクチャ:NetBurst(Willamette/Northwood) \nソケット名:socket478 \nコア数/スレッド数:1/1  \nベース:1.8GHz')
                return

    
            if 'eleron' in message.content and '2.4.' in message.content:
                await message.channel.send('名称:Celeron 2.4GHz/D320   \nマイクロアーキテクチャ:NetBurst(Northwood/Prescott) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.4GHz')
                return
            if 'eleron' in message.content and '2.8.' in message.content:
                await message.channel.send('名称:Celeron 2.8GHz/D335/D335J   \nマイクロアーキテクチャ:NetBurst(Northwood/Prescott) \nソケット名:socket478 ※D335JはLGA775 \nコア数/スレッド数:1/1  \nベース:2.8GHz')
                return






            if 'eleron' in message.content and '1.7.' in message.content or 'SL68C' in message.content or 'SL69Z' in message.content:
                await message.channel.send('名称:Celeron 1.7GHz   \nマイクロアーキテクチャ:NetBurst(Willamette) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:1.7GHz')
                return
            if 'SL68D' in message.content or 'SL6A2' in message.content:
                await message.channel.send('名称:Celeron 1.8GHz   \nマイクロアーキテクチャ:NetBurst(Willamette) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:1.8GHz')
                return



            if 'SL7RU' in message.content:
                await message.channel.send('名称:Celeron 1.8GHz   \nマイクロアーキテクチャ:NetBurst(NorthWood) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:1.8GHz')
                return
            if 'eleron' in message.content and '2.0.' in message.content or 'SL6HY' in message.content or 'SL6LC' in message.content or 'SL6RV' in message.content or 'SL6SW' in message.content or 'SL6VR' in message.content or 'SL6VY' in message.content:
                await message.channel.send('名称:Celeron 2GHz   \nマイクロアーキテクチャ:NetBurst(Northwood) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2GHz')
                return
            if 'eleron' in message.content and '2.1.' in message.content or 'SL6RS' in message.content or 'SL6SY' in message.content or 'SL6VS' in message.content or 'SL6VZ' in message.content:
                await message.channel.send('名称:Celeron 2.1GHz   \nマイクロアーキテクチャ:NetBurst(Northwood) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.1GHz')
                return
            if 'eleron' in message.content and '2.2.' in message.content or 'SL6RW' in message.content or 'SL6SX' in message.content or 'SL6VT' in message.content or 'SL6W2' in message.content:
                await message.channel.send('名称:Celeron 2.2GHz   \nマイクロアーキテクチャ:NetBurst(Northwood) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.2GHz')
                return
            if 'eleron' in message.content and '2.3.' in message.content or 'SL6T2' in message.content or 'SL6T3' in message.content or 'SL6T5' in message.content or 'SL6XJ' in message.content or 'SL6WC' in message.content or 'SL6WD' in message.content or 'SL6WT' in message.content:
                await message.channel.send('名称:Celeron 2.3GHz   \nマイクロアーキテクチャ:NetBurst(Northwood) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.3GHz')
                return
            if 'SL6V2' in message.content or 'SL6XG' in message.content or 'SL6VU' in message.content or 'SL6W4' in message.content:
                await message.channel.send('名称:Celeron 2.4GHz   \nマイクロアーキテクチャ:NetBurst(Northwood) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.4GHz')
                return
            if 'eleron' in message.content and '2.5.' in message.content or 'SL6ZY' in message.content or 'SL62B' in message.content:
                await message.channel.send('名称:Celeron 2.5GHz   \nマイクロアーキテクチャ:NetBurst(Northwood) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.5GHz')
                return
            if 'eleron' in message.content and '2.6.' in message.content or 'SL6W5' in message.content or 'SL6VV' in message.content:
                await message.channel.send('名称:Celeron 2.6GHz   \nマイクロアーキテクチャ:NetBurst(Northwood) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.6GHz')
                return
            if 'eleron' in message.content and '2.7.' in message.content or 'SL77S' in message.content or 'SL77U' in message.content:
                await message.channel.send('名称:Celeron 2.7GHz   \nマイクロアーキテクチャ:NetBurst(Northwood) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.7GHz')
                return
            if 'SL77T' in message.content or 'SL77V' in message.content:
                await message.channel.send('名称:Celeron 2.8GHz   \nマイクロアーキテクチャ:NetBurst(Northwood) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.8GHz')
                return


#　プレスコ(478)９、(775)１２、シダミル５



            if 'eleron' in message.content and '310.' in message.content or 'SL8RZ' in message.content or 'SL8S2' in message.content or 'SL93R' in message.content:
                await message.channel.send('名称:Celeron D 310    \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.13GHz')
                return
            if 'eleron' in message.content and '315.' in message.content or 'SL7XG' in message.content or 'SL7WS' in message.content or 'SL7XY' in message.content or 'SL87K' in message.content or 'SL8AW' in message.content or 'SL8HH' in message.content or 'SL93Q' in message.content:
                await message.channel.send('名称:Celeron D 315   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.26GHz')
                return
            if 'eleron' in message.content and '320.' in message.content or 'SL7C4' in message.content or 'SL7JV' in message.content or 'SL7KX' in message.content or 'SL7VW' in message.content or 'SL87J' in message.content or 'SL8HJ' in message.content:
                await message.channel.send('名称:Celeron D 320   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.4GHz')
                return
            if 'eleron' in message.content and '325.' in message.content or 'SL7C5' in message.content or 'SL7TG' in message.content or 'SL7ND' in message.content or 'SL7NU' in message.content or 'SL7VX' in message.content or 'SL8HK' in message.content:
                await message.channel.send('名称:Celeron D 325   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.53GHz')
                return
            if 'eleron' in message.content and '330.' in message.content or 'SL7C6' in message.content or 'SL7TH' in message.content or 'SL7DL' in message.content or 'SL7KZ' in message.content or 'SL7ST' in message.content or 'SL7NV' in message.content or 'SL7VY' in message.content or 'SL8HL' in message.content:
                await message.channel.send('名称:Celeron D 330   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.66GHz')
                return
            if 'eleron' in message.content and '335.' in message.content or 'SL7C7' in message.content or 'SL7TJ' in message.content or 'SL7DM' in message.content or 'SL7L2' in message.content or 'SL7SU' in message.content or 'SL7NW' in message.content or 'SL7VZ' in message.content or 'SL8HL' in message.content:
                await message.channel.send('名称:Celeron D 335   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.8GHz')
                return
            if 'eleron' in message.content and '340.' in message.content or 'SL7Q9' in message.content or 'SL7RN' in message.content or 'SL7SV' in message.content or 'SL7TS' in message.content or 'SL7W2' in message.content or 'SL8HN' in message.content:
                await message.channel.send('名称:Celeron D 340   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:2.93GHz')
                return
            if 'eleron' in message.content and '345.' in message.content or 'SL7DN' in message.content or 'SL7NX' in message.content or 'SL7W3' in message.content or 'SL8HP' in message.content:
                await message.channel.send('名称:Celeron D 345   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:3.06GHz')
                return
            if 'eleron' in message.content and '350.' in message.content or 'SL7L4' in message.content or 'SL7NY' in message.content or 'SL8HQ' in message.content:
                await message.channel.send('名称:Celeron D 350   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:socket478  \nコア数/スレッド数:1/1  \nベース:3.2GHz')
                return


            if 'eleron' in message.content and '325J.' in message.content or 'SL7SS' in message.content or 'SL7TL' in message.content or 'SL7VR' in message.content:
                await message.channel.send('名称:Celeron D 325J   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:2.53GHz')
                return
            if 'eleron' in message.content and '330J.' in message.content or 'SL7TM' in message.content or 'SL7VS' in message.content:
                await message.channel.send('名称:Celeron D 330J   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:2.66GHz')
                return
            if 'eleron' in message.content and '335J.' in message.content or 'SL7TN' in message.content or 'SL7VT' in message.content:
                await message.channel.send('名称:Celeron D 335J   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:2.8GHz')
                return
            if 'eleron' in message.content and '340J.' in message.content or 'SL7TP' in message.content :
                await message.channel.send('名称:Celeron D 340J   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:2.93GHz')
                return
            if 'eleron' in message.content and '345J.' in message.content or 'SL7VV' in message.content or 'SL7TQ' in message.content:
                await message.channel.send('名称:Celeron D 345J   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:3.06GHz')
                return
            
            if 'eleron' in message.content and '326.' in message.content or 'SL7TU' in message.content or 'SL8H5' in message.content or 'SL98U' in message.content:
                await message.channel.send('名称:Celeron D 326   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:2.53GHz')
                return
            if 'eleron' in message.content and '331.' in message.content or 'SL7TV' in message.content or 'SL8H7' in message.content or 'SL98V' in message.content:
                await message.channel.send('名称:Celeron D 331   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:2.66GHz')
                return
            if 'eleron' in message.content and '336.' in message.content or 'SL7TW' in message.content or 'SL8H9' in message.content or 'SL98W' in message.content:
                await message.channel.send('名称:Celeron D 336   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:2.8GHz')
                return
            if 'eleron' in message.content and '341.' in message.content or 'SL7TX' in message.content or 'SL8HB' in message.content or 'SL98V' in message.content:
                await message.channel.send('名称:Celeron D 341   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:2.93GHz')
                return
            if 'eleron' in message.content and '346.' in message.content or 'SL7TY' in message.content or 'SL8HD' in message.content or 'SL9BR' in message.content:
                await message.channel.send('名称:Celeron D 341   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:3.06GHz')
                return
            if 'eleron' in message.content and '351.' in message.content or 'SL7TZ' in message.content or 'SL8HF' in message.content or 'SL9BS' in message.content:
                await message.channel.send('名称:Celeron D 351   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:3.2GHz')
                return
            if 'eleron' in message.content and '355.' in message.content or 'SL8HS' in message.content:
                await message.channel.send('名称:Celeron D 355   \nマイクロアーキテクチャ:NetBurst(Prescott) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:3.33GHz')
                return



            # ここからシダミル

            

            if 'eleron' in message.content and '347.' in message.content or 'SL9XU' in message.content or 'SL9KN' in message.content:
                await message.channel.send('名称:Celeron D 347   \nマイクロアーキテクチャ:NetBurst(CedarMill) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:3.06GHz')
                return
            if 'eleron' in message.content and '352.' in message.content or 'SL96P' in message.content or 'SL9KM' in message.content:
                await message.channel.send('名称:Celeron D 352   \nマイクロアーキテクチャ:NetBurst(CedarMill) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:3.2GHz')
                return
            if 'eleron' in message.content and '356.' in message.content or 'SL96N' in message.content or 'SL9KL' in message.content:
                await message.channel.send('名称:Celeron D 356   \nマイクロアーキテクチャ:NetBurst(CedarMill) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:3.33GHz')
                return
            if 'eleron' in message.content and '360.' in message.content or 'SL9KK' in message.content:
                await message.channel.send('名称:Celeron D 360   \nマイクロアーキテクチャ:NetBurst(CedarMill) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:3.46GHz')
                return
            if 'eleron' in message.content and '365.' in message.content or 'SL9KJ' in message.content:
                await message.channel.send('名称:Celeron D 365   \nマイクロアーキテクチャ:NetBurst(CedarMill) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nベース:3.6GHz')
                return


            if 'eleron' in message.content and '220.' in message.content or 'SLAF2' in message.content:
                await message.channel.send('名称:Celeron 220 \nマイクロアーキテクチャ:Core(Conroe) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nクロック:1.2GHz')
                return
            if 'eleron' in message.content and '420.' in message.content or 'SL9XP' in message.content:
                await message.channel.send('名称:Celeron 420 \nマイクロアーキテクチャ:Core(Conroe) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nクロック:1.6GHz')
                return
            if 'eleron' in message.content and '430.' in message.content or 'SL9XN' in message.content:
                await message.channel.send('名称:Celeron 430 \nマイクロアーキテクチャ:Core(Conroe) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nクロック:1.8GHz')
                return
            if 'eleron' in message.content and '440.' in message.content or 'SL9XL' in message.content:
                await message.channel.send('名称:Celeron 440 \nマイクロアーキテクチャ:Core(Conroe) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nクロック:2GHz')
                return
            if 'eleron' in message.content and '450.' in message.content or 'SLAFZ' in message.content:
                await message.channel.send('名称:Celeron 450 \nマイクロアーキテクチャ:Core(Conroe) \nソケット名:LGA775  \nコア数/スレッド数:1/1  \nクロック:2.2GHz')
                return

            
            if 'eleron' in message.content and '445.' in message.content or 'SLAGH' in message.content:
                await message.channel.send('名称:Celeron E  \nマイクロアーキテクチャ:Core(Conroe-CL) \nソケット名:LGA771  \nコア数/スレッド数:1/1  \nクロック:1.86GHz')
                return


            if 'eleron' in message.content and 'E1200.' in message.content or 'SLAQW' in message.content:
                await message.channel.send('名称:Celeron E1200  \nマイクロアーキテクチャ:Core(Allendale) \nソケット名:LGA775  \nコア数/スレッド数:2/2  \nクロック:1.6GHz')
                return
            if 'eleron' in message.content and 'E1400.' in message.content or 'SLAR2' in message.content:
                await message.channel.send('名称:Celeron E1400  \nマイクロアーキテクチャ:Core(Allendale) \nソケット名:LGA775  \nコア数/スレッド数:2/2  \nクロック:2GHz')
                return
            if 'eleron' in message.content and 'E1500.' in message.content or 'SLAQZ' in message.content:
                await message.channel.send('名称:Celeron E1500  \nマイクロアーキテクチャ:Core(Allendale) \nソケット名:LGA775  \nコア数/スレッド数:2/2  \nクロック:2.2GHz')
                return
            if 'eleron' in message.content and 'E1600.' in message.content or 'SLAQY' in message.content:
                await message.channel.send('名称:Celeron E1600  \nマイクロアーキテクチャ:Core(Allendale) \nソケット名:LGA775  \nコア数/スレッド数:2/2  \nクロック:2.4GHz')
                return
            if 'eleron' in message.content and 'E3200.' in message.content or 'SLGU5' in message.content:
                await message.channel.send('名称:Celeron E3200  \nマイクロアーキテクチャ:Core(Wolfdale) \nソケット名:LGA775  \nコア数/スレッド数:2/2  \nクロック:2.4GHz')
                return
            if 'eleron' in message.content and 'E3300.' in message.content or 'SLGU4' in message.content:
                await message.channel.send('名称:Celeron E3300  \nマイクロアーキテクチャ:Core(Wolfdale) \nソケット名:LGA775  \nコア数/スレッド数:2/2  \nクロック:2.5GHz')
                return
            if 'eleron' in message.content and 'E3400.' in message.content or 'SLGTZ' in message.content:
                await message.channel.send('名称:Celeron E3400  \nマイクロアーキテクチャ:Core(Wolfdale) \nソケット名:LGA775  \nコア数/スレッド数:2/2  \nクロック:2.6GHz')
                return
            if 'eleron' in message.content and 'E3500.' in message.content or 'SLGTY' in message.content:
                await message.channel.send('名称:Celeron E3500  \nマイクロアーキテクチャ:Core(Wolfdale) \nソケット名:LGA775  \nコア数/スレッド数:2/2  \nクロック:2.7GHz')
                return














            if 'entium' in message.content and 'G5400.' in message.content or 'SR3X9' in message.content:
                await message.channel.send('名称:Pentium Gold G5400   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:2/4  \nベース:3.70GHz') 
                return
            if 'entium' in message.content and 'G5400T.' in message.content or 'SR3XB' in message.content:
                await message.channel.send('名称:Pentium Gold G5400T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:2/4  \nベース:3.10GHz') 
                return
            if 'entium' in message.content and 'G5420.' in message.content or 'SR3XA' in message.content:
                await message.channel.send('名称:Pentium Gold G5420   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:2/4  \nベース:3.80GHz') 
                return
            if 'entium' in message.content and 'G5420T.' in message.content or 'SR3XC' in message.content:
                await message.channel.send('名称:Pentium Gold G5420T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:2/4  \nベース:3.20GHz')
                return
            if 'entium' in message.content and 'G5500.' in message.content or 'SR3YD' in message.content:
                await message.channel.send('名称:Pentium Gold G5500   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:2/4  \nベース:3.80GHz') 
                return
            if 'entium' in message.content and 'G5500T.' in message.content or 'SR3YE' in message.content:
                await message.channel.send('名称:Pentium Gold G5500T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:2/4  \nベース:3.20GHz') 
                return
            if 'entium' in message.content and 'G5600.' in message.content or 'SR3YB' in message.content:
                await message.channel.send('名称:Pentium Gold G5600   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:2/4  \nベース:3.90GHz') 
                return
            if 'entium' in message.content and 'G5600T.' in message.content or 'SR3YF' in message.content:
                await message.channel.send('名称:Pentium Gold G5600T   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:2/4  \nベース:3.30GHz') 
                return
            if 'entium' in message.content and 'G5620.' in message.content or 'SR3YC' in message.content:
                await message.channel.send('名称:Pentium Gold G5620   \nマイクロアーキテクチャ:Coffee Lake \nソケット名:LGA1151-2  \nコア数/スレッド数:2/4 \nベース:4.00GHz')
                return

            if 'eleron' in message.content and '1610.' in message.content or 'SR10K' in message.content:
                await message.channel.send('名称:Cereron G 1610   \nマイクロアーキテクチャ:Ivy Bridge  \nソケット名:LGA1155  \nコア数/スレッド数:2/2  \nクロック:2.6GHz') 
                return






        
        #await message.channel.send('登録されていない型番。次のことを確認してください\n＞ピリオドの打ち忘れ\n＞英語が小文字\n＞全角入力している')
    await bot.process_commands(message)

@bot.command()
async def poop(ctx,arg):
    await ctx.send('%s、まじうんこ！！！！%sはガチでうんこ！！！普通のうんこを超えしエクストリームハイパーうんこ！！！スペシャルスーパーゴールデンうんこ！！！' % (arg,arg,))
@bot.command()
async def god(ctx,arg):
    await ctx.send('%s、まじ神！！！！%sはガチで神！！！普通の神を超えしエクストリームハイパー神！！！スペシャルスーパーゴールデン神！！！' % (arg,arg,))
@bot.command()

async def custom(ctx,arg1,arg2):
    await ctx.send('%s、まじ%s！！！！%sはガチで%s！！！普通の%sを超えしエクストリームハイパー%s！！！スペシャルスーパーゴールデン%s！！！' % (arg1,arg2,arg1,arg2,arg2,arg2,arg2,))





@bot.command()

async def tweet(ctx,arg1):




    consumer_key="8DJbuI9dUTBW9TObrPdAKKHfJ"
    consumer_secret="Be5E7hM3xI3KRJMlwGFgvuxb3Lp0GJH9ZUKz4C6GtEDKBzl2O3"
    token="1142721964911448069-LmvD4qv58swY0waZmqAzBHj8rAxlB4"
    token_secret="yNO79K47d0MjzYzMqYTP54PPATIPt7EhEsYiX1ssHQG7D"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)

    api = tweepy.API(auth)
    
    api.update_status(arg1)
    await ctx.send('---ツイートしました---\n')
    await ctx.send(arg1)


@bot.command()   
async def reply(ctx , arg1):




    consumer_key="8DJbuI9dUTBW9TObrPdAKKHfJ"
    consumer_secret="Be5E7hM3xI3KRJMlwGFgvuxb3Lp0GJH9ZUKz4C6GtEDKBzl2O3"
    token="1142721964911448069-LmvD4qv58swY0waZmqAzBHj8rAxlB4"
    token_secret="yNO79K47d0MjzYzMqYTP54PPATIPt7EhEsYiX1ssHQG7D"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)
    
    l = ["katmai_","pprn_227","kuromochisan","okakimochipc","aiueokakimochi","Siraisi_Ch","IFG250455","Osatu_R_LFA10","KumaAyasa"]
    if arg1 == "random":
        idname = random.choice(l)
    else:
        if arg1 in l:
            idname = arg1
        else:
            await ctx.send('そのIDには送れません。作成者にリストに追加してもらってください。')
            return
        
    texts = ["やぁ！","くぁｗせｄｒｆｔｇｙふじこｌｐ","なんかdiscoで命令されたのでリプしてみよーっと！俺は悪くない！","ぷーぷ","︎︎"]
    reply_text = random.choice(texts)

    
    results = api.user_timeline(screen_name=idname, count=1,exclude_replies="true",include_rts="false")

    for result in results:
        if result.id not in id_list:
            print(result.id)
            print(result.created_at)
            print(result.text)
            print()
            rep_id = result.id
            tweet_rep = "@" + idname + " " + reply_text
            api.update_status(status=tweet_rep,in_reply_to_status_id=rep_id)
            id_list.append(result.id)
            if len(id_list) > 40:
                del id_list[0]
            await ctx.send('@%sにリプを飛ばしました。'%(idname))
        else:
            await ctx.send('@%sの最新ツイートはすでにリプ済みです。'%(idname))



@bot.command()   
async def pf(ctx , arg1):
    n = int(arg1)
    factor = []
    #2から√n以下の数字で割っていく
    tmp = int(math.sqrt(n)) + 1
    for num in range(2,tmp):
        while n % num == 0:
            n //= num
            factor.append(num)


    if not factor:
        await ctx.send('prime number')
    else:
        factor.append(n)
        await ctx.send(factor) 

#    c = collections.Counter(prime_factorize(arg1))
#    await ctx.send(arr)    


    
bot.run(TOKEN)
