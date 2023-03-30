"""LOGIN page class"""

from .base_page import BasePage
from ui.utilities.support import yaml_parser


class LoginPage(BasePage):

    exp_login_page_title = yaml_parser('testdata/login_page.yaml', 'exp_page_title')
    exp_main_text = yaml_parser('testdata/login_page.yaml', 'exp_main_title')
    exp_no_account_text = yaml_parser('testdata/login_page.yaml', 'exp_dont_have_account')
    exp_sign_in_text = yaml_parser('testdata/login_page.yaml', 'exp_sign_in')


    def __init__(self, browser):
        super().__init__(browser)

    def draft(self):
        pass
