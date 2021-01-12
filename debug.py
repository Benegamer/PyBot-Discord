import setup
import config
import main
import json

#initzialising  #setting default
botname = 'DEFAULT NAME'
botid = 'DEFAULT ID'

#overwrite
botname = main.username
botid = main.userid

def printme(printme):
    print(setup.debug)

if setup.debug == True:
    print(f"The bot {botname} with the id {botid} just performed an action!")
    print(f"The action is:")
    print(printme)
elif setup.minimal == True:
    print("\n")
else:
    print(printme)


if setup.debug == True:

    print("==================================")
    print("Token: " + config.token)
    print("Prefix: " + config.bot_prefix)
    print("Default game:" + main.default_game )
    print("==================================")

    try:
        # Opening JSON file
        with open('config.json', 'r') as openfile:
            # Reading from json file
            data = json.load(openfile)
            print(data= json.load(openfile))
            token = (data['token'])

            bot_prefix = (data['bot_prefix'])

            admin_id = (data['admin_id'])
    except:
        print("Somethin went wrong with your Settings! I can feel it! \n")
        print("Maybe run with '--settings'")