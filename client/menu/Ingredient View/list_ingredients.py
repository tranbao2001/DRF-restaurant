import requests

url = "http://127.0.0.1:8000/api/menu/ingredients/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
