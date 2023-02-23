import requests


# get_locations_for_us_90210_check_status_code_equals_200

def TestMethod():
    url = "http://api.zippopotam.us/us/90210"
    response = requests.get(url)
    print(response.content)
    assert response.status_code == 200


TestMethod()



