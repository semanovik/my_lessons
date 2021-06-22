from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators

class MainPage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # Метод, реализующий открывание страницы
    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Переход на страницу логирования с любой страницы сайта
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGOUT_LINK)
        link.click()

    def should_be_welcome_message(self):
        assert self.is_element_present(*MainPageLocators.WELCOME_MESSAGE), 'Welcome message is not presented'

    def get_text_from_welcome_message(self):
        message = self.browser.find_element(*MainPageLocators.WELCOME_MESSAGE)
        return message.text
