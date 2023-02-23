#API
import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

r = requests.get(url)

json_response = json.loads(r.text)

page = jsonpath.jsonpath(json_response,'total_pages')

print(page[0])

