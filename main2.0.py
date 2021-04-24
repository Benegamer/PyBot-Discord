# Imports
import asyncio
import discord
from discord.ext import commands
import youtube_dl
import random
import os
from datetime import datetime, timedelta
from pytz import timezone
import pytz

# Va
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
    'source_address': '0.0.0.0'  # bind to ipv4 since ipv6 addresses cause issues sometimes
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


# get bot_prefix form ENV
bot_prefix = os.environ['PREFIX']

# get token from ENV
token = os.environ['TOKEN']

# set env for Bot
bot = commands.Bot(command_prefix=bot_prefix)


#########################################################################################
@bot.event
async def on_ready():
    print('User connected:')
    print(bot.user.name)
    print(bot.user.id)
    print('---------------')
    await bot.change_presence(activity=discord.Game("!h for Help!"))
    pytz.timezone("UTC")


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}! See the: "{bot_prefix}help" command for details!')


#########################################################################################
# Botcommands


@bot.command(aliases=['t'], name="time", help='Get the current time')
async def time(ctx):
    utc_time = datetime.utcnow()
    tz = pytz.timezone('Europe/Berlin')

    utc_time = utc_time.replace(tzinfo=pytz.UTC)
    now = utc_time.astimezone(tz)

    current_time = now.strftime("%H:%M:%S")
    print(f"""Wir haben {current_time} Uhr""")


@bot.command(aliases=['f'], name="flip", help='Flip a coin')
async def flip(ctx):
    ran = random.randint(0, 10)
    if ran in range(0, 5):
        await ctx.send(":new_moon: ")
    else:
        await ctx.send(":full_moon:")


@bot.command(aliases=['b'], name="bug", help='Bugreports and other thinks:')
async def flip(ctx):
    await ctx.send('Please go to https://github.com/Benegamer/PyBot-Discord')


#########################################################################################
# Music


@bot.command(aliases=['purl'], name="playurl", help='Play a song with an url')
async def playurl(ctx, url):
    if not ctx.message.author.voice:
        await ctx.send("Your are not connected to a voice channel")
        return

    else:
        channel = ctx.message.author.voice.channel

    if ctx.voice_client == None:
        await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client
    ##Credit to SoftwareStep
    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=bot.loop)
        try:
            voice_channel.stop()
        except:
            pass
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

        await ctx.send(f'**Now playing:**{player.title}')


@bot.command(aliases=['j'], name='join', help='Joins to yor channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return

    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()


@bot.command(name='play', help='Play songs from the queue')
async def play(ctx):
    global queue

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(queue[0], loop=bot.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))
    del (queue[0])

    if queue:
        await ctx.send("!play")


@bot.command(aliases=['q'], name='queue', help='Add a song to the Queue')
async def queue_(ctx, url):
    global queue

    queue.append(url)
    await ctx.send(f'`{url}` added to queue!')


@bot.command(aliases=['l'], name="leave", help='Makes the Bot go away')
async def stop(ctx):
    if ctx.author.voice is None:
        await ctx.send("Im not in a channel ")
        return
    await ctx.voice_client.disconnect()


@bot.command(name='remove', help='Remove a song from the Queue')
async def remove(ctx, number):
    global queue

    try:
        del (queue[int(number)])
        await ctx.send(f'Your queue is now `{queue}!`')

    except:
        await ctx.send('Your queue is either **empty** or the index is **out of range**')


@bot.command(aliases=['m'], name='pause', help='Pause the current song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()


@bot.command(aliases=['r'], name='resume', help='Resume the current song')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()


@bot.command(aliases=['s'], name='stop', help='Stops the current song')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()


@bot.command(aliases=['v'], name='view', help='Shows the queue')
async def view(ctx):
    await ctx.send(f'Your queue is now `{queue}!`')


# Startup
bot.run(token)
