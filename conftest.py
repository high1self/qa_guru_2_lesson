import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def set_webdriver():
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    return browser.config.driver


@pytest.fixture()
def set_browser_size():
    # options = Options()
    # options.add_argument('--window-size = 1920,1080')
    # return options
    browser.config.driver.set_window_size(1920,1080)


@pytest.fixture()
def open_browser(set_webdriver, set_browser_size):
    browser.open('https://google.com/ncr')