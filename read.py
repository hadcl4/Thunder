import sys
import configparser
from guizero import *
import subprocess
from PIL import Image

argv = sys.argv
argc = len(sys.argv)

if argc == 2:
    configur = configparser.ConfigParser()
    configur.read(argv[1])
    name = configur.get("Game","NM")
    exec = configur.get("Game","ID")
    icon = configur.get("Game","CV")
    runner = configur.get("Game","RN")
    def gamerun():
        if runner == "linux":
            command = f''+exec
        if runner == "wine":
            command = f'wine '+exec
        if runner == "steam":
            command = f'steam steam://rungameid/'+exec
        if runner == "browser":
            command = f'x-www-browser '+exec
        if runner == "flatpak":
            command = f'flatpak run '+exec
        if runner == "mednafen":
            command = f'mednafen '+exec
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
