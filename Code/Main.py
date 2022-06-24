import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext  
import random


list = '프랑키 검은수염 아오키지 상디 아카이누 키자루 루치 타시기 로우 샹크스 나미 시라호시 스네이크맨 브룩 키드 빅맘 드래곤 시키 제트 센고쿠 미호크 비비 에이스 핸콕 오뎅 갓에넬 시노부 레드필드'
list = list.split()



prefix = "접두사를 정해주세요!"
token = "토큰을 입력해주세요!"




bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
  print('로딩완료')
  await bot.change_presence(activity=discord.Game("/docs"))


@slash.slash(name="밴살",description="",guild_ids=[919390564363931738])
async def 밴살(ctx, 갯수 : int):
  random.shuffle(list)

  a = 0
  text = "```\n"
  tex2 = "\n```"
  for i in list:
    if a == 갯수:
      await ctx.send(text + tex2)
      return None
    text = text + " " + list[a]
    a += 1


bot.run(token)
