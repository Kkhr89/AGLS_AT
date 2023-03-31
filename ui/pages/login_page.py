"""LOGIN page class"""

from .base_page import BasePage
from ui.utilities.support import yaml_parser


class LoginPage(BasePage):


    def __init__(self, browser):
        super().__init__(browser)

    @staticmethod
    def login_yaml_parser(key: str):
        return yaml_parser('testdata/login_page.yaml', key)
