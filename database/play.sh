#!/bin/bash
FLATPAK_LOCATION=$(command -v flatpak)
if [[ $FLATPAK_LOCATION == "/usr/bin/flatpak" ]]; then
echo "Installing Play!..."
flatpak install org.purei.Play && echo "Install complete."
else
echo "Flatpak is not installed. Please run this setup again after Flatpak is installed."
echo "Will install Flatpak in 5 seconds... Press Ctrl+C to cancel..."
echo "5..."
sleep 1s
echo "4..."
sleep 1s
echo "3..."
sleep 1s
echo "2..."
sleep 1s
echo "1..."
sleep 1s
echo "0"
bash ${HOME}/Thunder/database/flatpak.sh
fi
