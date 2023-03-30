import pytest
from ui.pages.login_page import LoginPage
from ui.utilities.links import link_home
from ui.pages.locators import LoginPageLocators


class TestLoginPage:
    @pytest.mark.smoke
    def test_1_open_assert_close_page(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_home)
        page.check_btn_is_present_and_enabled(LoginPageLocators.BTN_FEEDBACK_SURVEY)
        page.check_btn_is_present_and_enabled(LoginPageLocators.BTN_EPAM_LOGIN)
        page.check_btn_is_present_and_enabled(LoginPageLocators.BTN_GITHUB_LOGIN)
        page.check_btn_is_present_and_enabled(LoginPageLocators.BTN_QUICK_ACCESS)
        page.check_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)
        page.check_link_is_present_and_enabled(LoginPageLocators.LINK_HEADER_LOGO)
        page.check_link_is_present_and_enabled(LoginPageLocators.LINK_SIGN_UP)
        page.check_link_is_present_and_enabled(LoginPageLocators.LINK_RECOVER_MY_PASSWORD)
        print(page.get_text(LoginPageLocators.TEXT_DONT_HAVE_ACCOUNT))
        print(page.get_text(LoginPageLocators.TEXT_SIGN_IN))
        print(page.get_text(LoginPageLocators.TEXT_MAIN_TITLE))


