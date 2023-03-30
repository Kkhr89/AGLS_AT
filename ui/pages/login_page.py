# from locators import LoginPageLocators
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def draft(self):
        pass
