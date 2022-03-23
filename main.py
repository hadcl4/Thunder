#!/usr/bin/env python3

# Attention to developers! This file may look all cluttered, but it uses Guizero, a simple GUI module based on Tk. It should be easy to understand, and for
# non-Guizero commands there are usually comments explaining what they do. If there is something you do not understand, create an issue on the GitHub repo
# and we'll try to explain it to you. Here are some frequently used commands that aren't from Guizero:
# x.write(), x.open(), x.read() - Write to a file, open it, or read it
# def - Define a function
# import - Import a module
# x.close() - Close an opened file
# subprocess - Run an external command (such as a BASH command)
# Lines commented out are outdated code no longer used.
# And this seems like about all. Please look back to this section for reference while editing the file.

global browser

import sys # For file path and various other things
import os # For file path
import subprocess # For external commands
from os.path import expanduser # For file path
from guizero import * # Guizero
from PIL import Image # Python Imaging Library
import tkinter as tk # For using things guizero doesn't have
from configparser import * # For reading config files
import webview # For webpages like Steam, GOG, and Itch

# This is required for file paths
user = sys.argv[1]
section = sys.argv[2]
startupmessageif = sys.argv[3]
home_path = expanduser("~%s" % user)
print("")
print('Thunder currently running under user "'+user+'".')
# Fetch the chosen theme at boot
color = open(home_path+"/.thunder/config.cfg")
bgcolor = color.read()
print("")
print("Current theme:")
print(bgcolor) # Let the user know what theme is currently selected
color.close()
messagestart = open(home_path+"/.thunder/default.txt")
startmessage = messagestart.read()
messagestart.close()

configur = ConfigParser()

pagenumber = open(home_path+"/.thunder/page.cfg")
panum = pagenumber.read()
pagenumber.close()

print("")
print("Window Mode:")
if panum == "y":
    panumy = "Fullscreen"
else:
    panumy = "Windowed"
print(panumy)

print("")
print("News Download:")
newscfg = open(home_path+"/.thunder/news.cfg", "r")
newsread = newscfg.read()
newscfg.close()
if newsread == "y":
    print("Yes")
if newsread == "n":
    print("No")

print("")
print("Startup Message:")
print(startmessage)

librarysizes = open(home_path+"/.thunder/size.cfg")
librarysize = librarysizes.read()
librarysizes.close()

print("Library Icon Size:")
print(librarysize)
print("")

mesaconfigur = ConfigParser()
mesaread = mesaconfigur.read(home_path+"/.thunder/mesa.cfg")
mesa32 = mesaconfigur.get("mesa","ARMHF")
mesa64 = mesaconfigur.get("mesa","ARM64")
mesaon = mesaconfigur.get("mesa","ON")

configy = ConfigParser()

browserchoicy = configy.read(home_path+"/.thunder/browser.cfg")
browserchoices = configy.get("Browser", "NM")

if browserchoices == "Chromium":
    browser = "chromium"
if browserchoices == "Firefox":
    browser = "firefox"
if browserchoices == "Firefox ESR":
    browser = "firefox-esr"
else:
    browser = browserchoices

library = configur.read(home_path+"/.thunder/library.cfg")

