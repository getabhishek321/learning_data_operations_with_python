import requests

BASE_URL = "https://jsonmock.hackerrank.com/api/food_outlets"

response = requests.get(BASE_URL)
response.raise_for_status()  # this will throw an error if request failed

data = response.json()  # JSON -> Python (dict)

print(type(data))
print("Top-level keys:", data.keys())
# keeping it till here to understand the high level format of data
