# Include modules
import sys
import os
import subprocess

global debug
global minimal

debug = False
minimal = False

# Get arguments
full_cmd_arguments = sys.argv

# cut
argument_list = full_cmd_arguments[1:]
if argument_list == ['--debug']:
    print("Setting debug = True")
    print("Starting main")
elif argument_list == ['--minimal']:
    print("Setting minimal start to True")
    print("Starting main")
else:
    print("Starting normal with no arguments")
    print("Starting main")