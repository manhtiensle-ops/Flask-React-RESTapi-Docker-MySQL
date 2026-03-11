import requests

BASE = "http://127.0.0.1:5000"
payload = {
    "username": "admin",
    "password": 123
}
response = requests.post(BASE + "/AI", json=payload)


print(response.json())
        
