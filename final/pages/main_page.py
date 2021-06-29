from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators


class MainPage():

    def __init__(self, browser, url, language=None, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.language = language

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Переход на страницу логирования с главной
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    # Переходим в каталог с главной страницы
    def go_to_catalogue_page(self):
        link = self.browser.find_element(*MainPageLocators.ALL_GOODS_CATALOGUE)
        link.click()

    # Появление приветствия
    def should_be_welcome_message(self):
        assert self.is_element_present(*MainPageLocators.WELCOME_MESSAGE), 'Welcome message is not presented'

    # Получение текста приветствия
    def get_text_from_welcome_message(self):
        message = self.browser.find_element(*MainPageLocators.WELCOME_MESSAGE)
        return message.text

    # Проверка соответствия url главной страницы
    def should_be_main_page_url(self, language):
        current_url = self.browser.current_url
        text = language
        real_url = f'http://selenium1py.pythonanywhere.com/{text.lower()}/'
        assert current_url == real_url, f"Wrong main page url {current_url} == {real_url}"

    # Проверка ожидаемого текста полученному
    def should_be_correct_message(self, expected_message, message):
        assert message in expected_message, 'Wrong welcome message'
