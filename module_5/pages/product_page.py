from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    # Получить название книги
    def get_book_title_before(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        return book_title.text

    # Получить цену книги
    def get_book_price_before(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return book_price.text

    # Добавить в корзину
    def add_to_shopping_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        link.click()

    # Наличие элементов перед добавлением
    def should_be_before_product_page(self):
        self.should_be_add_to_cart_button()
        self.should_be_book_title()
        self.should_be_book_price()

    # Наличие элементов после добавления
    def should_be_after_product_page(self):
        self.should_be_added_book_title()
        self.should_be_cart_amount()

    # Наличие кнопки добавления в корзину
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), 'Add to cart button is not presented'

    # Наличие названия книги
    def should_be_book_title(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_TITLE), 'Book title is not presented'

    # Наличие цены книги
    def should_be_book_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), 'Book price is not presented'

    # Наличие названия книги в сообщении о добавлении
    def should_be_added_book_title(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_BOOK_TITLE), "Added book price is not presented"

    # Наличие суммы в корзине после добавления книги в корзину
    def should_be_cart_amount(self):
        assert self.is_element_present(*ProductPageLocators.CART_AMOUNT), "Cart amount is not presented"

    # Получить название книги в сообщении о добавлении
    def get_book_title_after(self):
        book_title_after = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_TITLE)
        return book_title_after.text

    # Получить сумму корзины
    def get_cart_amount(self):
        cart_amount_after = self.browser.find_element(*ProductPageLocators.CART_AMOUNT)
        return cart_amount_after.text


