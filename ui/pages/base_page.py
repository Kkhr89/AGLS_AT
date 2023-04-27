"""Base Class for all pages, contains all common methods"""

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ui.utilities.support import *


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

    @allure.step('Click outside of modal window')
    def do_click_outside_modal_wdw(self, locator: WebElement):
        modal_wdw = self.wait.until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.browser)
        actions.move_to_element_with_offset(modal_wdw, -100, -100).click().perform()

    @allure.step('Fill in text into input field by typing it from the keyboard')
    def do_input_keys_with_keyboard(self, locator: WebElement, text_data: str):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text_data)

    @allure.step('Copy text to clipboard and fill it into input field by pasting with CTRL+V from keyboard')
    def do_paste_keys_with_ctrl_v(self, locator: WebElement, text_data: str):
        pyperclip.copy(text_data)
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(Keys.CONTROL, 'v')

    @allure.step('Clear the input field with keyboard BACKSPACE key')
    def do_clear_input_with_backspace(self, locator: WebElement):
        input_field = self.wait.until(EC.visibility_of_element_located(locator))
        while input_field.get_attribute("value") != "":
            input_field.send_keys(Keys.BACKSPACE)

    @allure.step('Create, switch to new tab and open url')
    def do_create_new_tab(self, url: str):
        self.browser.switch_to.new_window('tab')
        self.browser.get(url)

    @allure.step('Switch to existing tab')
    def do_switch_to_existing_tab(self, window_id):
        self.browser.switch_to.window(window_id)

    @allure.step('Create dummy link to use on localhost')
    def do_create_new_link(self, locator: WebElement, new_text: str):
        initial_link = self.wait.until(EC.visibility_of_element_located(locator)).text
        modified_link = initial_link[:17] + new_text + initial_link[21:]
        return modified_link

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

    @allure.step('Assert text is changed after input(last symbols are removed)')
    def assert_input_text_was_changed(self, locator: WebElement, expected_text: str):
        actual_text = self.wait.until(EC.visibility_of_element_located(locator)).text
        assert actual_text != expected_text, \
            f'{locator} saved text is same as inputted: "{actual_text}" vs "{expected_text}"'

    @allure.step('Execute SQL query in database and receive response')
    def assert_db_received_data(self, host_link: str, query: str, sent_data: str):
        query_result = db_connect_execute_query_return_cell(host_link, query)
        assert query_result == sent_data, f'Database did not received data / data received is incorrect:\n' \
                                          f'Was sent: "{sent_data}"\n' \
                                          f'In database:"{query_result}"'

    @allure.step('Check cursor is changed arrow->hand when hover on element')
    def assert_cursor_changed_to_hand_on_hover(self, locator: WebElement):
        initial_style = "default"
        element = self.wait.until(EC.visibility_of_element_located(locator))
        webdriver.ActionChains(self.browser).move_to_element(element).perform()
        new_style = self.wait.until(EC.visibility_of_element_located(locator)).value_of_css_property("cursor")
        assert initial_style != new_style and new_style == "pointer", \
               f"Cursor did not change to hand on hover. Initial style: {initial_style}, new style: {new_style}"

    @allure.step('Check cursor is changed arrow->text when hover on element')
    def assert_cursor_changed_to_text_on_hover(self, locator: WebElement):
        initial_style = "default"
        element = self.wait.until(EC.visibility_of_element_located(locator))
        webdriver.ActionChains(self.browser).move_to_element(element).perform()
        new_style = self.wait.until(EC.visibility_of_element_located(locator)).value_of_css_property("cursor")
        assert initial_style != new_style and (new_style == "text" or new_style == "auto"), \
               f"Cursor did not change to text on hover. Initial style: {initial_style}, new style: {new_style}"

    @allure.step('Refresh the page')
    def do_refresh(self):
        self.browser.refresh()

    @allure.step('Return text string of the element')
    def get_text(self, locator: WebElement):
        return self.wait.until(EC.visibility_of_element_located(locator)).text


