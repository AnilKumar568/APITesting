import requests


url = "https://reqres.in"

resp = requests.delete(url + "/api/users/2")
print(resp.status_code)
