import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "localhost:3000"


@pytest.mark.smoke
class TestsSmoke:

    def test_smoke_login_page_opens(self, browser):
        browser.get(link)
        WebDriverWait(browser, 20).until(EC.title_contains('Agiles'))
        print(browser.title)
        #assert browser.title in "Agiles", "Incorrect page title/Page is not opened"
'''
    def test_smoke_sign_up_check(selfself, browser):
        wait = WebDriverWait(browser, 10)
        browser.get(link)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > div.BasePage__container > div.BasePage__content > div > form > div.TextLink__container > a")))
        browser.find_element(By.CSS_SELECTOR, "#root > div.BasePage__container > div.BasePage__content > div > form > div.TextLink__container > a").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//input[@placeholder='Enter First Name']").send_keys('Bob')
        time.sleep(2)
'''