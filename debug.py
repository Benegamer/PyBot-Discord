import main
import setup
import config
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
        return
    else:
        print(printme)


if setup.debug == True:
    print("==================================")
    print("Token: " + config.token)
    print("Prefix: " + config.bot_prefix)
    print("Default game:" + main.default_game )
    print("==================================")
