echo Godot Setup running...
sudo apt install libc6 libpthread-stubs0-dev librtmp1 libdlt2 libnm0 libasound2 libpulse0 libudev1
echo "When using Godot, head to 'Project' -> 'Project Settings' -> 'Quality' and select 'fallback to Gles2' as 'ON' or 'Driver' as 'GLES2'. Godot currently does not run on the Pi4 with GLES3 (the editor will freeze). However, this may not be a problem on RK3399 and SD845 devices."
echo "Also know Godot likely won't run on Pi3 boards."
echo Setup complete. Enjoy playing!
read -p "Exit? Then hit enter." exitsetup
