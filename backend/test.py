import requests

BASE = "http://localhost:8000"
payload = {
    "username": "manhtien",
    "password": "manhtien"
}
# File test.py
response = requests.post(BASE + "/login", json=payload)

# In toàn bộ JSON trả về từ Server
print(response.json()) 
