#!/usr/bin/env python3
print("Patching mesa.cfg...")
import sys
user = sys.argv[1]
home = "/home/"+user
f = open(home+"/.thunder/mesa.cfg","a")
f.write("GALLIUM_HUD=OFF\n")
f.close()

