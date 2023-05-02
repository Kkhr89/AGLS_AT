"""LOGIN page class"""

from .base_page import BasePage
from ui.utilities.support import *
from ui.testdata.links import *
from ui.pages.locators import *


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    @staticmethod
    @allure.step('Take key-related text from testdata.yml file')
    def login_yaml_parser(key: str):
        return yaml_parser('ui/testdata/login_page.yaml', key)

    @allure.step('Open Quick Access page')
    def go_to_quick_access(self):
        page = LoginPage(self.browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)

    @allure.step('Open "Feedback Survey" modal window')
    def go_to_feedback_survey(self):
        page = LoginPage(self.browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_FEEDBACK_SURVEY)

    @allure.step('Open "Sign Up" page')
    def go_to_sign_up(self):
        page = LoginPage(self.browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.LINK_SIGN_UP)
