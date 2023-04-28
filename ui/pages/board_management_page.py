"""BOARD MANAGEMENT page class"""

from .base_page import BasePage
from ui.utilities.support import *
from ui.testdata.links import *
from ui.pages.locators import *
from ui.pages.login_page import LoginPage


class BoardManagementPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    @staticmethod
    @allure.step('Take key-related text from testdata.yaml file')
    def board_management_yaml_parser(key: str):
        return yaml_parser('testdata/board_management_page.yaml', key)

    @allure.step('Open Board Management page')
    def go_to_board_management(self):
        page = BoardManagementPage(self.browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL,
                                         LoginPage.login_yaml_parser('user_1_email_cred'))
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_PASSWORD, "Godfather1989!")
        page.do_click(LoginPageLocators.BTN_SIGN_IN)
