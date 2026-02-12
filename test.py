import requests

BASE = "http://127.0.0.1:5000"
Reponse = requests.get(BASE + "/hello")
print(Reponse.json())
        
