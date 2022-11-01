
import sys
import Code.Data as Data
import Code.run as run

def main():
    try:
        subcommand = sys.argv[1]
        if subcommand == "run":
            run.run()
        else:
            print("Todo")
    except IndexError:
        Data.subcommand_Print()
if __name__ == "__main__":
    main()