import pytest
import allure
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Method to make browser types callable from terminal:
def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome, firefox or edge')


@allure.step('Initialize, maintain and quite session in browser')
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('--browser')
    if browser_name == 'chrome':
        service = selenium.webdriver.chrome.service.Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == 'firefox':
        service = selenium.webdriver.firefox.service.Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        browser = webdriver.Firefox(service=service, options=options)
    elif browser_name == 'edge':
        service = selenium.webdriver.edge.service.Service(EdgeChromiumDriverManager().install())
        options = webdriver.EdgeOptions()
        options.use_chromium = True
        browser = webdriver.Edge(service=service, options=options)
    else:
        raise pytest.UsageError('==browser_name should be chrome, firefox or edge')
    browser.maximize_window()
    yield browser
    browser.quit()
