#Setup script
import json

def write_json():
    # Data to be written
    dictionary = {
        "token": "Put your Token here!",
        "prefix": "Put your Prefix here!",
        #"keep_songs": "True/False"
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=3)

    # Writing to config.json
    with open("config.json", "w") as outfile:
        outfile.write(json_object)

print("Setup complete! I did it!")
write_json()
