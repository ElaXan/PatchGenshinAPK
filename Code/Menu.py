import Code.Data as Data
import os
import shutil
import re
from pathlib import Path

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

def apkmitm(File_Name: str):
    os.chdir(Path.home())
    Data.Check_Requirements_apkmitm()
    if (File_Name == ""):
        print(Data.Error_Info + "File not found!...\nExit with code 1")
        exit(1)
    if not (os.path.exists(File_Name)):
        print(Data.Error_Info + File_Name + " not found!...\nExit with code 1")
        exit(1)
    if not (File_Name.endswith(".apk")):
        print(Data.Error_Info + File_Name + " is not apk file!...\nExit with code 1")
        exit(1)
    os.chdir(Path.home())
    print(Data.Progress_Info + f"Patching {os.path.basename(File_Name)}")
    try:
        os.system(f"apk-mitm --apktool {Data.Path_APKTOOL} {File_Name}")
    except KeyboardInterrupt:
        print(Data.Error_Info + "Exit/Cancel by User")
        exit(1)
    except Exception as e:
        print(Data.Error_Info + "Error while patching...", e)
        exit(1)
    print(Data.Progress_Info + "Trying move .apk/.apks to /sdcard")
    Name_Patch = re.sub(r".apk$", "", os.path.basename(File_Name))
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

def Update():
    try:
        os.system("curl -s https://elaxan.com/Project/PatchGenshinAPK/PatchGenshinAPK.json > PatchGenshinAPK.json")
    except Exception as e:
        print(Data.Error_Info + "Error while loading PatchGenshinAPK.json", e)
        exit(1)
    if not (os.path.exists("PatchGenshinAPK.json")):
        print(Data.Error_Info + "PatchGenshinAPK.json not found!...\nExit with code 1")
        exit(1)
    if (os.stat("PatchGenshinAPK.json").st_size == 0):
        print(Data.Error_Info + "PatchGenshinAPK.json is empty!...\nExit with code 1")
        exit(1)
    with open("PatchGenshinAPK.json", "r") as f:
        json_file = f.read()
    if (Data.Version in json_file):
        print(Data.Progress_Info + "You are using the latest version")
        os.remove("PatchGenshinAPK.json")
        exit(0)
    else:
        try:
            os.remove("PatchGenshinAPK.json")
            print("New version available!")
            asking_to_update = input("Do you want to update? [y/N] : ")
            if asking_to_update == "y" or asking_to_update == "Y":
                pass
            elif asking_to_update == "n" or asking_to_update == "N":
                exit(0)
            else:
                print(Data.Error_Info + "Wrong input!")
                exit(1)
            os.system("apt update -y && apt upgrade -y")
            if not (os.path.exists("/data/data/com.termux/files/usr/bin/git")):
                os.system("apt install git -y")
            if (os.path.exists("/data/data/com.termux/files/usr/share/PatchGenshinAPK")):
                shutil.rmtree("/data/data/com.termux/files/usr/share/PatchGenshinAPK")
            if (os.path.exists("/data/data/com.termux/files/usr/bin/patchgenshin")):
                os.remove("/data/data/com.termux/files/usr/bin/patchgenshin")
            if not (os.path.exists("/data/data/com.termux/files/home/PGAPK_Update")):
                os.mkdir("/data/data/com.termux/files/home/PGAPK_Update")
            os.chdir("/data/data/com.termux/files/home/PGAPK_Update")
            os.system("git clone https://github.com/Score-Inc/PatchGenshinAPK.git")
            shutil.move("/data/data/com.termux/files/home/PGAPK_Update/PatchGenshinAPK", "/data/data/com.termux/files/usr/share")
            os.system("ln -s /data/data/com.termux/files/usr/share/PatchGenshinAPK/main.py /data/data/com.termux/files/usr/bin/patchgenshin")
            os.system("chmod 755 /data/data/com.termux/files/usr/bin/patchgenshin")
            if (os.path.exists("/data/data/com.termux/files/home/PGAPK_Update")):
                shutil.rmtree("/data/data/com.termux/files/home/PGAPK_Update")
            if (os.path.exists("/data/data/com.termux/files/usr/share/PatchGenshinAPK")):
                print(Data.Success_Info + "Success update PatchGenshinAPK")
                exit(0)
            else:
                print(Data.Error_Info + "Failed update PatchGenshinAPK")
                exit(1)
        except Exception as e:
            print(Data.Error_Info + "Error while updating PatchGenshinAPK", e)
            exit(1)