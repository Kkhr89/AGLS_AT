"""Base Class for all API calls, contains all common methods"""


import requests
import allure
from api.utilities.service import *


class BaseMethods:

    @staticmethod
    @allure.step('Parse url for API request')
    def parse_from_api_urls(key: str):
        return parse_json_file('testdata/api_urls.json')[key]

    @staticmethod
    @allure.step('Parse data for API request')
    def parse_from_api_jsons(key: str):
        return parse_json_file('testdata/api_jsons.json')[key]

    @staticmethod
    @allure.step('Get authorization token request')
    def get_auth_token_request(url, json_body):
        url = BaseMethods.parse_from_api_urls("url_post_token_request")
        return requests.post(url, json=json_body, headers={"Content-Type": "application/json"})

    @staticmethod
    @allure.step('GET request')
    def get_request(url):
        return requests.get(url)

    @staticmethod
    @allure.step('POST request')
    def post_request(url, headers, body):
        return requests.post(url, headers, body)
