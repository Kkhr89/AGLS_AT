""" Login page Test suite """

import pytest
from ui.pages.login_page import LoginPage
from ui.testdata.links import link_app
from ui.pages.locators import LoginPageLocators


@pytest.mark.login_page_testsuite
class TestLoginPageMain:

    # Open Login page and assert all elements are present:
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_assert_all_elements(self, browser):
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
        page.assert_page_title(LoginPage.login_yaml_parser('exp_page_title'))
        page.assert_element_text_is_correct(LoginPageLocators.TEXT_SIGN_IN,
                                            LoginPage.login_yaml_parser('exp_sign_in_text'))
        page.assert_element_text_is_correct(LoginPageLocators.TEXT_DONT_HAVE_ACCOUNT,
                                            LoginPage.login_yaml_parser('exp_dont_have_account_text'))
        page.assert_element_text_is_correct(LoginPageLocators.TEXT_MAIN_TITLE,
                                            LoginPage.login_yaml_parser('exp_main_title_text'))
        page.assert_input_is_present_with_placeholder(LoginPageLocators.INPUT_EMAIL,
                                                      LoginPage.login_yaml_parser('exp_email_placeholder'))
        page.assert_input_is_present_with_placeholder(LoginPageLocators.INPUT_PASSWORD,
                                                      LoginPage.login_yaml_parser('exp_password_placeholder'))
        page.assert_any_element_is_present(LoginPageLocators.PIC_EPAM_LOGO)

    # Standard login scenario with correct credentials, input from keyboard:
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_standard_login_keyboard(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL,
                                         LoginPage.login_yaml_parser('user_1_email_cred'))
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_PASSWORD,
                                         LoginPage.login_yaml_parser('user_pass_cred'))
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_SIGN_IN)
        page.do_click(LoginPageLocators.BTN_SIGN_IN)
        page.assert_any_element_is_present(LoginPageLocators.MODAL_WHATS_NEW)

    # Not registered Email input shows Error pop-up:
    @pytest.mark.critical_path
    @pytest.mark.negative
    def test_wrong_email_input(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL,
                                         LoginPage.login_yaml_parser('neg_user_email_cred'))
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_PASSWORD,
                                         LoginPage.login_yaml_parser('user_pass_cred'))
        page.do_click(LoginPageLocators.BTN_SIGN_IN)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_POP_UP,
                                            LoginPage.login_yaml_parser('exp_pop_up_text'))

    # Wrong password input shows Error pop-up:
    @pytest.mark.critical_path
    @pytest.mark.negative
    def test_wrong_password_input(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL,
                                         LoginPage.login_yaml_parser('user_1_email_cred'))
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_PASSWORD,
                                         LoginPage.login_yaml_parser('neg_user_pass_cred'))
        page.do_click(LoginPageLocators.BTN_SIGN_IN)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_POP_UP,
                                            LoginPage.login_yaml_parser('exp_pop_up_text'))

    # Login with empty Email field
    @pytest.mark.critical_path
    @pytest.mark.negative
    def test_email_input_empty(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_PASSWORD,
                                         LoginPage.login_yaml_parser('user_pass_cred'))
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)

    # Login with empty Password field
    @pytest.mark.critical_path
    @pytest.mark.negative
    def test_password_input_empty(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL,
                                         LoginPage.login_yaml_parser('user_1_email_cred'))
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)

    # Standard login scenario with correct credentials, paste with ctr+v from clipboard:
    @pytest.mark.extended
    @pytest.mark.positive
    def test_standard_login_ctrl_v_paste(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_paste_keys_with_ctrl_v(LoginPageLocators.INPUT_EMAIL, LoginPage.login_yaml_parser('user_1_email_cred'))
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)
        page.do_paste_keys_with_ctrl_v(LoginPageLocators.INPUT_PASSWORD, LoginPage.login_yaml_parser('user_pass_cred'))
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_SIGN_IN)
        page.do_click(LoginPageLocators.BTN_SIGN_IN)
        page.assert_any_element_is_present(LoginPageLocators.MODAL_WHATS_NEW)

    # "This field is required" message check for Email
    @pytest.mark.extended
    @pytest.mark.negative
    def test_email_input_clear_message_check(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL,
                                         LoginPage.login_yaml_parser('user_1_email_cred'))
        page.do_clear_input_with_backspace(LoginPageLocators.INPUT_EMAIL)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_MESSAGE_EMAIL,
                                            LoginPage.login_yaml_parser('exp_err_email_required_text'))

    # "This field is required" message check for Name
    @pytest.mark.extended
    @pytest.mark.negative
    def test_name_input_clear_message_check(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_QA_NAME,
                                         LoginPage.login_yaml_parser('user_1_name_cred'))
        page.do_clear_input_with_backspace(LoginPageLocators.INPUT_QA_NAME)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_MESSAGE_EMAIL,
                                            LoginPage.login_yaml_parser('exp_err_email_required_text'))

    # Wrong input to Email field to check error message and "Send" button keeps disabled:
    @pytest.mark.extended
    @pytest.mark.negative
    @pytest.mark.parametrize('input_param', LoginPage.login_yaml_parser('email_input_neg_data'))
    def test_email_input_error_message_check(self, browser, input_param):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL, input_param)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_MESSAGE_EMAIL,
                                            LoginPage.login_yaml_parser('exp_err_email_text'))
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)


