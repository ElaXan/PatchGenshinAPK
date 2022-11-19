import shutil
import os
import re
import Code.Data as Data
from shutil import which
from time import sleep
from pathlib import Path

def run(file_apk_to_patch: str):
    os.chdir(Data.Path_Patch)
    if not (which("java")):
        Data.Install_Program("openjdk-17")
    Data.Check_Requirements_LSPatch()
    # if file_apk_to_patch is null, then exit with print File not found
    if (file_apk_to_patch == ""):
        print(Data.Error_Info + "File not found!...\nExit with code 1")
        exit(1)
    # If user_input is not file .apk
    if not (file_apk_to_patch.endswith(".apk")):
        print(Data.Error_Info + "File is not .apk")
        exit(1)
    # If user_input file not found
    if not (os.path.exists(file_apk_to_patch)):
        print(Data.Error_Info + "File not found!")
        exit(1)
    # If Folder Path.home() + "/.ElaXan" not found, will be create immediately
    if not (os.path.exists(f"{Path.home()}/.ElaXan")):
        os.mkdir(Path.home() + "/.ElaXan")
    
    if not (os.path.exists(Data.Path_Patch)):
        os.mkdir(Data.Path_Patch)
    print(Data.Progress_Info + "Copying files from " + file_apk_to_patch + " to " + Data.Path_Patch)
    # Copying files
    shutil.copy(file_apk_to_patch, Data.Path_Patch)
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
    Getting_FileName = os.path.basename(file_apk_to_patch)
    Getting_FileName_Module = os.path.basename(Data.Path_Module_LSPosed)
    try:
        # Change Directory
        os.chdir(Data.Path_Patch)
        print(Data.Progress_Info + "Patching Genshin .apk")
        # Start patching Genshin .apk
        os.system("java -jar lspatch.jar " + Getting_FileName + " -m " + Getting_FileName_Module)
        print(Data.Progress_Info + "Trying to move apk")
        Name_Patch = re.sub(r".apk$", "", Getting_FileName)
        File_Move = f"/sdcard/{Name_Patch}-ElaXan.apk"
        shutil.move(Name_Patch + "-348-lspatched.apk", File_Move)
        # Remove file from Getting_FileName
        os.remove(Getting_FileName)
        if not (os.path.exists(File_Move)):
            print(f"Failed to move {Name_Patch} to /sdcard")
            if (os.path.exists(f"{Name_Patch}-ElaXan.apk")):
                os.remove(f"{Name_Patch}-ElaXan.apk")
            exit(1)
        else:
            print(Data.Progress_Info + f"Done Move file to /sdcard with name {Name_Patch}-ElaXan.apk")
            exit(0)
    except Exception as e:
        print(f"Failed patch {Getting_FileName}.\nReason : ", e)
        exit(1)