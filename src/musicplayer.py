# File Name    : musicplayer.py
# Author       : Minseok Ryu
# Date Created : 06/12/23
# Purpose      : Music player in python

from pygame import mixer
from libs.choosefile import findpathGUI

mixer.init()
filename = findpathGUI()
mixer.music.load(filename)
mixer.music.set_volume(0.5)
mixer.music.play()

while True:
    print("Press 'p' to pause")
    print("Press 'r' to resume")
    print("Press 'v' set volume")
    print("Press 'e' to exit")

    ch = input("['p','r','v','e']>>>")

    if ch == "p":
        mixer.music.pause()
    elif ch == "r":
        mixer.music.unpause()
    elif ch == "v":
        v = float(input("Enter volume(0 to 1): "))
        mixer.music.set_volume(v)
    elif ch == "e":
        mixer.music.stop()
        break