# First game in library
libraryoneNM = configur.get("one", "NM")
libraryoneID = configur.get("one", "ID")
libraryoneCV = configur.get("one", "CV")
libraryoneRN = configur.get("one", "RN")
# Second game in library
librarytwoNM = configur.get("two", "NM")
librarytwoID = configur.get("two", "ID")
librarytwoCV = configur.get("two", "CV")
librarytwoRN = configur.get("two", "RN")
# Third game in library
librarythreeNM = configur.get("three", "NM")
librarythreeID = configur.get("three", "ID")
librarythreeCV = configur.get("three", "CV")
librarythreeRN = configur.get("three", "RN")
# Fourth game in library
libraryfourNM = configur.get("four", "NM")
libraryfourID = configur.get("four", "ID")
libraryfourCV = configur.get("four", "CV")
libraryfourRN = configur.get("four", "RN")
# Fifth game in library
libraryfiveNM = configur.get("five", "NM")
libraryfiveID = configur.get("five", "ID")
libraryfiveCV = configur.get("five", "CV")
libraryfiveRN = configur.get("five", "RN")
# Sixth game in library
librarysixNM = configur.get("six", "NM")
librarysixID = configur.get("six", "ID")
librarysixCV = configur.get("six", "CV")
librarysixRN = configur.get("six", "RN")
# Seventh game in library
librarysevenNM = configur.get("seven", "NM")
librarysevenID = configur.get("seven", "ID")
librarysevenCV = configur.get("seven", "CV")
librarysevenRN = configur.get("seven", "RN")
# Eighth game in library
libraryeightNM = configur.get("eight", "NM")
libraryeightID = configur.get("eight", "ID")
libraryeightCV = configur.get("eight", "CV")
libraryeightRN = configur.get("eight", "RN")
# Ninth game in library
librarynineNM = configur.get("nine", "NM")
librarynineID = configur.get("nine", "ID")
librarynineCV = configur.get("nine", "CV")
librarynineRN = configur.get("nine", "RN")
# Tenth game in library
librarytenNM = configur.get("ten", "NM")
librarytenID = configur.get("ten", "ID")
librarytenCV = configur.get("ten", "CV")
librarytenRN = configur.get("ten", "RN")
# 11 game in library
library11NM = configur.get("11", "NM")
library11ID = configur.get("11", "ID")
library11CV = configur.get("11", "CV")
library11RN = configur.get("11", "RN")
# 12 game in library
library12NM = configur.get("12", "NM")
library12ID = configur.get("12", "ID")
library12CV = configur.get("12", "CV")
library12RN = configur.get("12", "RN")
# 13 game in library
library13NM = configur.get("13", "NM")
library13ID = configur.get("13", "ID")
library13CV = configur.get("13", "CV")
library13RN = configur.get("13", "RN")
# 14 game in library
library14NM = configur.get("14", "NM")
library14ID = configur.get("14", "ID")
library14CV = configur.get("14", "CV")
library14RN = configur.get("14", "RN")
# 15 game in library
library15NM = configur.get("15", "NM")
library15ID = configur.get("15", "ID")
library15CV = configur.get("15", "CV")
library15RN = configur.get("15", "RN")
# 16 game in library
library16NM = configur.get("16", "NM")
library16ID = configur.get("16", "ID")
library16CV = configur.get("16", "CV")
library16RN = configur.get("16", "RN")
# 17 game in library
library17NM = configur.get("17", "NM")
library17ID = configur.get("17", "ID")
library17CV = configur.get("17", "CV")
library17RN = configur.get("17", "RN")
# 18 game in library
library18NM = configur.get("18", "NM")
library18ID = configur.get("18", "ID")
library18CV = configur.get("18", "CV")
library18RN = configur.get("18", "RN")
# 19 game in library
library19NM = configur.get("19", "NM")
library19ID = configur.get("19", "ID")
library19CV = configur.get("19", "CV")
library19RN = configur.get("19", "RN")
# 20 game in library
library20NM = configur.get("20", "NM")
library20ID = configur.get("20", "ID")
library20CV = configur.get("20", "CV")
library20RN = configur.get("20", "RN")

# The config menu and restart commands
def restart():
    app.destroy()
    print("Restarting Thunder...")
    command = f'cd ~/Thunder && ./start'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def refreshdown():
    app.destroy()
    print("Restarting Thunder...")
    if section == "1":
        command = f'export LD_PRELOAD="$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0"; cd ~/Thunder && python3 main.py $USER 2 0 > ~/.thunder/thunder.log'
    if section == "2":
        command = f'export LD_PRELOAD="$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0"; cd ~/Thunder && python3 main.py $USER 3 0 > ~/.thunder/thunder.log'
    if section == "3":
        command = f'export LD_PRELOAD="$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0"; cd ~/Thunder && python3 main.py $USER 4 0 > ~/.thunder/thunder.log'
    if section == "4":
        command = f'export LD_PRELOAD="$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0"; cd ~/Thunder && python3 main.py $USER 5 0 > ~/.thunder/thunder.log'
    if section == "5":
        command = f'export LD_PRELOAD="$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0"; cd ~/Thunder && python3 main.py $USER 5 0 > ~/.thunder/thunder.log'
    process = subprocess.Popen(command, stdout=True, stderr=True, shell=True)
