"""Base Class for all API calls, contains all common methods"""

import requests
from api.utilities.service import *


class BaseMethods:

    @staticmethod
    @allure.step('Create url')
    def parse_from_api_urls(key: str):
        return parse_json_file('testdata/api_urls.json')[key]

    @staticmethod
    @allure.step('Create JSON body')
    def parse_from_api_jsons(key: str):
        return parse_json_file('testdata/api_jsons.json')[key]

    @staticmethod
    @allure.step('Create header')
    def parse_from_api_headers(key: str):
        return parse_json_file('testdata/api_headers.json')[key]

    @staticmethod
    @allure.step('Get authorization token')
    def return_auth_token():
        url = BaseMethods.parse_from_api_urls("url_post_token_request")
        json_body = BaseMethods.parse_from_api_jsons("json_body_post_token_request")
        header = BaseMethods.parse_from_api_headers("header_content_type_json")
        response = requests.post(url=url, json=json_body, headers=header)
        return {'Authorization': f"Bearer {response.json()['accessToken']}"}

    @staticmethod
    @allure.step('Send POST request to upload file')
    def post_request_to_upload_file(file_path: str, file_key: str, url: str, access_token):
        with open(file_path, 'rb') as file:
            file_to_upload = {file_key: file}
            response_upload = requests.post(url=url, files=file_to_upload, headers=access_token)
        return response_upload

    @staticmethod
    @allure.step('Assert status code')
    def assert_status_code(response, code: int):
        assert response.status_code == code, f'Status code is {response.status_code} instead of {code}'

    @staticmethod
    @allure.step('Assert string existence in json')
    def assert_str_in_json(response, key: str):
        assert key in response.json(), f'No "{key}" in JSON response..'

    @staticmethod
    @allure.step('Assert string existence in json 2nd level')
    def assert_str_in_json_2nd_lvl(response, upper_key: str, lwr_key: str):
        assert lwr_key in response.json()[upper_key], f'No "{lwr_key}" in JSON response..'