@pytest.mark.quick_access_suite
class TestLoginPageQuickAccess:

    # "Quick Access" sub-page open and assert all elements
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_quick_access_open_assert_all_elements(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_FEEDBACK_SURVEY)
        page.assert_link_is_present_and_enabled(LoginPageLocators.LINK_HEADER_LOGO)
        page.assert_element_text_is_correct(LoginPageLocators.TEXT_MAIN_TITLE,
                                            LoginPage.login_yaml_parser('exp_main_title_text'))
        page.assert_element_text_is_correct(LoginPageLocators.TEXT_QA_QUICK_ACCESS,
                                            LoginPage.login_yaml_parser('exp_qa_quick_access_text'))
        page.assert_input_is_present_with_placeholder(LoginPageLocators.INPUT_QA_NAME,
                                                      LoginPage.login_yaml_parser('exp_qa_name_placeholder'))
        page.assert_element_text_is_correct(LoginPageLocators.TEXT_QA_NOTICE,
                                            LoginPage.login_yaml_parser('exp_qa_notice_text'))
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_QA_CANCEL)
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_QA_ENTER)
        page.assert_any_element_is_present(LoginPageLocators.PIC_EPAM_LOGO)

    # Login through "Quick Access", standard scenario:
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_quick_access_standard_login(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_QA_NAME,
                                         LoginPage.login_yaml_parser('user_1_name_cred'))
        page.do_click(LoginPageLocators.BTN_QA_ENTER)
        page.assert_any_element_is_present(LoginPageLocators.MODAL_WHATS_NEW)

    # Go Back from "Quick Access" page with "Cancel" button:
    @pytest.mark.critical_path
    @pytest.mark.positive
    def test_quick_access_go_back_with_cancel(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_click(LoginPageLocators.BTN_QA_CANCEL)
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)

    # "Quick Access" standard login scenario with correct credentials, paste with ctrl+v from clipboard:
    @pytest.mark.extended
    @pytest.mark.positive
    def test_quick_access_standard_login_ctrl_v_paste(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_paste_keys_with_ctrl_v(LoginPageLocators.INPUT_QA_NAME, LoginPage.login_yaml_parser('user_1_name_cred'))
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_QA_ENTER)
        page.do_click(LoginPageLocators.BTN_QA_ENTER)
        page.assert_any_element_is_present(LoginPageLocators.MODAL_WHATS_NEW)

    # "Quick Access" input allowed different symbols length:
    @pytest.mark.extended
    @pytest.mark.postitive
    @pytest.mark.parametrize('input_text', [
        LoginPage.login_yaml_parser("text_254"),
        LoginPage.login_yaml_parser("text_255")
    ])
    def test_quick_access_input_allowed_length(self, browser, input_text):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_QA_NAME, input_text)
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_QA_ENTER)
        page.do_click(LoginPageLocators.BTN_QA_ENTER)
        page.assert_any_element_is_present(LoginPageLocators.MODAL_WHATS_NEW)

    # "Quick Access" input not allowed symbols length (>255) and assert error message:
    @pytest.mark.draft
    @pytest.mark.extended
    @pytest.mark.negative
    def test_quick_access_input_not_allowed_length(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_QA_NAME, LoginPage.login_yaml_parser('text_256_neg'))
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_QA_ENTER)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_MESSAGE_EMAIL,
                                            LoginPage.login_yaml_parser('exp_qa_err_255_symbols'))