def refreshup():
    app.destroy()
    print("Restarting Thunder...")
    if section == '1':
        command = f'export LD_PRELOAD="$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0"; cd ~/Thunder && python3 main.py $USER 1 0 > ~/.thunder/thunder.log'
    if section == "2":
        command = f'export LD_PRELOAD="$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0"; cd ~/Thunder && python3 main.py $USER 1 0 > ~/.thunder/thunder.log'
    if section == "3":
        command = f'export LD_PRELOAD="$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0"; cd ~/Thunder && python3 main.py $USER 2 0 > ~/.thunder/thunder.log'
    if section == "4":
        command = f'export LD_PRELOAD="$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0"; cd ~/Thunder && python3 main.py $USER 3 0 > ~/.thunder/thunder.log'
    if section == "5":
        command = f'export LD_PRELOAD="$LD_PRELOAD:/usr/\$LIB/libgamemodeauto.so.0"; cd ~/Thunder && python3 main.py $USER 4 0 > ~/.thunder/thunder.log'
    process = subprocess.Popen(command, stdout=True, stderr=True, shell=True)
def config():
    global browser
    config = Window(app, bg="darkgrey", title="Thunder - Configuration", height=750, width=600)
    choosecol = Text(config, text="Choose the window's color: (Restart Required)")
    def blue_color():
        color_choice = "darkblue"
        c = open(home_path+"/.thunder/config.cfg", "w")
        c.write(color_choice)
        c.close()
        restart()
    def grey_color():
        color_choice = "darkgrey"
        c = open(home_path+"/.thunder/config.cfg", "w")
        c.write(color_choice)
        c.close()
        restart()
    def red_color():
        color_choice = "darkred"
        c = open(home_path+"/.thunder/config.cfg", "w")
        c.write(color_choice)
        c.close()
        restart()
    def black_color():
        color_choice = "black"
        c = open(home_path+"/.thunder/config.cfg", "w")
        c.write(color_choice)
        c.close()
        restart()
    blue = PushButton(config, text="Blue", command=blue_color)
    grey = PushButton(config, text="Grey", command=grey_color)
    red = PushButton(config, text="Red", command=red_color)
    black = PushButton(config, text="Black", command=black_color)
    fullscreeny = Text(config, text="Choose if Thunder should be in fullscreen (Restart Required):")
    def fullyes():
        fullchoice = "y"
        full = open(home_path+"/.thunder/page.cfg", "w")
        full.write(fullchoice)
        full.close()
        restart()
    def fullno():
        fullchoice = "n"
        full = open(home_path+"/.thunder/page.cfg", "w")
        full.write(fullchoice)
        full.close()
        restart()
    yesfull = PushButton(config, text="Fullscreen", command=fullyes)
    nofull = PushButton(config, text="Windowed", command=fullno)
    browswerchoice = Text(config, text="Choose which browser Thunder should use:")
    def browswer():
        global browser
        if browserchoice.value == "Chromium":
            browser = "chromium"
        if browserchoice.value == "Firefox":
            browser = "firefox"
        if browserchoice.value == "Firefox ESR":
            browser = "firefox-esr"
        print("New Browser: "+browser)
        boom = open(home_path+"/.thunder/browser.cfg", "w")
        boom.write("[Browser]\n")
        boom.write("NM = "+browser)
        boom.close()
    browserchoice = ButtonGroup(config, options=["Chromium", "Firefox", "Firefox ESR"], selected="Chromium", command=browswer)
    justanote = Text(config, text="The selected browser at config startup does not represent your choice.")
    def makeitsmall():
        smally = open(home_path+"/.thunder/size.cfg","w")
        smally.write("small")
        smally.close()
        restart()
    def makeitnormal():
        normally = open(home_path+"/.thunder/size.cfg","w")
        normally.write("normal")
        normally.close()
        restart()
    def makeitlarge():
        largey = open(home_path+"/.thunder/size.cfg","w")
        largey.write("large")
        largey.close()
        restart()
    choosedasize = Text(config, text="Select the size of the icons in `My Collection` (Restart Required):")
    besmall = PushButton(config, text="Small", command=makeitsmall)
    benormal = PushButton(config, text="Normal", command=makeitnormal)
    belarge = PushButton(config, text="Large", command=makeitlarge)
    def newson():
        newswrite = open(home_path+"/.thunder/news.cfg", "w")
        newswrite.write("y")
        newswrite.close()
        restart()
    def newsno():
        newswrite = open(home_path+"/.thunder/news.cfg", "w")
        newswrite.write("n")
        newswrite.close()
        restart()
    newstext = Text(config, text="Should Thunder download news at startup?")
    newsyes = PushButton(config, text="Yes", command=newson)
    newsno = PushButton(config, text="No", command=newsno)
    def mesaconfig():
        command = f'gnome-terminal --window --command="/home/'+user+'/Thunder/thunder-cli --mesaconfig"'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    Text(config, text="Other Settings:")
    PushButton(config, text="Mesa", command=mesaconfig)
