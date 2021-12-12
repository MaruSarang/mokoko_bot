import time
import random
import asyncio
import discord
import requests
import youtube_dl
from discord.ext import commands
from bs4 import BeautifulSoup

"""
 음성인식 
 import speech_recognition as sr
 sr.__version__ 
 r = sr.Recognizer()
"""
bot = commands.Bot(command_prefix="!")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
base_url = 'https://loawa.com/char/%EC%A0%84%EC%9E%90%EB%A7%88%EB%A3%A8'

# 로그인

@bot.event
async def on_ready():
    print("We have loggedd in as {0.user}".format(bot))

# 봇 명령어

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

@bot.command()
async def 응애(ctx):
    await ctx.send("응애")

@bot.command()
async def 테에엥(ctx):
    await ctx.send("테에엥")

@bot.command()
async def test(ctx):
    await ctx.send(":test:")

@bot.command()
async def 로하(ctx):
    await ctx.send("로하~!")

@bot.command()
async def 전자마루(ctx):
    await ctx.send("https://loawa.com/char/%EC%A0%84%EC%9E%90%EB%A7%88%EB%A3%A8")

@bot.command()
async def 테스트(ctx):
    await ctx.send(":maru:")

# 봇 노래 틀기

@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel

    #음성채널 입장

    if bot.voice_clients == []:
        await channel.connect()
        await ctx.send("음성채널에 입장했습니다, " + str(bot.voice_clients[0].channel))

    my_song = []
    song_list = []
    #노래 정보 받기

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        play_link = info['formats'][0]['url']
    song_list.append(play_link)
    title = info['title']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(song_list[0], **FFMPEG_OPTIONS))

    my_song.append(title) # title을 my_song에 저장함
    my_song.append(100) # my_song에 100을 추가하고 !queue를 입력하니['88', 100] 가 출력됨. 정상
    # 결국 노래 목록들을 못받아와서 막힌거
    my_song.append(200)
    # print(my_song,type(my_song))
    # print(song_list,type(song_list))

    f_my_song_0 = my_song[0]
    f_my_song_1 = my_song[1:]
    # @bot.command()
    # async def queue(ctx):
    #     await ctx.send(f'현재 재생중인 곡은 " + {f_my_song_0} + "입니다.')
    #     await ctx.send(f'{f_my_song_1}')
    #     print(type(f_my_song_0))
    #     print(type(f_my_song_1))

    @bot.command(aliases=['queue'])
    async def playlist(ctx):
        embed = discord.Embed(title = "현재 재생곡\n\n" + my_song[0], description="", color=0x4432a8)

        embed.add_field(name="1." + str(my_song[1]), value="value를 입력해야 합니다.", inline=False)
        embed.add_field(name="2." + str(my_song[2]), value="value를 입력해야 합니다.", inline=False)
        # embed.add_field(name="3." + str(my_song[3]), value="", inline=False)
        await ctx.send(embed=embed)


@bot.command()
async def pause(ctx):
    if not bot.voice_clients[0].is_paused():
        bot.voice_clients[0].pause()
        await ctx.send("노래를 일시정지 했습니다.")
    else:
        await ctx.send("이미 일시정지 되어있습니다.")


@bot.command()
async def resume(ctx):
    if bot.voice_clients[0].is_paused():
        bot.voice_clients[0].resume()
        await ctx.send("노래를 다시 재생했습니다.")
    else:
        await ctx.send("이미 재생중입니다.")


@bot.command()
async def stop(ctx):
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()
        await ctx.send("노래를 정지하였습니다.")
    else:
        await ctx.send("재생중인 노래가 없습니다.")

# 실시간 모코코 갯수 체크 #

@bot.command()
async def 모코코(ctx):

    while True :
        i = []
        try:
            json_string = requests.get(base_url, headers=headers)
        except :
            time.sleep(3)
            continue
        if json_string.status_code != 200:
            time.sleep(3)
            continue
        soup = BeautifulSoup(json_string.content, 'html.parser')
        mokoko = soup.find(attrs = {'class': 'd-none d-lg-block p-1 text-center'}).text[:]

        i.append(mokoko)

        await ctx.send("지금까지 " + i[0] +"개의 모코코를 모았어요!")
        break

# 모코코 음성인식 #
#
# mokoko = sr.AudioFile('mokoko.wav')
# with mokoko as source:
#     audio = r.record(source)
# type(audio)


@bot.command()
async def leave(ctx):
    await bot.voice_clients[0].disconnect()

@bot.command()
async def 주사위(ctx):
    await ctx.send("주사위를 굴립니다.")
    a = random.randrange(1, 7)
    # b = random.randrange(1, 7)
    await ctx.send("주사위를 굴려서 " + str(a) +"가 나왔습니다.")



@bot.command()
async def 로또(ctx) :
    lotto_count = 0
    while lotto_count < 6 :
        lotto_count = lotto_count + 1
        lotto_number = random.randrange(1, 46)

        await ctx.send(f"로또 번호 {lotto_count}번째 숫자는 {lotto_number} 입니다.")


    # if a > b:
    #         await ctx.send("패배")
    #         await ctx.send("봇의 숫자: " + str(a) + " 당신의 숫자: " + str(b))
    #     elif a == b:
    #         await ctx.send("무승부")
    #         await ctx.send("봇의 숫자: " + str(a) + " 당신의 숫자: " + str(b))
    #     elif a < b:
    #         await ctx.send("승리")
    #         await ctx.send("봇의 숫자: " + str(a) + " 당신의 숫자: " + str(b))

@bot.command(aliases=['도움말', 'h'])
async def 도움(ctx):
    embed = discord.Embed(title="mokoko_bot", description="모코코 봇입니다.", color=0x4432a8)
    embed.add_field(name="1. 인사", value="!hello", inline=False)
    embed.add_field(name="2. 응애", value="!응애", inline=False)
    embed.add_field(name="3. 테에엥", value="!테에엥", inline=False)
    # embed.add_field(name="2. 주사위", value="!roll [범위숫자]", inline=False)
    # embed.add_field(name="3. 음성채널 입장/퇴장", value="!join / !leave (초대자가 입장된 상태에만 가능)", inline=False)
    embed.add_field(name="4. 음악", value="!play [Youtube URL] : 음악을 재생\n!pause : 일시정지\n!resume : 다시 재생\n!stop : 중지", inline=False)
    await ctx.send(embed=embed)


# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send("명령어를 찾지 못했습니다")


bot.run("")
