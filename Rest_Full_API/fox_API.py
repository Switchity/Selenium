import json
import requests

response = requests.get("https://randomfox.ca/floof/")

print(response.json())
fox_img=response.json()

print(fox_img['link'])

