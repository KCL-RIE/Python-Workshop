from src.musicplayer2 import Player
from src import weather
from libs import choosefile, apiMet

here = lambda x: os.path.abspath(os.path.join(os.path.dirname(__file__), x))
musicDisgust = here('../resources/music/disgust/')

class WeatherPlayer(Player):
	def __init__(self, file, mood):
        super().__init__(file)
        self.mood = mood

	def playDisgusting():
		super(WeatherPlayer, self).play_music()
		return self