def system():
    system = Window(app, bg="darkgrey", title="Thunder - System Info")
    textsys = Text(system, text="System Info (config.txt):")
    sysinfo = open("/boot/config.txt") # If you're on a distro where config.txt isn't at /boot/ (like on Ubuntu), change this line to /boot/firmware/config.txt
    sysinfotext = Text(system, text=sysinfo.read())
    sysinfo.close()
    exitsysinfo = PushButton(system, text="Exit System Info", command=system.destroy)
def manual():
    helpinfo = info("Thunder - Help", "Please see the HELP.md file for help. If you need more help, create an issue on Thunder's GitHub repo.")
def lic():
    licenseinfo = info("Thunder - License", "Thunder is distributed under the Hadcl4 Studios Open-Source License. See the LICENSE.md file for more info.")
def source_add():
    addsourcy = info("Thunder - Source Add", "Sources are add-ons to Thunder. Please view your specific source's guide on how to install it. For creating a source, view SOURCE.md for info.")
def game_collection():
    command = f'pcmanfm /home/$USER/Thunder/database'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def thundercloud():
    command = f'python3 ~/Thunder/scp.py'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def thunderclient():
    command = f''+browser+' steamcommunity.com/chat'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def setup_game():
    command = f'gnome-terminal --window --command="/home/$USER/Thunder/thunder-cli --setup"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def thunder_update():
    command = f'gnome-terminal --window --command="/bin/bash /home/$USER/Thunder/update"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def thunder_docs():
    command = f'gnome-terminal --window --command="/home/$USER/Thunder/thunder-cli --docs"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def thunder_doc_html():
    command = f'python3 /home/'+user+'/Thunder/viewdoc '+user
    process = subprocess.Popen(command, stdout=True, stderr=True, shell=True)
