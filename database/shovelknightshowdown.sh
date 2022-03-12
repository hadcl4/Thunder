#!/bin/bash
echo Shovel Knight: Showdown setup running...
read -p "This will override your current graphics config for Shovel Knight Showdown. You will need to have launched the game at least once. Continue? Hit enter. Otherwise hit Ctrl+C."
rm -f /home/$USER/.local/share/"Yacht Club Games"/"Shovel Knight Showdown"/render.bin
cp /home/$USER/Thunder/database/configs/shovelknightshowdown.bin /home/$USER/.local/share/"Yacht Club Games"/"Shovel Knight Showdown"/render.bin
echo Setup complete. Enjoy playing!
read -p "Exit? Then hit enter."
