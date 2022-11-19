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
Success_Info = Color.GREEN + "✓: " + Color.RESET
Cancel_Info = Color.YELLOW + "X: " + Color.RESET
Get_Home = Path.home()
Path_Patch = f"{Get_Home}/.ElaXan/Patch"
Path_Module = f"{Path_Patch}/lspatch.jar"
Path_APKTOOL = f"{Path_Patch}/apktool.jar"
Path_Module_LSPosed = f"{Path_Patch}/yuuki.yuukips.apk"
Link_LSPatch = "https://github.com/LSPosed/LSPatch/releases/download/v0.5/lspatch.jar"
Link_Module_LSPosed = "https://elaxan.com/download/Genshin-Android/yuuki.yuukips.apk"
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

def Move_Files(path: str, path2: str):
    os.system("mv " + path + " " + path2 + " > /dev/null 2>&1")
    sleep(1)

def Change_Permission(path: str):
    os.system("chmod 777 " + path + " > /dev/null 2>&1")
    sleep(1)

def Check_Files(path: str):
    if not os.path.exists(path):
        return False
    else:
        return True

def Download_LSPatch():
    if not Check_Files(Path_Module):
        print(Progress_Info + "Downloading LSPatch")
        Download_Files(Link_LSPatch, Path_Module)
        Change_Permission(Path_Module)
        print(Success_Info + "Downloaded LSPatch")
    else:
        print(Progress_Info + "LSPatch already downloaded")

def Download_APKTOOL():
    if not Check_Files(Path_APKTOOL):
        print(Progress_Info + "Downloading APKTOOL")
        Download_Files(Link_APKTOOL, Path_APKTOOL)
        Change_Permission(Path_APKTOOL)
        print(Success_Info + "Downloaded APKTOOL")
    else:
        print(Progress_Info + "APKTOOL already downloaded")

def Download_Module_LSPosed():
    if not Check_Files(Path_Module_LSPosed):
        print(Progress_Info + "Downloading LSPosed Module")
        Download_Files(Link_Module_LSPosed, Path_Module_LSPosed)
        print(Success_Info + "Downloaded LSPosed Module")
    else:
        print(Progress_Info + "LSPosed Module already downloaded")

def Install_apkmitm():
    # check if command apk-mitm is not installed
    if not (which("apk-mitm")):
        print(Progress_Info + "Installing apk-mitm")
        os.system("pip install apk-mitm > /dev/null 2>&1")
        print(Success_Info + "Installed apk-mitm")
    else:
        print(Progress_Info + "apk-mitm already installed")

def Check_Requirements_apkmitm():
    # if Path_Patch not exist
    if not Check_Files(Path_Patch):
        # create Path_Patch folder
        os.system("mkdir " + Path_Patch + " > /dev/null 2>&1")
        sleep(1)
        # download APKTOOL
        Download_APKTOOL()
        # install apk-mitm
        Install_apkmitm()
    else:
        # download APKTOOL
        Download_APKTOOL()
        # install apk-mitm
        Install_apkmitm()

def Check_Requirements_LSPatch():
    # if Path_Patch not exist
    if not Check_Files(Path_Patch):
        # create Path_Patch folder
        os.system("mkdir " + Path_Patch + " > /dev/null 2>&1")
        sleep(1)
        # download LSPatch
        Download_LSPatch()
        # download Module LSPosed
        Download_Module_LSPosed()
    else:
        # download LSPatch
        Download_LSPatch()
        # download Module LSPosed
        Download_Module_LSPosed()
