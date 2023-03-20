import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser',
                    action='store',
                    default='chrome',
                    help='Choose browser: chrome, firefox or edge')


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
