import asyncio
import discord
import random
import youtube_dl
from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("We have loggedd in as {0.user}".format(bot))


@bot.command(aliases=['도움말', 'h'])
async def 도움(ctx):
    embed = discord.Embed(title="mokoko_bot", description="모코코 봇입니다.", color=0x4432a8)
    embed.add_field(name="1. 인사", value="!hello", inline=False)
    embed.add_field(name="2. 응애", value="!응애", inline=False)
    embed.add_field(name="3. 테에엥", value="!테에엥", inline=False)
    # embed.add_field(name="2. 주사위", value="!roll [범위숫자]", inline=False)
    # embed.add_field(name="3. 음성채널 입장/퇴장", value="!join / !leave (초대자가 입장된 상태에만 가능)", inline=False)
    # embed.add_field(name="4. 음악", value="!play [Youtube URL] : 음악을 재생\n!pause : 일시정지\n!resume : 다시 재생\n!stop : 중지", inline=False)
    await ctx.send(embed=embed)


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
async def 주사위(ctx):
    await ctx.send("주사위를 굴립니다.")
    a = random.randrange(1, 7)
    b = random.randrange(1, 7)
    if a > b:
        await ctx.send("패배")
        await ctx.send("봇의 숫자: " + str(a) + " 당신의 숫자: " + str(b))
    elif a == b:
        await ctx.send("무승부")
        await ctx.send("봇의 숫자: " + str(a) + " 당신의 숫자: " + str(b))
    elif a < b:
        await ctx.send("승리")
        await ctx.send("봇의 숫자: " + str(a) + " 당신의 숫자: " + str(b))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다")


bot.run("OTE1MjkyNTQ2MjgyOTUwNzE2.YaZenA.RjLpk1tXmWtnYERur0OYMgT9yY8")
