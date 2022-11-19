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
            Data.Version()
        elif sys.argv[1] == "--update":
            run.Update()
        elif sys.argv[1] == "--apkmitm":
            Menu.apkmitm("")
        elif sys.argv[1] == "--lspatch":
            run.run("")
        else:
            Data.Help()
    elif len(sys.argv) == 3:
        if sys.argv[1] == "--apkmitm" or sys.argv[1] == "-a":
            Menu.apkmitm(sys.argv[2])
        elif sys.argv[1] == "--lspatch" or sys.argv[1] == "-l":
            run.run(sys.argv[2])
        else:
            Data.Help()
    else:
        Data.Help()