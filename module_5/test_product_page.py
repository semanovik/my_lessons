import time
import pytest
from .pages.product_page import ProductPage


class TestProductPage:

    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        # Arrange
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}'
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.should_be_before_product_page()  # Проверяем, что все нужные элементы есть на странце
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
