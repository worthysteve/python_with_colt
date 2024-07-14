x = (1,2,3)
print(3 in x)

alphabet = ('a', 'b', 'c', 'd')
print(type(alphabet))

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
print(months[0])

locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office",
}

print(locations[(40.7128, 74.0060)])

cat = {"name": "biscuit", "age": .5, "favorite_toy": "my chapstick"}
print(cat.items()) # returns a tuple