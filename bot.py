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
client.run('')



