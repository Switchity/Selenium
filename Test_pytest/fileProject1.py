import pytest
import requests
d = [
    ("us", "90210", "Beverly Hills"),
    ("ca", "B2A", "North Sydney South Central"),
    ("it", "50123", "Firenze")]
@pytest.mark.parametrize(c,z,l,d)
def test_chandan(c,z,l):

    url = f'https://api.zippopotam.us/us/90210/{c}\{z}'

    response = requests.get(url)
    respjsonBody = response.json()
    assert respjsonBody[placess][0]['places Name']===l




