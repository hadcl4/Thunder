#!/bin/bash
read -p "You don't need to run this script if you installed Steam during setup. Want to continue? Press enter. Otherwise press Ctrl+C."
boxcheck=$(command -v box86)
if [[ $boxcheck == "/usr/local/bin/box86" ]]; then
cd ~/box86
echo "Running Box86's Steam install script..."
bash install_steam.sh
else
echo "Please install Box86 before installing Steam."
echo "Don't want to have to compile Box86 by yourself? Check out Box86-Manager:"
echo "https://github.com/hadcl4/Box86-Manager"
fi
