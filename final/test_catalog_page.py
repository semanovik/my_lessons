import time
import pytest
from pages.catalogue_page import CatalogPage
from pages.main_page import MainPage

class TestCatalogPage:

    def go_to_catalog_from_main_page(self, browser):
        page = MainPage()