import pytest
import openpyxl
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testdata import *
from sqlalchemy import create_engine, text


# Function to parse emails from users.xlsx:
def users_parser():
    dict_users = dict()
    wb = openpyxl.load_workbook('users_creator/users.xlsx')
    sheet = wb.active
    i = 1
    for row in sheet.iter_rows(min_row=2, values_only=True):
        first_name, last_name, email = row
        dict_users[f'first_name_{i}'] = first_name
        dict_users[f'last_name_{i}'] = last_name
        dict_users[f'email_{i}'] = email
        i += 1
    return dict_users


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
        service = webdriver.chrome.service.Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == 'firefox':
        service = webdriver.firefox.service.Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(service=service, options=options)
    elif browser_name == 'edge':
        service = webdriver.edge.service.Service(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        browser = webdriver.Edge(service=service, options=options)
    else:
        raise pytest.UsageError('==browser_name should be chrome, firefox or edge')
    browser.maximize_window()
    yield browser
    browser.quit()


# Function to open Retro tab:
@pytest.fixture(scope="function")
def retro(browser):
    wait = WebDriverWait(browser, 20)

    # Open http://localhost:3000/:
    browser.get(link_home)

    # Fill in "Email" field:
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input[placeholder="Enter Your Email"]'))
    ).send_keys(users_parser()['email_1'])


    # Fill in "Password" field:
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter Your Password"]')\
        .send_keys('Godfather1989!')

    # Click "Sign in" button:
    browser.find_element(By.CSS_SELECTOR, '.Button__button.Button__blue.styles__actionButton').click()

    # Wait for "Not Found" button to be displayed:
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div[role="alert"]')
    ))

    # Close "Not Found" alert:
    if len(browser.find_elements(By.CSS_SELECTOR, 'div[role="alert"]')) != 0:
        alert = browser.find_element(By.CSS_SELECTOR, 'div[role="alert"] > div > button')
        browser.execute_script("arguments[0].scrollIntoView();", alert)
        alert.click()

    # Click "Got it" if modal wdw "What's New" is opened(button appears):
    if len(browser.find_elements(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button')) != 0:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button').click()

    # Click "Retrospective" tab:
    browser.find_element(By.CSS_SELECTOR, 'a[href="/retro"]').click()


# Function to open Feedback tab:
@pytest.fixture(scope="function")
def feedback(browser, retro):
    wait = WebDriverWait(browser, 20)

    # Click "Feedback" button:
    browser.find_element(By.CSS_SELECTOR, 'div[data-testid="header-menu-icon-wrapper"] >button:first-child').click()

# Function to click Scale button in Feedback tab:
@pytest.fixture(scope="function")
def feedback_input(browser, feedback):
    wait = WebDriverWait(browser, 20)

    # Click on 1 scale button:
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'label[for="point1"] > div')
    )).click()

    # Check If "Send" button becomes available:
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '.ant-modal-footer .Button__button.Button__limeGreen')
    ))
    assert browser.find_element(By.CSS_SELECTOR, '.ant-modal-footer .Button__button.Button__limeGreen').is_enabled(), \
        'Send button is disabled'


# Function to create board:
@pytest.fixture(scope="function")
def board_create(browser, retro):
    wait = WebDriverWait(browser, 20)

    # Click on "Create board" button:
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.BoardManagement__boardManagementHeader > button')
    )).click()

    # Fill in "Board name":
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'input[placeholder="Board name"]')
    )).send_keys('Board #1')

    # Click "Create" button:
    browser.find_element(By.XPATH, '//button[text()="Create"]').click()

    # Wait pop-up loading:
    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/div')
    ))


@pytest.fixture(scope="function")
def board_add_member(browser, board_create):
    wait = WebDriverWait(browser, 20)

    # Click "Manage members" button:
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.BoardPage__usersPanel > button')
    )).click()

    # Fill in member email:
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.TextInput__textInput.ManageUsersModal__emailInput')
    )).send_keys(users_parser()['email_2'])

    # Click "Add" button:
    browser.find_element(By.CSS_SELECTOR, '.ManageUsersModal__addMember > button').click()

    # Click "Save Changes" button:
    browser.find_element(By.CSS_SELECTOR, '.ant-modal-footer > .Button__button.Button__limeGreen').click()


# Function for database setup:
@pytest.fixture(scope='function')
def feedback_database_setup():
    # DB connect:
    engine = create_engine('postgresql://postgres:postgres@localhost:54324/agl_db')
    connection = engine.connect()
    yield connection
    # DB close
    connection.close()

