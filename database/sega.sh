#!/bin/bash
echo Sega Classics setup running...
read -p "Please enter the path to the Sega Classics folder" pathtogame
read -p "Then enter the game you wish to extract (case sensitive! example: SONIC3D_UE.68K)" actualgame
cd ~/Thunder
mkdir segaclassics
sudo cp $pathtogame/"uncompressed ROMs"/$actualgame ~/Thunder/segaclassics/$actualgame
echo The specified ROM has now been moved to "Thunder's subdirectory" segaclassics!
echo Setup complete! Enjoy playing!