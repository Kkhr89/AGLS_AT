""" Login page Test suite """


import pytest
import allure
from ui.pages.login_page import LoginPage
from ui.testdata.links import *
from ui.pages.locators import *


@allure.suite('Logging')
@allure.sub_suite('"Login" page test suite')
@pytest.mark.login_page_testsuite
class TestLoginPageMain:

    @allure.title('[Smoke]Page elements check')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_open_assert_all_elements(self, browser):
        """
        This is a smoke test to assert Login page.
        It opens the page and checks each element is present and enabled/disabled
        """
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
        page.assert_input_is_present_receive_text_with_placeholder(LoginPageLocators.INPUT_EMAIL,
                                                                   LoginPage
                                                                   .login_yaml_parser('exp_email_placeholder'))
        page.assert_input_is_present_receive_text_with_placeholder(LoginPageLocators.INPUT_PASSWORD,
                                                                   LoginPage
                                                                   .login_yaml_parser('exp_password_placeholder'))
        page.assert_any_element_is_present(LoginPageLocators.PIC_EPAM_LOGO)

    @allure.title('[Smoke]Successful logging')
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_standard_login_keyboard(self, browser):
        """
        This is a smoke test to assert logging scenario on Login page.
        It opens the page, inputs correct credentials into "Email" and "Password" fields,
        and clicks "Sign in" button
        """
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


    @allure.title('[Critical Path]Wrong email error pop-up check')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.critical_path
    @pytest.mark.negative
    def test_wrong_email_input(self, browser):
        """
        This is a critical path test to assert error pop-up is displayed when
        input wrong email on Login page.
        It opens the page, inputs incorrect email into "Email" field, correct password
        into "Password" field and clicks "Sign in" button
        """
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL,
                                         LoginPage.login_yaml_parser('neg_user_email_cred'))
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_PASSWORD,
                                         LoginPage.login_yaml_parser('user_pass_cred'))
        page.do_click(LoginPageLocators.BTN_SIGN_IN)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_POP_UP,
                                            LoginPage.login_yaml_parser('exp_pop_up_text'))

    @allure.title('[Critical Path]Wrong password error pop-up check')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.critical_path
    @pytest.mark.negative
    def test_wrong_password_input(self, browser):
        """
        This is a critical path test to assert error pop-up is displayed when
        input wrong password on Login page.
        It opens the page, inputs correct email into "Email" field, incorrect password
        into "Password" field and clicks "Sign in" button
        """
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL,
                                         LoginPage.login_yaml_parser('user_1_email_cred'))
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_PASSWORD,
                                         LoginPage.login_yaml_parser('neg_user_pass_cred'))
        page.do_click(LoginPageLocators.BTN_SIGN_IN)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_POP_UP,
                                            LoginPage.login_yaml_parser('exp_pop_up_text'))

    @allure.title('[Critical Path]Logging with empty "Email" field')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.critical_path
    @pytest.mark.negative
    def test_email_input_empty(self, browser):
        """
        This is a critical path test to assert "Sign in" button does not
        enable when keep "Email" field empty.
        It opens the page, inputs correct password into "Password" field and
        asserts "Sign in" button is disabled
        """
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_PASSWORD,
                                         LoginPage.login_yaml_parser('user_pass_cred'))
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)

    @allure.title('[Critical Path]Logging with empty "Password" field')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.critical_path
    @pytest.mark.negative
    def test_password_input_empty(self, browser):
        """
        This is a critical path test to assert "Sign in" button does not
        enable when keep "Password" field empty.
        It opens the page, inputs correct email into "Email" field and
        asserts "Sign in" button is disabled
        """
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL,
                                         LoginPage.login_yaml_parser('user_1_email_cred'))
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)

    @allure.title('[Extended]Logging with credentials pasting with CTRL+V')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.extended
    @pytest.mark.positive
    def test_standard_login_ctrl_v_paste(self, browser):
        """
        This is an extended test to assert possibility to paste credentials
        into input fields using keyboard.
        It opens the page, inputs correct email into "Email" field and
        correct password into "Password" field using CTRL + V command and
        asserts successful logging.
        """
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_paste_keys_with_ctrl_v(LoginPageLocators.INPUT_EMAIL, LoginPage.login_yaml_parser('user_1_email_cred'))
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)
        page.do_paste_keys_with_ctrl_v(LoginPageLocators.INPUT_PASSWORD, LoginPage.login_yaml_parser('user_pass_cred'))
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_SIGN_IN)
        page.do_click(LoginPageLocators.BTN_SIGN_IN)
        page.assert_any_element_is_present(LoginPageLocators.MODAL_WHATS_NEW)

    @allure.title('[Extended]Error message check when input->clear Email field')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.extended
    @pytest.mark.negative
    def test_email_input_clear_message_check(self, browser):
        """
        This is an extended test to assert an error text message appearing
        when input some text into "Email" field and then clear it.
        It opens the page, inputs correct email into "Email" field,
        clears it then and asserts an error message is appeared.
        """
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL,
                                         LoginPage.login_yaml_parser('user_1_email_cred'))
        page.do_clear_input_with_backspace(LoginPageLocators.INPUT_EMAIL)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_MESSAGE_EMAIL,
                                            LoginPage.login_yaml_parser('exp_err_email_required_text'))

    @allure.title('[Extended]Error message check wrong Email input')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.extended
    @pytest.mark.negative
    @pytest.mark.parametrize('input_param', LoginPage.login_yaml_parser('email_input_neg_data'))
    def test_email_input_error_message_check(self, browser, input_param):
        """
        This is an extended test to assert an error text message appearing
        when input incorrect/disabled email into "Email" field and "Sign in" button
        keeps disabled.
        It opens the page, inputs incorrect/disabled email into "Email" field,
        asserts an error message is appeared and "Sign in" button is disabled.
        """
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_input_keys_with_keyboard(LoginPageLocators.INPUT_EMAIL, input_param)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_MESSAGE_EMAIL,
                                            LoginPage.login_yaml_parser('exp_err_email_text'))
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)


