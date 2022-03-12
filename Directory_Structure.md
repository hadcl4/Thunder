###### This file is outdated very often. Please view Thunder's filesystem for a more up-to-date view of Thunder's directory structure.
# Directory Structure
Thunder's directory structure is discussed in this file. If you're not a developer interested in contributing to Thunder, and just a normal user, this file probably won't interest you. Well, let's get started!
## Assets
Assets are stored in the base Thunder directory, located at ~/Thunder. Here is a diagram of the assets' location:
```
~/Thunder
--|logo.gif
--|logo.png
--|play.gif
--|setup.gif
--|up.png
--|down.png
```
The difference between `logo.png` and `logo.gif` is the .png file is the icon for the .desktop file. And the .gif file is used the Thunder app itself.
## Game Database
Thunder features a built-in database of games. These include both setup scripts for games and covers. Here is its structure:
```
~/Thunder
--|database/
----|<gamename>.sh
----|<gamename>.gif
----|configs/
------|<game configs>
```
Thunder's database is by no means complete, but it features a large library to make setting up games easier.
## Program Files
Here is the structure for Thunder's main files:
```
~/Thunder
--|main.py
--|mednafen.cfg
--|setup
--|start
--|thunder-cli
```
All of the files other than the `mednafen.cfg` are used directly in Thunder. The `mednafen.cfg` is copied during setup to Mednafen's folder.
## Markdown Files
All the markdown files are in the base directory:
```
~/Thunder
--|Directory_Structure.md
--|HELP.md
--|LICENSE.md
--|README.md
--|SOURCES.md
```
## Configuration Files
The configuration files are a little scattered:
```
~/.thunder
--|config.cfg
--|page.cfg
--|library.cfg
--|default.txt
```
The .cfg files located in the `.thunder/` store the user's game library for a specific platform, and the `config.cfg` stores user settings (like the selected theme).