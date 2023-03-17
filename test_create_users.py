import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link_home = "http://localhost:3000/"
link_admin = "http://localhost:8025/"


@pytest.mark.smoke
class TestsCreateUsers:

    def test_smoke_login_page_opens(self, browser):
        browser.get(link_home)
        assert browser.title in "Agiles", "Incorrect page title/Page is not opened"

    @pytest.mark.createusers
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
        wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Inbox")))
        browser.find_element(By.CSS_SELECTOR, '.msglist-message.row.ng-scope').click()
        auth_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'http://localhost:8086')
        access_link = 'http://127.0.0.1:3000/' + auth_link.text[22:]
        browser.switch_to.window(w_agiles)
        browser.get(access_link)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.WhatsNewModal__modalTitle')))

    @pytest.mark.createusers
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
        wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Inbox")))
        browser.find_element(By.CSS_SELECTOR, '.msglist-message.row.ng-scope').click()
        auth_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'http://localhost:8086')
        access_link = 'http://127.0.0.1:3000/' + auth_link.text[22:]
        browser.switch_to.window(w_agiles)
        browser.get(access_link)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.WhatsNewModal__modalTitle')))

    @pytest.mark.createusers
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
        wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Inbox")))
        browser.find_element(By.CSS_SELECTOR, '.msglist-message.row.ng-scope').click()
        auth_link = browser.find_element(By.PARTIAL_LINK_TEXT, 'http://localhost:8086')
        access_link = 'http://127.0.0.1:3000/' + auth_link.text[22:]
        browser.switch_to.window(w_agiles)
        browser.get(access_link)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.WhatsNewModal__modalTitle')))

