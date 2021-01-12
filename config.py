#imports
import discord
import json

#v
global token
global bot_prefix
global admin_id


def read_json():
    try:
        # Opening JSON file
        with open('config.json', 'r') as openfile:
            # Reading from json file
            data = json.load(openfile)

            token = (data['token'])

            bot_prefix = (data['bot_prefix'])

            admin_id = (data['admin_id'])
    except:
        print("Somethin went wrong! I can feel it! \n")
        print("Maybe run with '--settings'")

############################################################################
#helpembed
############################################################################

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
    value="Dies sind alle Befehle, das Prefix ist !\n"
          "COMMING SOON! play Yt url !!!Es gehen NUR Yt urls!!!\n"
          "COMMING SOON! pause um das Lied zu Pausieren\n"
          "COMMING SOON! resume zum weiteren Wiedergeben des Liedes\n"
          "leave / l dammit der Bot den Channel verläst\n"
          "COMMING SOON! uptime um die online Zeit des Bot zu sehen",
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


############################################################################
#Game Stuff
############################################################################
default_game = "!helpme for personal help"
