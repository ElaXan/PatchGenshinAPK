from colorama import Fore as Color
from pathlib import Path

Error_Info = Color.RED + "E: " + Color.RESET
Progress_Info = Color.GREEN + "I: " + Color.RESET
Warning_Info = Color.YELLOW + "W: " + Color.RESET
Get_Home = Path.home()
Path_Patch = f"{Get_Home}/.ElaXan/Patch"
Path_Module = f"{Path_Patch}/lspatch.jar"
Path_Module_LSPosed = f"{Path_Patch}/app-release.apk"
Link_LSPatch = "https://github.com/LSPosed/LSPatch/releases/download/v0.5/lspatch.jar"
Link_Module_LSPosed = "https://elaxan.com/Download/Genshin-Android/app-release.apk"

def subcommand_Print():
    print(Color.YELLOW + "Subcommand Not entered!" + Color.RESET)
    exit(1)
