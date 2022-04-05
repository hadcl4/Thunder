export software_installed=$(command -v gnome-software)
export flatpak_installed=$(command -v flatpak)
if [[ $flatpak_installed == "/usr/bin/flatpak" ]]; then
echo "Flatpak already installed..."
else
sudo apt install flatpak
if [[ $software_installed == "/usr/bin/gnome-software" ]]; then
sudo apt install gnome-software-plugin-flatpak
fi
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
echo "Flatpak install complete. Please restart your device."
sleep 1d
fi
