# HELP
Thunder is initially easy to use, but here we'll go over the basics. If what you need help with isn't discussed here, create an issue on Thunder's GitHub repo.
## Adding A Game
First, click the "Add" button on Thunder's menu bar. And then click "Add Game". Soon a terminal will appear with nano ready for you to add games.
## Adding A Source
Please view Thunder/SOURCE.md for info.
## Changing Themes
Select Thunder->Configuration. Then select what color you want. After that, Thunder will close and you'll need to open it again for the theme to be applied.
## System Information
Select Thunder->System Info (config.txt). Thunder will then fetch the contents on the config.txt file. If you're on Ubuntu (or any other distro where config.txt isn't located at `/boot/config.txt`), you'll need to modify Thunder's code to change where it fetches its data from. On Ubuntu, the config.txt file is located at `/boot/firmware/config.txt`. To find where the code is at that needs changed, simply open a text editor and try `Ctrl+F`, and type in `config.txt`. The location should come up for you to change it.

If you're not on a Raspberry Pi, select Thunder->System Info (all platforms).
## Retro Games in Mednafen
If a retro game is failing to boot, try running this command outside of Thunder:
```
mednafen /path/to/game/
```
If an error comes up about a missing file, you're likely missing the BIOS/firmware. You'll need to obtain the BIOS/firmware, but we won't document how here :). Then you'll need to rename the file to what Mednafen is saying is missing, and move it to the directory Mednafen says it's missing in.

If it's still not working and/or it didn't say anything about a missing file, the game probably just won't work in Mednafen.
## Steam Games
Not all Steam games run on the Pi, so here are some things that should help you know either if the game doesn't work or if there's something you need to do to get it to work:
###### `Unimplemented opcode: ## ## ## ## ##` | Box86/64 currently cannot run this game
###### `Error loading one of needed lib (no such file or directory)` | You need to install an additional library
###### `Error: Global symbol ###### not found, cannot apply ###### in ######` | Box86/64 currently cannot run this game
###### `Segmentation Fault (core dumped)` | Something made the game crash, possibly too low-profile OpenGL version. You may need to fake a higher-profile OpenGL to run the game (documented in Box64's readme).
###### The game crashes without errors | You may need to fake a higher-profile OpenGL to run the game (documented in Box64's readme).
## Using Thunder from the CLI
To use Thunder from the CLI, run this:
```
thunder-cli
```
It will print off enough to get it up and running for you. 
## Running Games from Platforms not Supported in Thunder
Currently the best way to run games for platforms currently not available in Thunder (like an emulator or cloud-gaming service) is to create a BASH script:
```
#!/bin/bash
/path/to/emulator /path/to/game
```
```
#!/bin/bash
chromium <cloud-gaming service address>
```
There are 2 examples above for an emulator and a cloud-gaming service, so that should get you started.

After you make the BASH script, run in a terminal `chmod +x /path/to/bash/script`.

Finally, add the game with "linux" as the platform and the ID as the path to the BASH script.
## Creating a Desktop Shortcut
Select Add->Create Desktop Shortcut. Thunder will then use the same data as the config it reads for a game to create a desktop shortcut. You can choose which game it will create a shortcut for. On some systems (e.g. Ubuntu) you will have to right click the shortcut, select Properties, then allow the file to be executed.
## License
Please view Thunder/LICENSE.md for info.
