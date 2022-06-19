import sys
import configparser
from guizero import *
import subprocess
from PIL import Image
import os

argv = sys.argv
argc = len(sys.argv)
home_path = os.getenv("HOME")
mesaconfigur = configparser.ConfigParser()
mesaread = mesaconfigur.read(home_path+"/.thunder/mesa.cfg")
mesa32 = mesaconfigur.get("mesa","ARMHF")
mesa64 = mesaconfigur.get("mesa","ARM64")
mesaon = mesaconfigur.get("mesa","ON")
galliumon = mesaconfigur.get("mesa","GALLIUM_HUD")
gallium = open(home_path+"/.thunder/gallium.cfg", "r")
gallium_args = gallium.read()
gallium.close()

if argc == 2:
    args = ""
    if galliumon == "ON":
        args += " GALLIUM_HUD="+gallium_args+" "
    if mesaon == "1":
        args += " LD_LIBRARY_PATH=$LD_LIBRARY_PATH:"+mesa64+":"+mesa32+" "
    configur = configparser.ConfigParser()
    configur.read(argv[1])
    name = configur.get("Game","NM")
    exec = configur.get("Game","ID")
    icon = configur.get("Game","CV")
    runner = configur.get("Game","RN")
    def gamerun():
        if runner == "linux":
            command = f''+args+' '+exec
        if runner == "wine":
            command = f''+args+' wine '+exec
        if runner == "steam":
            command = f''+args+' steam steam://rungameid/'+exec
        if runner == "browser":
            command = f''+args+' x-www-browser '+exec
        if runner == "flatpak":
            command = f''+args+' flatpak run '+exec
        if runner == "mednafen":
            command = f''+args+' mednafen '+exec
        process = subprocess.Popen(command, stderr=True, stdout=True, shell=True)
    app = App(title="Thunder - "+name, width=600,bg="white")
    app.icon = icon
    PushButton(app,text="Run Game...",command=gamerun,align="bottom")
    cover = Image.open(icon)
    cover_pic = Picture(app, image=cover, align="top", height=308, width=220)
    Text(app, text=name)
    Text(app, text="Platform: "+runner)
    app.display()
    print("\n")
