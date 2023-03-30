""" Login page Test suite """

import pytest
from ui.pages.login_page import LoginPage
from ui.testdata.links import link_app
from ui.pages.locators import LoginPageLocators


class TestLoginPage:
    @pytest.mark.smoke
    def test_1_open_assert_close_page(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_FEEDBACK_SURVEY)
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_EPAM_LOGIN)
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_GITHUB_LOGIN)
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_QUICK_ACCESS)
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)
        page.assert_link_is_present_and_enabled(LoginPageLocators.LINK_HEADER_LOGO)
        page.assert_link_is_present_and_enabled(LoginPageLocators.LINK_SIGN_UP)
        page.assert_link_is_present_and_enabled(LoginPageLocators.LINK_RECOVER_MY_PASSWORD)
        page.assert_page_title(LoginPage.exp_login_page_title)
        page.assert_element_text_is_correct(LoginPageLocators.TEXT_SIGN_IN, LoginPage.exp_sign_in_text)
        page.assert_element_text_is_correct(LoginPageLocators.TEXT_DONT_HAVE_ACCOUNT, LoginPage.exp_no_account_text)
        page.assert_element_text_is_correct(LoginPageLocators.TEXT_MAIN_TITLE, LoginPage.exp_main_text)
