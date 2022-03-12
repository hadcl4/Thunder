#!/bin/env python3
print("Mednagui - Mednafen Frontend")
print("Created under the Hadcl4 Studios Open-Source License")
from guizero import *
import subprocess
def default_config():
    print("Setting config to default...")
    command = f'/home/$USER/Thunder/emulators/mednagui/settings --default'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def edit_settings():
    print("Editing settings...")
    command = f'gnome-terminal --window --command="/home/$USER/Thunder/emulators/mednagui/settings --edit"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def emusettings():
    print("Configuring settings...")
    ask = Window(app, title="Mednagui - Settings", bg="white", width=600, height=400)
    asktitle = Text(ask, text="Settings", font="Ubuntu", size=45)
    asktext = Text(ask, text="Do you want to edit settings or set them to default?", width=45, font="Ubuntu")
    askbuttona = PushButton(ask, text="Edit Config",command=edit_settings)
    askbuttonb = PushButton(ask, text="Set Config to Default",command=default_config)
def runrom():
    print("Running ROM...")
    if options.value == "-yourargument":
        command = f'mednafen '+pathenter.value
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    else:
        command = f'mednafen '+options.value+' '+pathenter.value
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
app = App(title="Mednagui - Mednafen Frontend", bg="white", width=600)
title = Text(app, text="Mednagui",size=70,font="Ubuntu")
titlefront = Text(app, text="Mednafen Frontend",size=25,font="Ubuntu")
rompath = Text(app, text="Enter the path to your game ROM:", font="Ubuntu")
pathenter = TextBox(app, text="/path/to/ROM/here",width=45)
specialoptions = Text(app, text="Enter any extra arguments here (leave it as '-yourargument' for none):", font="Ubuntu")
options = TextBox(app, text="-yourargument",width=45)
start = PushButton(app, text="Click here to run ROM.", command=runrom)
licenseinfo = Text(app, text="Created under the Hadcl4 Studios Open-Source License. View LICENSE.md for info.", size=10, color="lightgrey", align="bottom")
settings = PushButton(app, text="Emulator Settings", align="bottom", command=emusettings)
app.display()
