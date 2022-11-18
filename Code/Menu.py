import Code.Data as Data
import os
import shutil
import re
from pathlib import Path
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
    os.chdir(Path.home())
    Data.Check_Files_Patch()
    Apk_to_Patch = input(Data.Ask_Info + "Path Genshin.apk : ")
    if not (os.path.exists(Apk_to_Patch)):
        print(Data.Error_Info + Apk_to_Patch + " not found!...\nExit with code 1")
        exit(1)
    # if not file is apk
    if not (Apk_to_Patch.endswith(".apk")):
        print(Data.Error_Info + Apk_to_Patch + " is not apk file!...\nExit with code 1")
        exit(1)
    os.chdir(Path.home())
    print(Data.Progress_Info + f"Patching {os.path.basename(Apk_to_Patch)}")
    try:
        os.system(f"apk-mitm --apktool {Data.Path_APKTOOL} {Apk_to_Patch}")
    except KeyboardInterrupt:
        print(Data.Error_Info + "Exit/Cancel by User")
        exit(1)
    except Exception as e:
        print(Data.Error_Info + "Error while patching...", e)
        exit(1)
    print(Data.Progress_Info + "Trying move .apk/.apks to /sdcard")
    Name_Patch = re.sub(r".apk$", "", os.path.basename(Apk_to_Patch))
    File_Move = f"{Name_Patch}-patched.apk"
    try:
        shutil.move("./" + File_Move, f"/sdcard/{Name_Patch}-Z3RO.apk")
    except FileNotFoundError:
        print(Data.Error_Info + f"Error move {File_Move} to /sdcard because not exist\n\nExit with code 1")
        exit(1)
    if (os.path.exists(f"/sdcard/{Name_Patch}-Z3RO.apk")):
        print(Data.Success_Info + f"Success move .apk to /sdcard with name {Name_Patch}-Z3RO.apk")
        exit(0)
    else:
        print(Data.Error_Info + f"Failed move .apk to /sdcard with name {Name_Patch}-Z3RO.apk")
        exit(1)