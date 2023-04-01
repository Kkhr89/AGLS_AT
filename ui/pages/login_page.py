"""LOGIN page class"""

from .base_page import BasePage
from ui.utilities.support import *


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @staticmethod
    @allure.step('Take key-related text from testdata.yml file')
    def login_yaml_parser(key: str):
        return yaml_parser('testdata/login_page.yaml', key)
