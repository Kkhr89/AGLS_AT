import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service


# Method to make browser types callable from terminal:
def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     default='chrome',
                     help='Choose browser: chrome, firefox or edge')


# Method to initialize-maintain-quite session in browser:
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
