""" Board Management page Test suite """


import pytest
from ui.pages.board_management_page import BoardManagementPage
from ui.testdata.links import *
from ui.pages.locators import *
from ui.utilities.support import *

@allure.suite('Board Management')
@allure.sub_suite('Board Management page test suite')
@pytest.mark.board_management_suite
class TestBoardManagementPage:

    @allure.title('[Smoke]Window elements check')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.draft
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_whats_new_open_assert_all_elements(self, browser):
        page = BoardManagementPage(browser)
        page.go_to_board_management()
        page.assert_any_element_is_present(WhatsNewModalPageLocators.MODAL_WHATS_NEW)
        #page.assert_element_text_is_correct(WhatsNewModalPageLocators.TITLE_WHATS_NEW,
        #                                    BoardManagementPage.board_management_yaml_parser('exp_wn_page_title'))
        page.assert_element_text_is_correct(WhatsNewModalPageLocators.TITLE_LATEST_RELEASE,
                                            BoardManagementPage
                                            .board_management_yaml_parser('exp_wn_latest_release_title'))
        page.assert_element_text_is_correct(WhatsNewModalPageLocators.TITLE_NEW_FEATURES,
                                            BoardManagementPage
                                            .board_management_yaml_parser('exp_wn_new_features_title'))
        page.assert_element_text_is_correct(WhatsNewModalPageLocators.TITLE_BUGS,
                                            BoardManagementPage
                                            .board_management_yaml_parser('exp_wn_latest_bugs_title'))
        page.assert_btn_is_present_and_enabled(WhatsNewModalPageLocators.BTN_GOT_IT)

