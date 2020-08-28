#imports
import discord
from discord.ext import commands
from discord.utils import get
import setup
import config
import time

if setup.debug == True:
    print("==================================")
    print("Token: " + config.token)
    print("Prefix: " + config.bot_prefix)
    print("==================================")

def printme(printme):
    print(setup.debug)
    if setup.debug == True:
        print(f"The bot {bot.user.name} with the id {bot.user.id} just performed an action!")
        print(f"The action is:")
        print(printme)
    elif setup.minimal == True:
        return
    else:
        print(printme)

bot = commands.Bot(command_prefix=config.bot_prefix)
bot_prefix = config.bot_prefix
default_game = "null"

@bot.event
async def on_ready():
    print('Music User connected')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------')

#===============================================================================================
#Text commands
#===============================================================================================
@bot.command(pass_context=True, aliases=['h'])
async def helpme(ctx):
    printme(f"Send help to {ctx.message.author}")
    await ctx.send(embed=config.embed)

#@bot.command(pass_context=True, aliases=['r'])
#async def room(ctx):
#   closetime = time.asctime() #doesnt work! Str is included
#   time = 1
#   person = 8
#
#   Create Temporary room for 1H, create for x amount of persons
#   !room --1h --2p

#===============================================================================================
#Music stuff
#===============================================================================================
@bot.command(pass_context = True, aliases=['j'])
async def join(ctx):

    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    try:
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
            printme(f"Join to {ctx.message.author} in channel {channel}")

        await ctx.send(f"Joined {channel}")
    except:
        print(Exception)
        await ctx.send(Exception + "Something is wrong I can feel it!")

@bot.command(pass_context = True, aliases=['l'])
async def leave(ctx):
    try:
        await ctx.voice_client.disconnect()
        printme(f"User {ctx.message.author.id} wants me to go!")
    except:
        await ctx.send(Exception + "Maybe Im not in a Channel? ")

bot.run(config.token)
