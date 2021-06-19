import time
import pytest
from .pages.product_page import ProductPage

common_link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'


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
        book_title = page.get_book_title_before()  # Запоминаем название книги до добавления
        book_price = page.get_book_price_before()  # Запоминаем цену книги
        page.add_to_shopping_cart()  # Добавляем в корзину
        page.solve_quiz_and_get_code()  # Решаем уравнение

        # Assert
        page.should_be_after_product_page()  # Проверяем, что все нужные элементы есть на странице после добавления
        assert book_title == page.get_book_title_after(), f'Wrong book was added: selected book: {book_title}, in ' \
                                                          f'message: {page.get_book_title_after()} '
        assert book_price in page.get_cart_amount(), f'Wrong cart amount:price of selected book: {book_price}, in ' \
                                                     f'cart after: {page.get_cart_amount()} '

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

    # Проверяем, что нет сообщения об успешном добавлении на странице с товаром
    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, common_link)

        # Act
        page.open()

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
    def test_guest_can_go_to_login_page_from_product_page(self,browser):
        # Arrange
        page = ProductPage(browser, common_link)

        # Act
        page.open()

        # Assert
        page.go_to_login_page()
