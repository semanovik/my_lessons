from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def get_book_name_before(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        return book_name.text

    def get_book_price_before(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return book_price.text

    def add_to_shopping_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        link.click()

    def should_be_on_product_page(self):
        self.should_be_add_to_cart_button()
        self.should_be_book_title()
        self.should_be_book_price()
        self.should_be_added_book_title()
        self.should_be_cart_amount()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), 'Add to cart button is not presented'

    def should_be_book_title(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_TITLE), 'Book title is not presented'

    def should_be_book_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), 'Book price is not presented'

    def should_be_added_book_title(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_BOOK_TITLE), "Added book price is not presented"

    def should_be_cart_amount(self):
        assert self.is_element_present(*ProductPageLocators.CART_AMOUNT), "Cart amount is not presented"




