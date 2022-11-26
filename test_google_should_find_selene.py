from selene.support.shared import browser
from selene import be, have


def test_google(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('rfrfrgrgrgsddf').press_enter()
    browser.element('#res').should(have.text('По запросу rfrfrgrgrgsddf ничего не найдено.'))
