"""Base Class for all API calls, contains all common methods"""


import requests
import allure
from api.utilities.service import *


class BaseMethods:

    @staticmethod
    @allure.step('Parse url for API request')
    def parse_from_api_urls():
        urls = parse_json_file('api/testdata/api_urls.json')
        return urls

    @staticmethod
    @allure.step('Parse data for API request')
    def parse_from_api_jsons():
        content = parse_json_file('api/testdata/api_urls.json')
        return content

