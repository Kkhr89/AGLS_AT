"""LOGIN page class"""

from .base_page import BasePage
from ui.utilities.support import *
from ui.testdata.links import *


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @staticmethod
    @allure.step('Take key-related text from testdata.yml file')
    def login_yaml_parser(key: str):
        return yaml_parser('testdata/login_page.yaml', key)

    @staticmethod
    @allure.step('Execute SQL query in "User" database and receive response')
    def db_user_query(query: str):
        return db_connect_execute_query_return_cell(link_agl_db_user, query)

    @staticmethod
    @allure.step('Execute SQL query in "Feedback Survey" database and receive response')
    def db_feedback_query(query: str):
        return db_connect_execute_query_return_cell(link_agl_db_feedback, query)

    def assert_database_received_data(self):
        pass
