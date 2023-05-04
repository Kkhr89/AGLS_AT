""" API Test suite """

import pytest
import requests
from api.commands.commands import *


class TestAPI:

    def test_get_request(self):
        url = BaseMethods.parse_from_api_urls("url_post_token_request")
        request_body = BaseMethods.parse_from_api_jsons("post_body_token_request")
        response = BaseMethods.get_auth_token_request(url, request_body)
        response_json = response.json()
        access_token = response_json['accessToken']
        assert response.status_code == 200
        assert 'accessToken' in response_json


        
