import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testdata import *


@pytest.mark.feedbackform
class TestFeedbackForm:

    @pytest.mark.smoke
    def test_smoke_form_opens(self, browser, feedback):
        wait = WebDriverWait(browser, 20)

        # Open Feedback form (by feedback as a function arg)

        # Check if opened dialog title is displayed:
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.ant-modal-header')
        ))
        assert browser.find_element(By.CSS_SELECTOR, '.ant-modal-header').text in 'AGILES APP FEEDBACK SURVEY',\
            'Feedback Form was not opened'

    @pytest.mark.smoke
    def test_smoke_form_submits(self, browser, feedback):
        wait = WebDriverWait(browser, 20)

        # Open Feedback form (by feedback as a function arg)

        # Check if opened dialog title is displayed:
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.ant-modal-header')
        ))

        # Click on 1 scale button:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/ol/li[1]/label/div').click()

        # Click on "Send" button:
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]')
        ))
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()

        # Check if Succsessfull message appeared:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div')
        ))
        assert browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div').text in\
               'Your feedback has been submitted. Thank you!', 'Incorrect Successful message'

    @pytest.mark.feedbacksymbolslimit
    def test_5246_allowed_limit_254(self, browser, feedback):
        wait = WebDriverWait(browser, 20)

        # Open Feedback form (by feedback as a function arg)

        # Click on 1 scale button:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/ol/li[1]/label/div').click()

        # Check If "Send" button becomes available:
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]')
        ))
        assert browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').is_enabled()

        # Put 254 symbols into input field:
        input_f = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div/textarea')
        input_f.send_keys(FEEDBACK_INPUT['254'])

        # Check if input field received 254 symbols:
        assert len(input_f.text) == 254, f'Error - length is {len(input_f.text)} instead of 254 symbols'

        # Click on "Send" button:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()

        # Check if Succsessfull message appeared:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div')
        ))
        assert browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div').text in\
               'Your feedback has been submitted. Thank you!', 'Incorrect Successful message'

    @pytest.mark.feedbacksymbolslimit
    def test_5246_allowed_limit_255(self, browser, feedback):
        wait = WebDriverWait(browser, 20)

        # Open Feedback form (by feedback as a function arg)

        # Click on 1 scale button:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/ol/li[1]/label/div').click()

        # Check If "Send" button becomes available:
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]')
        ))
        assert browser.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').is_enabled()

        # Put 255 symbols into input field:
        input_field = browser.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div/textarea')
        input_field.send_keys(FEEDBACK_INPUT['255'])

        # Check if input field received 255 symbols:
        assert len(input_field.text) == 255, f'Error - length is {len(input_field.text)} instead of 255 symbols'

        # Click on "Send" button:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()

        # Check if Succsessfull message appeared:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div')
        ))
        assert browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div').text in \
               'Your feedback has been submitted. Thank you!', 'Incorrect Successful message'

    @pytest.mark.feedbacksymbolslimit
    def test_5247_not_allowed_limit(self, browser, feedback):
        wait = WebDriverWait(browser, 20)

        # Open Feedback form (by feedback as a function arg)

        # Put 256 symbols into input field:
        input_field = browser.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div/textarea')
        input_field.send_keys(FEEDBACK_INPUT['256'])

        # Check if input field have not received 256 symbols:
        assert len(input_field.text) == 255, f'Error - length is {len(input_field.text)} instead of 255 max allowed'

        # Check If "Send" button does not become available:
        assert not browser.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').is_enabled(), \
            '"Send" button became available without scaling'

class TestBoard:

    @pytest.mark.boardexport
    def test_smoke_board_is_created(self, browser, board_create):
        wait = WebDriverWait(browser, 20)

        # Wait loading:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div')
        ))

        assert browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div').text\
               in "Board is created", 'Failed to create board/Succsess message is incorrect'