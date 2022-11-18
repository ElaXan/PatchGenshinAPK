# PatchGenshinAPK

Tool for patching .apk on Android Phone using Termux.

## Features available for now

### LSPatch

[LSPatch](https://github.com/LSPosed/LSPatch)\
Patching APK and embed module for no root user can use a LSPosed Module.

### apk-mitm

[apk-mitm](https://github.com/shroudedcode/apk-mitm)\
Patch AnimeGame uses apk-mitm to be able to use mitmproxy/mitmdump.\
And for my project [AnimeGamePatch](https://github.com/Score-Inc/AnimeGamePatch)

# Commands

1. > `patchgenshin` : Patching APK with LSPatch
2. > `patchgenshin <Path_To_APK.apk>` : shortcut for Patching with LSPatch
3. > `patchgenshin -m apk-mitm` : Patching apk with apk-mitm to support with Mitmproxy/Mitmdump
4. > `patchgenshin -m uninstall` : Uninstall PatchGenshinAPK\

## Requirements

* Python
* Java
* Termux

# Install

Copy this command and paste to Termux
```bash
bash <(curl -Ls https://raw.githubusercontent.com/Score-Inc/PatchGenshinAPK/main/install.sh)
```

# How to use

Sadly there is no tutorial how to use this for now.\
You should know what are you doing
