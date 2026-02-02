from selenium import webdriver
from selenium.webdriver.firefox import options
import pytest

@pytest.fixture()
def firefox():
    options = Options("--headless")
    browser = webdriver.Firefox(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()