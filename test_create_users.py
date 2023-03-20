import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link_home = "http://localhost:3000/"
link_admin = "http://localhost:8025/"


@pytest.mark.createusers
class TestsCreateUsers:

    def test_create_board_owner(self, browser):
        wait = WebDriverWait(browser, 20)
        browser.get(link_home)
        w_agiles = browser.current_window_handle
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign Up")))
        browser.find_element(By.LINK_TEXT, "Sign Up").click()
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys('Board')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']").send_keys('Owner')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys('board_owner@mail.com')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys('Godfather1989!')
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
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys('First')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']").send_keys('Member')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys('first_member@mail.com')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys('Godfather1989!')
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
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys('Second')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']").send_keys('Member')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys('second_member@mail.com')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys('Godfather1989!')
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
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys('Third')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']").send_keys('Member')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys('third_member@mail.com')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys('Godfather1989!')
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
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys('Fourth')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']").send_keys('Member')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys('fourth_member@mail.com')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys('Godfather1989!')
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
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys('Fifth')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Last Name (Optional)']").send_keys('Member')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Email']").send_keys('fifth_member@mail.com')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('G')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('odfather1')
        browser.find_element(By.XPATH, "//input[@placeholder='Enter Your Password']").send_keys('989!')
        browser.find_element(By.XPATH, "//input[@placeholder='Confirm Password']").send_keys('Godfather1989!')
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


