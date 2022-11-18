import os
import sys
from shutil import which
from colorama import Fore as Color
from pathlib import Path
from time import sleep
import requests

Error_Info = Color.RED + "E: " + Color.RESET
Progress_Info = Color.GREEN + "I: " + Color.RESET
Warning_Info = Color.YELLOW + "W: " + Color.RESET
Ask_Info = Color.MAGENTA + "?: " + Color.RESET
Get_Home = Path.home()
Path_Patch = f"{Get_Home}/.ElaXan/Patch"
Path_Module = f"{Path_Patch}/lspatch.jar"
Path_APKTOOL = f"{Path_Patch}/apktool.jar"
Path_Module_LSPosed = f"{Path_Patch}/app-release.apk"
Link_LSPatch = "https://github.com/LSPosed/LSPatch/releases/download/v0.5/lspatch.jar"
Link_Module_LSPosed = "https://elaxan.com/download/Genshin-Android/app-release.apk"
Usage = f"{Error_Info}Subcommand not entered!\nUsage :\n1. {os.path.basename(sys.argv[0])} -m uninstall\n2. {os.path.basename(sys.argv[0])} -m apk-mitm"
Link_APKTOOL = "https://elaxan.com/download/apktool/apktool.jar"

def Download_Files(url: str, path: str):
    Download = requests.get(url, allow_redirects=True)
    with open(path, "wb") as Downloading:
        Downloading.write(Download.content)
        Downloading.close()

def Download_Files2(url: str, path: str):
    # Check if command wget is not installed
    if not (which("wget")):
        print(Progress_Info + "Installing wget command")
        os.system("apt install wget -y &> /dev/null")
    os.system("wget " + url + " -O " + path + " > /dev/null 2>&1")
    sleep(1)