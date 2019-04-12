import requests


url = "https://reqres.in"

data = {
    "name": "Anil",
    "job": "QA-Lead"
}

resp = requests.put(url + "/api/users", params=data)
print(resp.json())