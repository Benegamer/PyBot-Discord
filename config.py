#imports
import discord

#v
global token
global bot_prefix

#token
def read_token():
    try:
        with open("token", "r") as tokenn:
            lines = tokenn.readlines()
            return lines[0].strip()
    except:
        print("token file cant be empty")
token = read_token()

#bot_prefix
def read_bot_prefix():
    try:
        with open("prefix", "r") as prefixx:
            lines = prefixx.readlines()
            return lines[0].strip()
    except:
        print("prefix.txt file cant be empty!")

bot_prefix = read_bot_prefix()

#helpembed
embed = discord.Embed(
    title="Hallo World",
    color=0xe67e22,
    description="Herzlich Wilkommen auf meinem Disocrd server\n"
                "Dies ist der !h befehl\n"
)
embed.set_author(
    name="Benegamer",
)
embed.add_field(
    name="Befehle",
    value="Dies sind alle Befehle, das Prefix ist !\n"
          "play Yt url !!!Es gehen NUR Yt urls!!!\n"
          "pause um das Lied zu Pausieren\n"
          "resume zum weiteren Wiedergeben des Liedes\n"
          "quit dammit der Bot den Channel verläst\n"
          "uptime um die online Zeit des Bot zu sehen",
    inline=False
)
embed.add_field(
    name="Bei Fragen einfach fragen",
    value="Wenn es Problem gibt einen Moderator fragen",
    inline=False
)
embed.add_field(
    name="Dieser Bot wurde von Benegamer geschrieben",
    value="Bei Bugs ihn anschreiben !",
    inline=False
)