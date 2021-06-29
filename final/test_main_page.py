import time
from pages.main_page import MainPage
from pages.catalogue_page import CatalogPage
from pages.login_page import LoginPage

main_page_link = 'https://selenium1py.pythonanywhere.com/'


class TestMainPage:

    # Переход на страницу каталога с главной, проверка наличия всех важных эл-в страницы каталога
    def test_go_to_catalogue_from_main_page(self, browser, language):
        # Arrange
        page = MainPage(browser, main_page_link)

        # Act
        page.open()
        page.go_to_catalogue_page()
        catalogue_page = CatalogPage(browser, browser.current_url)

        # Assert
        catalogue_page.should_be_always_on_catalog_page()
        catalogue_page.should_be_catalog_url(language)

    # Переход на страницу логирования с главной, проверка наличия всех важных эл-в страницы логирования
    def test_go_to_login_page_from_main_page(self, browser, language):
        page = MainPage(browser, main_page_link)

        # Act
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.go_to_login_page()
        login_page.should_be_login_url(language)
        login_page.should_be_to_login_in()
        login_page.should_be_for_registration()

