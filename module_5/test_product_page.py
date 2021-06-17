import time

from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


class TestProductPage:

    def test_guest_can_add_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.should_be_before_product_page()    # Проверяем, что все нужные элементы есть на странце
        book_title = page.get_book_title_before()   # Запоминаем название книги до добавления
        book_price = page.get_book_price_before()   # Запоминаем цену книги
        page.add_to_shopping_cart()   # Добавляем в корзину
        page.solve_quiz_and_get_code()    # Решаем уравнение

        # Assert
        page.should_be_after_product_page()    # Проверяем, что все нужные элементы есть на странице после добавления
        assert book_title in page.get_book_title_after(), 'Wrong book was added'
        assert book_price in page.get_cart_amount(), 'Wrong cart amount'









