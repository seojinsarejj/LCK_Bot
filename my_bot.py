import asyncio, discord
from discord.ext import commands
from lckschedule import LckSchedule 

import os 
import json

token_path = os.path.dirname( os.path.abspath(__file__)) + "/config.json"
t = open(token_path,"r", encoding="utf-8")
token = json.loads(t.read())['token']


game = discord.Game("명령어 : 도구야")

bot = commands.Bot(command_prefix='도구야 ', status=discord.Status.online,activity=game)

lckschedule = LckSchedule()

@bot.event
async def on_ready():
    print('봇 시작')

@bot.command()
async def 오늘LCK(ctx):
        
    embed=discord.Embed(title="LCK 오늘 일정", color=0x00ff56)
    schedule = lckschedule.today_schedule()
    for i in range(len(schedule)):
        embed.add_field(
            name=schedule[i]["time"], 
            value= schedule[i]["team1"]+" VS "+schedule[i]["team2"],
            inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def 이번주LCK(ctx):
        
    embed=discord.Embed(title="LCK 이번주 일정", color=0x00ff56)
    schedule = lckschedule.week_schedule()
    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            embed.add_field(
                name=schedule[i][j]["date"],
                value= schedule[i][j]["time"] + " - " + schedule[i][j]["team1"]+" VS "+ schedule[i][j]["team2"],
                inline=False)

    await ctx.send(embed=embed)




bot.run(token)

