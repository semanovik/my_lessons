import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):  # метод для передачи параметров командной строке
    parser.addoption('--browser_name',  # принимаем браузер
                     action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language',  # принимаем язык
                     action='store',
                     default='en-gb',
                     help="Choose language : ru, en ...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    browser = None

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("language")