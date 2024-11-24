import requests
import json

url = "http://127.0.0.1:8000/api/auth/jwt/create"

payload = json.dumps({
  "email": "bao@gmail.com",
  "password": "123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
