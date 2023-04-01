"""Base class for all pages"""

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ui.utilities.support import *

"""Base Class for all pages, contains all common methods"""


class BasePage:
    def __init__(self, browser: webdriver):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    @allure.step('Open url')
    def go_to_url(self, url: str):
        """
        Open specified url
        """
        self.browser.get(url)

    @allure.step('Click web-element')
    def do_click(self, locator: WebElement):
        """
        Click on web-element
        """
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    @allure.step('Fill in text into input field by typing it from the keyboard')
    def do_input_keys_with_keyboard(self, locator: WebElement, text: str):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.step('Copy text to clipboard and fill it into input field by pasting with CTRL+V from keyboard')
    def do_paste_keys_with_ctrl_v(self, locator: WebElement, text: str):
        pyperclip.copy(text)
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(Keys.CONTROL, 'v')

    @allure.step('Clear the input field with keyboard BACKSPACE key')
    def do_clear_input_with_backspace(self, locator: WebElement):
        input_field = self.wait.until(EC.visibility_of_element_located(locator))
        while input_field.get_attribute("value") != "":
            input_field.send_keys(Keys.BACKSPACE)

    @allure.step('Assert the element presence')
    def assert_any_element_is_present(self, locator: WebElement):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    @allure.step('Assert button is present and clickable')
    def assert_btn_is_present_and_enabled(self, locator: WebElement):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        assert self.wait.until(EC.element_to_be_clickable(locator)).is_enabled()

    @allure.step('Assert button is present and not clickable')
    def assert_btn_is_present_and_disabled(self, locator: WebElement):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        assert not self.wait.until(EC.visibility_of_element_located(locator)).is_enabled()

    @allure.step('Assert link is present and clickable')
    def assert_link_is_present_and_enabled(self, locator: WebElement):
        assert self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        assert self.wait.until(EC.element_to_be_clickable(locator)).is_enabled()

    @allure.step('Assert input field is present, can receive text and the placeholder is correct')
    def assert_input_is_present_receive_text_with_placeholder(self, locator: WebElement, exp_placeholder: str):
        input_field = self.wait.until(EC.visibility_of_element_located(locator))
        assert input_field.is_displayed()
        input_field.send_keys('test')
        assert input_field.get_attribute('value') == 'test', 'Input field cannot receive text'
        input_field.clear()
        act_placeholder = input_field.get_attribute('placeholder')
        assert act_placeholder == exp_placeholder, f'Placeholder is "{act_placeholder}" instead of "{exp_placeholder}"'

    @allure.step('Assert page title correctness')
    def assert_page_title(self, expected_title: str):
        actual_title = self.browser.title
        assert actual_title == expected_title, f'Page title is "{actual_title}" instead of "{expected_title}"'

    @allure.step('Assert the text correctness')
    def assert_element_text_is_correct(self, locator: WebElement, expected_text: str):
        actual_text = self.wait.until(EC.visibility_of_element_located(locator)).text
        assert actual_text == expected_text, f'{locator} text is "{actual_text}" instead of "{expected_text}"'

    @allure.step('Refresh the page')
    def do_refresh(self):
        self.browser.refresh()

    @allure.step('Return text string of the element')
    def get_text(self, locator: WebElement):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step('Execute SQL query in database and receive response')
    def assert_db_received_data(self, host_link: str, query: str, sent_data: str):
        query_result = db_connect_execute_query_return_cell(host_link, query)
        assert query_result == sent_data, 'Database did not received data / data received is incorrect'
