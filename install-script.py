#Setup script
import json
import sys

def write_json():
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

print("Setup complete! I did:")
write_json()
sys.exit(1)
