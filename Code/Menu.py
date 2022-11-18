import Code.Data as Data
import os
import shutil
from shutil import which

def Uninstall():
    asking_to_uninstall = input("Are you sure want to uninstall? [y/N] : ")
    if asking_to_uninstall == "y" or asking_to_uninstall == "Y":
        pass
    elif asking_to_uninstall == "n" or asking_to_uninstall == "N":
        exit(0)
    else:
        print(Data.Error_Info + "Wrong input!")
        exit(1)
    Path = "/data/data/com.termux/files/usr"
    nameFile = "patchgenshin"
    nameFolder = "PatchGenshinAPK"
    if (os.path.exists(f"{Path}/bin/{nameFile}")):
        print(Data.Progress_Info + f"Removing {nameFile}")
        os.remove(f"{Path}/bin/{nameFile}")
    if (os.path.exists(f"{Path}/share/{nameFolder}")):
        print(Data.Progress_Info + f"Removing folder {nameFolder}")
        shutil.rmtree(f"{Path}/share/{nameFolder}")
    
    if not (os.path.exists(f"{Path}/bin/{nameFile}") and not (os.path.exists(f"{Path}/share/{nameFolder}"))):
        print(Data.Progress_Info + "Success uninstall PatchGenshinAPK")
        exit(0)
    else:
        print(Data.Error_Info + "Failed to uninstall PatchGenshinAPK")
        exit(1)

def apkmitm():
    if not (which("java")):
        print(Data.Progress_Info + "Installing Java Program")
        os.system("apt install openjdk-17")
    if not (which("npm")):
        print(Data.Error_Info + "Please install npm and node manually with newest version")
        print(Data.Error_Info + "Exit with code 1")
        exit(1)
    if not (which("apk-mitm")):
        print(Data.Progress_Info + "Installing apk-mitm Program with npm")
        os.system("npm install -g apk-mitm > /dev/null 2>&1")
    if not (os.path.exists(f"{Data.Path_Patch}")):
        print(Data.Progress_Info + f"Creating folder {Data.Path_Patch}")
        os.mkdir(Data.Path_Patch)
    if not (os.path.exists(f"{Data.Path_APKTOOL}")):
        print(Data.Progress_Info + "Downloading apktool.jar")
        Data.Download_Files2(Data.Link_APKTOOL, Data.Path_APKTOOL)
    Apk_to_Patch = input(Data.Ask_Info + "Path Genshin.apk : ")
    if not (os.path.exists(Apk_to_Patch)):
        print(f"{Data.Error_Info} not found!... Exit with code 1")
        exit(1)
    print(Data.Progress_Info + f"Patching {Apk_to_Patch}")
    try:
        os.system(f"apk-mitm --apktool {Data.Path_APKTOOL} {Apk_to_Patch}")
    except KeyboardInterrupt:
        print(Data.Error_Info + "Exit/Cancel by User")
        exit(1)
    except Exception as e:
        print(Data.Error_Info + "Error while patching...", e)
        exit(1)
