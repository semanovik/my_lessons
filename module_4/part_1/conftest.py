import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Учим командную строку понимать новое условие запуска
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en-GB, es, fr")


# Фикстура, подготавливающая и закрывающая окружение
@pytest.fixture(scope="function")
def browser(language):
    print(f"\nstart {language} vesion..")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()


# Фикстура, возвращающая значение опции языка, на котором запущен браузер
@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("language")
