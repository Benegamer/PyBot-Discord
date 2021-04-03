#Imports
import datetime
import discord
from discord.ext import commands
from discord.utils import get
import json

#Va
default_game = "!helpme for personal help"

#read json for token prefix and adminid
def read_json():
    try:
        # Opening JSON file
        with open('config.json', 'r') as openfile:
            # Reading from json file
            data = json.load(openfile)
            global token
            token = (data['token'])

            global bot_prefix
            bot_prefix = (data['prefix'])

            global admin_id
            admin_id = (data['admin_id'])
    except:
        print("Somethin went wrong! I can feel it! \n")

read_json()
#set env for Bot
bot = commands.Bot(command_prefix=bot_prefix)
bot_prefix = bot_prefix

#embed for help
embed = discord.Embed(
    title="Hallo World",
    color=0xe67e22,
    description="Help Bot\n"
                "Dies ist der !h befehl\n"
)
embed.set_author(
    name="Benegamer",
)
embed.add_field(
    name="Befehle",
    value="Dies sind alle Befehle, das Prefix ist " + bot_prefix + "\n"
          "...",
    inline=False
)
embed.add_field(
    name="Dieser Bot wurde von Benegamer geschrieben",
    value="Bei Bugs ihn anschreiben !",
    inline=False
)

@bot.event
async def on_ready():
    print('User connected:')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------')
    username = bot.user.name
    botid = bot.user.id

#Botcommands
@bot.command(pass_context=True, aliases=['h'])
async def helpme(ctx):
    #debug.printme(f"Send help to {ctx.message.author}")
    await ctx.send(embed=embed)


@bot.command(pass_context=True, aliases=['t'])
async def time(ctx):
    await ctx.send(f"""Wir haben {datetime.datetime.now().time()} Uhr""")


#Music
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

        await ctx.send(f"Joined {channel}")
    except:
        print(Exception)
        await ctx.send(Exception + "Something is wrong I can feel it!")

@bot.command(pass_context = True, aliases=['l'])
async def leave(ctx):
    try:
        await ctx.voice_client.disconnect()
    except:
        await ctx.send(Exception + "Maybe Im not in a Channel? ")

#Startup
bot.run(token)