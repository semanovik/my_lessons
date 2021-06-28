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
