from selene.support.shared import browser
from selene import have, be


def test_google_good_search(open_browser):
    browser.element('[id=suggestion-search]').should(be.blank).type('batman 2005').press_enter()


