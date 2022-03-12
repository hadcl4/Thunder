#!/usr/bin/python
import sys
import os
from os.path import expanduser

user = sys.argv[1]

desktop_content = "[Desktop Entry]\nName=melonDS\nComment=DS Emulator, Sorta\nExec=/home/"+user+"/melonDS_Pi/launcher\nIcon=/home/"+user+"/melonDS_Pi/icon.png\nTerminal=false\nType=Application\nCategories=Game;\nStartupNotify=true"

file_dir = "/usr/share/applications/melonds.desktop"

f = open(file_dir, "w+")
f.write(desktop_content)
f.close
