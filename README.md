# PatchGenshinAPK

Tool for patching .apk on Android Phone using Termux.

## Note

For now you can only patch using the .apk extension, so please don't patch using the .apks, .xapk extension or something else

## Requirements

* Python
* Java
* Termux

## Features available

### LSPatch

[LSPatch](https://github.com/LSPosed/LSPatch)\
Patching APK and embed module for no root user can use a LSPosed Module.

### apk-mitm

[apk-mitm](https://github.com/shroudedcode/apk-mitm)\
Patch AnimeGame uses apk-mitm to be able to use mitmproxy/mitmdump.\
And for my project [AnimeGamePatch](https://github.com/Score-Inc/AnimeGamePatch)

### Clone

Clone AnimeGane APK\
With custom name Package by yourself\
See [Clone APK](#clone-apk) for how to use it

# Commands

```sh
~$ patchgenshin --help
Usage: patchgenshin [option] [file] [package_name] [custom_name_apk]
Options:
  -h, --help            Show this help message and exit
  -u, --uninstall       Uninstall PatchGenshinAPK
  -v, --version         Show version
  -l, --lspatch         Patch Genshin.apk with LSPatch
  -a, --apkmitm         Patch Genshin.apk with apk-mitm
  -c, --clone           Clone Genshin package name
  -up, --update         Update PatchGenshinAPK

file:
Path to APK want to Patch : /sdcard/Genshin.apk

package_name:
Only for use -c or --clone feature
Enter custom package name : com.elaxan.z3ro

custom_name_apk:
Only for use -c or --clone feature
Enter custom_name_apk : Clone apk by Z3RO
```

# Install

Copy this command and paste to Termux
```bash
bash <(curl -Ls https://raw.githubusercontent.com/Score-Inc/PatchGenshinAPK/main/install.sh)
```

# How to use

Make sure you already have AnimeGame.apk for Patch

## Patching with LSPatch

Commands:
```sh
~$ patchgenshin -l <path to APK>
```

Example:
```sh
~$ patchgenshin -l /sdcard/animegame.apk
```

> Then it will patch for animegame.apk.

> If patch success will save to /sdcard with file name animegame-ElaXan.apk

## Patching with apk-mitm

Commands:
```sh
~$ patchgenshin -a <path to APK>
```

Example:
```sh
~$ patchgenshin -a /sdcard/animegame.apk
```

> Then it will.patch for animegame.apk

> If patch success will save to /sdcard with file bame animegame-Z3RO.apk

## Clone APK

Commands:
```sh
~$ patchgenshin -c <path to APK> <package name>
```

Example:
```sh
~$ patchgenshin -c /sdcard/animegame.apk com.elaxan.z3ro
```

> Then it will clone package name for animegame.apk

> If clone success will save to /sdcard with file name animegame-clone-Z3RO.apk

If you want to change the name of the cloned APK, you can use the following command:
```sh
~$ patchgenshin -c <path to APK> <package name> <custom name apk>
``` 

Example:
```sh
~$ patchgenshin -c /sdcard/animegame.apk com.elaxan.z3ro "Clone apk by Z3RO"
```

> Then it will clone package name with custom apk name for animegame.apk

> If clone success will save to /sdcard with file name animegame-clone-Z3RO.apk