import time
from pages.main_page import MainPage
from pages.catalogue_page import CatalogPage

main_page_link = 'https://selenium1py.pythonanywhere.com/'


class TestMainPage:

    def test_go_to_catalogue_from_main_page(self, browser, language):
        # Arrange
        page = MainPage(browser, main_page_link)

        # Act
        page.open()
        page.go_to_catalogue_page()
        catalogue_page = CatalogPage(browser, browser.current_url)

        # Assert
        catalogue_page.should_be_on_catalog_page()
        catalogue_page.should_be_catalog_url(language)
