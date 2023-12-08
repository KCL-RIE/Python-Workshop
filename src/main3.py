from src import musicplayer2, weather
from libs import choosefile, apiMet

file = choosefile.find_path_GUI()

apiKey       = "{INSERT-YOU-APIKEY-HERE}"
metData      = apiMet.MetManager(apiKey)
metData      = metData.extract_from_api()
weatherNewry = metData[5]  # Code smells of five fish!

mood = weather.mood_upon_weather(weatherNewry)

if __name__=="__main__":
	# Class instance
	# player = musicplayer2.Player(file, mood)
	# player.play_music()

	print(mood)

	## TODO
	# Queue playlist
	# Save state