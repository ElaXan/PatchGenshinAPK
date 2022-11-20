#!/data/data/com.termux/files/usr/bin/python3

import Code.run as run
import Code.Menu as Menu
import Code.Data as Data
from pathlib import Path
import os
import sys

if __name__ == "__main__":
    if not (os.path.exists(f"{Path.home()}/.ElaXan")):
        os.mkdir(f"{Path.home()}/.ElaXan")
    if not (os.path.exists(f"{Path.home()}/.ElaXan/Patch")):
        os.mkdir(f"{Path.home()}/.ElaXan/Patch")
    if os.geteuid() == 0:
        print(Data.Error_Info + "Please run this script as normal user")
        exit(1)
    if not (os.path.exists("/sdcard")):
        print(Data.Error_Info + "Please grant storage permission for Termux")
        exit(1)
    if len(sys.argv) == 1:
        Data.Help()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--uninstall" or sys.argv[1] == "-u":
            Menu.Uninstall()
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            Data.Help()
        elif sys.argv[1] == "--version" or sys.argv[1] == "-v":
            print("Version : " + Data.Version)
        elif sys.argv[1] == "--update" or sys.argv[1] == "-up":
            Menu.Update()
        elif sys.argv[1] == "--apkmitm" or sys.argv[1] == "-a":
            print(Data.Error_Info + "Please enter file name")
            exit(1)
        elif sys.argv[1] == "--lspatch" or sys.argv[1] == "-l":
            print(Data.Error_Info + "Please enter file name")
            exit(1)
        elif sys.argv[1] == "--clone" or sys.argv[1] == "-c":
            print(Data.Error_Info + "Please enter file name")
            exit(1)
        else:
            print(Data.Error_Info + "Wrong input!")
            Data.Help()
    elif len(sys.argv) == 3:
        if sys.argv[1] == "--apkmitm" or sys.argv[1] == "-a":
            Menu.apkmitm(sys.argv[2])
        elif sys.argv[1] == "--lspatch" or sys.argv[1] == "-l":
            run.run(sys.argv[2])
        elif sys.argv[1] == "--clone" or sys.argv[1] == "-c":
            print(Data.Error_Info + "Please enter Package name")
            exit(1)
        else:
            print(Data.Error_Info + "Wrong input!")
            Data.Help()
    elif len(sys.argv) == 4:
        if sys.argv[1] == "--clone" or sys.argv[1] == "-c":
            Menu.CloneAPK(sys.argv[2], sys.argv[3], "")
        elif sys.argv[1] == "--lspath" or sys.argv[1] == "-l":
            run.run(sys.argv[2], sys.argv[3])
        else:
            print(Data.Error_Info + "Please enter package name!")
            Data.Help()
    elif len(sys.argv) == 5:
        if sys.argv[1] == "--clone" or sys.argv[1] == "-c":
            Menu.CloneAPK(sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print(Data.Error_Info + "Please enter Custom Name APK!")
            Data.Help()
    else:
        print(Data.Error_Info + "Wrong input!")
        Data.Help()