import shutil
import os
import Code.Data as Data
from shutil import which
from time import sleep
from pathlib import Path

def run():
    # Check if java is installed
    if not (which("java")):
        print(Data.Progress_Info + "Installing Java")
        os.system("apt install openjdk-17 -y")
    user_input = input("Enter file Genshin.apk : ")
    if (user_input == ""):
        while (user_input == ""):
            # If user not entered path to Genshin.apk
            print(Data.Error_Info + "Please enter path!")
            sleep(1)
            user_input = input("Enter file Genshin.apk : ")
    if not (os.path.exists(user_input)):
        # If file not found, this message will be appears
        print(Data.Error_Info + "File for " + user_input + " Not exist")
        exit(1)
    # If Folder not found, will be create immediately
    if not (os.path.exists(f"{Path.home()}/.ElaXan")):
        os.mkdir(f"{Path.home()}/.ElaXan")
    if not (os.path.exists(Data.Path_Patch)):
        os.mkdir(Data.Path_Patch)
    print(Data.Progress_Info + "Copying files from " + user_input + " to " + Data.Path_Patch)
    # Copying files
    shutil.copy(user_input, Data.Path_Patch)
    if not (os.path.exists(Data.Path_Module)):
        try:
            # Downloading lspatch.jar if its not exists/found
            print(Data.Progress_Info + "Downloading module .jar")
            Data.Download_Files(Data.Link_LSPatch, Data.Path_Module)
        except Exception as e:
            # If Failed download, this message will appear
            print(Data.Error_Info + "Cant download lspatch.jar\nReason : ", e)
            exit(1)
    if not (os.path.exists(Data.Path_Module_LSPosed)):
        try:
            # Downloading Module LSPosed in my website, if its not exists/found
            print(Data.Progress_Info + "Downloading Module LSPosed")
            Data.Download_Files2(Data.Link_Module_LSPosed, Data.Path_Module_LSPosed)
        except Exception as e:
            # If Failed download, this message will appear
            print(Data.Error_Info + "Cant download module LSPosed\nReason : ", e)
            exit(1)
    Getting_FileName = os.path.basename(user_input)
    Getting_FileName_Module = os.path.basename(Data.Path_Module_LSPosed)
    try:
        # Change Directory
        os.chdir(Data.Path_Patch)
        print(Data.Progress_Info + "Patching Genshin .apk")
        # Start patching Genshin .apk
        os.system("java -jar lspatch.jar " + Getting_FileName + " -m " + Getting_FileName_Module)
        print(Data.Progress_Info + "Trying to move apk")
        Name_Patch = Getting_FileName.replace(".apk", "")
        shutil.move(Name_Patch + "-348-lspatched.apk", f"/sdcard/{Name_Patch}-ElaXan.apk")
        print(Data.Progress_Info + f"Done Move file to /sdcard/{Name_Patch}-ElaXan.apk")
    except Exception as e:
        print(f"Failed patch {Getting_FileName}.\nReason : ", e)
        exit(1)