import requests
import json


with open('token.txt') as soubor:
    token = soubor.read().strip()

headers = {'Authorization': 'token ' + token}

"""
stranka = requests.get('https://api.github.com/user', headers=headers)
stranka.raise_for_status()
print(stranka.text)

data = json.loads(stranka.text)
print(json.dumps(data, ensure_ascii=True, indent=2))
print(data["avatar_url"])
"""

stranka = requests.put('https://api.github.com/user/starred/pyvec/naucse.python.cz', headers=headers)
stranka.raise_for_status()
