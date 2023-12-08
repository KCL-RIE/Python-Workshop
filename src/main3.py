from src import musicplayer2, weatherplayer, weatherplayer
from libs import choosefile, apiMet

file = choosefile.find_path_GUI()

apiKey       = "20079105-05bc-481c-bd82-87310eee8eca"
metData      = apiMet.MetManager(apiKey)
metData      = metData.extract_from_api()
weatherNewry = metData[5]  # Code smells of five fish!

if __name__=="__main__":
	print("Manual : m  |  Automatic : a")
	mode = input("Enter your mode: ")

	if mode == 'm':
		player = musicplayer2.Player(file)
		player.play_music()
	elif mode == 'a':
		moodChoice = input('Angry : a  |  Disgust : d  |  Fear : f  |  Sad : s  |  Joy : j')

		here = lambda x: os.path.abspath(os.path.join(os.path.dirname(__file__), x))
		musicDisgust = here('../resources/music/disgust/R.I.E_Tribe.mp3')
		# for song in musicDisgust:
		mood   = weather.mood_upon_weather(weatherNewry)
		player = weatherplayer.WeatherPlayer(musicDisgust, mood=mood)
		player.play_music()
			


## TODO
# Queue playlist
# Save state