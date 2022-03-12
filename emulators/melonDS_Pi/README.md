# melonDS for Raspberry Pi
## Installation
Run these commands in a terminal to install melonDS for Raspberry Pi:
```
cd ~/melonDS_Pi
chmod +x install; ./install
```
You may need to enter your password during install. After installation has finished, you may run
```
melonDS
```
in a terminal to launch it, or select it in the application launcher.
## Why did I make this?
I was dissatisfied with DeSmuME's slow speed, and melonDS needed a bit of a trick to work on the Pi (without the trick rendering is software only!). However, it gets annoying to export the same environment variable, over and over, just to run melonDS. Because of this, melonDS for Pi does the trick for you with its launcher script, and also lets you run melonDS from the terminal or application launcher, rather than navigating to its location and launching it from there with the environment variable active. It might not seem like much, but it makes running melonDS on the Pi easier. Just know this was a quick weekend project so it very likely has bugs.