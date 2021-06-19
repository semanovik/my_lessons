from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    # Наличие сообщения, что корзина пуста
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'Empty basket message is not ' \
                                                                                  'presented '

    # Проверка отсутствия книг в корзине
    def should_be_no_books_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is not empty'
