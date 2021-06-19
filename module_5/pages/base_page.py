from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators

import math


class BasePage():

    #
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # Метод, реализующий открывание страницы
    def open(self):
        self.browser.get(self.url)

    #
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Метод проверяющий наличие элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Метод на решение неравенства на странице
    def solve_quiz_and_get_code(self):  # Это нужно только для выполнения математического уравнения
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # Метод, который проверяет, что элемент не появляется на странице в течение заданного времени:
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # Метод, чтобы проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с
    # функцией until_not, в зависимости от того, какой результат мы ожидаем:
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Переход на страницу логирования с любой страницы сайта
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    # Переход в корзину с любой страницы сайта
    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.CART_LINK)
        link.click()

    # Смотрим наличие ссылки для перехода на страницу логирования
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # Проверяем, что пользователь залогинен
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"