#imports
import discord
from discord.ext import commands
from discord.utils import get
import setup
import config
import datetime
import debug

bot = commands.Bot(command_prefix=config.bot_prefix)
bot_prefix = config.bot_prefix
default_game = ""
username = ""
userid = ""

@bot.event
async def on_ready():
    print('User connected:')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------')
    username = bot.user.name
    botid = bot.user.id

#===============================================================================================
#Text commands
#===============================================================================================
@bot.command(pass_context=True, aliases=['h'])
async def helpme(ctx):
    #debug.printme(f"Send help to {ctx.message.author}")
    await ctx.send(embed=config.embed)
#===============================================================================================

#@bot.command(pass_context=True, aliases=['r'])
#async def room(ctx):
#   closetime = time.asctime() #doesnt work! Str is included
#   time = 1
#   person = 8
#
#   Create Temporary room for 1H, create for x amount of persons
#   !room --1h --2p

@bot.command(pass_context=True, aluases=['t'])
async def time(ctx):
    await ctx.send(f"""Wir haben {datetime.datetime.now().time()} Uhr""")
#===============================================================================================
#config.default_game
#discord.Game(default_game)




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
            debug.printme(f"Join to {ctx.message.author} in channel {channel}")

        await ctx.send(f"Joined {channel}")
    except:
        print(Exception)
        await ctx.send(Exception + "Something is wrong I can feel it!")

@bot.command(pass_context = True, aliases=['l'])
async def leave(ctx):
    try:
        await ctx.voice_client.disconnect()
        debug.printme(f"User {ctx.message.author.id} wants me to go!")
    except:
        await ctx.send(Exception + "Maybe Im not in a Channel? ")
#===============================================================================================
bot.run(config.token)