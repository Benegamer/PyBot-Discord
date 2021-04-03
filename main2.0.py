#Imports
import asyncio
import datetime
import discord
from discord import member  #test
from discord.ext import commands, tasks
from discord.utils import get
import json
import youtube_dl
from random import choice

#Va
default_game = "!helpme for personal help"

queue = []
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

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

#########################################################################################
@bot.event
async def on_ready():
    print('User connected:')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------')
    await bot.change_presence(activity=discord.Game("!h for Help!"))

#########################################################################################
#Botcommands
@bot.command(pass_context=True, aliases=['h'])
async def helpme(ctx):
    #debug.printme(f"Send help to {ctx.message.author}")
    await ctx.send(embed=embed)


@bot.command(pass_context=True, aliases=['t'])
async def time(ctx):
    await ctx.send(f"""Wir haben {datetime.datetime.now().time()} Uhr""")
#########################################################################################
#Music
@bot.command(name='queue')
async def queue_(ctx, url):
    global queue

    queue.append(url)
    await ctx.send(f'`{url}` added to queue!')


@bot.command(name='remove')
async def remove(ctx, number):
    global queue

    try:
        del (queue[int(number)])
        await ctx.send(f'Your queue is now `{queue}!`')

    except:
        await ctx.send('Your queue is either **empty** or the index is **out of range**')


@bot.command(name='play')
async def play(ctx):
    global queue

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(queue[0], loop=bot.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))
    del (queue[0])


@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()

@bot.command(name='resume', help='This command resumes the song!')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()

@bot.command(name='view', help='This command shows the queue')
async def view(ctx):
    await ctx.send(f'Your queue is now `{queue}!`')

@bot.command(name='leave', help='This command stops makes the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@bot.command(name='stop', help='This command stops the song!')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()

#Startup
bot.run(token)