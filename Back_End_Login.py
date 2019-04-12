import requests
from bs4 import BeautifulSoup
import re
session = requests.session()
resp = session.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')

# soup = BeautifulSoup(resp.text, 'lxml')
# token = soup.select("#csrf_token")[0].get("value")
# print(token)

pat = re.compile(r'<input type="hidden" name="_csrf_token" value="(.+)?" id="csrf_token"')
# You need to remove an angular bracket '>'
res = re.search(pat, resp.text)
print(res.group(1))
# If you wont pass 1 it'llprint as <input type="hidden" name="_csrf_token" value="(.+)?" id="csrf_token" so use 1

