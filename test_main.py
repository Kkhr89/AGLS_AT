import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testdata import *
from sqlalchemy import text

@pytest.mark.clsfeedbackform
class TestFeedbackForm:

    @pytest.mark.smoke
    def test_smoke_feedback_empty_form_submits(self, browser, feedback, feedback_database_setup):
        wait = WebDriverWait(browser, 20)

        # Open Feedback form (by feedback as a function arg)

        # Check if opened dialog title is displayed:
        assert browser.find_element(By.CSS_SELECTOR, '.ant-modal-root').is_displayed()

        # # Click on #1 scale button:
        try:
            wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f'label[for="point1"]')
            )).click()
        except:
            wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f'label[for="point1"] > div')
            )).click()

        # Click on "Send" button:
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.ant-modal-footer .Button__button.Button__limeGreen')
        )).click()

        # Check if Successful message appeared:
        displayed_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.uui-snackbar-item-self>div>div>div>div')
        )).text
        correct_message = 'Your feedback has been submitted. Thank you!'
        assert displayed_message == correct_message, \
            f'Incorrect Successful message - "{displayed_message}" instead of "{correct_message}"'

        # Check that database received correct data:
        result = feedback_database_setup.execute(text("SELECT value FROM agl_feedback.response_answer"
                                                      " WHERE question_id = 1 ORDER BY id DESC LIMIT 1")).fetchone()
        db_result = int(result[0])
        assert db_result == 1, f'Value in database is {db_result} instead of 1'

    @pytest.mark.feedbacksymbolslimit
    @pytest.mark.parametrize("scale", range(2, 11))
    def test_feedback_form_scale_check(self, browser, feedback, feedback_database_setup, scale):
        wait = WebDriverWait(browser, 20)

        # Open Feedback form (by feedback as a function arg)

        # # Click on scale button:
        try:
            wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f'label[for="point{scale}"]')
            )).click()
        except:
            wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f'label[for="point{scale}"] > div')
            )).click()

        # Click on "Send" button:
        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.ant-modal-footer .Button__button.Button__limeGreen')
        )).click()

        # Check if Successful message appeared:
        displayed_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.uui-snackbar-item-self>div>div>div>div')
        )).text
        correct_message = 'Your feedback has been submitted. Thank you!'
        assert displayed_message == correct_message, \
            f'Incorrect Successful message - "{displayed_message}" instead of "{correct_message}"'

        # Check that database received correct data:
        result = feedback_database_setup.execute(text("SELECT value FROM agl_feedback.response_answer"
                                                      " WHERE question_id = 1 ORDER BY id DESC LIMIT 1")).fetchone()
        db_result = int(result[0])
        assert db_result == scale, f'Value in database is {db_result} instead of {scale}'

    @pytest.mark.draft
    @pytest.mark.feedbacksymbolslimit
    @pytest.mark.parametrize("input_length", [254, 255])
    def test_5246_feedback_input_allowed_limit(self, browser, feedback_input, feedback_database_setup, input_length):
        wait = WebDriverWait(browser, 20)

        # Perform Feedback_input

        # Put 254 symbols into input field:
        input_f = browser.find_element(By.CSS_SELECTOR, 'textarea[data-testid="feedback-comment-field"]')
        input_f.send_keys(FEEDBACK_INPUT[f'{input_length}'])

        # Check if input field received 254 symbols:
        assert len(input_f.text) == input_length, f'Error - length is {len(input_f.text)}' \
                                                  f' instead of {input_length} symbols'

        # Click on "Send" button:
        browser.find_element(By.CSS_SELECTOR, '.ant-modal-footer .Button__button.Button__limeGreen').click()

        # Check if Successful message appeared:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div')
        ))
        assert browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div').text in\
               'Your feedback has been submitted. Thank you!', 'Incorrect Successful message'

        # Check that database received the data:

        result = feedback_database_setup.execute(text("SELECT * FROM agl_feedback.response_answer")).fetchall()
        assert len(result) > 0, 'Database is empty'

    @pytest.mark.xfail
    @pytest.mark.feedbacksymbolslimit
    def test_5247_feedback_input_not_allowed_limit(self, browser, feedback):

        # Perform feedback

        # Put 256 symbols into input field:
        input_field = browser.find_element(By.CSS_SELECTOR, 'textarea[data-testid="feedback-comment-field"]')
        input_field.send_keys(FEEDBACK_INPUT['256'])

        # Check if input field have not received 256 symbols:
        assert len(input_field.text) == 255, f'Error - length is {len(input_field.text)} instead of 255 max allowed'

        # Check If "Send" button does not become available:
        assert not browser.find_element(By.CSS_SELECTOR, '.ant-modal-footer .Button__button.Button__limeGreen')\
            .is_enabled(), '"Send" button became available without scaling'


@pytest.mark.clsboard
class TestBoard:

    @pytest.mark.boardexport
    def test_smoke_board_is_created(self, browser, board_create):

        assert browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div').text\
               in "Board is created", 'Failed to create board/Success message is incorrect'

@pytest.mark.xfail
@pytest.mark.clsbugcheck
class TestBugFixes:

    def test_5407_email_link_with_dot(self, browser, board_add_member):
        wait = WebDriverWait(browser, 20)

        # Add Member to board (conftest.py)

        # Open new window for MailHog:
        w_agiles = browser.current_window_handle
        browser.switch_to.new_window('tab')
        browser.get(link_admin)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]')
        ))

        # Click first email:
        browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]').click()

        # Parse link and save it:
        auth_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'http://localhost:8082')
        access_link = 'http://127.0.0.1:3000/' + auth_link.text[22:]

        # Open link in new window
        browser.switch_to.window(w_agiles)
        browser.get(access_link)

        # Check if board was loaded:
        browser.implicitly_wait(3)
        assert browser.find_element(By.CSS_SELECTOR, '.BoardPage__usersPanel > button'),\
            'Failed to access the board'
