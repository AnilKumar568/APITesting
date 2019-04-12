import requests
# import json

BASE_URL = "https://reqres.in"
payload = {
    "name": "Anil",
    "job": "QA"
}

resp = requests.post(BASE_URL + "/api/users", data=payload)
print(resp.json())
