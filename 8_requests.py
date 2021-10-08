# simple fetch request module
# return data in json format

import requests

res = requests.get("https://jsonplaceholder.typicode.com/todos");
data = res.json()
print(data)
for item in data:
   print(item['title'])
