import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def config_options():
    options = Options()
    options.add_argument('--window-size = 1920,1080')
    return options


@pytest.fixture()
def browser_config(config_options):
    browser.config.driver = webdriver.Chrome(options=config_options)
    return browser_config


@pytest.fixture()
def open_browser(browser_config):
    browser.open('https://google.com')
    yield
