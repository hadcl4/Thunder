# Emulators
These are prebuilt binaries of various emulators. You can use them outside of Thunder too. Here is a list of emulators included here and their platform:
## Dolphin
- Platform: Wii/GameCube
- Arch: aarch64
- Renderer: OpenGLES or Vulkan
#### Additional Notes:
Because Dolphin needs OpenGL 3.0+ to render in OpenGL mode (the default), it doesn't run on the Pi out of the box. However, the `GFX.ini` file included switches the renderer to OpenGLES and has many performance improvements to make many games playable. Dolphin also needs a 64-bit OS or chroot to run. If you're still using a Pi4 with the old default of 1.5Ghz we recommend overclocking to 1.8Ghz, and we recommend at least using a Pi4 4GB RAM with Dolphin. You can also use Vulkan with Dolphin, but only if you have the Vulkan 1.1 Mesa update (with 1.0 it is *very* unstable, except when using `llvmpipe`, but that is too slow to be playable).
## PCSXR
- Platform: PSX (AKA PS1)
- Arch: ARMHF
- Renderer: OpenGL
#### Additional Notes:
The build included here is 32-bit. However, on 64-bit operating systems, you may run the following command to install a 64-bit version of PCSXR on your system:
```
sudo apt install pcsxr:arm64
```
We also strongly recommend using Mednafen for playing PS1/PSX games instead of PCSXR. However, we include PCSXR because it doesn't require a BIOS and some games run better in it than in Mednafen.
## PPSSPP
- Platform: PSP
- Arch: ARMHF
- Renderer: OpenGL, OpenGLES, or Vulkan
#### Additional Notes:
PPSSPP is included precompiled for ARMHF. To get the best performance possible, we recommend installing the latest Mesa Vulkan drivers, and setting PPSSPP's renderer to "Vulkan".
## melonDS_Pi
- Platform: NDS
- Arch: aarch64
- Renderer: OpenGL
#### Additional Notes:
This is an optimized version of melonDS for the Raspberry Pi. Normally melonDS lacks HW acceleration because the Pi only has OpenGL 2.1. However, I managed to make a little hack that gets full hardware OpenGL rendering working, and most games run at 60FPS. For the best performance set the renderer as Software with OpenGL Display as ON, and turn on "Use seperate thread".
## Mednagui
- Platform: Multiple
- Arch: ARMHF or aarch64
- Renderer: OpenGL
#### Additional Notes:
Mednagui is a frontend for Mednafen. It is made to be a replacement for Mednaffe, and most configuration options for Mednafen are optimized for a good balance between speed and accuracy. You just tell it the path to the ROM you want to run. It's made to be simple and lightweight.
## Box86
- Platform: x86 Linux
- Arch: ARMHF
- Renderer: OpenGL, Vulkan, OpenGLES, etc.
#### Additional Notes:
The build here was compiled on an Aarch64 Pi4, so I'm not sure if it's compatable with ARMHF. However, it should work (since on ARM64 Linux you need to run `sudo dpkg --add-architecture armhf` to use Box86 anyway). This build was made for the Pi4. If you skipped compiling Box86 and instead want to use this build, extract Box86 from the tarball and run the following command:
```
sudo cp box86 /usr/local/bin/box86
```
There also are some additional steps to get Box86's binfmt running, but we won't document that here. This build has been tested on RPiOS and doesn't work currently.
## Box64
- Platform: x86_64 Linux
- Arch: aarch64
- Renderer: OpenGL, Vulkan, OpenGLES, etc.
#### Additional Notes:
This build was made for the Pi4. If you skipped compiling Box64 and instead want to use this build, extract Box64 from the tarball and run the following command:
```
sudo cp box64 /usr/local/bin/box64
```
There also are some additional steps to get Box64's binfmt running, but we won't document that here. This build has been tested on RPiOS and doesn't work currently.
## mGBA
- Platform: Gameboy Advance
- Arch: aarch64
- Renderer: OpenGL
#### Additional Notes:
This build was compiled on a Raspberry Pi 4 with 8GB RAM, running Ubuntu 21.04. In settings you must select OpenGL 1.x as the renderer. This build has been tested on RPiOS and doesn't work currently.
