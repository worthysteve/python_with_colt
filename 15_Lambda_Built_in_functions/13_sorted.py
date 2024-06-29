more_nums = [6,1,8,2]
print(sorted(more_nums))

sorted(more_nums)
print(more_nums)

nums = [4,6,1,30,55,23]
print(sorted(nums, reverse=True))

print("========================================")

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
] 

# To sort users by their username
print(sorted(users,key=lambda user: user['username']))


print("========================================")
# Finding our most active users...
# Sort users by number of tweets, descending
print(sorted(users,key=lambda user: len(user["tweets"]), reverse=True))


print("========================================")
# ANOTHER EXAMPLE DATA SET==================================
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
print(sorted(songs, key=lambda s: s['playcount'], reverse=True))
