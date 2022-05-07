#!/usr/bin/env python3

import os
from guizero import *
import sys

home = os.getenv("HOME")
thunder_version = sys.argv[1]
commit = open(home+"/Thunder/.git/ORIG_HEAD","r").read()

app = App(title="Thunder - Build Info",height=550)
Picture(app, image=home+"/Thunder/logo.gif",height=340,width=340)
Text(app, text="Version: "+thunder_version)
Text(app, text="Commit: "+commit)
Text(app, text="Python Version: "+sys.version)
Text(app, text="Operating System Type: "+os.name)
Text(app, text="_______________________\n")
Text(app, text="License: Hadcl4 Studios Open-Source License")
Text(app, text="Created By: Hadcl4")
app.display()
