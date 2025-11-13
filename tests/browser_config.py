import pytest
from selene import browser, have

browser.config.base_url = 'https://todomvc.com'
browser.config.timeout = 4

def test_todomvc():
    browser.element().with_(timeout=browser.config.timeout * 2)

    browser.open('/')


