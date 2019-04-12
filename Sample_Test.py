import requests
import json

BASE_URL = "https://reqres.in"
params = {'page': 2}
response = requests.get(BASE_URL + "/api/users", params=params)
print(response) # Response value will be displayed 200 for OK or anything else

resp = response.json()
print(resp)
print(json.dumps(response.json(), indent=4))

# Getting Specific values. In the response we've list of info in data and fetching first name details

names = [d["first_name"] for d in resp["data"]]  # fetching specific data
print(names)


