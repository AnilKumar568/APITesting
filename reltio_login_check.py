import requests

url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"

payload = {
    "txtUsername": "Admin",
    "txtPassword": "admin123"
}

resp = requests.get(url=url, data=payload)
print("OrangeHRM" in resp.text)
