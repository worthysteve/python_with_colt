names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# finds the minimum length of a name in names
print(min(len(name) for name in names)) # 3

# find the longest name itself
print(max(names, key=lambda n:len(n))) #Ollivander

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
print(min(songs, key=lambda s: s['playcount'])) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
print(max(songs, key=lambda s: s['playcount'])['title']) #YMCA