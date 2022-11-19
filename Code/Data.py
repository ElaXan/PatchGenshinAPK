import os
import sys
from shutil import which
from colorama import Fore as Color
from pathlib import Path
from time import sleep
import requests

Version = "1.0.1"
Error_Info = Color.RED + "E: " + Color.RESET
Progress_Info = Color.GREEN + "I: " + Color.RESET
Warning_Info = Color.YELLOW + "W: " + Color.RESET
Ask_Info = Color.MAGENTA + "?: " + Color.RESET
Success_Info = Color.GREEN + "✓: " + Color.RESET
Cancel_Info = Color.YELLOW + "X: " + Color.RESET
json_link = "https://elaxan.com/Project/PatchGenshinAPK/PatchGenshinAPK.json"
Get_Home = Path.home()
Path_Patch = f"{Get_Home}/.ElaXan/Patch"
Path_Module = f"{Path_Patch}/lspatch.jar"
Path_APKTOOL = f"{Path_Patch}/apktool.jar"
Path_Module_LSPosed = f"{Path_Patch}/yuuki.yuukips.apk"
Path_Module_LSPosed_Chinese = f"{Path_Patch}/xfk233.genshinproxy.apk"
Path_SIGNAPK = f"{Path_Patch}/uber-apk-signer-1.2.1.jar"
Link_LSPatch = "https://github.com/LSPosed/LSPatch/releases/download/v0.5/lspatch.jar"
Link_Module_LSPosed = "https://elaxan.com/download/Genshin-Android/yuuki.yuukips.apk"
Link_Module_LSPosed_Chinese = "https://elaxan.com/download/Genshin-Android/xfk233.genshinproxy.apk"
Link_APKTOOL = "https://elaxan.com/download/apktool/apktool.jar"
Link_SIGNAPK = "https://github.com/patrickfav/uber-apk-signer/releases/download/v1.2.1/uber-apk-signer-1.2.1.jar"


def Help():
    print("Usage: patchgenshin [option] [file] [package_name]")
    print("Options:")
    print("  -h, --help\t\tShow this help message and exit")
    print("  -u, --uninstall\tUninstall PatchGenshinAPK")
    print("  -v, --version\t\tShow version")
    print("  -l, --lspatch\t\tPatch Genshin.apk with LSPatch")
    print("  -a, --apkmitm\t\tPatch Genshin.apk with apk-mitm")
    print("  -c, --clone\t\tClone Genshin package name")
    print("")
    print("file:")
    print("Path to APK want to Patch : /sdcard/Genshin.apk")
    print("")
    print("package_name:")
    print("Only for use -c or --clone feature")
    print("Enter custom package name : com.elaxan.z3ro")
    print("")

def Download_Files(url: str, path: str):
    Download = requests.get(url, allow_redirects=True)
    with open(path, "wb") as Downloading:
        Downloading.write(Download.content)
        Downloading.close()

def Download_Files2(url: str, path: str):
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

def get_Text_From_Server():
    text = requests.get("https://elaxan.com/download/Genshin-Android/Text.txt").text
    return text

def Install_Program(program_name: str):
    print(Progress_Info + "Installing " + program_name)
    os.system("apt install " + program_name + " -y > /dev/null 2>&1")
    print(Success_Info + "Installed " + program_name)

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
        Download_Files2(Link_APKTOOL, Path_APKTOOL)
        Change_Permission(Path_APKTOOL)
        print(Success_Info + "Downloaded APKTOOL")
    else:
        print(Progress_Info + "APKTOOL already downloaded")

def Download_Module_LSPosed():
    if not Check_Files(Path_Module_LSPosed):
        print(Progress_Info + "Downloading LSPosed Module [Yuuki]")
        Download_Files2(Link_Module_LSPosed, Path_Module_LSPosed)
        print(Success_Info + "Downloaded LSPosed Module [Yuuki]")
    else:
        print(Progress_Info + "LSPosed Module already downloaded [Yuuki]")

def Download_Chinese_Module():
    if not Check_Files(Path_Module_LSPosed_Chinese):
        print(Progress_Info + "Downloading LSPosed Module [Chinese]")
        Download_Files2(Link_Module_LSPosed_Chinese, Path_Module_LSPosed_Chinese)
        print(Success_Info + "Downloaded LSPosed Module [Chinese]")
    else:
        print(Progress_Info + "LSPosed Module already downloaded [Chinese]")

def Install_apkmitm():
    if not (which("apk-mitm")):
        print(Progress_Info + "Installing apk-mitm")
        os.system("pip install apk-mitm > /dev/null 2>&1")
        print(Success_Info + "Installed apk-mitm")
    else:
        print(Progress_Info + "apk-mitm already installed")

def Download_SIGNAPK():
    if not Check_Files(Path_SIGNAPK):
        print(Progress_Info + "Downloading uber-apk-signer")
        Download_Files2(Link_SIGNAPK, Path_SIGNAPK)
        Change_Permission(Path_SIGNAPK)
        print(Success_Info + "Downloaded uber-apk-signer")
    else:
        print(Progress_Info + "SIGNAPK already uber-apk-signer")

def Check_Requirements_apkmitm():
    if not Check_Files(Path_Patch):
        os.system("mkdir " + Path_Patch + " > /dev/null 2>&1")
        sleep(1)
        Download_APKTOOL()
        Install_apkmitm()
    else:
        Download_APKTOOL()
        Install_apkmitm()

def Check_Requirements_LSPatch():
    if not Check_Files(Path_Patch):
        os.system("mkdir " + Path_Patch + " > /dev/null 2>&1")
        sleep(1)
        Download_LSPatch()
        Download_Module_LSPosed()
        Download_Chinese_Module()
    else:
        Download_LSPatch()
        Download_Module_LSPosed()
        Download_Chinese_Module()