def sysinfo():
    command = f'gnome-terminal --window --command="/home/$USER/Thunder/thunder-cli --sysinfo" --geometry=102x30+200+200'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def setup():
    command = f'gnome-terminal --window --command="/home/$USER/Thunder/thunder-cli --setup"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def restartgameadd():
    app.destroy()
    print("Restarting Thunder...")
    command = f'cd ~/Thunder && ./start'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    command2 = f'killall thunder-cli'
    process2 = subprocess.Popen(command2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def addgame_all():
    command = f'gnome-terminal --window --command="/home/$USER/Thunder/thunder-cli --addgame"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    key = Window(app, title="Key", bg="white", width=700, height=125)
    keytext = Text(key, text='NM: Name of a game - Example: "Shovel Knight"')
    keytext2 = Text(key, text='ID: The path or ID of a game - Example: /home/pi/Games/Game.x86')
    keytext3 = Text(key, text="CV: Path to game's cover - Example: /home/pi/Pictures/cover.png")
    keytext4 = Text(key, text="RN: What to run the game with - Possible Values: mednafen, steam, wine, linux, browser")
    keybutton = PushButton(key, text="Click here to restart for your changes to take affect.", command=restartgameadd)
def cloud_cli():
    command = f'gnome-terminal --window --command="/home/$USER/Thunder/thunder-cli --cloud"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def dolphin_emu():
    if mesaon == "0":
        command = f'cd ~/Thunder/emulators/dolphin && ./dolphin-emu'
    if mesaon == "1":
        command = 'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'+mesa64+':'+mesa32+' ~/Thunder/emulators/dolphin/dolphin-emu'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def pcsxr():
    if mesaon == "0":
        command = f'cd ~/Thunder/emulators/pcsxr && ./pcsxr'
    if mesaon == "1":
        command = 'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'+mesa64+':'+mesa32+' ~/Thunder/emulators/pcsxr/pcsxr'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def melonds():
    if mesaon == "0":
        command = f'cd ~/Thunder/emulators/melonDS_Pi && ./launcher'
    if mesaon == "1":
        command = 'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'+mesa64+':'+mesa32+' ~/Thunder/emulators/melonDS_Pi/launcher'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def mednagui():
    if mesaon == "0":
        command = f'cd ~/Thunder/emulators/mednagui && python3 mednagui.py'
    if mesaon == "1":
        command = 'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'+mesa64+':'+mesa32+' python3 ~/Thunder/emulators/mednagui/mednagui.py'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def ppsspp():
    if mesaon == "0":
        command = f'~/Thunder/emulators/ppsspp/PPSSPPSDL'
    if mesaon == "1":
        command = 'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'+mesa64+':'+mesa32+' ~/Thunder/emulators/ppsspp/PPSSPPSDL'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def mgba():
    if mesaon == "0":
        command = f'~/Thunder/emulators/mgba/mgba-start'
    if mesaon == "1":
        command = 'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'+mesa64+':'+mesa32+' ~/Thunder/emulators/mgba/mgba-start'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
# The functions for running games
def gamerun(title, path, runner):
    print('Thunder is now running '+title+'...')
    if runner == "mednafen":
        if mesaon == "0":
            command = f'mednafen '+path
        if mesaon == "1":
            command = f'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'+mesa64+':'+mesa32+' mednafen '+path
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    if runner == "steam":
        if mesaon == "0":
            command = f'steam steam://rungameid/'+path
        if mesaon == "1":
            command = f'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'+mesa64+':'+mesa32+' steam steam://rungameid/'+path
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    if runner == "linux":
        if mesaon == "0":
            command = f''+path
        if mesaon == "1":
            command = f'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'+mesa64+':'+mesa32+' '+path
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    if runner == "wine":
        if mesaon == "0":
            command = f'wine '+path
        if mesaon == "1":
            command = f'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'+mesa64+':'+mesa32+' wine '+path
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    if runner == "browser":
        if mesaon == "0":
            command = f''+browser+' '+path
        if mesaon == "1":
            command = f'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'+mesa64+':'+mesa32+' '+browser+' '+path
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        
def onerun():
    gamerun(title=libraryoneNM, path=libraryoneID, runner=libraryoneRN)
def tworun():
    gamerun(title=librarytwoNM, path=librarytwoID, runner=librarytwoRN)
def threerun():
    gamerun(title=librarythreeNM, path=librarythreeID, runner=librarythreeRN)
def fourrun():
    gamerun(title=libraryfourNM, path=libraryfourID, runner=libraryfourRN)
def fiverun():
    gamerun(title=libraryfiveNM, path=libraryfiveID, runner=libraryfiveRN)
def sixrun():
    gamerun(title=librarysixNM, path=librarysixID, runner=librarysixRN)
def sevenrun():
    gamerun(title=librarysevenNM, path=librarysevenID, runner=librarysevenRN)
def eightrun():
    gamerun(title=libraryeightNM, path=libraryeightID, runner=libraryeightRN)
def ninerun():
    gamerun(title=librarynineNM, path=librarynineID, runner=librarynineRN)
def tenrun():
    gamerun(title=librarytenNM, path=librarytenID, runner=librarytenRN)
def elevenrun():
    gamerun(title=library11NM, path=library11ID, runner=library11RN)
def twelverun():
    gamerun(title=library12NM, path=library12ID, runner=library12RN)
def thirteenrun():
    gamerun(title=library13NM, path=library13ID, runner=library13RN)
def fourteenrun():
    gamerun(title=library14NM, path=library14ID, runner=library14RN)
def fifteenrun():
    gamerun(title=library15NM, path=library15ID, runner=library15RN)
def sixteenrun():
    gamerun(title=library16NM, path=library16ID, runner=library16RN)
def seventeenrun():
    gamerun(title=library17NM, path=library17ID, runner=library17RN)
def eighteenrun():
    gamerun(title=library18NM, path=library18ID, runner=library18RN)
def nineteenrun():
    gamerun(title=library19NM, path=library19ID, runner=library19RN)
def twentyrun():
    gamerun(title=library20NM, path=library20ID, runner=library20RN)

def create_short():
    command = f'python3 '+home_path+'/Thunder/createdesktop '+user
    process = subprocess.Popen(command, stdout=True, stderr=True, shell=True)

def steambrowser():
    webview.create_window("Steam", "https://store.steampowered.com")
    webview.start()
    
def itchbrowser():
    webview.create_window("Itch.io", "https://itch.io")
    webview.start()
    
def gogbrowser():
    webview.create_window("GOG", "https://gog.com")
    webview.start()

def viewrepo():
    webview.create_window("Thunder on GitHub", "https://github.com/hadcl4/Thunder")
    webview.start()

def webbrowser():
    command = f'python3 '+home_path+'/Thunder/thunderwebhelper 0'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

def exit_thunder():
    exit()

def store():
    def teeinstall():
        command = f'gnome-terminal --window --command="/home/$USER/Thunder/thunder-cli --install teeworlds"'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    def aatainstall():
        command = f'gnome-terminal --window --command="/home/$USER/Thunder/thunder-cli --install armagetronad"'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    storefront = Window(app, title="Thunder - Store", bg="white", width=1000)
    storefrontname = Text(storefront, text="Store", font="Ubuntu", color="black", size=50)
    teeworldsinstore = Picture(storefront, image=home_path+"/Thunder/database/teeworlds.png", align="left", height=120, width=120)
    teeworldsinstoretwo = PushButton(storefront, text="Install", align="left", command=teeinstall)
    teeworldsdescription = Text(storefront, text="| 2D Platform Shooter", align="left")
    teeworldsinstore = Picture(storefront, image=home_path+"/Thunder/database/armagetron.png", align="left", height=120, width=120)
    teeworldsinstoretwo = PushButton(storefront, text="Install", align="left", command=aatainstall)
    teeworldsdescription = Text(storefront, text="| 3D Lightcycle Game", align="left")

def libraryup():
    refreshup()
def librarydown():
    refreshdown()

# Adjust the "My Collection" text to the chosen theme
if bgcolor=="darkblue":
    colcolor = "darkgrey"
elif bgcolor=="darkgrey":
    colcolor = "lightgreen"
elif bgcolor=="darkred":
    colcolor = "yellow"
else: # This is for the SOURCES.md tutorial
    colcolor = "white"

if librarysize == "small":
    libraryx = 110
    libraryy = 154

if librarysize == "normal":
    libraryx = 220
    libraryy = 308

if librarysize == "large":
    libraryx = 440
    libraryy = 616

app = App(bg=bgcolor, height=1000, width=1880, title="Thunder - The ARM SBC Gaming Platform")
app.icon = home_path+"/Thunder/logo.gif"
mainico = Picture(app, image=home_path+"/Thunder/logo.gif", height=275, width=275)
mycollection = Text(app, align="top", text="My Collection", size=30, color=colcolor)
if panum == "y":
    app.set_full_screen(keybind="<Escape>")
if startupmessageif == "1":
    startup = Window(app, title="Thunder - Welcome", height=550)
    startupicon = Image.open(home_path+"/Thunder/logo.gif")
    startico = Picture(startup, image=startupicon, height=340, width=340)
    whatsnew = Text(startup, text=startmessage)
downbutton = PushButton(app, image=home_path+"/Thunder/down.png", align="bottom", height=32, width=32, command=librarydown)
upbutton = PushButton(app, image=home_path+"/Thunder/up.png", align="bottom", height=32, width=32, command=libraryup)

if section == "1":
    if not libraryoneCV == "0":
        soniccover = Image.open(libraryoneCV)
        cover_sonic = Picture(app, image=soniccover, align="left", height=libraryy, width=libraryx)
    if not libraryoneID == "0":
        sonic = PushButton(app, text="Run", command=onerun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not libraryoneNM == "0" and not libraryoneRN == "0":
        setup_sonic = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

    if not librarytwoCV == "0":
        godotcover = Image.open(librarytwoCV)
        cover_godot = Picture(app, image=godotcover, align="left", height=libraryy, width=libraryx)
    if not librarytwoID == "0":
        godot_run = PushButton(app, text="Run", command=tworun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not librarytwoNM == "0" and not librarytwoRN == "0":
        setup_godot = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

    if not librarythreeCV == "0":
        teecover = Image.open(librarythreeCV)
        cover_tee = Picture(app, image=teecover, align="left", height=libraryy, width=libraryx)
    if not librarythreeID == "0":
        teeworlds_run = PushButton(app, text="Run", command=threerun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not librarythreeNM == "0" and not librarythreeRN == "0":
        setup_tee = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

    if not libraryfourCV == "0":
        cover_shovel = Image.open(libraryfourCV)
        cover_shovelknight = Picture(app, image=cover_shovel, align="left", height=libraryy, width=libraryx)
    if not libraryfourID == "0":
        shovel_run = PushButton(app, text="Run", command=fourrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not libraryfourNM == "0" and not libraryfourRN == "0":
        shovel_setup = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

    if not libraryfiveCV == "0":
        vo_cover = Image.open(libraryfiveCV)
        cover_vo = Picture(app, image=vo_cover, align="left", height=libraryy, width=libraryx)
    if not libraryfiveID == "0":
        vrcyber = PushButton(app, text="Run", command=fiverun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not libraryfiveNM == "0" and not libraryfiveRN == "0":
        setup_vr = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

if section == "2":
    if not librarysixCV == "0":
        cavecover = Image.open(librarysixCV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not librarysixID == "0":
        cave = PushButton(app, text="Run", command=sixrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not librarysixNM == "0" and not librarysixRN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)
    
    if not librarysevenCV == "0":
        cavecover = Image.open(librarysevenCV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not librarysevenID == "0":
        cave = PushButton(app, text="Run", command=sevenrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not librarysevenNM == "0" and not librarysevenRN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)
        
    if not libraryeightCV == "0":
        cavecover = Image.open(libraryeightCV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not libraryeightID == "0":
        cave = PushButton(app, text="Run", command=eightrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not libraryeightNM == "0" and not libraryeightRN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

    if not librarynineCV == "0":
        cavecover = Image.open(librarynineCV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not librarynineID == "0":
        cave = PushButton(app, text="Run", command=ninerun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not librarynineNM == "0" and not librarynineRN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

    if not librarytenCV == "0":
        cavecover = Image.open(librarytenCV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not librarytenID == "0":
        cave = PushButton(app, text="Run", command=tenrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not librarytenNM == "0" and not librarytenRN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

if section == "3":
    if not library11CV == "0":
        cavecover = Image.open(library11CV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not library11ID == "0":
        cave = PushButton(app, text="Run", command=elevenrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not library11NM == "0" and not library11RN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)
    
    if not library12CV == "0":
        cavecover = Image.open(library12CV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not library12ID == "0":
        cave = PushButton(app, text="Run", command=twelverun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not library12NM == "0" and not library12RN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)
        
    if not library13CV == "0":
        cavecover = Image.open(library13CV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not library13ID == "0":
        cave = PushButton(app, text="Run", command=thirteenrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not library13NM == "0" and not library13RN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

    if not library14CV == "0":
        cavecover = Image.open(library14CV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not library14ID == "0":
        cave = PushButton(app, text="Run", command=fourteenrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not library14NM == "0" and not library14RN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

    if not library15CV == "0":
        cavecover = Image.open(library15CV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not library15ID == "0":
        cave = PushButton(app, text="Run", command=fifteenrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not library15NM == "0" and not library15RN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)
        
if section == "4":
    if not library16CV == "0":
        cavecover = Image.open(library16CV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not library16ID == "0":
        cave = PushButton(app, text="Run", command=sixteenrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not library16NM == "0" and not library16RN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)
    
    if not library17CV == "0":
        cavecover = Image.open(library17CV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not library17ID == "0":
        cave = PushButton(app, text="Run", command=seventeenrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not library17NM == "0" and not library17RN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)
        
    if not library18CV == "0":
        cavecover = Image.open(library18CV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not library18ID == "0":
        cave = PushButton(app, text="Run", command=eighteenrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not library18NM == "0" and not library18RN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

    if not library19CV == "0":
        cavecover = Image.open(library19CV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not library19ID == "0":
        cave = PushButton(app, text="Run", command=nineteenrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not library19NM == "0" and not library19RN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

    if not library20CV == "0":
        cavecover = Image.open(library20CV)
        cover_sonic = Picture(app, image=cavecover, align="left", height=libraryy, width=libraryx)
    if not library20ID == "0":
        cave = PushButton(app, text="Run", command=twentyrun, align="left", image=home_path+"/Thunder/play.gif", height=64, width=64)
    if not library20NM == "0" and not library20RN == "0":
        setup_cave = PushButton(app, text="Setup", command=setup, align="left", image=home_path+"/Thunder/setup.gif", height=64, width=64)

menubar = MenuBar(app,
                  toplevel=["Thunder", "Add", "About", "Cloud", "Emulators"],
                  options=[
                      [ ["Configuration", config], ["Update Thunder", thunder_update], ["System Info (config.txt)", system], ["System Info (all platforms)", sysinfo], ["Game Database", game_collection], ["ThunderStore", store], ["Web Browser", webbrowser], ["Exit Thunder", exit_thunder] ],
                      [ ["Add Game...", addgame_all], ["Add Source...", source_add], ["Run Setup...", setup_game], ["Create Desktop Shortcut...", create_short], ["Browse Games on Steam", steambrowser], ["Browse Games on Itch.io", itchbrowser], ["Browse Games on GOG.com", gogbrowser] ],
                      [ ["Help", manual], ["License", lic], ["Docs (less)", thunder_docs], ["Docs (html)", thunder_doc_html], ["View Thunder on GitHub", viewrepo] ],
                      [ ["ThunderCloud Data Transfer", cloud_cli], ["Steam Chat", thunderclient] ], # This needs some work!
                      [ ["Dolphin-Emu", dolphin_emu], ["PCSX Reloaded", pcsxr], ["melonDS_Pi", melonds], ["Mednagui", mednagui], ["PPSSPP", ppsspp], ["mGBA", mgba] ]
                  ])

app.display()
