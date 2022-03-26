#!/bin/bash
cd ~
wget https://cdn.akamai.steamstatic.com/client/installer/steam.deb
sudo dpkg -i steam.deb # This will work because Steam is a hybrid amd64/i386 app, so it's marked as "all" architectures supported, you can't have 2!
rm ~/steam.deb # Clean it up afterwards
sudo sed -i 's/set -e/set -e\nexport STEAMOS=1\nexport STEAM_RUNTIME=1/' /usr/lib/steam/bin_steam.sh # Let's sed hack some stuff!
mkdir -p ~/.local/share/Steam/config # Prepare for the next hack.
wget https://raw.githubusercontent.com/Botspot/Steam-RPi/main/DialogConfig.vdf -O ~/.local/share/Steam/config/DialogConfig.vdf # Now let's hack Steam some more!
echo Now for the dependencies... # Without them it might not work.
sudo apt install libnss3:armhf libnm0:armhf libdbus-glib-1-2:armhf libudev1:armhf libnspr4:armhf libgudev-1.0-0:armhf libusb-1.0-0:armhf libappindicator1:armhf libsm6:armhf libxtst6:armhf libice6:armhf # This command has only been tested on Focal and Hisute, and might not work on other distros!
echo If you need help with Steam, view steampowered.com or box86.org
echo Steam installed!
