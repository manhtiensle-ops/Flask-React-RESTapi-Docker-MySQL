import requests

BASE = "http://localhost:8000"
payload = {
    "username": "manhtien",
    "password": "manhtien"
}
response = requests.post(BASE + "/login", json=payload)


print(response.json())
        
