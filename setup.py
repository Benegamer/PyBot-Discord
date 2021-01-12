# Include modules
import sys
import json

global debug
global minimal

debug = False
minimal = False

#Function
def Default_settings():
    # Data to be written
    dictionary = {
        "token": "Put your Token here!",
        "prefix": "Put your Prefix here!",
        "admin_id": "Put the Admin ID here!"
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=3)

    # Writing to sample.json
    with open("config.json", "w") as outfile:
        outfile.write(json_object)


# Get arguments
full_cmd_arguments = sys.argv

# cut
argument_list = full_cmd_arguments[1:]
if argument_list == ['--debug']:
    print("Setting debug = True")
    print("Starting main")
    debug = True
elif argument_list == ['--minimal']:
    print("Setting minimal start to True")
    print("Starting main")
    minimal = True
elif argument_list == ['--settings']:
    print("Generating default Settings!")
    Default_settings()
    sys.exit(1)
else:
    print("Starting normal with no arguments")
    print("Starting main")