import pytest

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import random

common_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'

@pytest.mark.product_page_guest
class TestProductPage:

    # Проверяем добавление книги в корзину
    # Проверяем соответсвие названия книги названию в сообщении об успешном добавлении
    # Проверяем увеличение суммы корзины на сумму добавленной в корзину книги
    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
    @pytest.mark.skip
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Arrange
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}'
        page = ProductPage(browser, link)
        page.open()

        # Act
        book_title = page.get_book_title_before()
        book_price = page.get_book_price_before()
        page.add_to_shopping_cart()
        page.solve_quiz_and_get_code()

        # Assert
        page.should_be_after_product_page()
        assert book_title == page.get_book_title_after(), f'Wrong book was added: selected book: {book_title}, in ' \
                                                          f'message: {page.get_book_title_after()} '
        assert book_price in page.get_cart_amount(), f'Wrong cart amount:price of selected book: {book_price}, in ' \
                                                     f'cart after: {page.get_cart_amount()} '

    # Проверяем, что нет сообщения об успешном добавлении на странице с товаром
    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, common_link)

        # Act
        page.open()

        # Assert
        page.should_not_be_success_message_after_adding_product_to_basket()

    # Проверяем, что сообщения о добавлении нет сразу после добавления книги в корзину
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, common_link)

        # Act
        page.open()
        page.add_to_shopping_cart()

        # Assert
        page.should_not_be_success_message_after_adding_product_to_basket()

    # Проверяем, что сообщение о добавлении пропадает после добавления книги в корзину
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, common_link)

        # Act
        page.open()
        page.add_to_shopping_cart()

        # Assert
        page.should_not_be_message_disappeared_after_adding_product_to_basket()

    # Проверяем, что на странице товара есть конкретные элементы
    def test_should_be_on_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, common_link)

        # Act
        page.open()

        # Assert
        page.should_be_before_product_page()

    # Проверяем, что на странице товара есть ссылка на страницу логирования
    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, common_link)

        # Act
        page.open()

        # Assert
        page.should_be_login_link()

    # Проверяем, что можем перейти на страницу логирования со страницы с товаром
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, common_link)

        # Act
        page.open()

        # Assert
        page.go_to_login_page()

    # Пререходим в корзину с главной страницы
    # Проверяем, что она пуста
    # Проверяем наличие сообщения, что корзина пуста
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, common_link)

        # Act
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)

        # Assert
        basket_page.should_be_no_books_in_basket()
        basket_page.should_be_empty_basket_message()


@pytest.mark.product_page_user
class TestUserAddToBasketFromProductPage:

    # Создаем нового юзера
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, common_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user()
        login_page.should_be_authorized_user()
        

    # На активном пользователе
    # Проверяем, что нет сообщения об успешном добавлении на странице с товаром
    def test_user_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, common_link)

        # Act
        page.open()

        # Assert
        page.should_not_be_success_message_after_adding_product_to_basket()

    # На активном пользователе
    # Проверяем добавление книги в корзину
    # Проверяем соответсвие названия книги названию в сообщении об успешном добавлении
    # Проверяем увеличение суммы корзины на сумму добавленной в корзину книги
    def test_user_can_add_product_to_basket(self, browser):
        # Arrange
        link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()

        # Act
        book_title = page.get_book_title_before()  # Запоминаем название книги до добавления
        book_price = page.get_book_price_before()  # Запоминаем цену книги
        page.add_to_shopping_cart()  # Добавляем в корзину

        # Assert
        page.should_be_after_product_page()  # Проверяем, что все нужные элементы есть на странице после добавления
        assert book_title == page.get_book_title_after(), f'Wrong book was added: selected book: {book_title}, in ' \
                                                          f'message: {page.get_book_title_after()} '
        assert book_price in page.get_cart_amount(), f'Wrong cart amount:price of selected book: {book_price}, in ' \
                                                     f'cart after: {page.get_cart_amount()} '