@allure.suite('Logging')
@allure.sub_suite('"Quick Access" page test suite')
@pytest.mark.quick_access_suite
class TestQuickAccessPage:

    @allure.title('[Smoke]Page elements check')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_quick_access_open_assert_all_elements(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.assert_btn_is_present_and_enabled(LoginPageLocators.BTN_FEEDBACK_SURVEY)
        page.assert_btn_is_present_and_enabled(QuickAccessPageLocators.BTN_QA_CANCEL)
        page.assert_btn_is_present_and_disabled(QuickAccessPageLocators.BTN_QA_ENTER)
        page.assert_link_is_present_and_enabled(LoginPageLocators.LINK_HEADER_LOGO)
        page.assert_element_text_is_correct(LoginPageLocators.TEXT_MAIN_TITLE,
                                            LoginPage.login_yaml_parser('exp_main_title_text'))
        page.assert_element_text_is_correct(QuickAccessPageLocators.TEXT_QA_QUICK_ACCESS,
                                            LoginPage.login_yaml_parser('exp_qa_quick_access_text'))
        page.assert_input_is_present_receive_text_with_placeholder(QuickAccessPageLocators.INPUT_QA_NAME,
                                                                   LoginPage
                                                                   .login_yaml_parser('exp_qa_name_placeholder'))
        page.assert_element_text_is_correct(QuickAccessPageLocators.TEXT_QA_NOTICE,
                                            LoginPage.login_yaml_parser('exp_qa_notice_text'))
        page.assert_any_element_is_present(LoginPageLocators.PIC_EPAM_LOGO)

    @allure.title('[Smoke]Successful logging')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_quick_access_standard_login(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_input_keys_with_keyboard(QuickAccessPageLocators.INPUT_QA_NAME,
                                         LoginPage.login_yaml_parser('user_1_name_cred'))
        page.do_click(QuickAccessPageLocators.BTN_QA_ENTER)
        page.assert_any_element_is_present(LoginPageLocators.MODAL_WHATS_NEW)

    @allure.title('[Smoke]Open & Close with "Cancel" button')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_quick_access_go_back_with_cancel(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_click(QuickAccessPageLocators.BTN_QA_CANCEL)
        page.assert_btn_is_present_and_disabled(LoginPageLocators.BTN_SIGN_IN)

    @allure.title('[Critical Path]Error message check for "Name" field when clear with BACKSPACE')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.critical_path
    @pytest.mark.negative
    def test_name_input_clear_message_check(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_input_keys_with_keyboard(QuickAccessPageLocators.INPUT_QA_NAME,
                                         LoginPage.login_yaml_parser('user_1_name_cred'))
        page.do_clear_input_with_backspace(QuickAccessPageLocators.INPUT_QA_NAME)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_MESSAGE_EMAIL,
                                            LoginPage.login_yaml_parser('exp_err_email_required_text'))

    @allure.title('[Extended]Logging with credentials pasting with CTRL+V')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.extended
    @pytest.mark.positive
    def test_quick_access_standard_login_ctrl_v_paste(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_paste_keys_with_ctrl_v(QuickAccessPageLocators.INPUT_QA_NAME,
                                       LoginPage.login_yaml_parser('user_1_name_cred'))
        page.assert_btn_is_present_and_enabled(QuickAccessPageLocators.BTN_QA_ENTER)
        page.do_click(QuickAccessPageLocators.BTN_QA_ENTER)
        page.assert_any_element_is_present(LoginPageLocators.MODAL_WHATS_NEW)

    @allure.title('[Extended]Input allowed (<=255) symbols length into "Name field')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.extended
    @pytest.mark.positive
    @pytest.mark.parametrize('input_text', [
        LoginPage.login_yaml_parser("text_254"),
        LoginPage.login_yaml_parser("text_255")
    ])
    def test_quick_access_input_allowed_length(self, browser, input_text):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_input_keys_with_keyboard(QuickAccessPageLocators.INPUT_QA_NAME, input_text)
        page.assert_btn_is_present_and_enabled(QuickAccessPageLocators.BTN_QA_ENTER)
        page.do_click(QuickAccessPageLocators.BTN_QA_ENTER)
        page.assert_any_element_is_present(LoginPageLocators.MODAL_WHATS_NEW)

    @allure.title('[Extended]Input not allowed (>255) symbols length into "Name field')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.extended
    @pytest.mark.negative
    def test_quick_access_input_not_allowed_length(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_QUICK_ACCESS)
        page.do_input_keys_with_keyboard(QuickAccessPageLocators.INPUT_QA_NAME,
                                         LoginPage.login_yaml_parser('text_256_neg'))
        page.assert_btn_is_present_and_disabled(QuickAccessPageLocators.BTN_QA_ENTER)
        page.assert_element_text_is_correct(LoginPageLocators.ERR_MESSAGE_EMAIL,
                                            LoginPage.login_yaml_parser('exp_qa_err_255_symbols'))


@allure.suite('Logging')
@allure.sub_suite('"Feedback Survey" modal window test suite')
@pytest.mark.quick_access_suite
class TestFeedbackModal:

    @allure.title('[Smoke]Window elements check')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_feedback_open_assert_all_elements(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_FEEDBACK_SURVEY)
        page.assert_element_text_is_correct(FeedbackModalPageLocators.TEXT_FB_TITLE,
                                            LoginPage.login_yaml_parser('exp_fb_title'))
        page.assert_element_text_is_correct(FeedbackModalPageLocators.TEXT_FB_SCALE,
                                            LoginPage.login_yaml_parser('exp_fb_scale_title'))
        page.assert_element_text_is_correct(FeedbackModalPageLocators.TEXT_FB_FEEDBACK,
                                            LoginPage.login_yaml_parser('exp_fb_input_title'))
        page.assert_btn_is_present_and_enabled(FeedbackModalPageLocators.BTN_FB_CLOSE_CROSS)
        page.assert_btn_is_present_and_enabled(FeedbackModalPageLocators.BTN_FB_NOT_NOW)
        page.assert_btn_is_present_and_disabled(FeedbackModalPageLocators.BTN_FB_SEND)
        for i in range(1, 11):
            page.assert_btn_is_present_and_enabled(FeedbackModalPageLocators.BTN_SCALE_DICT[f"BTN_FB_RADIO_SCALE_{i}"])
        page.assert_input_is_present_receive_text_with_placeholder(FeedbackModalPageLocators.INPUT_FB_FEEDBACK,
                                                                   LoginPage
                                                                   .login_yaml_parser('exp_fb_feedback_placeholder'))

    @allure.title('[Smoke]Feedback submit')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.draft
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_feedback_feedback_submit(self, browser):
        page = LoginPage(browser)
        page.go_to_url(link_app)
        page.do_click(LoginPageLocators.BTN_FEEDBACK_SURVEY)
        page.do_click(FeedbackModalPageLocators.BTN_SCALE_DICT["BTN_FB_RADIO_SCALE_1"])
        page.assert_btn_is_present_and_enabled(FeedbackModalPageLocators.BTN_FB_SEND)
        page.do_input_keys_with_keyboard(FeedbackModalPageLocators.INPUT_FB_FEEDBACK,
                                         LoginPage.login_yaml_parser('text_254'))
        page.do_click(FeedbackModalPageLocators.BTN_FB_SEND)
        page.assert_db_received_data(link_agl_db_feedback,
                                     LoginPage.login_yaml_parser('query_fb_latest_feedback_text'),
                                     LoginPage.login_yaml_parser('text_254'))
        page.assert_db_received_data(link_agl_db_feedback,
                                     LoginPage.login_yaml_parser('query_fb_latest_feedback_scale'),
                                     '1')

    @allure.title('[Smoke]"Not now" button check')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_feedback_cancel(self, browser):
        pass

    @allure.title('[Critical path]Scale check with submit')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.critical_path
    @pytest.mark.positive
    # @pytest.mark.parametrize()
    def test_feedback_scale_check(self, browser):
        pass

    @allure.title('[Critical path]Quite by clicking outside of the modal window')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.critical_path
    @pytest.mark.positive
    def test_feedback_click_outside_window_quit(self, browser):
        pass

    @allure.title('[Critical path]Feedback without Scale check')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.critical_path
    @pytest.mark.negative
    def test_feedback_input_without_scale(self, browser):
        pass

    @allure.title('[Extended]Feedback input with CTRL + V')
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.extended
    @pytest.mark.positive
    def test_feedback_input_without_scale(self, browser):
        pass
