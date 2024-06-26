
----

TODO
----

### Add RK3399 compatability `Complete!`
Many SBCs and Chromebooks use the RK3399 CPU, so it would be a great platform for Thunder to support!
### Add SD845 compatability `Complete, not tested`
Many phones and laptops use the SD845 CPU (and even though the laptops may have Windows by default, you can install Linux on them), and it's capable of running many PC games. As such, it's a great platform for Thunder to support!
### Add the ability to add games from the GUI `Pretty much Done`
Thunder is supposed to be easy, so why not be able to add games to your library without coding? I'm thinking of using a sort of system where you can create seperate libraries (which are each a single folder containing .cfg files) containg the needed information for Thunder to grab cover art and launch the game. My plan is to support having up to 5 games in a library, and up to 10 libraries, which means up to 50 games!

You can now have up to 15 games in Thunder. I aim to eventually support 25.
### Finish ThunderCloud to compete with Steam Cloud `Partial, not tested`
Since Thunder is supposed to basically be Steam on ARM devices, Thunder needs an alternative to Steam Cloud (which allows you to sync your save files and games, and chat with your friends). I call it ThunderCloud (Get it?), but since Thunder is open-source, I can't store everything on an online server (for one thing I don't have the money!). So my idea is to make a gui for the `scp` BASH command, which will allow you to send your save files and games to other devices on the same local network. And for chatting, I'm not sure yet but I'm thinking of creating an Electron version of Steam Chat that natively runs on ARM.

Currently the code is complete for transferring files from one device to another, however I'm not able to test it. Currently for chatting Thunder will just open Steam Chat in the web browser you've set in settings.
### Add Dolphin Integration `Complete!`
This would be possible with `dolphin-emu-nogui`, but I would need to figure out a way to preconfigure Dolphin to get the best performance, and to use OpenGLES or Vulkan out-of-the-box instead of OpenGL 3.0+ (I've tested and the Pi's GL3 capabilities aren't enough to get Dolphin running, so you need Vulkan or OpenGLES). However, on the RK3399 and SD845 platforms, OpenGL version shouldn't be a problem.

Now you can launch a pre-configured Dolphin from Thunder. Yay!
### Finish CLI mode `Complete!`
This is important for people running Thunder for game servers (so for something like a Terraria server). Currently `thunder-cli` has enough to launch games, view system info, and setup games. In fact I would consider it more complete than the GUI!
### Add a Storefront `Complete!`
It would be nice to add a basic storefront to Thunder for installing free and open-source games (although games that are just free but not open-source would be acceptable as well). I'm thinking of mainly having popular FOSS games like Teeworlds in the store.

The store is now complete! It's usable from both the GUI and the CLI.
### Add PPSSPP integration `Complete!`
PPSSPP works great on the Pi out of the box, for both 3D and 2D games. However, the thing is I'm not sure how I would make it be installable with Thunder. The only ways to install it on the Pi are either through Flatpak or from source. Now of course I could make it so it would compile from source, but that would just add more time to how long the setup already takes. So the problem with this is how to install it, unlike how Dolphin's problem is configuration.

An ARMHF build of PPSSPP is now included with Thunder.
### Add Wine integration `Complete!`
Wine is now fully usable in Thunder, other than you have to install it prior to installing the game in Thunder.
### Add Browser Support `Complete!`
The code is added. However many games are now on the internet or in HTML5 format, so having browser support in a game launcher is useful. The following browsers are supported:
- Chromium
- Firefox
- Firefox ESR
### Allow Games to be Configured Individually `Complete!`
This is a feature I've wanted for a long time (in fact it's the whole reason the empty `configs` folder exists in `.thunder`), however I haven't gotten a working solution yet. Mainly I want the following options:
- OpenGL version to run the game with (by default it will use your current OpenGL version)
- If the game should be ran by another executable (so games that use emulators other than mednafen can run)
- Any arguments for the game (I haven't found any games that need this, however there most likely are games out there that do)
- Any environment variables (for example, if a game needs Box86/64 to have Dynarec off to run correctly)

You can now configure games individually using virtual cartridges.

### Add an Updater `Done`
Now that Thunder is on GitHub, instead of making the user manually running `git pull` and possible breaking their install in the process, it would be much more convenient to have an updater. How? Not sure yet.
### Add Redream `Not Done Yet`
Redream has a Raspberry Pi version of their emulator easily available, so why don't I have it included? Simple. Ever since Redream has moved to Gitlab, I haven't been able to find its license, so I don't know if I can freely redistribute it. If you know it's legal to redristibute it, let me know!
### Add to Settings the option to turn off Thunder downloading news at startup `Complete!`
For people who don't have good internet or don't have a constant internet connection this is important, and should be quite easy to add. However, the downside is that I'll have to create a new config file, so I'll have to work on that soon.
### Add more GUIs `Not Done Yet`
While the current way of adding games through `thunder-cli` is fine for me, a lot of people would most likely prefer a full GUI. So putting it on the to-do list.
### Add Flatpak Support `Complete!`
Many games are packaged as Flatpaks, so it would be a good platform for Thunder to support.
