#!/bin/bash
echo "Mednafen Setup running..."
read -p "You do NOT need to run this if you installed Mednafen during Thunder's setup. Continue? Then hit enter. Otherwise press Ctrl+C."
sudo apt install mednafen
mednafen
rm ~/.mednafen/mednafen.cfg
cp ~/Thunder/mednafen.cfg ~/.mednafen/mednafen.cfg
echo "Setup complete. Enjoy playing!"
read -p "Exit? Then hit enter."
