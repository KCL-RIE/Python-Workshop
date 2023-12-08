from src import musicplayer2, weatherplayer, weatherplayer
from libs import choosefile, apiMet

file = choosefile.find_path_GUI()

apiKey       = "{INSERT-YOU-APIKEY-HERE}"
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
		mood   = weather.mood_upon_weather(weatherNewry)
		player = weatherplayer.WeatherPlayer(file, mood=mood)
		player.play_music()


## TODO
# Queue playlist
# Save state