#!/data/data/com.termux/files/usr/bin/python3

import Code.run as run
import Code.Menu as Menu
import Code.Data as Data
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        Data.Help()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--uninstall":
            Menu.Uninstall()
        elif sys.argv[1] == "--help":
            Data.Help()
        elif sys.argv[1] == "--version":
            print("Version : " + Data.Version)
        elif sys.argv[1] == "--update":
            print("Still development")
            exit(0)
        elif sys.argv[1] == "--apkmitm" or sys.argv[1] == "-a":
            print(Data.Error_Info + "Please enter file name")
            exit(1)
        elif sys.argv[1] == "--lspatch" or sys.argv[1] == "-l":
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
        else:
            print(Data.Error_Info + "Wrong input!")
            Data.Help()
    else:
        print(Data.Error_Info + "Wrong input!")
        Data.Help()