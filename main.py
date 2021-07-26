# base libraries
from datetime import datetime
import os
from sqlite3.dbapi2 import Timestamp

# installed libraries
import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

# custom libraries
from santoral import Santoral

# Definitions
santoral=Santoral("./db/db.db")

bot=commands.Bot(command_prefix="!", description="this is a jarf's helper bot")

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Hola que hace", url="https://www.youtube.com/watch?v=lcYJhHqotIQ"))
    # use this to generate and keep logs
    print("Hey everyone! I'm online now")

## Commands
# assist-commands
@bot.command()
async def onomastico(ctx,fecha=None):
    message=santoral.saludaSanto(fecha)
    embed=discord.Embed(title="Santoral del día",description=message, timestamp=datetime.utcnow(),color=0xebb734)
    await ctx.send(embed=embed)

# Debugg-commands
@bot.command()
async def info(ctx):
    embed=discord.Embed(title=f"{ctx.guild.name}",description="Lorem impsum", timestamp=datetime.utcnow(),color=0xebb734)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send('pong!')


DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
bot.run(DISCORD_BOT_TOKEN)
