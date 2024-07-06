# Requesting JSON with python

import requests

url = "https://icanhazdadjoke.com/"
# response = requests.get(url, headers = {"Accept": "text/plain"})
response = requests.get(url, headers = {"Accept": "application/json"})

# print(response.text)
data = response.json()
print(type(data))
print(data)
print(data["joke"])
print(f"status: {data['status']}")