import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, ... (etc.)")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    browser = webdriver.Chrome()
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    yield browser
    print("\nquit browser..")
    browser.quit()
