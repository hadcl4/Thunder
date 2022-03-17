# Thunder Changelong

### 3/17/22
- You can now run Thunder in Devmode! Search files, edit them, view them, and use git, all from one easy-to-use interface! Run it with `thunder-cli --dev`.
- Setup code scanning, for better security.

### 3/14/22
- You can now turn off news downloading.

### 3/13/22
- Thunder now has an updater! Still expiremental, but useful.

### 3/12/22
- Thunder is now publicly available on GitHub!
- Now when you startup Thunder, it will fetch the latest news from GitHub.

### 3/1/22
- Viewing Thunder's documentation is now a much better experience! Now there are 2 Documentation options: "Docs (less)" and "Docs (html)". For those who like the old version better it's still there. Markdown files are rendered in HTML using `markdown`, and there's also a menu for selecting the files.
- Because of the new feature mentioned above, there is now a new file: `viewdoc`, and a new folder called `doc` containing the html used for `viewdoc`.

### 2/28/22
- Added the ability to create desktop shortcuts under "Add".
- Because of this new feature, there is now a new file: `createdesktop`

### 2/20/22
- Minor modifications to `thunder-cli` and `CLI.md`.
- Added `--log` to `CLI.md`.
- Logging is now optional.

### 2/18/22
- Changed some shell scripts to launch with `dash` instead of `bash`. This highly improves performance.

### 2/7/22
- Updated configs for Shovel Knight games to improve performance. Both games now can run full speed using these configs.
- Various QOL improvements.

### 2/6/22
- Updated "System Info (all platforms)" to include "Build Details".
- Updated `thunder-cli --version` to `STABLE Rev 1.0`.
- When a game finishes installing, Thunder now displays a notification.
- Due to the new feature mentioned above, `zenity` is now a dependency. Install it with `sudo apt install zenity`.
- Thunder now logs errors to `~/.thunder/thunder.log`.

### 2/5/22
- Added slots for up to 15 games

### 2/4/22
- Performance improvements.

### 2/3/22
- Added `gamemode` for better performance.

### 2/1/22
- Highly improved performance, thanks to removing old code that is no longer needed. This code was removed due to how games were noticeably slower running in Thunder compared to running independantly. Especially performance in 3D games has been improved (over 5FPS faster in PPSSPP).
- Changed the configs for the Shovel Knight games to what they were originally, due to major testing. Small stages in Showdown run perfectly in 720p, but medium and large sized stages only work well with 2 players, 3 or more will cause major lag. To fix this, the resolution has been lowered. Same for Shovel of Hope, where certain stages (especially Plague Knight's) will occasionally lag in 720p.

### 1/31/22
- Improved thunderwebhelper so that it can open a wepage on startup.

### 1/30/22
- Added a Web Browser, called "thunderwebhelper". It's based on python3-webview, so it works the same as the game storefronts. Currently though it lacks many major features, such as History and Cookies, and as such still has many bugs.

### 1/29/22
- Changed the names of 3 items in "Add". "Buy a Game on \<insert store\>" is now "Browse Games on \<insert store\>".
- Storefronts now open in python3-webview, for faster loading and better performance (although currently GOG performs better in an actual browser, but it still will load in python3-webview to keep it consistent with the other storefronts). However certain features do not work. We're working on a way to fix these issues (particularly cookies do not work, which mainly affects logins to each site, especially on Steam it breaks compatability in logins between steampowered.com and steamcommunity.com). For now though it works enough for you to browse games on each store. Please purchase games in an actual browser until these issues are fixed.
- Due to the feature mentioned above, a new dependency has been added to setup: `python3-webview`. You may install it using `sudo apt install --no-install-recommends python3-webview`.
- Updated configs for "Shovel Knight: Shovel of Hope" and "Shovel Knight Showdown" to higher the resolution to 1280x720, due to the performance increase with these games in the latest Box64 update, which is included with Thunder.

### 1/28/22
- Added the ability to change the size of library covers
- Due to the new feature mentioned above, added the file "Thunder/size.cfg"
- Made "Thunder/setup" not force you to reset your configs
- Added 3 new items to "Add": "Buy a Game on Steam", "Buy a Game on Itch.io", "Buy a Game on GOG.com"

### 1/27/22
- Added "Thunder/CHANGELOG.md"
- Updated Box86 to newest build to ensure Steam compatability
- Updated Box64 to newest build
- Updated "Thunder/README.md" to include "Thunder/CHANGELOG.md"

____
