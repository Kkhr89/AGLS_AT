import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testdata import *


# Function to make browser types callable from terminal:
def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome, firefox or edge')


# Function to initialize browser:
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('--browser')
    if browser_name == 'chrome':
        browser = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == 'edge':
        browser = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        raise pytest.UsageError('==browser_name should be chrome, firefox or edge')
    yield browser
    browser.quit()


# Function to open Retro tab
@pytest.fixture(scope="function")
def retro(browser):
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

    # Wait for "Not Found" x button to be displayed:
    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//div[@role="alert"]')
    ))
    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/button')
    ))

    # Close "Not Found" alert:
    if len(browser.find_elements(By.XPATH, '//div[@role="alert"]')) != 0:
        alert = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/button')
        browser.execute_script("arguments[0].scrollIntoView();", alert)
        alert.click()

    # Click "Got it" if modal wdw "What's New" is opened(button appears):
    if len(browser.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button')) != 0:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button').click()

    # Click "Retrospective" tab:
    browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/a[3]/div').click()


# Function to open Feedback tab
@pytest.fixture(scope="function")
def feedback(browser, retro):
    wait = WebDriverWait(browser, 20)

    # Click "Feedback" button:
    browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/nav/div[3]/button[1]/div').click()

    # Check if opened dialog title is displayed:
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.ant-modal-header')
    ))


@pytest.fixture(scope="function")
def board_create(browser, retro):
    wait = WebDriverWait(browser, 20)

    # Click on "Create board" button:
    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/button')
    ))
    browser.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[1]/button').click()

    # Fill in "Board name":
    browser.find_element(By.XPATH, '//input[@placeholder="Board name"]')\
        .send_keys('Board #1')

    # Click "Create" button:
    browser.find_element(By.XPATH, '//button[text()="Create"]').click()
