import Code.Data as Data
import os
import shutil
import re
import zipfile
from pathlib import Path
from time import sleep

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


def CloneAPK(filename: str, name_to_clone: str):
    if not (os.path.exists(Data.Path_SIGNAPK)):
        Data.Download_SIGNAPK()
    if not (os.path.exists(filename)):
        print(Data.Error_Info + f"{filename} not found!...\nExit with code 1")
        exit(1)
    if (os.stat(filename).st_size == 0):
        print(Data.Error_Info + f"{filename} is empty!...\nExit with code 1")
        exit(1)
    if (name_to_clone == ""):
        print(Data.Error_Info + "Error: name_to_clone is null")
        exit(1)
    if (os.path.exists(f"{Data.Path_Patch}/{name_to_clone}.apk")):
        os.remove(f"{Data.Path_Patch}/{name_to_clone}.apk")
    try:
        shutil.copy(filename, Data.Path_Patch)
    except Exception as e:
        print(Data.Error_Info + f"Error while copying {filename} to {Data.Path_Patch}", e)
        exit(1)
    if (os.path.exists(f"{Data.Path_Patch}/{os.path.basename(filename)}")):
        print(Data.Success_Info + f"Success copy {filename} to {Data.Path_Patch}")
    else:
        print(Data.Error_Info + f"Failed copy {filename} to {Data.Path_Patch}")
        exit(1)
    try:
        with zipfile.ZipFile(f"{Data.Path_APKTOOL}") as z:
            z.testzip()
    except zipfile.BadZipFile:
        print(Data.Error_Info + "Error: apktool.jar is corrupted")
        print(Data.Progress_Info + "Downloading apktool.jar again...")
        try:
            os.remove(Data.Path_APKTOOL)
        except Exception as e:
            print(Data.Error_Info + f"Error while removing {Data.Path_APKTOOL}", e)
            exit(1)
        Data.Download_APKTOOL()
    try:
        os.chdir(Data.Path_Patch)
        os.system(f"java -jar {Data.Path_APKTOOL} d {os.path.basename(filename)} -o decompiling_zex")
    except Exception as e:
        print(Data.Error_Info + f"Error while decompiling {filename}", e)
        exit(1)
    if not (os.path.exists(f"{Data.Path_Patch}/decompiling_zex")):
        print(Data.Error_Info + f"Failed decompiling {filename}")
        exit(1)
    if (os.stat(f"{Data.Path_Patch}/decompiling_zex").st_size == 0):
        print(Data.Error_Info + f"Failed decompiling {filename}")
        exit(1)
    try:
        with open(f"{Data.Path_Patch}/decompiling_zex/AndroidManifest.xml", "r") as f:
            manifest = f.read()
        manifest = manifest.replace("com.miHoYo.GenshinImpact", name_to_clone)
        with open(f"{Data.Path_Patch}/decompiling_zex/AndroidManifest.xml", "w") as f:
            print(Data.Progress_Info + "Writing to AndroidManifest.xml to change package name...")
            f.write(manifest)
            sleep(1)
    except Exception as e:
        print(Data.Error_Info + f"Error while editing manifest {filename}", e)
        exit(1)
    try:
        os.system(f"java -jar {Data.Path_APKTOOL} b decompiling_zex -o {os.path.basename(filename)}.patched.apk")
    except Exception as e:
        print(Data.Error_Info + f"Error while compiling {filename}", e)
        exit(1)
    if not (os.path.exists(f"{Data.Path_Patch}/{os.path.basename(filename)}.patched.apk")):
        print(Data.Error_Info + f"Failed compiling {filename}")
        exit(1)
    if (os.stat(f"{Data.Path_Patch}/{os.path.basename(filename)}.patched.apk").st_size == 0):
        print(Data.Error_Info + f"Failed compiling {filename}")
        exit(1)
    print(Data.Success_Info + f"Success clone {os.path.basename(filename)} to {name_to_clone}")
    print(Data.Progress_Info + "Signing APK...")
    try:
        with zipfile.ZipFile(f"{Data.Path_SIGNAPK}") as z:
            z.testzip()
    except zipfile.BadZipFile:
        print(Data.Error_Info + "Error: uber-apk-signer.jar is corrupted")
        print(Data.Progress_Info + "Downloading uber-apk-signer.jar again...")
        try:
            os.remove(Data.Path_SIGNAPK)
        except Exception as e:
            print(Data.Error_Info + f"Error while removing {Data.Path_SIGNAPK}", e)
            exit(1)
        Data.Download_SIGNAPK()
    try:
        os.system(f"java -jar {Data.Path_SIGNAPK} --apks {os.path.basename(filename)}.patched.apk")
    except Exception as e:
        print(Data.Error_Info + f"Error while signing {filename}", e)
        print(Data.Progress_Info + "Cleaning up...")
        try:
            os.remove(f"{Data.Path_Patch}/{os.path.basename(filename)}.patched.apk")
            shutil.rmtree(f"{Data.Path_Patch}/decompiling_zex")
            os.remove(f"{Data.Path_Patch}/{os.path.basename(filename)}")
            exit(1)
        except Exception as e:
            print(Data.Error_Info + f"Error while cleaning up {filename}", e)
            exit(1)
    if (os.path.exists(f"{Data.Path_Patch}/{os.path.basename(filename)}.patched-aligned-debugSigned.apk")):
        print(Data.Success_Info + f"Success sign {os.path.basename(filename)}.patched.apk")
        print(Data.Progress_Info + "Cleaning up...")
        try:
            os.remove(f"{Data.Path_Patch}/{os.path.basename(filename)}.patched.apk")
            shutil.rmtree(f"{Data.Path_Patch}/decompiling_zex")
            os.remove(f"{Data.Path_Patch}/{os.path.basename(filename)}")
            print(Data.Success_Info + f"Success clone {os.path.basename(filename)} to {name_to_clone}")
        except Exception as e:
            print(Data.Error_Info + f"Error while cleaning up {filename}", e)
            exit(1)
    try:
        print(Data.Progress_Info + "Rename signed APK...")
        os.rename(f"{Data.Path_Patch}/{os.path.basename(filename)}.patched-aligned-debugSigned.apk", f"{Data.Path_Patch}/{os.path.basename(filename)}-clone-Z3RO.apk")
    except Exception as e:
        print(Data.Error_Info + f"Error while renaming {filename}", e)
        exit(1)
    try:
        print(Data.Progress_Info + "Moving APK to /sdcard...")
        shutil.move(f"{Data.Path_Patch}/{os.path.basename(filename)}-clone-Z3RO.apk", f"/sdcard/{os.path.basename(filename)}-clone-Z3RO.apk")
    except Exception as e:
        print(Data.Error_Info + f"Error while moving {filename}", e)
        exit(1)
    print(Data.Success_Info + f"Success move {os.path.basename(filename)}-clone-Z3RO.apk to /sdcard")
    exit(0)