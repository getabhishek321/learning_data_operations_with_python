import requests

BASE_URL = "https://jsonmock.hackerrank.com/api/food_outlets"

response = requests.get(BASE_URL)  # send GET request to the URL

print("Status code:", response.status_code)
print("Raw text:")
print(response.text[:500])  # show first 500 characters
