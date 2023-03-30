from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Base Class for all pages, contains all common methods"""


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    # Method to open url:
    def go_to_url(self, url):
        self.browser.get(url)

    # Method to click web element:
    def do_click(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    # Method to fill in text into input field:
    def do_input_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    # Method to assert element presence:
    def check__any_element_is_present(self, locator):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    # Method to assert button is present and clickable
    def check_btn_is_present_and_enabled(self, locator):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        assert self.wait.until(EC.element_to_be_clickable(locator)).is_enabled()

    # Method to assert button is present and not clickable
    def check_btn_is_present_and_disabled(self, locator):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        assert not self.wait.until(EC.visibility_of_element_located(locator)).is_enabled()

    # Method to assert link is present and clickable
    def check_link_is_present_and_enabled(self, locator):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        assert self.wait.until(EC.element_to_be_clickable(locator)).is_enabled()

    # Method to refresh the page:
    def do_refresh(self):
        self.browser.refresh()

    # Method to return current page title:
    def get_page_title(self):
        return self.browser.title.text

    def get_text(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.browser.find_element(locator).text
