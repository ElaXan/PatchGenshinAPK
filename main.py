#!/data/data/com.termux/files/usr/bin/python3

import Code.run as run
import Code.Menu as Menu
import Code.Data as Data
import sys

if __name__ == "__main__":
    try:
        subcommand = sys.argv[1]
        subcommand2 = sys.argv[2]
        if subcommand == "-m":
            if subcommand2 == "uninstall":
                Menu.Uninstall()
            else:
                print(Data.Usage)
    except IndexError:
        try:
            if subcommand == "-m":
                print(Data.Usage)
                exit(1)
            elif not subcommand == "":
                run.run(subcommand)
        except NameError:
            run.run("")