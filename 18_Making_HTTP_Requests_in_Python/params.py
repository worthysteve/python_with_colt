# Requesting JSON with python and params

import requests

url = "https://icanhazdadjoke.com/search"
# response = requests.get(url, headers = {"Accept": "text/plain"})
response = requests.get(
    url, 
    headers = {"Accept": "application/json"},
    params={"term": "cat", "limits": 1})

# print(response.text)
data = response.json()
# print(type(data))
print(data)
print(data["results"])
# print(data["joke"])
# print(f"status: {data['status']}")

