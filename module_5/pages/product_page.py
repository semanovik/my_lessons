from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_shopping_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        link.click()

    def should_be_product_page(self):
        self.should_be_add_to_cart_button()
        self.should_be_review_button()
        self.should_be_wishlist_button()
        self.should_be_product_description()
        self.should_be_book_title()
        self.should_be_book_price()
        self.should_be_added_book_title()
        self.should_be_cart_amount()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), 'Add to cart button is not presented'

    def should_be_review_button(self):
        assert self.is_element_present(*ProductPageLocators.REVIEW_BUTTON), 'Review button is not presented'

    def should_be_wishlist_button(self):
        assert self.is_element_present(*ProductPageLocators.WISHLIST_BUTTON), 'Wishlist button is not presented'

    def should_be_product_description(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_DESCRIPTION), 'Description is not presented'

    def should_be_book_title(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_TITLE), 'Book title is not presented'

    def should_be_book_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), 'Book price is not presented'

    def should_be_added_book_title(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_BOOK_TITLE), "Added book price is not presented"

    def should_be_cart_amount(self):
        assert self.is_element_present(*ProductPageLocators.CART_AMOUNT), "Cart amount is not presented"
