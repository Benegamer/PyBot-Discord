#imports
import discord
from discord.ext import commands
from discord.utils import get
import setup
import config

setup.minimal

if setup.debug == True:
    print("==================================")
    print("Token: " + config.token)
    print("Prefix: " + config.bot_prefix)
    print("==================================")


bot = commands.Bot(command_prefix=config.bot_prefix)
BOT_PREFIX = config.bot_prefix

@bot.event
async def on_ready():
    print('Music User connected')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------')

bot.run(config.token)
