import discord
from discord.ext import commands
client = commands.Bot(command_prefix="+")
@client.event
async def on_ready():
    print("bot is ready")
@client.command ()
async def hello(a):
    z='hi'
    await a.send(z)
client.run('ODUwNzI3Nzk3NDM3NzU5NTA4.YLt8AA.3Tchf1CDMbev0pFM4AvDtAWOins')



