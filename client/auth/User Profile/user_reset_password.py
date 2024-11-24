import requests
import json

url = "http://127.0.0.1:8000/api/auth/users/reset_password/"

payload = json.dumps({
  "email": "admin@gmail.com"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
