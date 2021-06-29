import pytest
from pages.catalogue_page import CatalogPage


link_catalog_page = 'http://selenium1py.pythonanywhere.com/catalogue/'


class TestCatalogPage:

    # Проверка отсутствия форм логирования/регистрации на главной странице каталога
    def test_should_not_be_on_catalog_start_page(self, browser):
        # Arrange
        page = CatalogPage(browser, link_catalog_page)

        # Act
        page.open()

        # Assert
        page.should_not_be_login_form()
        page.should_not_be_registration_form()

    # Проверка наличия важных элементов страницы каталога на всех разделах каталога
    @pytest.mark.parametrize('category', ["clothing_1", "books_2", "books/fiction_3", "books/non-fiction_5"])
    def test_switching_sections_of_catalog(self, browser, category):
        # Arrange
        link = f'http://selenium1py.pythonanywhere.com//catalogue/category/{category}/'
        page = CatalogPage(browser, link_catalog_page)

        # Act
        page.open()
        page.should_be_always_on_catalog_page()


