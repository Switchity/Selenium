import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"


def test_creat():
    file = open("C:\\Users\\Switchity Networks\\Desktop\\REST_API\creat_user.json", 'r')
    # the content will be in string
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    # make post request
    post_response = requests.post(url, request_json)
    print(post_response)
    assert post_response.status_code == 202
    response_json = json.loads(post_response.text)
    updated = jsonpath.jsonpath(response_json, 'job')
    print(updated)


def test_creat1():
    file = open("C:\\Users\\Switchity Networks\\Desktop\\REST_API\creat_user.json", 'r')
    # the content will be in string
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    # make post request
    post_response = requests.post(url, request_json)
    print(post_response)
    assert post_response.status_code == 202
    response_json = json.loads(post_response.text)
    updated = jsonpath.jsonpath(response_json, 'job')
    print(updated)
