from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


class TestProductPage:

    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        # page.should_be_on_product_page()  # Проверяем, что все нужные элементы есть на странце
        book_name = page.get_book_name_before()

        assert 'smth' in book_name.text, 'асерт работает'
        # Тут метод на проверку названия книги изначального и добавленного
        # Тут метод на проверку увеличения суммы корзины от цены книги
