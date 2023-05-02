""" API Test suite """

import requests
from api.utilities.service import parse_json_file


class TestAPI:
    def test_get_request(self):
        response = requests.post(url, json)
        assert response.status_code == 200
        assert response.json() == {'message': 'Hello, World!'}