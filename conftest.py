import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Edge()
    yield browser
    browser.quit()
