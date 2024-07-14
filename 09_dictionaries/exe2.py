# Access Data in a Dictionary Exercise
# Given the dictionary below:

# artist = {
#     "first": "Neil",
#     "last": "Young",
# }
# Declare a variable called full_name  that is equal to artist's first  and last  names with a space between. You must reference the values associated with those keys in the artist dictionary.

# print(full_name)
# # Neil Young

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist['first'] + " " + artist['last']
print(full_name)

# format() Solution
# Solution using the format() method:

artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = "{} {}".format(artist["first"], artist["last"])
print(full_name)

# F-String Solution
# My personal favorite version, BUT remember it only works in Python 3.6 or greater.   
# Note: we have to pay attention to our quotes in this solution!

artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = f"{artist['first']} {artist['last']}"
print(full_name)