# File Name    : musicplayer.py
# Author       : Minseok Ryu
# Date Created : 06/12/23
# Purpose      : To play, given a music file

from pygame import mixer
from libs.choosefile import find_path_GUI
from libs.decorators import prettyprint

# import sys
# here = lambda x: os.path.abspath(os.path.join(os.path.dirname(__file__), x))

class Player:
    def __init__(self, file):
        self.file = file
        self._setup_audio_env()

    # @prettyprint
    def _setup_audio_env(self):
        mixer.init()
        mixer.music.load(self.file)
        mixer.music.set_volume(0.5)
        mixer.music.play()

        print("")
        print("Playing: %s" % self.file)
        print("")

    def play_music(self):
        while True:

            # Terminal-based control
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


if __name__=="__main__":
    file = choosefile.find_path_GUI()
    Player.play_music()