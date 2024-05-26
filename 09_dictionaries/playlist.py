playlist = {
	'title': 'patagonia bus', 
	'author': 'Steven Daniel', 
	'songs': [
		{'title': "I don't care", 'artist': ['Boy spice', 'khalid'], 'duration': 2.5},
		{'title': 'One life', 'artist': ['Famous'], 'duration': 5.25},
		{'title': 'I love you', 'artist': ['P-square'], 'duration': 2.0}
	]
}

total_length = 0
for song in playlist['songs']:
	total_length += song['duration']
	# print(song['title'])

print(total_length)
print(f"The playlist {playlist['title']} by {playlist['author']} has {len(song)} songs with a total duration of {total_length} minutes!")