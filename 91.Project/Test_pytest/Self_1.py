

import requests
import json

def chandan():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    print(response_body)

chandan()