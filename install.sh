if ! (command -v git &> /dev/null); then 
    apt install git -y
fi
if ! (command -v python3 &> /dev/null); then
    apt install python -y
fi
path="$PREFIX/share"
pathPatch="$path/PatchGenshinAPK"
if [ -d $pathPatch ]; then
    rm -rf $pathPatch
fi
if [ -f "$PREFIX/bin/patchgenshin" ]; then
    rm "$PREFIX/bin/patchgenshin"
fi
cd $path
git clone https://github.com/Score-Inc/PatchGenshinAPK
cd $pathPatch
pip3 install -r requirements.txt
ln -sv $pathPatch/main.py $PREFIX/bin/patchgenshin
chmod +x $PREFIX/bin/patchgenshin
if [[ -f "$PREFIX/bin/patchgenshin" ]]; then
    echo "Install Success, now enter command \"patchgenshin\""
    exit 0
else
    echo "Failed install"
    exit 1
fi