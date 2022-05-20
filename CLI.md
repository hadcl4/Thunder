# `thunder-cli` Documentation
## Introduction
`thunder-cli` is a command line tool for using Thunder on operating systems without X11 or Wayland, or to use Thunder in a terminal. Most of the things you can do in the GUI can be done in `thunder-cli`. The only notable exception is `thunder-cli` doesn't keep track of your game library, but it still is very simple to launch games. Many of the features in the GUI (viewing the docs, viewing system info, running a setup, etc.) actually use `thunder-cli`!
## The Basics
To get started using `thunder-cli`, run the following command in the terminal:
```
thunder-cli --help
```
This will list off all of `thunder-cli`'s functions. In this section we'll go over the following:

> --gui

> --setup

> --debug

> --docs

> --help

> --version

> --addgame

> --run

### `--gui`
Launch Thunder's graphical user interface (X11 or Wayland required).
### `--setup`
Run a setup for a game. You may enter `viewlist` to see a list of games with setup scripts.
### `---debug`
`--debug` is mainly for debugging a game in an emulator (Box86, Box64, or Mednafen), but you may also use it to launch a game. If you want to launch Steam, select Box86 as the emulator, and simply set "steam" as the path (without the quotes). I've written it so that it will just launch Steam, because of how steam works with launching it. To launch Steam you'll *need* Box86's binfmt set up (if compiled manually it should be working).
### `--docs`
View Thunder's helpful markdown files (including this!).
### `--help`
Get a list of commands to use with `thunder-cli`.
### `--version`
View Thunder's version.
### `--addgame`
Add a game to Thunder's library (only affects gui).
### `--run`
Run a `.thunder` file. A `.thunder` file is basically an entry to the configuration file used in `thunder-cli --addgame`, however only one game can be stored in a `.thunder` file. The main difference is that, instead of a section being referred to by a number (like `[15]`), `.thunder` files begin with `[Game]`. Other than that, everything else is the same.
## Advanced Features
This section will go over more advanced features:

> --sysinfo

> --cloud

> --reset

> --log

> --update

> --dev

> --clear-cache

### `--sysinfo`
View your system info from the CLI (including all the data neofetch gets, your Vulkan version, OpenGLES and OpenGL version, CPU architecture, and IP address).
### `--cloud`
Use ThunderCloud from the CLI. You'll need to give quite a bit of info (IP address, username, path to the file you want to copy, etc.). Currently you can only copy games/save files across your local network.
### `--reset`
Reset Thunder's configuration files (only affects GUI). Good if you modified a config yourself and accidentally made a mistake, causing Thunder's GUI to not launch. However be careful as this will also reset your game library.
### `--log`
View Thunder's log. Needs to be enabled by uncommenting a certain part of `start`. Instructions are included there.
### `--update`
Update Thunder (both GUI and CLI).
### `--dev`
Enter development mode. This what you'll use when developing Thunder.
### `--clear-cache`
Clear web browser cache.
