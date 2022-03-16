#!/usr/bin/env python3
from guizero import *
import sys
from configparser import *
user = sys.argv[1]
configur = ConfigParser()
library = configur.write("/home/"+user+"/.thunder/library.cfg")
library = configur.read("/home/"+user+"/.thunder/library.cfg")
def addgame():
    print(slot.value)
    print(gamename.value)
    print(execname.value)
    print(picname.value)
    print(runnername.value)
    if slot.value == "1":
    # First game in library
        libraryoneNM = configur.set("one", "NM", gamename.value)
        libraryoneID = configur.set("one", "ID", execname.value)
        libraryoneCV = configur.set("one", "CV", picname.value)
        libraryoneRN = configur.set("one", "RN", runnername.value)
    if slot.value == "2":
    # Second game in library
        librarytwoNM = configur.get("two", "NM")
        librarytwoID = configur.get("two", "ID")
        librarytwoCV = configur.get("two", "CV")
        librarytwoRN = configur.get("two", "RN")
    if slot.value == "3":
    # Third game in library
        librarythreeNM = configur.get("three", "NM")
        librarythreeID = configur.get("three", "ID")
        librarythreeCV = configur.get("three", "CV")
        librarythreeRN = configur.get("three", "RN")
    if slot.value == "4":
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
    info("Thunder - Add Game", "Please restart Thunder for changes to take effect.")

app = App(title="Thunder - Add Game", bg="white")
Text(app, text="Which slot?:")
slot = Combo(app, options=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"], selected="1")
gamename = TextBox(app, text="Enter name here...", width=50)
picname = TextBox(app, text="Enter the path to cover art...", width=50)
execname = TextBox(app, text="Enter the game's ID, or path, or address, etc.", width=50)
Text(app, text="What to run the game with?:")
runnername = Combo(app, options=["steam","wine","mednafen","linux","browser"], selected="steam")
PushButton(app,text="Add Game", command=addgame)
app.display()
