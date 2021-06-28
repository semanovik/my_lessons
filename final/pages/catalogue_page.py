from .main_page import MainPage
from .locators import CatalogPageLocators
import time


class CatalogPage(MainPage):

    def should_be_always_on_catalog_page(self):
        assert self.is_element_present(*CatalogPageLocators.SIDE_CATEGORIES), 'Side categories is not presented'
        assert self.is_element_present(*CatalogPageLocators.ALL_GOODS_TITLE), "Catalog's page title is not presented"
        assert self.is_element_present(*CatalogPageLocators.SOME_FIRST_PRODUCT), 'First product is not presented'
        assert self.is_element_present(*CatalogPageLocators.CLOTHING_CATEGORY), "Clothing category is not presented"
        assert self.is_element_present(*CatalogPageLocators.BOOKS_CATEGORY), "Books category is not presented"
        assert self.is_element_present(*CatalogPageLocators.BASKET_FIELD), "Basket is not presented"
        assert self.is_element_present(*CatalogPageLocators.FICTION_CATEGORY), "Fiction category is not presented"
        assert self.is_element_present(*CatalogPageLocators.NON_FICTION_CATEGORY), "Non-Fiction category is not " \
                                                                                   "presented "

    def should_be_catalog_url(self, language):
        current_url = self.browser.current_url
        language = language.lower()
        assert current_url == f'https://selenium1py.pythonanywhere.com/{language}/catalogue/', "Wrong catalog url"
