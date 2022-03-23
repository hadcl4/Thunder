#!/usr/bin/python
import sys
import os
from os.path import expanduser

user = sys.argv[1]
dir_path = os.path.dirname(os.path.realpath(__file__))

f_content = "[Desktop Entry]\nName=Thunder\nComment=Thunder makes using your ARM SBC as a Gaming PC easy and simple. With all your PC games in one place, easily run any game for almost any platform.\nExec="+dir_path+"/start\nIcon="+dir_path+"/logo.png\nTerminal=false\nType=Application\nCategories=Game;\nStartupNotify=false"

x_dir = "/usr/share/applications/thunder.desktop"

f2 = open(x_dir, "w+")
f2.write(f_content)
f2.close
