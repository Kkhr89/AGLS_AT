import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testdata import *


@pytest.mark.createusers
class TestsCreateUsers:

    def test_create_board_owner(self, browser):
        wait = WebDriverWait(browser, 20)
        browser.get(link_home)
        w_agiles = browser.current_window_handle
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign Up")))
        browser.find_element(By.LINK_TEXT, "Sign Up").click()
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys(USERS['first_name_1'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']")\
            .send_keys(USERS['last_name_1'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys(USERS['email_1'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys(USERS['password'])
        browser.find_element(By.CSS_SELECTOR, ".Button__button.Button__blue.styles__actionButton").click()
        browser.switch_to.new_window('tab')
        browser.get(link_admin)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]')))
        browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]').click()
        auth_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'http://localhost:8086')
        access_link = 'http://127.0.0.1:3000/' + auth_link.text[22:]
        browser.switch_to.window(w_agiles)
        browser.get(access_link)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.WhatsNewModal__modalTitle')))

    def test_create_first_member(self, browser):
        wait = WebDriverWait(browser, 20)
        browser.get(link_home)
        w_agiles = browser.current_window_handle
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign Up")))
        browser.find_element(By.LINK_TEXT, "Sign Up").click()
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys(USERS['first_name_2'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']")\
            .send_keys(USERS['last_name_2-6'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys(USERS['email_2'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys(USERS['password'])
        browser.find_element(By.CSS_SELECTOR, ".Button__button.Button__blue.styles__actionButton").click()
        browser.switch_to.new_window('tab')
        browser.get(link_admin)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]')))
        browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]').click()
        auth_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'http://localhost:8086')
        access_link = 'http://127.0.0.1:3000/' + auth_link.text[22:]
        browser.switch_to.window(w_agiles)
        browser.get(access_link)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.WhatsNewModal__modalTitle')))

    def test_create_second_member(self, browser):
        wait = WebDriverWait(browser, 20)
        browser.get(link_home)
        w_agiles = browser.current_window_handle
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign Up")))
        browser.find_element(By.LINK_TEXT, "Sign Up").click()
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys(USERS['first_name_3'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']")\
            .send_keys(USERS['last_name_2-6'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys(USERS['email_3'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys(USERS['password'])
        browser.find_element(By.CSS_SELECTOR, ".Button__button.Button__blue.styles__actionButton").click()
        browser.switch_to.new_window('tab')
        browser.get(link_admin)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]')))
        browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]').click()
        auth_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'http://localhost:8086')
        access_link = 'http://127.0.0.1:3000/' + auth_link.text[22:]
        browser.switch_to.window(w_agiles)
        browser.get(access_link)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.WhatsNewModal__modalTitle')))

    def test_create_third_member(self, browser):
        wait = WebDriverWait(browser, 20)
        browser.get(link_home)
        w_agiles = browser.current_window_handle
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign Up")))
        browser.find_element(By.LINK_TEXT, "Sign Up").click()
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys(USERS['first_name_4'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']")\
            .send_keys(USERS['last_name_2-6'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys(USERS['email_4'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys(USERS['password'])
        browser.find_element(By.CSS_SELECTOR, ".Button__button.Button__blue.styles__actionButton").click()
        browser.switch_to.new_window('tab')
        browser.get(link_admin)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]')))
        browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]').click()
        auth_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'http://localhost:8086')
        access_link = 'http://127.0.0.1:3000/' + auth_link.text[22:]
        browser.switch_to.window(w_agiles)
        browser.get(access_link)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.WhatsNewModal__modalTitle')))

    def test_create_fourth_member(self, browser):
        wait = WebDriverWait(browser, 20)
        browser.get(link_home)
        w_agiles = browser.current_window_handle
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign Up")))
        browser.find_element(By.LINK_TEXT, "Sign Up").click()
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys(USERS['first_name_5'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']")\
            .send_keys(USERS['last_name_2-6'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys(USERS['email_5'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys(USERS['password'])
        browser.find_element(By.CSS_SELECTOR, ".Button__button.Button__blue.styles__actionButton").click()
        browser.switch_to.new_window('tab')
        browser.get(link_admin)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]')))
        browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]').click()
        auth_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'http://localhost:8086')
        access_link = 'http://127.0.0.1:3000/' + auth_link.text[22:]
        browser.switch_to.window(w_agiles)
        browser.get(access_link)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.WhatsNewModal__modalTitle')))

    def test_create_fifth_member(self, browser):
        wait = WebDriverWait(browser, 20)
        browser.get(link_home)
        w_agiles = browser.current_window_handle
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign Up")))
        browser.find_element(By.LINK_TEXT, "Sign Up").click()
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys(USERS['first_name_6'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']")\
            .send_keys(USERS['last_name_2-6'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys(USERS['email_6'])
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys(USERS['password'])
        browser.find_element(By.CSS_SELECTOR, ".Button__button.Button__blue.styles__actionButton").click()
        browser.switch_to.new_window('tab')
        browser.get(link_admin)
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]')))
        browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]').click()
        auth_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'http://localhost:8086')
        access_link = 'http://127.0.0.1:3000/' + auth_link.text[22:]
        browser.switch_to.window(w_agiles)
        browser.get(access_link)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.WhatsNewModal__modalTitle')))


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