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
bot_prefix = config.bot_prefix
default_game = "null"

@bot.event
async def on_ready():
    print('Music User connected')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------')

@bot.command(pass_context=True, aliases=['h'])
async def helpme(ctx):
    await ctx.send(embed=config.embed)

bot.run(config.token)
