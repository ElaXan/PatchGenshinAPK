import shutil
import os
import requests
import Code.Data as Data
from shutil import which
from time import sleep
from pathlib import Path

def run():
    if not (which("java")):
        print(Data.Progress_Info + "Installing Java")
        os.system("apt install openjdk-17 -y")
    user_input = input("Enter file Genshin.apk : ")
    if (user_input == ""):
        while (user_input == ""):
            print(Data.Error_Info + "Please enter path!")
            sleep(1)
            user_input = input("Enter file Genshin.apk : ")
    if not (os.path.exists(user_input)):
        print(Data.Error_Info + "File for " + user_input + " Not exist")
        exit(1)
    if not (os.path.exists(f"{Path.home()}/.ElaXan")):
        os.mkdir(f"{Path.home()}/.ElaXan")
    if not (os.path.exists(Data.Path_Patch)):
        os.mkdir(Data.Path_Patch)
    print(Data.Progress_Info + "Copying files from " + user_input + " to " + Data.Path_Patch)
    shutil.copy(user_input, Data.Path_Patch)
    if not (os.path.exists(Data.Path_Module)):
        try:
            print(Data.Progress_Info + "Downloading module .jar")
            Download = requests.get(Data.Link_LSPatch)
            open(Data.Path_Module, "wb").write(Download.content)
        except Exception as e:
            print(Data.Error_Info + "Cant download lspatch.jar\nReason : ", e)
            exit(1)
    if not (os.path.exists(Data.Path_Module_LSPosed)):
        try:
            print(Data.Progress_Info + "Downloading Module LSPosed")
            Download = requests.get(Data.Link_Module_LSPosed)
            open(Data.Path_Module_LSPosed, "wb").write(Download.content)
        except Exception as e:
            print(Data.Error_Info + "Cant download module LSPosed\nReason : ", e)
            exit(1)
    Getting_FileName = os.path.basename(user_input)
    Getting_FileName_Module = os.path.basename(Data.Path_Module_LSPosed)
    try:
        os.chdir(Data.Path_Patch)
        print(Data.Progress_Info + "Patching Genshin .apk")
        os.system("java -jar lspatch.jar " + Getting_FileName + " -m " + Getting_FileName_Module)
    except Exception as e:
        print(Data.Error_Info + "Error while patching.\nReason : ",e)
        exit(1)