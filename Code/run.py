import shutil
import os
import Code.Data as Data
from shutil import which
from pathlib import Path

def run(file_apk_to_patch: str, use_2_modules: bool = False, Modules_use_for_1_patch: str = "Not_Set"):
    if use_2_modules == "False" or use_2_modules == "false":
        print(Data.Progress_Info + "Using 1 modules for Patching")
    elif use_2_modules == "True" or use_2_modules == "true":
        print(Data.Progress_Info + "Using 2 modules for Patching")
    else:
        print(Data.Warning_Info + "Using 1 modules for Patching")
    if Modules_use_for_1_patch == "Not_Set":
        print(Data.Warning_Info + "Choosing Modules for Patching is not set, will use as default to YuukiModule")
        Modules_use_for_1_patch = "YuukiModule"
    if Modules_use_for_1_patch == "YuukiModule" or Modules_use_for_1_patch == "1":
        print(Data.Progress_Info + "Using Yuuki Module for Patching")
    elif Modules_use_for_1_patch == "xfk233" or Modules_use_for_1_patch == "2":
        print(Data.Progress_Info + "Using xfk233 Module for Patching")
    else:
        print(Data.Warning_Info + "Using Yuuki Module for Patching")
        Modules_use_for_1_patch = "YuukiModule"

    os.chdir(Data.Path_Patch)
    if not (which("java")):
        Data.Install_Program("openjdk-17")
    Data.Check_Requirements_LSPatch()
    if (file_apk_to_patch == ""):
        print(Data.Error_Info + "File not found!...\nExit with code 1")
        exit(1)
    if not (file_apk_to_patch.endswith(".apk")):
        print(Data.Error_Info + "File is not .apk")
        exit(1)
    if not (os.path.exists(file_apk_to_patch)):
        print(Data.Error_Info + "File not found!")
        exit(1)
    if not (os.path.exists(f"{Path.home()}/.ElaXan")):
        os.mkdir(Path.home() + "/.ElaXan")
    
    if not (os.path.exists(Data.Path_Patch)):
        os.mkdir(Data.Path_Patch)
    print(Data.Progress_Info + "Copying files " + os.path.basename(file_apk_to_patch) + " to " + Data.Path_Patch)
    shutil.copy(file_apk_to_patch, Data.Path_Patch)
    if not (os.path.exists(Data.Path_Module)):
        try:
            print(Data.Progress_Info + "Downloading module .jar")
            Data.Download_Files(Data.Link_LSPatch, Data.Path_Module)
        except Exception as e:
            print(Data.Error_Info + "Cant download lspatch.jar\nReason : ", e)
            exit(1)
    if not (os.path.exists(Data.Path_Module_LSPosed)):
        try:
            print(Data.Progress_Info + "Downloading Module LSPosed")
            Data.Download_Files2(Data.Link_Module_LSPosed, Data.Path_Module_LSPosed)
        except Exception as e:
            print(Data.Error_Info + "Cant download module LSPosed\nReason : ", e)
            exit(1)
    Getting_FileName = os.path.basename(file_apk_to_patch)
    Getting_FileName_Module = os.path.basename(Data.Path_Module_LSPosed)
    Getting_FileName_Module2 = os.path.basename(Data.Path_Module_LSPosed_Chinese)
    try:
        os.chdir(Data.Path_Patch)
        print(Data.Progress_Info + "Patching " + os.path.basename(file_apk_to_patch))
        if use_2_modules == "False" or use_2_modules == "false":
            if Modules_use_for_1_patch == "YuukiModule" or Modules_use_for_1_patch == "1":
                os.system(f"java -jar lspatch.jar {file_apk_to_patch} -m {Getting_FileName_Module} > /dev/null 2>&1")
            elif Modules_use_for_1_patch == "xfk233" or Modules_use_for_1_patch == "2":
                os.system(f"java -jar lspatch.jar {file_apk_to_patch} -m {Getting_FileName_Module2} > /dev/null 2>&1")
            else:
                os.system(f"java -jar lspatch.jar {file_apk_to_patch} -m {Getting_FileName_Module} > /dev/null 2>&1")
        elif use_2_modules == "True" or use_2_modules == "true":
            os.system("java -jar lspatch.jar " + Getting_FileName + " -m " + Getting_FileName_Module + " -m " + Getting_FileName_Module2 + " > /dev/null 2>&1")
        else:
            os.system("java -jar lspatch.jar " + Getting_FileName + " -m " + Getting_FileName_Module + " > /dev/null 2>&1")
        print(Data.Success_Info + "Patching " + os.path.basename(file_apk_to_patch) + " Done")
        print(Data.Progress_Info + "Trying to move apk")
        Name_Patch = Getting_FileName[:-4] + ""
        File_Move = f"/sdcard/{Name_Patch}-ElaXan.apk"
        shutil.move(Name_Patch + "-348-lspatched.apk", File_Move)
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