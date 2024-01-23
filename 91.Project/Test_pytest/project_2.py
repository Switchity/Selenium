import pytest
import requests

d = [
    ("us", "90210", "Beverly Hills"),
    ("ca", "B2A", "North Sydney South Central"),
    ("it", "50123", "chandan")]

@pytest.mark.parametrize("country, zip, expected_place_name",d)
def test_chandan(country, zip, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country}/{zip}")
    response_body = response.json()

    assert response_body["places"][0]["place name"] == expected_place_name,'pass'





