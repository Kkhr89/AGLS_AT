"""Base class for all pages"""

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Base Class for all pages, contains all common methods"""


class BasePage:
    def __init__(self, browser: webdriver):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    # Method to open url:
    def go_to_url(self, url: str):
        self.browser.get(url)

    # Method to click web element:
    def do_click(self, locator: WebElement):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    # Method to fill in text into input field:
    def do_input_keys(self, locator: WebElement, text: str):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    # Method to assert element presence:
    def assert_any_element_is_present(self, locator: WebElement):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    # Method to assert button is present and clickable
    def assert_btn_is_present_and_enabled(self, locator: WebElement):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        assert self.wait.until(EC.element_to_be_clickable(locator)).is_enabled()

    # Method to assert button is present and not clickable
    def assert_btn_is_present_and_disabled(self, locator: WebElement):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        assert not self.wait.until(EC.visibility_of_element_located(locator)).is_enabled()

    # Method to assert link is present and clickable
    def assert_link_is_present_and_enabled(self, locator: WebElement):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        assert self.wait.until(EC.element_to_be_clickable(locator)).is_enabled()

    # Method to refresh the page:
    def do_refresh(self):
        self.browser.refresh()

    # Method to assert current page title:
    def assert_page_title(self, expected_title: str):
        actual_title = self.browser.title
        assert actual_title == expected_title, f'Page title is "{actual_title}" instead of "{expected_title}"'

    # Method to assert text:
    def assert_element_text_is_correct(self, locator: WebElement, expected_text: str):
        actual_text = self.wait.until(EC.visibility_of_element_located(locator)).text
        assert actual_text == expected_text, f'{locator} text is "{actual_text}" instead of "{expected_text}"'

    # Method to return element text string:
    def get_text(self, locator: WebElement):
        return self.wait.until(EC.visibility_of_element_located(locator)).text



