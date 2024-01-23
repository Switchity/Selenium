import requests
import pytest
from readData import read_test_data_from_csv


@pytest.mark.parametrize("country_code, zip_code, expected_place_name", read_test_data_from_csv())
def test_Chandan(country_code, zip_code, expected_place_name):

    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")

    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name

