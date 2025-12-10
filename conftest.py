import pytest

from selenium import webdriver

from url import main_page_url

@pytest.fixture(scope="function")
def driver():

    browser = webdriver.Firefox()
    browser.get(main_page_url)
    yield browser
    browser.quit()