class TestFeedbackForm:
    @pytest.mark.smoke
    def test_smoke_form_opens(self, browser):
        wait = WebDriverWait(browser, 20)

        # Open http://localhost:3000/:
        browser.get(link_home)

        # Wait until "Email" input field is loaded on the page:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//input[@placeholder="Enter Your Email"]'))
        )

        # Fill in "Email" field:
        browser.find_element(By.XPATH, '//input[@placeholder="Enter Your Email"]').send_keys('board_owner@mail.com')

        # Fill in "Password" field:
        browser.find_element(By.XPATH, '//input[@placeholder="Enter Your Password"]').send_keys('Godfather1989!')

        # Click "Sign in" button:
        browser.find_element(By.CSS_SELECTOR, '.Button__button.Button__blue.styles__actionButton').click()

        # Wait for "Not Found" alert to be displayed:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@role="alert"]')
        ))

        # Close "Not Found" alert:
        if len(browser.find_elements(By.XPATH, '//div[@role="alert"]')) != 0:
            browser.find_element(By.XPATH,
                                 '//*[@id="root"]/div[2]/div/div/div/div/div/button').click()

        # Click "Got it" if modal wdw "What's New" is opened(button appears):
        if len(browser.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button')) != 0:
            browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button').click()

        # Click "Retrospective" tab:
        browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/a[3]/div').click()

        # Click "Feedback" button:
        browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/div[3]/button[1]/div').click()

        # Check if opened dialog title is displayed:
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.ant-modal-header')
        ))
        assert browser.find_element(By.CSS_SELECTOR, '.ant-modal-header').text in 'AGILES APP FEEDBACK SURVEY',\
            'Feedback Form was not opened'

    @pytest.mark.smoke
    def test_smoke_form_submits(self, browser):
        wait = WebDriverWait(browser, 20)

        # Open http://localhost:3000/:
        browser.get(link_home)

        # Wait until "Email" input field is loaded on the page:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//input[@placeholder="Enter Your Email"]'))
        )

        # Fill in "Email" field:
        browser.find_element(By.XPATH, '//input[@placeholder="Enter Your Email"]').send_keys('board_owner@mail.com')

        # Fill in "Password" field:
        browser.find_element(By.XPATH, '//input[@placeholder="Enter Your Password"]').send_keys('Godfather1989!')

        # Click "Sign in" button:
        browser.find_element(By.CSS_SELECTOR, '.Button__button.Button__blue.styles__actionButton').click()

        # Wait for "Not Found" alert to be displayed:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@role="alert"]')
        ))

        # Close "Not Found" alert:
        if len(browser.find_elements(By.XPATH, '//div[@role="alert"]')) != 0:
            browser.find_element(By.XPATH,
                                 '//*[@id="root"]/div[2]/div/div/div/div/div/button').click()

        # Click "Got it" if modal wdw "What's New" is opened(button appears):
        if len(browser.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button')) != 0:
            browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button').click()

        # Click "Retrospective" tab:
        browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/a[3]/div').click()

        # Click "Feedback" button:
        browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/div[3]/button[1]/div').click()

        # Check if opened dialog title is displayed:
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.ant-modal-header')
        ))

        # Click on 1 scale button:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/ol/li[1]/label/div').click()

        # Click on "Send" button:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()

        # Check if Succsessfull message appeared:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div')
        ))
        assert browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div').text in\
               'Your feedback has been submitted. Thank you!', 'Incorrect Successful message'

    @pytest.mark.feedbacksymbolslimit
    def test_5246_allowed_limit_254(self, browser):
        wait = WebDriverWait(browser, 20)

        # Open http://localhost:3000/:
        browser.get(link_home)

        # Wait until "Email" input field is loaded on the page:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//input[@placeholder="Enter Your Email"]'))
        )

        # Fill in "Email" field:
        browser.find_element(By.XPATH, '//input[@placeholder="Enter Your Email"]').send_keys('board_owner@mail.com')

        # Fill in "Password" field:
        browser.find_element(By.XPATH, '//input[@placeholder="Enter Your Password"]').send_keys('Godfather1989!')

        # Click "Sign in" button:
        browser.find_element(By.CSS_SELECTOR, '.Button__button.Button__blue.styles__actionButton').click()

        # Wait for "Not Found" alert to be displayed:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@role="alert"]')
        ))

        # Close "Not Found" alert:
        if len(browser.find_elements(By.XPATH, '//div[@role="alert"]')) != 0:
            browser.find_element(By.XPATH,
                                 '//*[@id="root"]/div[2]/div/div/div/div/div/button').click()

        # Click "Got it" if modal wdw "What's New" is opened(button appears):
        if len(browser.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button')) != 0:
            browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button').click()

        # Click "Retrospective" tab:
        browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/a[3]/div').click()

        # Click "Feedback" button:
        browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/div[3]/button[1]/div').click()

        # Check if opened dialog title is displayed:
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.ant-modal-header')
        ))

        # Click on 1 scale button:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/ol/li[1]/label/div').click()

        # Check If "Send" button becomes available:
        assert browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').is_enabled()

        # Put 254 symbols into input field:
        input_f = browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div/textarea')
        input_f\
            .send_keys('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.'
                       ' Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus'
                       ' mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis')

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
    def test_5246_allowed_limit_255(self, browser):
        wait = WebDriverWait(browser, 20)

        # Open http://localhost:3000/:
        browser.get(link_home)

        # Wait until "Email" input field is loaded on the page:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//input[@placeholder="Enter Your Email"]'))
        )

        # Fill in "Email" field:
        browser.find_element(By.XPATH, '//input[@placeholder="Enter Your Email"]').send_keys('board_owner@mail.com')

        # Fill in "Password" field:
        browser.find_element(By.XPATH, '//input[@placeholder="Enter Your Password"]').send_keys('Godfather1989!')

        # Click "Sign in" button:
        browser.find_element(By.CSS_SELECTOR, '.Button__button.Button__blue.styles__actionButton').click()

        # Wait for "Not Found" alert to be displayed:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@role="alert"]')
        ))

        # Close "Not Found" alert:
        if len(browser.find_elements(By.XPATH, '//div[@role="alert"]')) != 0:
            browser.find_element(By.XPATH,
                                 '//*[@id="root"]/div[2]/div/div/div/div/div/button').click()

        # Click "Got it" if modal wdw "What's New" is opened(button appears):
        if len(browser.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button')) != 0:
            browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button').click()

        # Click "Retrospective" tab:
        browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/a[3]/div').click()

        # Click "Feedback" button:
        browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/div[3]/button[1]/div').click()

        # Check if opened dialog title is displayed:
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.ant-modal-header')
        ))

        # Click on 1 scale button:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/ol/li[1]/label/div').click()

        # Check If "Send" button becomes available:
        assert browser.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').is_enabled()

        # Put 255 symbols into input field:
        input_field = browser.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div/textarea')
        input_field \
            .send_keys('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.'
                       ' Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus'
                       ' mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis1')

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
    def test_5247_not_allowed_limit(self, browser):
        wait = WebDriverWait(browser, 20)

        # Open http://localhost:3000/:
        browser.get(link_home)

        # Wait until "Email" input field is loaded on the page:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//input[@placeholder="Enter Your Email"]'))
        )

        # Fill in "Email" field:
        browser.find_element(By.XPATH, '//input[@placeholder="Enter Your Email"]').send_keys('board_owner@mail.com')

        # Fill in "Password" field:
        browser.find_element(By.XPATH, '//input[@placeholder="Enter Your Password"]').send_keys('Godfather1989!')

        # Click "Sign in" button:
        browser.find_element(By.CSS_SELECTOR, '.Button__button.Button__blue.styles__actionButton').click()

        # Wait for "Not Found" alert to be displayed:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, '//div[@role="alert"]')
        ))

        # Close "Not Found" alert:
        if len(browser.find_elements(By.XPATH, '//div[@role="alert"]')) != 0:
            browser.find_element(By.XPATH,
                                 '//*[@id="root"]/div[2]/div/div/div/div/div/button').click()

        # Click "Got it" if modal wdw "What's New" is opened(button appears):
        if len(browser.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button')) != 0:
            browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button').click()

        # Click "Retrospective" tab:
        browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/a[3]/div').click()

        # Click "Feedback" button:
        browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/div[3]/button[1]/div').click()

        # Check if opened dialog title is displayed:
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.ant-modal-header')
        ))

        # Put 256 symbols into input field:
        input_field = browser.find_element(By.XPATH,
                                           '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div/textarea')
        input_field \
            .send_keys('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.'
                       ' Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus'
                       ' mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis12')

        # Check if input field have not received 256 symbols:
        assert len(input_field.text) == 255, f'Error - length is {len(input_field.text)} instead of 255 max allowed'

        # Check If "Send" button does not become available:
        assert not browser.find_element(By.XPATH,
                                    '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').is_enabled(), \
            '"Send" button became available without scaling'
