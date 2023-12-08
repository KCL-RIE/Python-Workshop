## MOOD VARS
_MOOD_SAD     = 1
_MOOD_ANGRY   = 2
_MOOD_DISGUST = 3
_MOOD_FEAR    = 4
_MOOD_JOY     = 5

## TODO: Refactor by grouping similar weather <-> mood
def mood_upon_weather(weather):
	if weather == 'NA':  # Not available
		return _MOOD_SAD
	elif weather == 0:   # Clear night
		return _MOOD_JOY
	elif weather == 1:   # Sunny day
		return _MOOD_JOY
	elif weather == 2:   # Partly cloudy (night)
		return _MOOD_SAD
	elif weather == 3:   # Partly cloudy (day)
		return _MOOD_SAD
	elif weather == 4:   # Not used
		return _MOOD_SAD
	elif weather == 5:   # Mist
		return _MOOD_SAD
	elif weather == 6:   # Fog
		return _MOOD_SAD
	elif weather == 7:   # Cloudy
		return _MOOD_SAD
	elif weather == 8:   # Overcast
		return _MOOD_SAD
	elif weather == 9:   # Light rain shower (night)
		return _MOOD_SAD
	elif weather == 10:  # Light rain shower (day)
		return _MOOD_SAD
	elif weather == 11:  # Drizzle
		return _MOOD_SAD
	elif weather == 12:  # Light rain
		return _MOOD_SAD
	elif weather == 13:  # Heavy rain shower (night)
		return _MOOD_ANGRY
	elif weather == 14:  # Heavy rain shower (day)
		return _MOOD_ANGRY
	else:
		return _MOOD_JOY