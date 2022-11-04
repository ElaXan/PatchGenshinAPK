import Code.run as run
import sys

if __name__ == "__main__":
    try:
        subcommand = sys.argv[1]
        if not subcommand == "":
            run.run(subcommand)
    except IndexError:
        run.run("")