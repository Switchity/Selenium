import requests
import json

url = "https://reqres.in/api/users"
# read inpput file

file = open("C:\\Users\\Switchity Networks\\Desktop\\REST_API\creat_user.json", 'r')

# the content will be in string
json_input = file.read()

request_json = json.loads(json_input)
print(request_json)
# make post request into json file
post_response = requests.post(url, request_json)
print(post_response.content)
# validating response code
assert post_response.status_code == 201
