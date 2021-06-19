from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:

    @pytest.mark.login_guest
    class TestLoginFromMainPage:
        # Проверяется возможность перехода с основной страницы на страницу логирования
        def test_guest_can_go_to_login_page(self, browser):
            # Arrange
            page = MainPage(browser,
                            link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url

            # Act
            page.open()  # открываем страницу
            page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
            login_page = LoginPage(browser, browser.current_url)  # Меняем страницу на которой находимся

            # Assert
            login_page.should_be_login_page()  # Проверяем все локаторы с login_page.py

        # Проверяется наличие ссылки на страницу логирования
        def test_guest_should_see_login_link(self, browser):
            # Arrange
            page = MainPage(browser, link)

            # Act
            page.open()

            # Assert
            page.should_be_login_link()

    # Пререходим в корзину с главной страницы
    # Проверяем, что она пуста
    # Проверяем наличие сообщения, что корзина пуста
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        page = MainPage(browser, link)

        # Act
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)

        # Assert
        basket_page.should_be_no_books_in_basket()
        basket_page.should_be_empty_basket_message()



