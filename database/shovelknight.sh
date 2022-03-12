#!/bin/bash
echo Shovel Knight: Shovel of Hope setup running...
read -p "This will override your current graphics config for Shovel Knight: Shovel of Hope. You will need to have launched the game at least once. Continue? Hit enter. Otherwise hit Ctrl+C."
rm -f /home/$USER/.local/share/"Yacht Club Games"/"Shovel Knight - Shovel of Hope"/render.bin
cp /home/$USER/Thunder/database/configs/shovelknight.bin /home/$USER/.local/share/"Yacht Club Games"/"Shovel Knight - Shovel of Hope"/render.bin
echo Setup complete. Enjoy playing!
read -p "Exit? Then hit enter."
