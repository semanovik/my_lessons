import time
import pytest
from pages.catalogue_page import CatalogPage
from pages.main_page import MainPage

link_catalog_page = 'http://selenium1py.pythonanywhere.com/catalogue/'


class TestCatalogPage:

    def test_should_be_on_catalog_start_page(self, browser):
        page = CatalogPage(browser, link_catalog_page)

        page.open()

        page.should_be_always_on_catalog_page()

    @pytest.mark.parametrize('category', ["clothing_1", "books_2", "books/fiction_3", "books/non-fiction_5"])
    def test_switching_sections_of_catalog(self, browser, category):
        # Arrange
        link = f'http://selenium1py.pythonanywhere.com//catalogue/category/{category}/'
        page = CatalogPage(browser, link_catalog_page)

        # Act
        page.open()
        page.should_be_always_on_catalog_page()


