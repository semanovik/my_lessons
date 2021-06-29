from .main_page import MainPage
from .locators import CatalogPageLocators


class CatalogPage(MainPage):

    # Наличие элементов, которые присутствуют всегда в каталоге
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

    # Соответствие url каталога
    def should_be_catalog_url(self, language):
        current_url = self.browser.current_url
        language = language.lower()
        assert current_url == f'https://selenium1py.pythonanywhere.com/{language}/catalogue/', "Wrong catalog url"

    # Переход в раздел clothing
    def switch_to_catalog_clothing_directory(self):
        clothing_link = self.browser.find_element(*CatalogPageLocators.CLOTHING_CATEGORY)
        clothing_link.click()

    # Переход в раздел book
    def switch_to_catalog_book_directory(self):
        book_link = self.browser.find_element(*CatalogPageLocators.BOOKS_CATEGORY)
        book_link.click()

    # Переход в раздел fiction
    def switch_to_catalog_fiction_directory(self):
        fiction_link = self.browser.find_element(*CatalogPageLocators.FICTION_CATEGORY)
        fiction_link.click()

    # Переход в раздел non-fiction
    def switch_to_catalog_non_fiction_directory(self):
        non_fiction_link = self.browser.find_element(*CatalogPageLocators.NON_FICTION_CATEGORY)
        non_fiction_link.click()

    # Отсутствие формы логирования
    def should_not_be_login_form(self):
        self.is_not_element_present(*CatalogPageLocators.LOGIN_FORM), 'Login form is presented on catalog page'

    # Отсутсвие формы геристрации
    def should_not_be_registration_form(self):
        self.is_not_element_present(*CatalogPageLocators.REGISTRATION_FORM), 'Registration form is presented on ' \
                                                                             'catalog page '


